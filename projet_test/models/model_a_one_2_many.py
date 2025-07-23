#model_a_one_2_many linked with model_b_one_2_many by a one 2 many relation 
from odoo import fields,models

class Model_a_one_2_many(models.Model):
    _name="model.a.one2many"
    _description="trying to link model a one2many and model b one2many"

    name=fields.Char(string="Naming A:",required=True)

    model_b_one2many_id=fields.Many2one("model.b.one2many",string="Model B:")

    fact=fields.Float(default=1.10)
    