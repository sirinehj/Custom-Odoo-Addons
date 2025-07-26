#in this model we will try to compress all the fields and methods into a relatuionship var in the 
#other model 
#so like any model it need to be added in the models/__init__.py
#the security... and views ...
from odoo import models,fields,api,_


class Model_delegation1_inheritance(models.Model):
    _name="model.delegation1"
    _description="delegation1 compressed in delegation2"

    
    dele1=fields.Char(string=_("Dele1:"))
    