# -*- coding: utf-8 -*-

from odoo import models, fields, api
# import logging

# _logger = logging.getLogger(__name__)

class states_crm_leads(models.Model):
    _name = 'om_automata_licitaciones.states_crm_leads'
    _description = 'Estados de Licitación'

    name = fields.Char('Nombre')
#     sub_states = fields.One2many('crm.lead', 'stage_id', 'CRM SubStates')
    description = fields.Text('Description')
    
    