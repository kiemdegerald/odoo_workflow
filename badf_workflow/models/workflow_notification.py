# -*- coding: utf-8 -*-

from odoo import models, fields


class WorkflowNotification(models.Model):
    _name = 'workflow.notification'
    _description = 'Notification de Workflow'
    _order = 'create_date desc'

    name = fields.Char(string='Sujet', required=True)
    workflow_request_id = fields.Many2one('workflow.request', string='Demande', required=True, ondelete='cascade')
    recipient_user_id = fields.Many2one('res.users', string='Destinataire', required=True)
    notification_type = fields.Selection([
        ('email', 'Email'),
        ('system', 'Système'),
        ('sms', 'SMS'),
    ], string='Type de Notification', default='system', required=True)
    message = fields.Text(string='Message')
    sent_date = fields.Datetime(string='Date d\'Envoi')
    is_read = fields.Boolean(string='Lu', default=False)
    active = fields.Boolean(string='Actif', default=True)
