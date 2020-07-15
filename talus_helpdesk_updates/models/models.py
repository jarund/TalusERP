# -*- coding: utf-8 -*-

from odoo import models, fields, api


class talus_helpdesk_updates(models.Model):
    _inherit = 'helpdesk.ticket'
    # Changing Descr field to html from text
    description = fields.Html(string='Description')
    internal_notes = fields.Html(string='Internal Notes')