from odoo import models, fields, api

class Product(models.Model):
    _name = 'test.product'
    _description = 'Product'

    name = fields.Char(string = 'Name', required = True)
    id = fields.Char(string = 'ID', compute = '_compute_id', required = True, readonly = True)
    description = fields.Text(string = 'Product Description')
    image = fields.Image(string = 'Product Image')
    category = fields.Char(string = 'Product Category', required = True)
    price = fields.Integer(string = 'Price', required = True)

    def _compute_id(self):
        self.id = self.category + str(self.env['ir.sequence'].next_by_code('increment_your_field'))