# Copyright 2020 Pafnow

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProductAttribute(models.Model):
    _inherit = "product.attribute"

    force_default_select = fields.Boolean(string="Force Select Default Value", required=True,
                                          help="Force selection of a default value for this attribute on Variants tab of product template form")


class ProductTemplateAttributeLine(models.Model):
    _inherit = "product.template.attribute.line"

    default_value_id = fields.Many2one('product.attribute.value', string="Default Value", domain="[('id', 'in', value_ids)]")

    @api.constrains('default_value_id')
    def _check_default_value_id(self):
        for record in self:
            if record.attribute_id.force_default_select and not record.default_value_id:
                raise ValidationError("A Default Value need to be selected for the attribute %s" % record.attribute_id.name)
