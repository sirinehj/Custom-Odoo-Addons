from odoo import models, fields

class EstateType(models.Model):
    _name="real.estate.type"
    _description = "Estate Type"

    name=fields.Char(string="Name")