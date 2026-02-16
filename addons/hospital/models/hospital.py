# -*- coding: utf-8 -*-
from odoo import models, fields

class HospitalPaciente(models.Model):
    _name = 'hospital.paciente'
    _description = 'Paciente del Hospital'

    name = fields.Char(string='Nombre y Apellidos', required=True)
    sintomas = fields.Text(string='Síntomas')
    # Relación para ver todas sus consultas
    consulta_ids = fields.One2many('hospital.consulta', 'paciente_id', string='Consultas')

class HospitalMedico(models.Model):
    _name = 'hospital.medico'
    _description = 'Médico del Hospital'

    name = fields.Char(string='Nombre y Apellidos', required=True)
    numero_colegiado = fields.Char(string='Número de Colegiado')
    # Relación para ver a qué pacientes ha atendido
    consulta_ids = fields.One2many('hospital.consulta', 'medico_id', string='Consultas')

class HospitalConsulta(models.Model):
    _name = 'hospital.consulta'
    _description = 'Atención Médica'

    paciente_id = fields.Many2one('hospital.paciente', string='Paciente', required=True)
    medico_id = fields.Many2one('hospital.medico', string='Médico', required=True)
    diagnostico = fields.Text(string='Diagnóstico', required=True)
    fecha = fields.Date(string='Fecha de Atención', default=fields.Date.context_today)