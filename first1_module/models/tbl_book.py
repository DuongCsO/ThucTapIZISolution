from odoo import models, fields


class Book(models.Model):
    _name =  'tbl_book'
    _description = 'Book information'

    name = fields.Char(string='Name', required=True)
    image = fields.Binary(string = 'Image', attachment=True)
    author = fields.Char(string = 'Author')
    form = fields.Selection([('paperback book','Paperback Book'), ('ebook','Ebook')], string='Form', default='paperback book')
    publish_date = fields.Datetime(string = 'Publish Date')
    cost = fields.Float(string = 'Cost')

