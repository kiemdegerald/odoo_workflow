# -*- coding: utf-8 -*-

from odoo import models, fields


class WorkflowLevel(models.Model):
    _name = 'workflow.level'
    _description = 'Niveau d\'Approbation du Workflow'
    _order = 'workflow_definition_id, sequence'

    name = fields.Char(string='Nom du Niveau', required=True)
    workflow_definition_id = fields.Many2one('workflow.definition', string='Circuit de Workflow', required=True)
    sequence = fields.Integer(string='Séquence', required=True, default=10)
    approver_user_id = fields.Many2one('res.users', string='Approbateur')
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Actif', default=True)
