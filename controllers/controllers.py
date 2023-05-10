# -*- coding: utf-8 -*-
# from odoo import http


# class PersenanPlus(http.Controller):
#     @http.route('/persenan_plus/persenan_plus/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/persenan_plus/persenan_plus/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('persenan_plus.listing', {
#             'root': '/persenan_plus/persenan_plus',
#             'objects': http.request.env['persenan_plus.persenan_plus'].search([]),
#         })

#     @http.route('/persenan_plus/persenan_plus/objects/<model("persenan_plus.persenan_plus"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('persenan_plus.object', {
#             'object': obj
#         })
