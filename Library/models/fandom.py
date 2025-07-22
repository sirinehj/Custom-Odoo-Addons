from odoo import models, fields

class Fandom(models.Model):
    _name="library.fandom"
    _description="testing the many to one"

    name=fields.Char(string="Name")
    description = fields.Text(string="Description")  
    founding_year = fields.Integer(string="Founding Year")  
    is_active = fields.Boolean(string="Is Active?", default=True)  
    genre = fields.Selection(  
        selection=[  
            ('fantasy', 'Fantasy'),  
            ('sci_fi', 'Science Fiction'),  
            ('horror', 'Horror'),  
            ('mystery', 'Mystery'),  
            ('romance', 'Romance'),  
        ],  
        string="Primary Genre"  
    )  
    
    website = fields.Char(string="Official Website")  
    book_count = fields.Integer(string="Number of Books", compute="_compute_book_count") 

    membership_ids = fields.One2many(
        "library.membership",
        "fandom_id",
        string="Book Memberships"
    )

    def _compute_book_count(self):
    for fandom in self:
        fandom.book_count = len(fandom.membership_ids)
