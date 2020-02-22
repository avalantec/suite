# -*- coding: utf-8 -*-

from odoo import models, fields, api
class Invoice(models.Model):
    _inherit = "account.invoice"
    clave_proveedor = fields.Char(string="Clave Proveedor", )
    numero_consecutivo_aceptacion = fields.Char(string="Numero Consecutivo Aceptación", )

class CurrencyRate(models.Model):
    _inherit = "res.currency.rate"
    rate = fields.Float(string="Rate", digits=(18, 12))

class Currency(models.Model):
    _inherit = "res.currency"
    rate = fields.Float(string="Rate", digits=(18, 12))