# -*- coding: utf-8 -*-

from odoo import models, fields, api
import uuid

class Company(models.Model):
    _name = 'test.company'
    _description = 'Company'

    _id = fields.Char(string = 'ID', required = True, copy = False, default = 
    lambda self: 'CMPY' + str(uuid.uuid4())[:8], readonly = True)
    name = fields.Char(string = 'Name', required = True)
    logo = fields.Image(string = 'Company Logo')
    description = fields.Text()
    email = fields.Char(string = 'Email')
    phone_number = fields.Char(string = 'Phone Number')
    website = fields.Char(string = 'Website')