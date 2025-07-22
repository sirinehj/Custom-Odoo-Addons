from odoo import fields, models

class Membership(models.Model):
    _name = "library.membership"
    _description = "One Book → Many Memberships & One Fandom → Many Memberships"

    book_id = fields.Many2one("library.book", required=True, ondelete="cascade")
    fandom_id = fields.Many2one("library.fandom", required=True, ondelete="cascade")
    join_date = fields.Date(string="Join Date", default=fields.Date.today())
    popularity = fields.Integer(string="Popularity in Fandom", help="Ranking in this fandom (1-10)")
    is_official = fields.Boolean(string="Officially Recognized?", default=False)