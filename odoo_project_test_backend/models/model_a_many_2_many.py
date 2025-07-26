#model_a_many_2_many linked with model_b_many_2_many by a many 2 many relation 
from odoo import fields,models

class Model_a_many_2_many(models.Model):
    _name="model.a.many2many"
    _description="trying to link model a many2many and model b many2many"

    name=fields.Char(string="Naming A:",required=True)

    