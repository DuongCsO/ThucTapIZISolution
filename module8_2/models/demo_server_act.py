from odoo import models, fields

class DemoServerAction(models.Model):
    _name="demo_server_act"
    _description="Demo Server Action"

    name =  fields.Char(string="Name", size=20, required=True)
    status =  fields.Selection([
        ('1','1'),
        ('2','2'),
        ('3','3')
    ], readonly=True, default='1')

    def action_set_3(self):
        for rec in self:
            rec.status='3'
    
    def action_auto(self):
        print("automation action spam")