#model_a_many_2_one linked with model_b_many_2_one by a many 2 one relation 
from odoo import fields,models

class Model_a_many_2_one(models.Model):
    _name="model.a.many2one"
    _description="trying to link model a many2one and model b many2one"

    name=fields.Char(string="Naming A:",required=True)

    