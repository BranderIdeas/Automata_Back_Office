# -*- coding: utf-8 -*-

from odoo import models, fields, api


class crm_platform(models.Model):
    _name = 'om_automata_licitaciones.crm_platform'
    _description = 'Plataforma'

    name = fields.Char('Nombre')