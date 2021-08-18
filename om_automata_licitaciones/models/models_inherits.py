# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class models_inherits(models.Model):
    _inherit = 'crm.lead'
    
    object          = fields.Char('Objeto')
    link            = fields.Char('Link')
    pay_method      = fields.Char('Forma de Pago')
    dead_line       = fields.Char('Plazo de ejecución')
    platform        = fields.Selection([ ('secop_1', 'SECOP 1'),('secop_2', 'SECOP II'),('private', 'PRIVADA')],
                                          'Plataforma', default='secop_1')
    state_tender_id = fields.Many2one('om_automata_licitaciones.states_crm_leads', 'Estado', compute='_compute_state', store='True')
    motive_of_no_presentated_id = fields.Many2one('om_automata_licitaciones.motive_of_not_presentated', 'Motivo de NO PRESENTADA')
    
	
#     @api.depends('stage_id')
    def _compute_state(self):
        model_state = self.env['om_automata_licitaciones.states_crm_leads']
        borrador    = model_state.search([('name','=','Borrador')])
        convocado   = model_state.search([('name','=','Convocado')])
        drafts      = ['New','Qualified']
        for stage in self.stage_id:
            if stage.name in drafts:
                self.state_tender_id = borrador.id
            else:
                self.state_tender_id = convocado.id
            
