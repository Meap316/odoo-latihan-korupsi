# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Keyholder(models.Model):
    _name = 'persenan_plus.keyholder'
    _description = 'persenan_plus.keyholder'

    oknum_id = fields.Many2one('persenan_plus.oknum', string="Nama")
    bagian_persen = fields.Float(string="Persenan")
    jumlah_bagian = fields.Float(string="Bagian Didapat", compute="_compute_bagian")
    posisi = fields.Char(string="Posisi")

    project_id = fields.Many2one('project.project', string="Project")
    
    @api.depends('bagian_persen',)
    def _compute_bagian(self):
        for record in self:
            record.jumlah_bagian = record.bagian_persen * record.project_id.backdoor_salary / 100