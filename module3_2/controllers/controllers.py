# -*- coding: utf-8 -*-
# from odoo import http


# class Module3(http.Controller):
#     @http.route('/module3/module3', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module3/module3/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module3.listing', {
#             'root': '/module3/module3',
#             'objects': http.request.env['module3.module3'].search([]),
#         })

#     @http.route('/module3/module3/objects/<model("module3.module3"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module3.object', {
#             'object': obj
#         })

