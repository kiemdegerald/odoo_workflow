# -*- coding: utf-8 -*-

from odoo import models, fields


class WorkflowAuditLog(models.Model):
    _name = 'workflow.audit.log'
    _description = 'Journal d\'Audit du Workflow'
    _order = 'create_date desc'

    name = fields.Char(string='Action', required=True)
    workflow_request_id = fields.Many2one('workflow.request', string='Demande', required=True, ondelete='cascade')
    user_id = fields.Many2one('res.users', string='Utilisateur', required=True, default=lambda self: self.env.user)
    action_type = fields.Selection([
        ('create', 'Création'),
        ('submit', 'Soumission'),
        ('approve', 'Approbation'),
        ('reject', 'Rejet'),
        ('cancel', 'Annulation'),
        ('update', 'Mise à Jour'),
        ('comment', 'Commentaire'),
    ], string='Type d\'Action', required=True)
    action_date = fields.Datetime(string='Date de l\'Action', required=True, default=fields.Datetime.now)
    old_value = fields.Text(string='Ancienne Valeur')
    new_value = fields.Text(string='Nouvelle Valeur')
    comments = fields.Text(string='Commentaires')
    active = fields.Boolean(string='Actif', default=True)
