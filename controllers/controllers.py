# -*- coding: utf-8 -*-
from odoo import http

# class SoReport(http.Controller):
#     @http.route('/so_report/so_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/so_report/so_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('so_report.listing', {
#             'root': '/so_report/so_report',
#             'objects': http.request.env['so_report.so_report'].search([]),
#         })

#     @http.route('/so_report/so_report/objects/<model("so_report.so_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('so_report.object', {
#             'object': obj
#         })