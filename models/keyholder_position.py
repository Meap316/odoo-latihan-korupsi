# -*- coding: utf-8 -*-

from odoo import models, fields, api


class KeyholderPosition(models.Model):
    _name = 'persenan_plus.keyholder_position'
    _description = 'persenan_plus.keyholder_position'
    _rec_name = 'nama'

    nama = fields.Char(string="Nama")
    partner_id = fields.Many2one('res.partner', string="Relasi")