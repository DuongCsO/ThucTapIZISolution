from odoo import models, fields


class Book2(models.TransientModel):
    _name =  'tbl_book2'
    _description = 'Book information'
    _transient_max_hours=0.002
    _transient_max_count=1

    name = fields.Char(string='Name', required=True)
    image = fields.Binary(string = 'Image', attachment=True)
    author = fields.Char(string = 'Author')
    form = fields.Selection([('paperback book','Paperback Book'), ('ebook','Ebook')], string='Form', default='paperback book')
    publish_date = fields.Datetime(string = 'Publish Date')
    cost = fields.Float(string = 'Cost')

