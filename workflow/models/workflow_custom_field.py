# -*- coding: utf-8 -*-

from odoo import models, fields


class WorkflowCustomField(models.Model):
    _name = 'workflow.custom.field'
    _description = 'Champ Personnalisé de Workflow'
    _order = 'workflow_request_id, sequence'

    name = fields.Char(string='Nom du Champ', required=True)
    workflow_request_id = fields.Many2one('workflow.request', string='Demande', required=True, ondelete='cascade')
    field_type = fields.Selection([
        ('char', 'Texte'),
        ('text', 'Texte Long'),
        ('integer', 'Entier'),
        ('float', 'Décimal'),
        ('boolean', 'Booléen'),
        ('date', 'Date'),
        ('datetime', 'Date et Heure'),
    ], string='Type de Champ', required=True, default='char')
    value_char = fields.Char(string='Valeur Texte')
    value_text = fields.Text(string='Valeur Texte Long')
    value_integer = fields.Integer(string='Valeur Entier')
    value_float = fields.Float(string='Valeur Décimal')
    value_boolean = fields.Boolean(string='Valeur Booléen')
    value_date = fields.Date(string='Valeur Date')
    value_datetime = fields.Datetime(string='Valeur Date et Heure')
    sequence = fields.Integer(string='Séquence', default=10)
    active = fields.Boolean(string='Actif', default=True)
