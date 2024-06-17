from odoo import models, api

class DemoUrl(models.TransientModel):
    _name="demo_url"
    _description="Demo Url"


    def btn_view_google_ma(self):
        return {
            'type': 'ir.actions.act_url',
            'res_model': 'ir.actions.act_url',
            # 'name':'View Google Map',
            'url': "https://maps.google.com/?ll=0,0",
            'target': 'new'
        }