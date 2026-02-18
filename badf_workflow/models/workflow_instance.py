# -*- coding: utf-8 -*-

from odoo import models, fields


class WorkflowInstance(models.Model):
    _name = 'workflow.instance'
    _description = 'Instance de Workflow'
    _order = 'create_date desc'

    name = fields.Char(string='Référence', required=True)
    workflow_request_id = fields.Many2one('workflow.request', string='Demande', required=True, ondelete='cascade')
    workflow_definition_id = fields.Many2one('workflow.definition', string='Circuit Appliqué', required=True)
    current_level_id = fields.Many2one('workflow.level', string='Niveau Actuel')
    state = fields.Selection([
        ('running', 'En Cours'),
        ('completed', 'Terminé'),
        ('cancelled', 'Annulé'),
    ], string='Statut', default='running', required=True)
    start_date = fields.Datetime(string='Date de Début', default=fields.Datetime.now)
    end_date = fields.Datetime(string='Date de Fin')
    active = fields.Boolean(string='Actif', default=True)
