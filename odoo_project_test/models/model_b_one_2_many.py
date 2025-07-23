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