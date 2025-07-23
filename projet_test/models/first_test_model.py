from odoo import fields,models,api,_
from dateutil.relativedelta import relativedelta

from odoo.exceptions import UserError,ValidationError

class First_test_model(models.Model):
    _name="first.test_model"
    _description="first test model"

    name = fields.Char(string="Name",required=True)
    state=fields.Selection([
        ('draft','Draft'),
        ('confirmed','Confirmed'),
        ('done','Done')
    ],string="Status",default='draft')

    a=fields.Integer(required=True)
    b=fields.Integer(required=True)
    suming=fields.Integer(compute="_suming_first_model",readonly=True)
    def _suming_first_model(self):
        for i in self:
            i.suming=i.a+i.b
    days_limits=fields.Integer(default=7)
    deadline=fields.Date(compute="_max_deadline",inverse="_inv_deadline")
    @api.depends("days_limits")
    def _max_deadline(self):
        for i in self:
            i.deadline=fields.Date.today()+relativedelta(days=i.days_limits)
    def _inv_deadline(self):
        for i in self:
            i.days_limits=(i.deadline - fields.Date.today()).days
    todays=fields.Date(default=fields.Date.today())
    @api.onchange("todays")
    def _onchange_date(self):
        for i in self:
            if(i.todays != fields.Date.today()):
                return{
                    "warning":{
                        "title": _("my Warning"),
                        "message": _("my message")    
                    }
                }
    
    def warning_action(self):
        raise UserError(_("this is a warning button!"))
    def init_a_b(self):
        for i in self:
            i.a=20
            i.b=20
  #  def forming_view(self):
  #      return {
  #          "type":"ir.actions.act_window",
  #          "name":"forming button",
  #          "res_model":"first.test_model",
  #          "view_mode":"form"
  #      }


    _sql_constraints=[
        ("unique_name","UNIQUE(name)","Your name must be unique"),
    ]

    todays_day=fields.Date()
    @api.constrains("todays_day")
    def _valid_todays(self):
        for i in self:
            if(i.todays_day != fields.Date.today()):
                raise ValidationError(_("today is:"+str(fields.Date.today())))

    #to have order the data in view we have 2 diff ways model ordering and manuel ordering
    #all those odering will use the _order declartion in the model it's like:
    #1 model ordering:
    #_order="var1,var2,... desc" => this will list data from var1 to varX in desc order
    #another way to use is in the view.xml in the list/form view(tree) add the attribute default_order:
    #<list string="tree view" default_order="var desc"> ... </list>
    #or
    #<list string="tree view" default_order="var"> ... </list>
    #but in 2: manuel ordering you let the user have the freedom of ordering:
    #_order="sequence desc"
    #sequence=fields.Integer(default=1)
    #then go to the view.xml inside the list/tree tag or form tag on the top add a field tag like this:
    #<list string="tree view"> 
    #   <field name="sequence" widget="handel"/>
    #   ... 
    # </list>
    #i will use model_a_one_2_many for model oredering
    #and model_b_one_2_many for manuel oredering
