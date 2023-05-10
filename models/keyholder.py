# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Keyholder(models.Model):
    _name = 'persenan_plus.keyholder'
    _description = 'persenan_plus.keyholder'

    nama = fields.Char(string="Nama")
    bagian_persen = fields.Float(string="Persenan")
    jumlah_bagian = fields.Float(string="Bagian Didapat")
    posisi_id = fields.Many2one('persenan_plus.keyholder_position', string="Posisi")
    
    project_ids = fields.Many2many('project.project', string="Daftar Project")