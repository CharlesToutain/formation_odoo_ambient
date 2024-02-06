from odoo import models,fields

class ImmeubleTag(models.Model):
    _name = 'immeuble.tag'
    
    name = fields.Char(
        string='Nom du tag',
        required=True, 
    )
    description = fields.Text('Description')
    parent_id = fields.Many2one('immeuble.tag', string='Parent Tag', index=True, ondelete='cascade')
    color = fields.Integer('Color Index', default=0)