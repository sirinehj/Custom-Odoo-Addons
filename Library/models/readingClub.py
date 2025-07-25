from odoo import models, fields, api, _

class ReadingClub(models.Model):
    _name = "library.reading_club"
    _description = "Book reading clubs"
    _order = "sequence desc"
    

    sequence = fields.Integer(default=1)
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

    meeting_count = fields.Integer(compute="_compute_meeting_count")


    @api.depends('meeting_ids')
    def _compute_meeting_count(self):
        for rec in self:
            rec.meeting_count = len(rec.meeting_ids)
    
    @api.depends('meeting_ids.club_id') 
    def _compute_books_discussed(self):
        for club in self:
            club.book_ids = club.meeting_ids.mapped('book_id')


    def action_open_meeting_ids(self):
        return {
            "name": _("Related meetings"),
            "type": "ir.actions.act_window",
            "view_mode": "list,form",
            "res_model": "library.meeting",
            "target": "current",
            "domain": [("club_id", "=", self.id)],
            "context": {"default_club_id": self.id},
        }

