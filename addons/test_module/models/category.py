from odoo import models, fields, api

class Category(models.Model):
    _name = 'test.product_category'
    _description = 'Product Category'

    name = fields.Char(string = 'Product Category', required = True)
    description = fields.Char(string = 'Product Category Description', required = True)
    code = fields.Char(string = 'Product Category Code', required = True)