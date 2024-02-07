from odoo import models,fields, api
from odoo.exceptions import ValidationError

class ImmeubleOffre(models.Model):
    _name = 'immeuble.offre'
    _description = 'Immeuble offre'
    

    name = fields.Char(
        string='Nom de l\'offre',
        required=True, 
    )
    immeuble_id = fields.Many2one(
        'immeuble',
        string="Immeuble"
    )
    offreur_id = fields.Many2one(
        'res.partner',
        string='Offreur'
    )
    owner_id = fields.Many2one(
        'res.partner',
        string='Propriétaire',
        related='immeuble_id.owner_id',
    )
    amount = fields.Monetary(
        string="Montant",
        currency_field='company_currency_id',
    )
    company_currency_id = fields.Many2one(
        'res.currency',
        string="Devise"
    )

    @api.onchange('offreur_id', 'immeuble_id')
    def _onchange_offreur_id(self):
        # SI J'AI UN OFFREUR ET UN IMMEUBLE, JE METS LE NOM DE L'OFFRE
        #RAJOUTER LE MONTANT DE L'OFFRE
        #Une offre de [offreur] pour l'immeuble [immeuble] à un montant de [montant]
        if self.offreur_id and self.immeuble_id:
            self.name = 'Une offre de ' + self.offreur_id.name + ' pour l\'immeuble ' + self.immeuble_id.name
        else:
            self.name = ''
    
    @api.constrains('offreur_id', 'owner_id')
    def _check_offreur_id(self):
        if self.offreur_id == self.owner_id:
            raise ValidationError('Vous ne pouvez pas faire une offre sur votre propre immeuble !')

    def write(self, vals):
        for record in self:
            if vals.get('immeuble_id'):
                self._add_tag_in_immeuble()
        return super(ImmeubleOffre, self).write(vals)

    @api.model
    def create(self, vals):
        res = super(ImmeubleOffre, self).create(vals)
        if res.immeuble_id:
            res._add_tag_in_immeuble()
        return res

    def _add_tag_in_immeuble(self):
        tag = self.env.ref('immeuble.formation_tag')
        self.immeuble_id.tags_ids = [(4, tag.id, 0)]