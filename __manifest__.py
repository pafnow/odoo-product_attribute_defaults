# Copyright 2020 Pafnow
{
    'name': 'Product Attribute Default Values',
    'version': '13.0.1.0.0',
    'depends': ['product'],
    'author': 'MRM, Pafnow',
    'category': 'Product',
    'description': 'Add default value for product template attribute on product and partner',
    'data': [
        'views/partner_view.xml',
        'views/product_attribute_view.xml',
        'views/product_template_view.xml',
    ],
    'installable': True,
    'application': False,
}
