# -*- coding: utf-8 -*-

from odoo import models, fields, api

class crm_state_inherits(models.Model):
    _inherit = 'crm.stage'
    
    state_tender = fields.Char('Estado Licitación')