from odoo import models, fields, api

class DemoUrl(models.TransientModel):
    _name="demo_url"
    _description="Demo Url"

    def btn_view_google_map(self):
        return {
            'type': 'ir.actions.act_url',
            'name':'View Google Map',
            'url': "https://maps.google.com/?ll=0,0",
            'target': 'new'
        }