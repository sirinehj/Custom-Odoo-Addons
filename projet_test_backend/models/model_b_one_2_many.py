#model_b_one_2_many linked with model_a_one_2_many by a one 2 many relation 
from odoo import fields,models,api,_

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

    def action_open_model_a_ids(self):
        return{
            "name":_("Model A one 2 many"),
            "type":"ir.actions.act_window",
            "view_mode":"list,form",
            "res_model":"model.a.one2many",
            "target":"current",
            "domain":[("model_b_one2many_id","=",self.id)],
            "context":{"default_model_b_one2many_id":self.id}
        }
    model_b_one2many_count=fields.Integer(compute="_count_model_b_one2many_conut")
    @api.depends("model_a_ids")
    def _count_model_b_one2many_conut(self):
        for i in self:
            i.model_b_one2many_count=len(i. model_a_ids)
    