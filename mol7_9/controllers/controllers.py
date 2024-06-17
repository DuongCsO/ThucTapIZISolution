# -*- coding: utf-8 -*-
# from odoo import http


# class Mol7(http.Controller):
#     @http.route('/mol7/mol7', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mol7/mol7/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mol7.listing', {
#             'root': '/mol7/mol7',
#             'objects': http.request.env['mol7.mol7'].search([]),
#         })

#     @http.route('/mol7/mol7/objects/<model("mol7.mol7"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mol7.object', {
#             'object': obj
#         })

