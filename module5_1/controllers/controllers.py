# -*- coding: utf-8 -*-
# from odoo import http


# class Module5(http.Controller):
#     @http.route('/module5/module5', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module5/module5/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module5.listing', {
#             'root': '/module5/module5',
#             'objects': http.request.env['module5.module5'].search([]),
#         })

#     @http.route('/module5/module5/objects/<model("module5.module5"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module5.object', {
#             'object': obj
#         })

