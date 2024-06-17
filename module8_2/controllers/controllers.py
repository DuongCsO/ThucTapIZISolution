# -*- coding: utf-8 -*-
# from odoo import http


# class Module8(http.Controller):
#     @http.route('/module8/module8', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module8/module8/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module8.listing', {
#             'root': '/module8/module8',
#             'objects': http.request.env['module8.module8'].search([]),
#         })

#     @http.route('/module8/module8/objects/<model("module8.module8"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module8.object', {
#             'object': obj
#         })

