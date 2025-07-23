#model_b_one_2_many linked with model_a_one_2_many by a one 2 many relation 
from odoo import fields,models,api

class Model_b_one_2_many(models.Model):
    _name="model.b.one2many"
    _description="trying to link model b one2many and model a one2many"

    numb=fields.Integer(string="Int Model B:")

    model_a_ids=fields.One2many("model.a.one2many","model_b_one2many_id",string="Model A:")

    max_fact=fields.Float(compute="_maxing")

    @api.depends("model_a_ids.fact")
    def _maxing(self):
        for i in self:
            i.max_fact=sum(i.model_a_ids.mapped("fact"))*i.numb