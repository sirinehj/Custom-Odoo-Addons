from odoo import models,fields,api,_
from odoo.exceptions import ValidationError
#logging for print data in server console
import logging
_logger = logging.getLogger(__name__)

class Employee(models.Model):
    _name="employee.rif.2025"
    _description="employee_rif_2025"

    #need to use session user to compare data from candidat
    session_user = fields.Many2one("res.users",string="Session User",readonly=True,
        compute="_compute_session",store=False)
    session_user_name=fields.Char(string=_("session user name:"),readonly=True,
        compute="_compute_session",store=False)
    session_user_email=fields.Char(string=_("session user email:"),readonly=True,
        compute="_compute_session",store=False)

    #force the context with the session data
    @api.depends_context('uid')
    def _compute_session(self):
        for rec in self:
            #fetch the user session
            user = self.env.user
            rec.session_user = user
            rec.session_user_name = user.name
            rec.session_user_email = user.email
    #        _logger.info(str({
    #    "session_user_name":rec.session_user_name,
    #    "session_user_email":rec.session_user_email,
    # }))
    
    
    # employee get all the data from candidat
    # that's why i need a relation if it dosent exist to get the data and filter it
    # filtrying will be in func
    #  replace with the real candidat.model
    _inherits={"test_candidat.rif.2025":"employee_data_candidat"}
    #i made employee_data_candidat readonly so the user cant change and list throw all employees bc that option is for RH admin omly
    employee_data_candidat=fields.Many2one("test_candidat.rif.2025",ondelete="cascade",onupdate="cascade",readonly=True)
    original_employee_data_candidat=fields.Many2one("test_candidat.rif.2025",ondelete="cascade",onupdate="cascade")
    #editable fields from candidat to reset and store 
    departement = fields.Selection(related="employee_data_candidat.departement", store=True)
    #original_departement = fields.Selection(related="employee_data_candidat.departement", store=True)
    poste = fields.Selection(related="employee_data_candidat.poste", store=True)
    #original_poste = fields.Selection(related="employee_data_candidat.poste", store=True)
    #i cant override the default_get() twice here so i will get the session with the records
    @api.model
    def default_get(self,fields_list):
        defaults=super().default_get(fields_list)
        #fetch user session
        user=self.env.user
        defaults['session_user'] = user
        defaults['session_user_name']=user.name
        defaults['session_user_email']=user.email     
        return defaults
    #now i will create a rh field and set it to True
    #so i can controle it in view or try to reset the values here
    rh=fields.Boolean()
    #now i will try to reset the rh fields if modified
    @api.onchange("employee_data_candidat","rh","departement","poste")
    def departement_rh(self):
        for i in self:
            #fetch user data from candidat
            candidat=self.env["test_candidat.rif.2025"].search([('email','=',i.session_user_email)],limit=1)
            #testing with django@mail.com simple employee
            #candidat=self.env["test_candidat.rif.2025"].search([('email','=','django@mail.com')],limit=1)
            if(candidat):
                if(candidat.is_accepted):
                    #now i need to get the original data employee if it's not rh else a list of employees    
                    if(candidat.departement=='rh'):
                        i.employee_data_candidat=i.original_employee_data_candidat
                        _logger.info(str({
                        "candidat":candidat,
                        "original_candidat":i.original_employee_data_candidat,
                    }))    
                        if(candidat.poste=='rh'):
                            i.rh=True
                        else:
                            i.rh=False
                            i.employee_data_candidat=candidat
                            #i.original_departement=candidat.departement
                            #i.original_poste=candidat.poste
                    else:
                        i.rh=False
                        i.employee_data_candidat=candidat
                        #i.original_departement=candidat.departement
                        #i.original_poste=candidat.poste
                #testing with django@mail.com simple employee
                old_candidat=i.employee_data_candidat.search([('email','=',i.session_user_email)],limit=1)
                #old_candidat=i.employee_data_candidat.search([('email','=','django@mail.com')],limit=1)
                if(old_candidat):
                    original_dep=old_candidat.departement
                    original_poste=old_candidat.poste
                    _logger.info(str({
                        "original_dep":original_dep,
                        "original_poste":original_poste,
                    }))
                

                if(i.rh==False):
                    i.employee_data_candidat.departement=original_dep
                    i.employee_data_candidat.poste=original_poste
                    #i.employee_data_candidat.departement=i.original_departement
                    #i.employee_data_candidat.poste=i.original_poste
                    #raise ValidationError(_("you can't change those fields"))
            
            
    
    
    
