# -*- coding: utf-8 -*-

from odoo import models, fields, api


class persenan_plus(models.Model):
    _inherit = 'project.project'

    anggaran = fields.Float(string='Anggaran')
    persenan = fields.Float(string='Persenan')
    backdoor_salary = fields.Float(string='Gaji Sepihak', compute="_compute_gaji_sepihak")

    keyholder_ids = fields.Many2many('persenan_plus.keyholder', string="Pemegang Kunci")

    @api.depends('persenan', 'anggaran')
    def _compute_gaji_sepihak(self):
        for record in self:
            record.backdoor_salary = record.persenan * record.anggaran / 100
