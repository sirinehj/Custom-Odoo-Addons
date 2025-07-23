from dateutil.relativedelta import relativedelta   
from odoo import api , fields , models 

class RealEstate(models.Model):
    _name = 'real.estate'
    _description = 'Real Estate Model'

    name = fields.Char(default = "House", required = True)
    price = fields.Float()
    state=fields.Selection([
        ('draft','Draft'),
        ('confirmed','Confirmed'),
        ('done','Done')
    ],string="Status",default='draft')
    estate_type_id = fields.Many2one("real.estate.type")
    offer_ids = fields.One2many('real.estate.offer', 'estate_id')
    tag_ids = fields.Many2many('real.estate.tag')
    living_area = fields.Integer(string="Living Area (m²)", default=0)
    garden_area = fields.Integer(string="Garden Area (m²)", default=0)
    garden = fields.Boolean()
    garage = fields.Boolean()
    total_area = fields.Integer(compute='_comput_total_area')
    best_offer = fields.Float(compute='_compute_best_offer')

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):
        for rec in self:
            rec.best_offer = max(rec.offer_ids.mapped('price')) if rec.offer_ids else 0.0





    @api.depends('living_area', 'garden_area')
    def _comput_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area 

    @api.onchange('garden')
    def _onchange_garden(self):
        for record in self:
            if not record.garden:
                record.garden_area = 0
    @api.onchange('date_available') 
    def _onchange_date_available(self):
        for record in self:
            return {
                'warning': {
                    'title': 'Date Available Changed',
                    'message': 'The date available has been changed to today.',
                },
                'value': {
                    'date_available': fields.Date.today(),
                }
            }