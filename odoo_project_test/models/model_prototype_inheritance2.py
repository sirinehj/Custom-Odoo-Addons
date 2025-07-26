#in this model will put other models fields and method to do not recode them again
#so like any model it need to be added in the models/__init__.py
#the security... and views ...
from odoo import models,fields,api,_


class Model_prototype_inheritance2(models.Model):
    _name="model.proto2"
    _description="mixing models"

    #all the magic is in the _inherit="model.proto"
    _inherit="model.proto"
     
    proto2=fields.Char(string=_("Proto2:"))
    