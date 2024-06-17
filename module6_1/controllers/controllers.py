# -*- coding: utf-8 -*-
# from odoo import http


# class Module6(http.Controller):
#     @http.route('/module6/module6', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module6/module6/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module6.listing', {
#             'root': '/module6/module6',
#             'objects': http.request.env['module6.module6'].search([]),
#         })

#     @http.route('/module6/module6/objects/<model("module6.module6"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module6.object', {
#             'object': obj
#         })

