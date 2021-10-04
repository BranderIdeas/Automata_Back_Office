# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
# import logging

# _logger = logging.getLogger(__name__)

class crm_lead_inherits(models.Model):
    _inherit = 'crm.lead'
    
    object          = fields.Char('Objeto')
    link            = fields.Char('Link')
    pay_method      = fields.Char('Forma de Pago')
    dead_line       = fields.Char('Plazo de ejecución')
    platform        = fields.Many2one('om_automata_licitaciones.crm_platform', 'Plataforma')
    state_tender_id = fields.Many2one('om_automata_licitaciones.crm_states_tenders', 'Estado de Licitación', related="stage_id.state_tender_id")
    motive_of_no_presentated_id = fields.Many2one('om_automata_licitaciones.crm_motive_of_not_presentated', 'Motivo de NO PRESENTADA')
    
	
    def mark_no_presented(self):
        raise ValidationError('No presentada')
