from odoo import models, fields

class DemoModel2(models.Model):
    _name = "demo_model_2"
    _description = "Advanced field"

    binary_field = fields.Binary()
    html_field = fields.Html()
    image_field = fields.Image(max_width=50, max_height=30)
    selection_field = fields.Selection([
    ('1', 'Option 1'),
    ('2', 'Option 2'),
    ('3', 'Option 3'),
    ('4', 'Option 4'),
    ])
    text_field = fields.Text()