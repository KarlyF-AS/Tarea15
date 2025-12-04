# -*- coding: utf-8 -*-
# from odoo import http


# class BebidasAlumno(http.Controller):
#     @http.route('/bebidas_alumno/bebidas_alumno', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bebidas_alumno/bebidas_alumno/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bebidas_alumno.listing', {
#             'root': '/bebidas_alumno/bebidas_alumno',
#             'objects': http.request.env['bebidas_alumno.bebidas_alumno'].search([]),
#         })

#     @http.route('/bebidas_alumno/bebidas_alumno/objects/<model("bebidas_alumno.bebidas_alumno"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bebidas_alumno.object', {
#             'object': obj
#         })

