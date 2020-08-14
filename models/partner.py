# Copyright 2020 Pafnow

from odoo import api, fields, models
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    default_product_attribute_value_ids = fields.Many2many('product.attribute.value')

    @api.constrains('default_product_attribute_value_ids')
    def _check_default_product_attribute_value_ids(self):
        """ Only allow one attribute_value per attribute type """
        for record in self:
            dpav_attribute_ids = []
            for dpav in record.default_product_attribute_value_ids:
                if dpav.attribute_id.id in dpav_attribute_ids:
                    raise ValidationError("Two values cannot be selected as default for the same attribute [%s]." % (dpav.attribute_id.name))
                else:
                    dpav_attribute_ids.append(dpav.attribute_id.id)
