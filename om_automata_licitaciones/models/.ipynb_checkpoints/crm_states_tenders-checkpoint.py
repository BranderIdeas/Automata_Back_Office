# -*- coding: utf-8 -*-

from odoo import models, fields, api
# import logging

# _logger = logging.getLogger(__name__)

class crm_states_tenders(models.Model):
    _name = 'om_automata_licitaciones.crm_states_tenders'
    _description = 'Estados de Licitación'

    name = fields.Char('Nombre')
    
    