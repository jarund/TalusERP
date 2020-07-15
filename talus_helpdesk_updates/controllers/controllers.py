# -*- coding: utf-8 -*-
# from odoo import http


# class TalusHelpdeskUpdates(http.Controller):
#     @http.route('/talus_helpdesk_updates/talus_helpdesk_updates/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/talus_helpdesk_updates/talus_helpdesk_updates/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('talus_helpdesk_updates.listing', {
#             'root': '/talus_helpdesk_updates/talus_helpdesk_updates',
#             'objects': http.request.env['talus_helpdesk_updates.talus_helpdesk_updates'].search([]),
#         })

#     @http.route('/talus_helpdesk_updates/talus_helpdesk_updates/objects/<model("talus_helpdesk_updates.talus_helpdesk_updates"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('talus_helpdesk_updates.object', {
#             'object': obj
#         })
