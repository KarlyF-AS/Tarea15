#-- coding: utf-8 --
from odoo import models, fields, api

class Alumno(models.Model):
    _name = 'bebidas_alumno.castelao'
    _description = 'Alumno para determinar bebida según sueño'

    nombre = fields.Char(string='Alumno', required=True)
    nivel_sueno = fields.Integer(string='Nivel de sueño', required=True)  # <- corregido
    bebida_recomendada = fields.Char(
        string='Bebida recomendada',
        compute='_compute_bebida',
        store=True
    )

    @api.depends('nivel_sueno')
    def _compute_bebida(self):
        for record in self:
            if 1 <= record.nivel_sueno <= 3:
                record.bebida_recomendada = 'Café con leche'
            elif 4 <= record.nivel_sueno <= 6:
                record.bebida_recomendada = 'Café solo largo'
            elif 7 <= record.nivel_sueno <= 9:
                record.bebida_recomendada = 'Café solo larguísimo'
            elif record.nivel_sueno == 10:
                record.bebida_recomendada = 'Inyección de adrenalina'
            else:
                record.bebida_recomendada = 'Valor inválido'
