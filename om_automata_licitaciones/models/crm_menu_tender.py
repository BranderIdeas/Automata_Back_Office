# -*- coding: utf-8 -*-

from odoo import models, fields, api
# from odoo.exceptions import ValidationError
# import logging

# _logger = logging.getLogger(__name__)

class custom(models.Model):
    _name = 'om_automata_licitaciones.crm_menu_tender'
    _description = 'Menu_Licitaciones'

    name = fields.Char('Nombre')
