from odoo import fields, models, api
    
class Meeting(models.Model):
    _name = "library.meeting"
    _description = "Reading club meetings"
    _order = "meeting_date desc"
    
    club_id = fields.Many2one("library.reading_club", required=True, ondelete="cascade")
    book_id = fields.Many2one("library.book", string="Book Discussed")
    meeting_date = fields.Datetime(default=fields.Datetime.now)
    attendees = fields.Integer(string="Attendees Count")
    notes = fields.Text(string="Discussion Notes")
    
    state = fields.Selection(
        [('draft', 'Draft'), ('accepted', 'Accepted')],
        default='draft',
        string="Status"
    )
    
    def _valid_field_parameter(self, field, name):
        """Allow tracking parameter for state field"""
        return name == 'tracking' or super()._valid_field_parameter(field, name)

    @api.onchange('book_id')
    def _onchange_book_id(self):
        """Auto-generate discussion notes template when book is selected"""
        if self.book_id:
            self.notes = f"""Discussion Guide for {self.book_id.name}:
            
            1. Key Themes: 
            2. Character Analysis:
            3. Memorable Quotes:
            4. Critical Reception:
            5. Personal Ratings:
            """
            return {
                'warning': {
                    'title': "Notes Template Generated",
                    'message': f"A discussion template for '{self.book_id.name}' has been prepared. You can modify it as needed."
                }
            }


    def action_accept(self):
        """Mark meeting as accepted"""
        self.write({'state': 'accepted'})
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Meeting Accepted!',
                'type': 'rainbow_man',
            }
        }