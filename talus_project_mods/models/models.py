# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Holding internal notes - not cleint visible
class talus_project_task_mods(models.Model):
    _inherit = 'project.task'
    internal_notes = fields.Html(string='Internal Notes')
