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

    _sql_constraints = [
        ("check_price", "CHECK(price > 0)", "Price should be positive."),
        ("check_unique_name", "UNIQUE(name)", "Name must be unique.")
    ]
        
    @api.depends('meeting_ids.book_id')
    def _compute_reading_club_count(self):
        for book in self:
            book.reading_club_count = len(book.meeting_ids.mapped('club_id'))


    @api.constrains('pages', 'date')
    def _check_constraints(self):
        for book in self:
            if book.pages and book.pages <= 0:
                raise ValidationError("Number of pages must be positive!")
            if book.date and book.date > fields.Date.today():
                raise ValidationError("Publication date cannot be in the future!")
            if book.rating and (book.rating < 0 or book.rating > 10):
                raise ValidationError("Rating must be between 0 and 10!")

        