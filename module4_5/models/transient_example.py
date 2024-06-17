from odoo import models, fields, api


class TransientExample(models.TransientModel):
    _name = "transient_example"

    field1 = fields.Integer(string="Field 1")
    field2 = fields.Integer(string="Field 2")
    total = fields.Integer(string="Total", compute="_compute_total")
    _transient_max_count=1

    @api.depends('field1', 'field2')
    def _compute_total(self):
        for record in self:
            record.total = record.field1 + record.field2

    def action_compute_total(self):
        # Đây là phương thức được gọi từ giao diện người dùng để tính tổng
        self.ensure_one()
        self.total = self.field1 + self.field2
        
    @api.model
    def _cron_my_transient_model_cleanup(self):
        self.search([]).unlink()
