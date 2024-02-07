from odoo import models,fields, api

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
    tags_ids = fields.Many2many(
        'immeuble.tag',
        string='Tags'
    )
    offre_count = fields.Integer(
        string='Nombre d\'offres',
        compute='_compute_offre_count'
    )

    def _compute_offre_count(self):
        data = self.env['immeuble.offre'].read_group(
            [('immeuble_id', 'in', self.ids)],
            ['immeuble_id'],
            ['immeuble_id']
        )
        mapped_data = {m['immeuble_id'][0]: m['immeuble_id_count'] for m in data}
        for record in self:
            record.offre_count = mapped_data.get(record.id, 0)

    # def _compute_offre_count(self):
    #     # SELF PEUT CONTENIR PLUSIEURS RECORDSET D'IMMEUBLES IL FAUT DONC BOUCLER SUR SELF
    #     for record in self:
    #         # len permet de compter
    #         # self.env['immeuble.offre'] permet d'instancier le modèle immeuble.offre 
    #         #et search permet de faire une recherche
    #         ImmeubleOffre = self.env['immeuble.offre']
    #         domain = [
    #             ('immeuble_id', '=', record.id),
    #             ('offreur_id.name', 'ilike', 'toto' )
    #         ]
    #         ImmeubleOffre.search(domain)
    #         record.offre_count = len(
    #             self.env['immeuble.offre'].search(domain)
    #         )

    @api.onchange('tags_ids')
    # FAIRE LA MÊME CHOSE SUR IMMEUBLE.OFFRE MAIS UTILISER LE OFFREUR
    def _onchange_tags_ids(self):
        list_of_name = self.mapped('tags_ids.name')
        for name_tag in list_of_name:
            self.name = self.name + ' - ' + name_tag