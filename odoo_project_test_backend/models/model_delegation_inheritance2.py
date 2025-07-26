#so like any model it need to be added in the models/__init__.py
#the security... and views ...
from odoo import models,fields,api,_


class Model_delegation2_inheritance(models.Model):
    _name="model.delegation2"
    _description="delegation1 compressed here"

    #all the magic is inth _inherits={'model':'var'}

    _inherits={'model.delegation1':"dele1_id"}
    #relation_var
    dele1_id=fields.Many2many('model.delegation1',string=_("From Dele1:"))
    dele2=fields.Char(string=_("Dele2:"))
    