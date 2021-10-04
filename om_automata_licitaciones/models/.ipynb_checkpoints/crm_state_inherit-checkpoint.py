# -*- coding: utf-8 -*-

from odoo import models, fields, api

class crm_state_inherits(models.Model):
    _inherit = 'crm.stage'
    
    state_tender_id = fields.Many2one('om_automata_licitaciones.crm_states_tenders', 'Estado Licitación')