from odoo import models, fields, api

class DemoStatus(models.Model):
    _name="demo_status"
    _description="Demo status"

    name = fields.Char('Name', required=True)
    status = fields.Selection([('draft', 'Draft'), ('done', 'Done')], string='Status', default='draft')

    def action_serv(self):
        status = self.env['demo_status'].browse(self.id)
        status.write({'status':'done'})
        return True