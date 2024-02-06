from odoo import models,fields

class Immeuble(models.Model):
    _name = 'immeuble'
    _description = 'Immeuble'
    _order = 'id desc'

    name = fields.Char(
        string='Nom de l\'immeuble',
        required=True, 
    )
    test = fields.Char(
        string='Test',
        oldname="name"
    )
    value_estimated = fields.Float(
        string='Valeur estimée'
    )
    nb_etage = fields.Integer('Nombre d\'étage')
    city = fields.Char('Ville')
    country_id = fields.Many2one(
        'res.country',
        string='Pays'
    )
    owner_id = fields.Many2one(
        'res.partner',
        string='Propriétaire'
    )