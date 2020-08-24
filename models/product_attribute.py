# Copyright 2020 Pafnow

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ProductAttribute(models.Model):
    _inherit = "product.attribute"

    force_default_select = fields.Boolean(string="Force Select Default Value", required=True,
                                          help="Force selection of a default value for this attribute on Variants tab of product template form")


class ProductAttributeValue(models.Model):
    _inherit = "product.attribute.value"

    is_auto_add = fields.Boolean("Is auto added", help="Automatically add this value when the attribute is selected on a product template")


class ProductTemplateAttributeLine(models.Model):
    _inherit = "product.template.attribute.line"

    @api.onchange('attribute_id')
    def _onchange_attribute_id(self):
        super()._onchange_attribute_id()
        #Add auto_add values
        if not self.value_ids:
            pav_aa = self.env['product.attribute.value'].search([('attribute_id', '=', self.attribute_id.id), ('is_auto_add', '=', True)])
            if pav_aa:
                self.value_ids = [(4, r.id) for r in pav_aa]

    # Default Value required
    default_value_id = fields.Many2one('product.attribute.value', string="Default Value", domain="[('id', 'in', value_ids)]")

    @api.constrains('default_value_id')
    def _check_default_value_id(self):
        for record in self:
            if record.attribute_id.force_default_select and not record.default_value_id:
                raise ValidationError("A Default Value need to be selected for the attribute %s" % record.attribute_id.name)
