{
    'name': 'Immeuble',
    'version': '1.0',
    'description': 'Description toute',
    'summary': 'Sommaire tout simple',
    'author': 'un auteur',
    'website': 'un site web',
    'license': 'LGPL-3',
    'category': 'custom',
    'depends': [
        'base',
        'contacts',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/immeuble_views.xml',
        'views/res_partner_views.xml',
        'views/immeuble_tag_views.xml',
    ],
    # 'demo': [
    #     ''
    # ],
    # 'auto_install': False,
    # 'application': False,
    # 'assets': {
        
    # }
}