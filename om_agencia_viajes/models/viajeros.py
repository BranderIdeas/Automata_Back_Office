# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AgenciaViajero(models.Model):
    _name = 'om_agencia_viajes.viajeros'
    _description = 'Viajeros'
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name = 'viajero_name'

    viajero_document = fields.Char(string='Número de Documento', required=True)
    viajero_name = fields.Char(string='Nombre Completo', required=True)
    viajero_address = fields.Char(string='Dirección')
    viajero_phone = fields.Char(string='Teléfono')
    viajes_id = fields.Many2many(
        'om_agencia_viajes.viajes', string='Viajes', ondelete='restrict')
    viajes_count = fields.Integer('Cantidad de Viajes', compute="get_viajes_count")

    def get_viajes_count(self):
        self.viajes_count = self.env['om_agencia_viajes.viajes'].search_count([('viajeros_id','in',self.id)])

    @api.constrains('viajero_document')
    def check_document(self):
        for rec in self:
            if len(rec.viajero_document) < 4:
                raise ValidationError('Minimo 4 caracteres para el documento.')

    def action_btn_smart(self):
        print('BTN SMART')


class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'

    viajero_name = fields.Char(string='Nombre Viajero')

    # viajero_id = fields.Many2one('om_agencia_viajes.viajeros', string='Viajero', ondelete='restrict')