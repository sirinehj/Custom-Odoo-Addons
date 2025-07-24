#model_b_one_2_many linked with model_a_one_2_many by a one 2 many relation 
from odoo import fields,models
#import api
from odoo import api
class Model_b_one_2_many(models.Model):
    _name="model.b.one2many"
    _description="trying to link model b one2many and model a one2many"

    numb=fields.Integer(string="Int Model B:")

    #model_a_ids is a ref for model_a its the relationship one2many
    #model_b_one2many_id=fileds.One2many("model_name","the var of relationship in the other model",string="your message")
    model_a_ids=fields.One2many("model.a.one2many","model_b_one2many_id",string="Model A:")

#i will create a func that will calc fact from the other model
#first need to imoprt api
    max_fact=fields.Float(compute="_maxing")
#now we can access to fact from the relationship var model_a_ids thats why we need api
    @api.depends("model_a_ids.fact")
    def _maxing(self):
        for i in self:
            #for not having an err we will map each fact and do the sum and * numb operation
            #by default fact isn't empty
            i.max_fact=sum(i.model_a_ids.mapped("fact"))*i.numb
#now add the vars to views
    #2 manuel ordering you let the user have the freedom of ordering:
    #_order="sequence desc"
    #sequence=fields.Integer(default=1)
    #then go to the view.xml inside the list/tree tag or form tag on the top add a field tag like this:
    #<list string="tree view"> 
    #   <field name="sequence" widget="handel"/>
    #   ... 
    # </list>
    #and model_b_one_2_many for manuel oredering
    _order="sequence desc"
    sequence=fields.Integer(default=1)
    
    #we will create button that will lead to all the specific vars of the relationshiin the other model
    #in a curent page it's a nav button/redirction => we are taling about stat buttons
    #first in the model we need the relationship var here
    #we need 2 funcd one to open the view of the other linked model
    #and the second func will show us how many records that linked model has
    #so let's start with the first func
    def action_open_model_a_ids(self):
        #we will need self here just for it id so we don't need to loop
        #the id will be set in the context and domain
        #we will put the view config
        return{
            #dont forget to import _ from odoo in the top
            "name":_("Model A one 2 many"),
            "type":"ir.actions.act_window",
            "view_mode":"list,form",
            #the name of the other model of the relationship in this case is
            #"model.a.one2many"
            "res_model":"model.a.one2many",
            #here will set the target page in the same page not new one
            "target":"current",
            #now the domain
            #that will have the inverse var of the relationship in this model relation var:
            #"model_b_one2many_id"
            #it will be: "domain":[("model_b_one2many_id","=",self.id)]
            "domain":[("model_b_one2many_id","=",self.id)],
            #context will save the id in the new view action after the redirection by
            #default_the inverse var of the relationship in this model relation var:
            #"context":{"default_model_b_one2many_id":self.id}
            "context":{"default_model_b_one2many_id":self.id}
        }
    #now the second func that will show us the number of records by it need a new var that will use 
    #this func in compute param
    model_b_one2many_count=fields.Integer(compute="_count_model_b_one2many_conut")
    #the func
    #this func need @api.depends() so import api from odoo in the top:
    #in my case => @api.depends("model_a_ids")
    @api.depends("model_a_ids")
    def _count_model_b_one2many_conut(self):
        for i in self:
            #it will have the length of the relationship var  "model_a_ids"
            i.model_b_one2many_count=len(i. model_a_ids)
    #now to the view of this model in the form