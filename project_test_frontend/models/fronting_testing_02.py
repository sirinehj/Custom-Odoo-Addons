from odoo import models,fields,_,api

class Fronting_testing_02(models.Model):
    _name = 'fronting.testing_02'
    _description = 'Fronting Model'

    field1=fields.Char(string=_('Field 1:string'))
    field2=fields.Integer(string=_('Field 2:int'))
    #exemple of a file field
    #this file will be stored in the database as a binary field (field3)
    #and the name of the file will be stored in a char field (field3_name)
    field3=fields.Binary(string=_('Field 3:file'))
    