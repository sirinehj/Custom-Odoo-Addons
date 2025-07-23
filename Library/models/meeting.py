from odoo import fields, models
    
class Meeting(models.Model):
    _name = "library.meeting"
    _description = "Reading club meetings"
    
    club_id = fields.Many2one("library.reading_club", required=True, ondelete="cascade")
    book_id = fields.Many2one("library.book", string="Book Discussed")
    meeting_date = fields.Datetime(default=fields.Datetime.now)
    attendees = fields.Integer(string="Attendees Count")
    notes = fields.Text(string="Discussion Notes")