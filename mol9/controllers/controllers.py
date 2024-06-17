# -*- coding: utf-8 -*-
# from odoo import http


# class Mol9(http.Controller):
#     @http.route('/mol9/mol9', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mol9/mol9/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mol9.listing', {
#             'root': '/mol9/mol9',
#             'objects': http.request.env['mol9.mol9'].search([]),
#         })

#     @http.route('/mol9/mol9/objects/<model("mol9.mol9"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mol9.object', {
#             'object': obj
#         })

