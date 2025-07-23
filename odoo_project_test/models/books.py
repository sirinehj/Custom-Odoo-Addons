##########
#import anything from odoo lib
#and the class get models.Model

#each model need to have security,views so dont forget to aliment the __manifest__.py
##########
from odoo import models,fields,api,_

from dateutil.relativedelta import relativedelta

from odoo.exceptions import UserError,ValidationError

class Books(models.Model):
    #model name and description
    _name="Books"
    _description="Books ...."
    #model fileds
    #string:show field name
    title=fields.Char(string="Book's title",required=True,default="book's 1 title is 1")
    description=fields.Text(string="Book's topic",required=True,default="book's 1 blablabla")
    copies=fields.Integer(string="Book's copies",required=True,default=1)
    status=fields.Selection([
        #(value,title)    
        ("new","New")
        
        ],
        default="new",
        copy=False,
        required=True
    )
    state=fields.Selection([
        ('draft','Draft'),
        ('confirmed','Confirmed'),
        ('done','Done')
    ],string="Status",default='draft')
    #date method of it field
    def _default_date(self):
        return fields.Date.today()
    
    available=fields.Date(default=_default_date)

#to add methods to the model you just need to define a function and call it in a var
#for exp i will add a sum fun
# add the vars in the views
    a=fields.Integer(required=True)
    b=fields.Integer(required=True)
#to apply the funcs we need attributes like compute and inverse
#inverse it the inverse func of compute
    suming=fields.Integer(compute="_suming_first_model",readonly=True)
#now i will create the function suming_first_model with self as parameter
#self has all the var of the class so i need to loop throw it to get access to the fields
    def _suming_first_model(self):
        for i in self:
            i.suming=i.a+i.b
#now i will add a complexe method to use inverse for calc a deadline
#i will set dayslimit to 7 days
    days_limits=fields.Integer(default=7)
#now the deadline that will have the compute and the inverse
    deadline=fields.Date(compute="_max_deadline",inverse="_inv_deadline")
#now the functions
#to access to the days easily we need relativedelta
#and import it to the top 
#from dateutil.relativedelta import relativedelta
#we need to add days_limits as required to the function so we need api first
#and import it to the top
#from odoo import api
    @api.depends("days_limits")
    def _max_deadline(self):
        for i in self:
            i.deadline=fields.Date.today()+relativedelta(days=i.days_limits)
#now to show how many days are limited we will create the inverse func
    def _inv_deadline(self):
        for i in self:
            i.days_limits=(i.deadline - fields.Date.today()).days
#never forget to add vars in the views
#for the onchange event to add popup warning to user we need to use @api.onchange
#todays will have the default date of today
    todays=fields.Date(default=fields.Date.today())
    @api.onchange("todays")
    def _onchange_date(self):
        for i in self:
            if(i.todays != fields.Date.today()):
                #the warning will have a dictionary
                return{
                    "warning":{
                        #the _("") to translate
                        #dont forget to import _
                        "title":_("my Warning"),
                        "message":_("my message")    
                    }
                }
    #make a func to tag button in the view to make an err warning
    # first import UserError from odoo.exceptions on the top  
    def warning_action(self):
        raise UserError(_("this is a warning button!"))
    #making a func to change a and b values from button
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
  #constraints can be in SQL/python to force the user to fill vars with correct data
  #now we will create a SQL constraint
  #its always start with _sql_constraints=[] and its a table of constraints
  #this table will have :("constraint_name","SQL_method(var or var with condition)","err message for user if wrong value") 
  #as an exmple i will try to make the name here unique in the SQL
    _sql_constraints=[
        ("unique_name","UNIQUE(name)","Your name must be unique"),
    ]
  #their is many constraints like (all constraints method should be in Maj): 
  # unique(var) => to make the var unique
  # check(var with condition)=> to filter
  # not-null(var)=> not null values allowed
  # Primary Keys(var)=>to make primary keys
  # foreign keys(var)=> to make foreign keys
  # exclusion(var)=> this var can return null or false
  
    #ok now in python constaints way (it's  a func)
    #first python constraints won't work on complexe var of relationships only simple var=> no "var_ids.var"
    #it will do the same things of sql constraints
    #it required to import api and ValidationError from odoo.exceptions
    #if you work with floats use float_compare() or float_is_zero from odoo.tools.float_utils
    #it use @api.constrains("var") 
    #for exp i will try to raise an err if the user change the date of today in my case it's the var ("todays_day")
    todays_day=fields.Date()
    @api.constrains("todays_day")
    def _valid_todays(self):
        for i in self:
            if(i.todays_day != fields.Date.today()):
                raise ValidationError(_("today is:"+str(fields.Date.today())))