# -*- coding: utf-8 -*-

from odoo import models, fields, api


class k_modulo(models.Model):
    _inherit = 'res.partner'
    
    codigo = fields.Char('Codigo')
    

