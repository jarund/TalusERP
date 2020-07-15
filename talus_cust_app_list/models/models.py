# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Recording Installed Moduels
class talus_cust_app_list(models.Model):
    _name = 'talus_cust_app_list.custom_app_list'
    _inherit = 'mail.thread'
    _description = 'Custom App List'
    _rec_name = 'app_name'

    app_name = fields.Char("App Name",required=True)
    short_descr = fields.Text("Short Description")
    owner_id = fields.Many2one('res.partner', string="Customer", required=True)
    # partner_id = fields.Many2one('res.partner', string="Customer2")
    app_creator = fields.Many2one('res.partner', string="App Created By", required=True)
    install_date = fields.Date("Prod Install Date")
    update_date = fields.Date("Prod Last Updated Date", track_visibility="onchange")
    related_app = fields.Many2many('talus_app_list', string="Related Apps")
    app_notes = fields.Html(string='App Notes')
    key_code = fields.Html(string='Key Code')
    stage_id = fields.Many2one("talus_custom_stage_list")

class app_list(models.Model):
    _name = 'talus_app_list'
    _description = 'App List'
    name = fields.Char("Apps")

# Stages for Custom Apps
class custom_stage_list(models.Model):
    _name = 'talus_custom_stage_list'
    _description = 'Custom App Stages'
    name = fields.Char("Stages")

# Recording DB customizations
class cust_db_code(models.Model):
    _name = 'talus_cust_db_code'
    _inherit = 'mail.thread'
    _description = 'Custom DB Code List'
    _rec_name = 'app_name'

    app_name = fields.Char("App Name",required=True)
    short_descr = fields.Text("Short Description")
    owner_id = fields.Many2one('res.partner', string="Customer", required=True)
    app_creator = fields.Many2one('res.partner', string="App Created By", required=True)
    install_date = fields.Date("Prod Install Date")
    update_date = fields.Date("Prod Last Updated Date", track_visibility="onchange")
    related_app = fields.Many2many('talus_app_list', string="Related Apps")
    app_notes = fields.Html(string='App Notes')
    key_code = fields.Html(string='Key Code')
    stage_id = fields.Many2one("talus_custom_stage_list")

class talus_custom_apps(models.Model):
    _inherit = 'res.partner'
    m_code = fields.Char("M Code")
    odoo_url = fields.Char("Odoo Instance url")
    cust_app_ids = fields.One2many('talus_cust_app_list.custom_app_list', 'owner_id', 'Apps')
    cust_dbcode_ids = fields.One2many('talus_cust_db_code', 'owner_id', 'Cust DB Code')



#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
