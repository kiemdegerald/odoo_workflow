# -*- coding: utf-8 -*-

from odoo import models, fields


class WorkflowRequestDocument(models.Model):
    _name = 'workflow.request.document'
    _description = 'Document de Demande de Workflow'
    _order = 'workflow_request_id, sequence'

    name = fields.Char(string='Nom du Document', required=True)
    workflow_request_id = fields.Many2one('workflow.request', string='Demande', required=True, ondelete='cascade')
    document_type = fields.Char(string='Type de Document')
    attachment_id = fields.Many2one('ir.attachment', string='Pièce Jointe')
    sequence = fields.Integer(string='Séquence', default=10)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Actif', default=True)
