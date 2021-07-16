# -*- coding: utf-8 -*-
# from odoo import http


# class OmAgenciaViajes(http.Controller):
#     @http.route('/om_agencia_viajes/om_agencia_viajes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_agencia_viajes/om_agencia_viajes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_agencia_viajes.listing', {
#             'root': '/om_agencia_viajes/om_agencia_viajes',
#             'objects': http.request.env['om_agencia_viajes.om_agencia_viajes'].search([]),
#         })

#     @http.route('/om_agencia_viajes/om_agencia_viajes/objects/<model("om_agencia_viajes.om_agencia_viajes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_agencia_viajes.object', {
#             'object': obj
#         })
