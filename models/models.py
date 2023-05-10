# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class persenan_plus(models.Model):
#     _name = 'persenan_plus.persenan_plus'
#     _description = 'persenan_plus.persenan_plus'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
