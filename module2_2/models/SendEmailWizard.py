from odoo import models, fields, api
from odoo.exceptions import UserError


class SendEmailWizard(models.TransientModel):
    _name = 'send.email.wizard'
    _description = 'Send Email Wizard'

    recipient = fields.Char(string='Recipient', required=True)
    subject = fields.Char(string='Subject', required=True)
    body = fields.Text(string='Body', required=True)

    def send_email(self):
        self.ensure_one()
        Mail = self.env['mail.mail']
        vals = {
            'email_from': self.env.user.email,
            'email_to': self.recipient,
            'subject': self.subject,
            'body_html': self.body,
        }
        mail = Mail.create(vals)
        mail.send()
        return True
