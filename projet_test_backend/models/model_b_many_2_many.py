#model_b_many_2_many linked with model_a_many_2_many by a many 2 many relation 
from odoo import fields,models

class Model_b_many_2_many(models.Model):
    _name="model.b.many2many"
    _description="trying to link model b many2many and model a many2many"

    numb=fields.Integer(string="Int Model B:")

    model_a_ids=fields.Many2many("model.a.many2many",string="Model A:")
    
    name_a=fields.Char(related="model_a_ids.name",store=True)