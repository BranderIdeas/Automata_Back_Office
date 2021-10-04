# -*- coding: utf-8 -*-

from odoo import models, fields, api


class crm_motive_of_not_presentated(models.Model):
    _name = 'om_automata_licitaciones.crm_motive_of_not_presentated'
    _description = 'Motivos de NO PRESENTADA'

    name = fields.Char('Nombre')