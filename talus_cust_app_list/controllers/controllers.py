# -*- coding: utf-8 -*-
# from odoo import http


# class TalusCustAppList(http.Controller):
#     @http.route('/talus_cust_app_list/talus_cust_app_list/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/talus_cust_app_list/talus_cust_app_list/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('talus_cust_app_list.listing', {
#             'root': '/talus_cust_app_list/talus_cust_app_list',
#             'objects': http.request.env['talus_cust_app_list.talus_cust_app_list'].search([]),
#         })

#     @http.route('/talus_cust_app_list/talus_cust_app_list/objects/<model("talus_cust_app_list.talus_cust_app_list"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('talus_cust_app_list.object', {
#             'object': obj
#         })
