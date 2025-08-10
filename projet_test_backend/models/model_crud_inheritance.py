#in this model will try to override the CRUD of the model
#so like any model it need to be added in the models/__init__.py
#the security... and views ...
from odoo import models,fields,api,_

import logging

class Model_crud_inheritance(models.Model):
    _name="model.crud_modified"
    _description="modifying this model CRUD functions"

    

    field1=fields.Char()
    field2=fields.Integer()
    field3=fields.Char(readonly=True)
    #let's create view and security of the model then we will go back here

    #ok now let's modify the crud
    #to access to the crud funcs you need @api.create_multi so import api from odoo
    @api.model_create_multi
    #create func is called create it will take self(data from user) and list of vals(vars of model)
    def create(self,vals):
        #here i will loop thorw vars
        for var in vals:
            #every time that i will create i will notify user by it data
            #i will put the data in field3
            var["field3"]=_("created Name:"+str(var.get("field1"))+" Value:"+str(var.get("field2")))
        return super().create(vals)
    #delete func named unlink
    def unlink(self):
        #looping in self
        for i in self:
            #here i will info the user that he will delete data
            #i will use self.env.cr.postcommit.add(lambda: i.notify_info("message")
            #i will import logging in the top
            #_logger=logging.getLogger(__name__)
            #_logger.info("message")
            #and it will show in the termianl side
            _logger=logging.getLogger(__name__)
            _logger.info(_("deleting Name:"+str(i.field1)+" Value:"+str(i.field2)))
        return super().unlink()
    #you can do the same with write(update) and read(get)