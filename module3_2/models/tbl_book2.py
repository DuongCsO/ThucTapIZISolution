from datetime import datetime, timedelta
from odoo import models, fields
from odoo.exceptions import UserError


class Book2(models.TransientModel):
    _name =  'tbl_book2'
    _description = 'Book information'
    _transient_max_hours=0.1
    _transient_max_count=10

    name = fields.Char(string='Name', required=True)
    image = fields.Binary(string = 'Image', attachment=True)
    author = fields.Char(string = 'Author')
    form = fields.Selection([('paperback book','Paperback Book'), ('ebook','Ebook')], string='Form', default='paperback book')
    publish_date = fields.Datetime(string = 'Publish Date')
    cost = fields.Float(string = 'Cost')

    def action_xoa_du_lieu(self):
        # Xóa dữ liệu của transient model này
        self.delete()

        # Xóa dữ liệu của các model khác (tùy chọn)
        # ...

def cron_job(self):
    # Xóa các bản ghi transient model cũ hơn 1 ngày
    self.env['x_xoa_du_lieu_dinh_ky'].search([('create_date', '<', fields.Datetime.now() - timedelta(minutes=1))]).unlink()

