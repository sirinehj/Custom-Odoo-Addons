from odoo import fields, models

class EstateTag(models.Model):
    _name="real.estate.tag"
    _description = "Real Estate Tag"
    
    name = fields.Char( required=True)