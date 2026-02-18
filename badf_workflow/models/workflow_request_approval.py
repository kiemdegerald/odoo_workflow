# -*- coding: utf-8 -*-

from odoo import models, fields


class WorkflowRequestApproval(models.Model):
    _name = 'workflow.request.approval'
    _description = 'Approbation de Demande'
    _order = 'workflow_request_id, sequence'

    name = fields.Char(string='Nom', compute='_compute_name', store=True)
    workflow_request_id = fields.Many2one('workflow.request', string='Demande', required=True, ondelete='cascade')
    workflow_level_id = fields.Many2one('workflow.level', string='Niveau d\'Approbation', required=True)
    sequence = fields.Integer(string='Séquence', required=True)
    approver_user_id = fields.Many2one('res.users', string='Approbateur', required=True)
    approval_date = fields.Datetime(string='Date d\'Approbation')
    state = fields.Selection([
        ('pending', 'En Attente'),
        ('approved', 'Approuvé'),
        ('rejected', 'Rejeté'),
        ('skipped', 'Ignoré'),
    ], string='Statut', default='pending', required=True)
    comments = fields.Text(string='Commentaires')
    active = fields.Boolean(string='Actif', default=True)

    def _compute_name(self):
        for record in self:
            record.name = f"Approbation - Niveau {record.sequence}"
