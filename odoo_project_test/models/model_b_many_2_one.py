#model_b_many_2_one linked with model_a_many_2_one by a many 2 one relation 
from odoo import fields,models

class Model_b_many_2_one(models.Model):
    _name="model.b.many2one"
    _description="trying to link model b many2one and model a many2one"

    numb=fields.Integer(string="Int Model B:")

    #model_a_id is a ref for model_a its the relationship many2one
    #model_a_id=fileds.Many2one("model_name",string="your message")
    model_a_id=fields.Many2one("model.a.many2one",string="Model A:")