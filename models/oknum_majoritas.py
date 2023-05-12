# -*- coding: utf-8 -*-

from odoo import models, fields, api


class OknumMajoritas(models.Model):
    _name = 'persenan_plus.oknum'
    _description = 'persenan_plus.oknum'

    name = fields.Char(string="Nama")
    jabatan = fields.Char(string="Jabatan")
    domisili = fields.Char(string="Domain/Domisili")