# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tender_states(models.Model):
    _name = 'om_automata_licitaciones.tender_states'
    _description = 'Estados de Licitación'

    name = fields.Char('Nombre')