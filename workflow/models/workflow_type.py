# -*- coding: utf-8 -*-

from odoo import models, fields


class WorkflowType(models.Model):
    _name = 'workflow.type'
    _description = 'Type de Workflow'
    _order = 'name'

    name = fields.Char(string='Nom', required=True)
    code = fields.Char(string='Code', required=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Actif', default=True)
