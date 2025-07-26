#in this model will put other models fields and method to do not recode them again
#so like any model it need to be added in the models/__init__.py
#the security... and views ...
from odoo import models,fields,api,_


class Model_prototype_inheritance(models.Model):
    _name="model.proto"
    _description="mixing models"

    #i will take field1 from model_prototype_inheritance1
    #and field2 from model_prototype_inheritance2
    #both model_prototype_inheritance1 and model_prototype_inheritance2 will create
    #it owns tables with field1 and field2 each

    field1=fields.Char(string=_("Field1:"))
    field2=fields.Char(string=_("Field2:"))
    