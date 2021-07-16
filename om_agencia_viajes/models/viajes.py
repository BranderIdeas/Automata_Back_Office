# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class AgenciaViajes(models.Model):
    _name = 'om_agencia_viajes.viajes'
    _description = 'Viajes'
    _rec_name = 'viaje_code'

    viaje_code = fields.Char(string='Código del Viaje', required=True, copy=False,
                             readonly=True, index=True, default=lambda self: ('Nuevo Viaje'))
    viaje_places = fields.Integer('Numero de Plazas')
    viaje_date = fields.Date(string='Fecha del Viaje')
    viaje_origin = fields.Char(string='Origen del Viaje')
    viaje_destiny = fields.Char(string='Destino del Viaje')
    viaje_price = fields.Float(string='Precio del Viaje')
    viajeros_id = fields.Many2many(
        'om_agencia_viajes.viajeros', string='Viajeros', ondelete='restrict')
    state = fields.Selection([
        ('avalaible','Disponible'),
        ('unavalaible','No Disponible'),
        ('done','Realizado'),
        ('canceled','Cancelado'),
    ], string="Estado", index=True, readonly=True, default="avalaible")

    @api.model
    def create(self, vals):
        if vals.get('viaje_code', ('Nuevo Viaje')) == ('Nuevo Viaje'):
            vals['viaje_code'] = self.env['ir.sequence'].next_by_code('om_agencia_viajes.viajes.sequence') or ('Nuevo Viaje')
        result = super(AgenciaViajes, self).create(vals)
        return result

    @api.constrains('viaje_date')
    def check_document(self):
        for rec in self:
            if rec.viaje_date <= date.today():
                raise ValidationError('La fecha del viaje debe ser a futuro')

    def action_cancel(self):
        for rec in self:
            rec.state = 'canceled'

    def action_activate(self):
        for rec in self:
            rec.state = 'avalaible'