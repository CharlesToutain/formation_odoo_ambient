from random import randint
from odoo import models,fields, api, _
from odoo.exceptions import ValidationError

class ImmeubleTag(models.Model):
    _name = 'immeuble.tag'
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]

    def _get_default_color(self):
        return randint(1, 11)
    
    name = fields.Char(
        string='Nom du tag',
        required=True, 
    )
    description = fields.Text('Description')
    parent_id = fields.Many2one('immeuble.tag', string='Parent Tag', index=True, ondelete='cascade')
    color = fields.Integer('Color Index', default=_get_default_color)

    @api.constrains('parent_id')
    def _check_parent_id(self):
        if not self._check_recursion():
            raise ValidationError(_('You can not create recursive tags.'))