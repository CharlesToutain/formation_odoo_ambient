from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    immeuble_ids = fields.One2many(
        'immeuble',
        'owner_id',
        string='Immeubles'
    )
