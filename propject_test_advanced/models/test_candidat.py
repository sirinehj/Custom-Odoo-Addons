from odoo import fields,models,_

class TestCandidat(models.Model):
    _name="test_candidat.rif.2025"
    _description="just for testing candidat to employee"

    name=fields.Char(string=_("test_candidat name :"))
    email=fields.Char(string=_("test_candidat email:"))
    is_accepted=fields.Boolean(string=_("validate"))
    poste=fields.Selection([
        ('candidat',_('Candidat Stage')),
        ('rh',_('Human Resources')),
        ('py',_('python')),
        ('dev_b',_('Developer Back_End')),
        ('dev_f',_('Developer Front_End')),
        ('dev_fu',_('Developer FullStack')),
        ('cloud',_('Administation System Cloud')),
        ('dev_odoo_b',_('Developer Odoo Back_End(py)')),
        ('dev_odoo_f',_('Developer Odoo Front_End(owl)')),
        ('dev_odoo_fu',_('Developer Odoo FullStack(py+owl)'))
        ],string=_("test_candidat poste:"), default="candidat")
    departement=fields.Selection([
        ('rh',_('Human Resources')),
        ('dev_b',_('Back_End')),
        ('dev_f',_('Front_End')),
        ('dev_fu',_('FullStack')),
        ('cloud',_('Cloud')),
        ('dev_odoo_b',_('Odoo Back_End(py)')),
        ('dev_odoo_f',_('Odoo Front_End(owl)')),
        ('dev_odoo_fu',_('Odoo FullStack(py+owl)'))
        ],string=_('test_ candidat departement:'))