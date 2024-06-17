# -*- coding: utf-8 -*-
# from odoo import http


# class Module2(http.Controller):
#     @http.route('/module2/module2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module2/module2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module2.listing', {
#             'root': '/module2/module2',
#             'objects': http.request.env['module2.module2'].search([]),
#         })

#     @http.route('/module2/module2/objects/<model("module2.module2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module2.object', {
#             'object': obj
#         })

