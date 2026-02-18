# -*- coding: utf-8 -*-

from odoo import models, fields


class WorkflowRequest(models.Model):
    _name = 'workflow.request'
    _description = 'Demande de Workflow'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    name = fields.Char(string='Numéro de Demande', required=True, copy=False, default='Nouveau')
    workflow_type_id = fields.Many2one('workflow.type', string='Type de Workflow', required=True)
    workflow_definition_id = fields.Many2one('workflow.definition', string='Circuit Appliqué')
    requester_id = fields.Many2one('res.users', string='Demandeur', required=True, default=lambda self: self.env.user)
    request_date = fields.Datetime(string='Date de Demande', required=True, default=fields.Datetime.now)
    amount = fields.Float(string='Montant Demandé')
    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('submitted', 'Soumis'),
        ('in_progress', 'En Cours'),
        ('approved', 'Approuvé'),
        ('rejected', 'Rejeté'),
        ('cancelled', 'Annulé'),
    ], string='Statut', default='draft', required=True, tracking=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Actif', default=True)
