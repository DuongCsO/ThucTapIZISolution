from odoo import models, fields

class DemoModel1(models.Model):
    _name="demo_model_1"
    _description="Basic fields"

    bool_field = fields.Boolean(required=True, string="Field 1", help="Gợi ý 1",)
    char_field = fields.Char(size=10, trim=False, copy=False)
    float_field = fields.Float(digits=(6,3))
    integer_field = fields.Integer(default=6, readonly=True)