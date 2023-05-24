from odoo import api, models, fields
from odoo.exceptions import ValidationError
import json

class ReportJumlahProject(models.AbstractModel):
    _name = 'report.persenan_plus.laporan_jumlah_project'

    def _get_report_values(self, docids, data=None):
        
        # get the report action back as we will need its data
        report = self.env['ir.actions.report']._get_report_from_name('persenan_plus.laporan_jumlah_project')
        # get the records selected for this rendering of the report
        docs = self.env[report.model].browse(docids)
        
        jumlahproject = {}

        for doc in docs:
            for keyholder in doc.keyholder_ids:
                lines = self.env['persenan_plus.keyholder'].search([('oknum_id', '=', keyholder.oknum_id.id)])
                jumlah = len(lines)
                jumlahproject[str(keyholder.oknum_id.id)] = jumlah

        # raise ValidationError(json.dumps(jumlahproject))

        return {
            'docs': docs,
            'jumlahproject': jumlahproject
        }