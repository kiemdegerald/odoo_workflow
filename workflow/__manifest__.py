# -*- coding: utf-8 -*-
{
    'name': 'Workflow',
    'version': '17.0.1.0.0',
    'category': 'Productivity/Workflow',
    'summary': 'Système de validation hiérarchique des demandes de crédit',
    'description': """
        Workflow de Validation de Crédit
        =================================
        
        Module de gestion des workflows de validation multi-niveaux.
        
        Fonctionnalités principales :
        - Circuits de validation automatiques (A, B, C) selon le montant
        - Validation hiérarchique multi-niveaux
        - Routage automatique des demandes
        - Traçabilité complète avec audit log
        - Notifications automatiques
        - Gestion des pièces jointes
        
        Circuits :
        - Circuit A (< 5M FCFA) : 2 niveaux
        - Circuit B (5M-50M FCFA) : 3 niveaux  
        - Circuit C (≥ 50M FCFA) : 4 niveaux
    """,
    'author': 'Direction des Systèmes d\'Information',
    'website': '',
    'license': 'OPL-1',
    'depends': [
        'base',
        'mail',
        'web',
    ],
    'data': [
        # Sécurité
        'security/ir.model.access.csv',
        
        # Vues
        'views/workflow_type_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
