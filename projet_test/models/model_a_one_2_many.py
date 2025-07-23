#model_a_one_2_many linked with model_b_one_2_many by a one 2 many relation 
from odoo import fields,models

class Model_a_one_2_many(models.Model):
    _name="model.a.one2many"
    _description="trying to link model a one2many and model b one2many"

    name=fields.Char(string="Naming A:",required=True)

    model_b_one2many_id=fields.Many2one("model.b.one2many",string="Model B:")

    fact=fields.Float(default=1.10)
    
        #to have order the data in view we have 2 diff ways model ordering and manuel ordering
    #all those odering will use the _order declartion in the model it's like:
    #1 model ordering:
    #_order="var1,var2,... desc" => this will list data from var1 to varX in desc order
    
    _order="name,fact,model_b_one2many_id desc"

    #well for me it looks useless

    #another way to use is in the view.xml in the list/form view(tree) add the attribute default_order:
    #<list string="tree view" default_order="var desc"> ... </list>
    #or
    #<list string="tree view" default_order="var"> ... </list>
    #i will try this in model_b_many_2_many view
