# -*- coding: utf-8 -*-
# from odoo import http


# class TalusProjectMods(http.Controller):
#     @http.route('/talus_project_mods/talus_project_mods/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/talus_project_mods/talus_project_mods/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('talus_project_mods.listing', {
#             'root': '/talus_project_mods/talus_project_mods',
#             'objects': http.request.env['talus_project_mods.talus_project_mods'].search([]),
#         })

#     @http.route('/talus_project_mods/talus_project_mods/objects/<model("talus_project_mods.talus_project_mods"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('talus_project_mods.object', {
#             'object': obj
#         })
