# -*- coding: utf-8 -*-
# from odoo import http


# class OmAutomataLicitaciones(http.Controller):
#     @http.route('/om_automata_licitaciones/om_automata_licitaciones/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/om_automata_licitaciones/om_automata_licitaciones/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('om_automata_licitaciones.listing', {
#             'root': '/om_automata_licitaciones/om_automata_licitaciones',
#             'objects': http.request.env['om_automata_licitaciones.om_automata_licitaciones'].search([]),
#         })

#     @http.route('/om_automata_licitaciones/om_automata_licitaciones/objects/<model("om_automata_licitaciones.om_automata_licitaciones"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('om_automata_licitaciones.object', {
#             'object': obj
#         })
