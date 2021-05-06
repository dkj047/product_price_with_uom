from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _name = 'price.uom.info'
    _check_company_auto = True

    uom_id = fields.Many2one(
        'product.uom', company_dependent=True, check_company=True,
        help="uom id of the product.")
    price = fields.Float(default=0)
