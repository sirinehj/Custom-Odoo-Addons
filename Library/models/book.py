from odoo import models, fields, api
from datetime import date

class Book(models.Model):
    _name = "library.book"
    _description = "Test Model"

    name = fields.Char(default ="Book", required = True)
    date = fields.Date(string="Publication Date", default=fields.Date.today())
    pages = fields.Integer(string="Number of Pages")
    author = fields.Char(string="Author")
    publisher = fields.Char(string="Publisher")
    price = fields.Float(string="Price", digits=(6,2))
    cover_image = fields.Binary(string="Cover Image")
    available = fields.Boolean(string="Available", default=True, copy=False)
    category = fields.Selection(
        selection=[
            ('fiction', 'Fiction'),
            ('non-fiction', 'Non-Fiction'),
            ('biography', 'Biography'),
            ('technical', 'Technical'),
            ('action', 'Action'),
            ('romance', 'Romance'),
            ('mystery', 'Mystery'),
            ('horror', 'Horror'),
        ],
        string="Category"
    )
    rating = fields.Float(string="Rating", digits=(3,1),  copy=False)

    meeting_ids = fields.One2many(
        "library.meeting", 
        "book_id", 
        string="Discussed In Meetings"
    )
    reading_club_count = fields.Integer(
        string="Reading Clubs", 
        compute="_compute_reading_club_count",
        store=True
    )
    
    @api.depends('meeting_ids.book_id')
    def _compute_reading_club_count(self):
        for book in self:
            book.reading_club_count = len(book.meeting_ids.mapped('club_id'))