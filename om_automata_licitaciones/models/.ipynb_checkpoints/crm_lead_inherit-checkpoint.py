# -*- coding: utf-8 -*-

from odoo import models, fields, api
# from odoo.exceptions import ValidationError
# import logging

# _logger = logging.getLogger(__name__)

class crm_lead_inherits(models.Model):
    _inherit = 'crm.lead'
    
    object          = fields.Char('Objeto')
    link            = fields.Char('Link')
    pay_method      = fields.Char('Forma de Pago')
    dead_line       = fields.Char('Plazo de ejecución')
    platform        = fields.Many2one('om_automata_licitaciones.crm_platform', 'Plataforma')
    state_tender_id = fields.Many2one('om_automata_licitaciones.states_crm_leads', 'Estado', compute='_compute_state') #, store='True'
    motive_of_no_presentated_id = fields.Many2one('om_automata_licitaciones.motive_of_not_presentated', 'Motivo de NO PRESENTADA')
    
	
    @api.depends('stage_id')
    def _compute_state(self):
        model_state = self.env['om_automata_licitaciones.states_crm_leads']
        model_stage = self.env['crm.stage']
        borrador    = model_state.search([('name','=','Borrador')])
        convocado   = model_state.search([('name','=','Convocado')])
        drafts      = model_stage.search([('state_tender','=','Borrador')])
        self.state_tender_id = borrador.id if self.stage_id in drafts else convocado.id
        return self.state_tender_id
