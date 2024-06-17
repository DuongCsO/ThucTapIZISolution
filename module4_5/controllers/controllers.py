# -*- coding: utf-8 -*-
# from odoo import http


# class Module4(http.Controller):
#     @http.route('/module4/module4', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module4/module4/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module4.listing', {
#             'root': '/module4/module4',
#             'objects': http.request.env['module4.module4'].search([]),
#         })

#     @http.route('/module4/module4/objects/<model("module4.module4"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module4.object', {
#             'object': obj
#         })

