from odoo import models, fields, api

class ReadingClub(models.Model):
    _name = "library.reading_club"
    _description = "Book reading clubs"
    
    name = fields.Char(required=True)
    location = fields.Char()
    founding_date = fields.Date()
    member_count = fields.Integer(string="Members")
    meeting_ids = fields.One2many("library.meeting", "club_id", string="Past Meetings")

    book_ids = fields.Many2many(
        "library.book",
        string="Books Discussed",
        compute="_compute_books_discussed"
    )
    
    @api.depends('meeting_ids.club_id') 
    def _compute_books_discussed(self):
        for club in self:
            club.book_ids = club.meeting_ids.mapped('book_id')

