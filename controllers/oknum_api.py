# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json


class OknumAPI(http.Controller):
    @http.route('/api/login/', auth='public', methods=["POST"], csrf=False, cors="*", website=False)
    def login(self, **kw):
       # Validation
       try:
           login = kw["login"] 
       except KeyError:
           return request.make_response(json.dumps( {
                'status': 'failed',
                'message': '`login` is required.'
            }), headers={'Content-Type': 'application/json'})
       
       try:
           password = kw["password"]
       except KeyError:
           return request.make_response(json.dumps( {
                'status': 'failed',
                'message': '`password` is required.'
            }), headers={'Content-Type': 'application/json'})
       try:
           db = kw["db"]
           
       except KeyError:
           return request.make_response(json.dumps( {
                'status': 'failed',
                'message': '`db` is required.'
            }), headers={'Content-Type': 'application/json'})
       # Auth user
       http.request.session.authenticate(db, login, password)
       # Session info
       res = request.env['ir.http'].session_info()
       return request.make_response(json.dumps(res), headers={'Content-Type': 'application/json'})

    @http.route('/api/oknum/create', auth='user', methods=["POST"], csrf=False, cors="*", website=False)
    def oknumCreate(self, **kw):
        # 1. Validasi
        try:
            name = kw["name"]
        except KeyError:
            return request.make_response(json.dumps( {
                'status': 'failed',
                'message': '`name` is required.'
            }), headers={'Content-Type': 'application/json'})

        try:
            jabatan = kw["jabatan"]
        except KeyError:
            return request.make_response(json.dumps( {
                'status': 'failed',
                'message': '`jabatan` is required.'
            }), headers={'Content-Type': 'application/json'})

        try:
            domisili = kw["domisili"]
        except KeyError:
            return request.make_response(json.dumps( {
                'status': 'failed',
                'message': '`domisili` is required.'
            }), headers={'Content-Type': 'application/json'})

        # 2. Operasional
        Oknum = request.env['persenan_plus.oknum'].sudo()

        newOknum = Oknum.create({
            'name':name,
            'jabatan':jabatan,
            'domisili':domisili,
        })

        # 3. Return response 
        return request.make_response(json.dumps( {
            'status': 'success',
            'sales': 'Berhasil membuat oknum',
            'data': {
                'name': newOknum.name,
                'jabatan': newOknum.jabatan,
                'domisili': newOknum.domisili,
            }
        }), headers={'Content-Type': 'application/json'})

    @http.route('/api/oknum/read/<id>', auth='user', methods=["GET"], csrf=False, cors="*", website=False)
    def oknumGetById(self, id, **kw):
        # 1. Validasi & Operasi
        Oknum = request.env['persenan_plus.oknum'].sudo()
        
        existingOknum = Oknum.search([
            ('id', '=', id)
        ])

        if (len(existingOknum) < 1):
            return request.make_response(json.dumps( {
                'status': 'failed',
                'sales': 'Oknum dengan id ' + str(id) +' tidak ditemukan',
            }), headers={'Content-Type': 'application/json'})

        # 2. Return
        return request.make_response(json.dumps( {
            'status': 'success',
            'sales': 'Oknum ditemukan',
            'data': {
                'name': existingOknum.name,
                'jabatan': existingOknum.jabatan,
                'domisili': existingOknum.domisili,
            }
        }), headers={'Content-Type': 'application/json'})
    
    @http.route('/api/oknum/read/filter', auth='user', methods=["POST"], csrf=False, cors="*", website=False)
    def oknumGetByFilter(self, **kw):
        try:
            page = kw["page"]
        except KeyError:
            return request.make_response(json.dumps( {
                'status': 'failed',
                'message': '`page` is required.'
            }), headers={'Content-Type': 'application/json'})

        try:
            limit = kw["limit"]
        except KeyError:
            return request.make_response(json.dumps( {
                'status': 'failed',
                'message': '`limit` is required.'
            }), headers={'Content-Type': 'application/json'})

        filters = []
        sorts = []
        isValid = True
        if 'filter' in kw:
            filters = json.loads(kw["filter"])

            for filter in filters:
                if "field" not in filter:
                    isValid = False
                if "operator" not in filter:
                    isValid = False
                if "value" not in filter:
                    isValid = False
        
        if not isValid:
            return request.make_response(json.dumps( {
                'status': 'failed',
                'message': '`filter` is not valid.'
            }), headers={'Content-Type': 'application/json'})
        
        if 'sort' in kw:
            sorts = json.loads(kw["sort"])

            for sort in sorts:
                if "field" not in sort:
                    isValid = False
                if "type" not in sort:
                    isValid = False
        
        if not isValid:
            return request.make_response(json.dumps( {
                'status': 'failed',
                'message': '`sort` is not valid.'
            }), headers={'Content-Type': 'application/json'})

        # 2. Operasional
        filterObj = []
        sortString = ''

        for filter in filters:
            filterObj.append((filter['field'], filter['operator'], filter['value']))

        for sort in sorts:
            sortString += sort['field']+ ' '+sort['type'] if sort != '' else ', '+sort['field']+ ' '+sort['type']
        
        Oknum = request.env['persenan_plus.oknum'].sudo()

        offset = (int(page)-1)*int(limit)
        listOknum = Oknum.search(filterObj, order=sortString, offset=offset, limit=int(limit))
        
        result = []

        for oknum in listOknum:
            result.append({
                'name': oknum.name,
                'jabatan': oknum.jabatan,
                'domisili': oknum.domisili,
            })
        # 3. Return response 
        return request.make_response(json.dumps( {
            'status': 'success',
            'sales': 'Berhasil membuat oknum',
            'data': result
        }), headers={'Content-Type': 'application/json'})
    
    @http.route('/api/oknum/update', auth='user', methods=["POST"], csrf=False, cors="*", website=False)
    def oknumUpdate(self, **kw):
        try:
            id = kw["id"]
        except KeyError:
            return request.make_response(json.dumps( {
                'status': 'failed',
                'message': '`id` is required.'
            }), headers={'Content-Type': 'application/json'})
        
        try:
            name = kw["name"]
        except KeyError:
            return request.make_response(json.dumps( {
                'status': 'failed',
                'message': '`name` is required.'
            }), headers={'Content-Type': 'application/json'})

        try:
            jabatan = kw["jabatan"]
        except KeyError:
            return request.make_response(json.dumps( {
                'status': 'failed',
                'message': '`jabatan` is required.'
            }), headers={'Content-Type': 'application/json'})

        try:
            domisili = kw["domisili"]
        except KeyError:
            return request.make_response(json.dumps( {
                'status': 'failed',
                'message': '`domisili` is required.'
            }), headers={'Content-Type': 'application/json'})
        
        Oknum = request.env['persenan_plus.oknum'].sudo()

        existingOknum = Oknum.search([('id', '=', id)])

        if len(existingOknum) < 1:
            return request.make_response(json.dumps( {
                'status': 'failed',
                'message': 'Oknum dengan id '+ str(id)+' tidak ditemukan'
            }), headers={'Content-Type': 'application/json'})

        existingOknum = existingOknum[0]
        existingOknum.write({
            'name':name,
            'jabatan':jabatan,
            'domisili':domisili,
        })

        # 3. Return response 
        return request.make_response(json.dumps( {
            'status': 'success',
            'sales': 'Berhasil mengupdate oknum',
            'data': {
                'name': existingOknum.name,
                'jabatan': existingOknum.jabatan,
                'domisili': existingOknum.domisili,
            }
        }), headers={'Content-Type': 'application/json'})

    @http.route('/api/oknum/delete/<id>', auth='user', methods=["GET"], csrf=False, cors="*", website=False)
    def oknumDelete(self, id, **kw):
        Oknum = request.env['persenan_plus.oknum'].sudo()

        existingOknum = Oknum.search([('id', '=', id)])

        if len(existingOknum) < 1:
            return request.make_response(json.dumps( {
                'status': 'failed',
                'message': 'Oknum dengan id '+ str(id)+' tidak ditemukan'
            }), headers={'Content-Type': 'application/json'})

        existingOknum = existingOknum[0]
        existingOknum.unlink()

        # 3. Return response 
        return request.make_response(json.dumps( {
            'status': 'success',
            'sales': 'Berhasil menghapus oknum dengan id '+str(id),
        }), headers={'Content-Type': 'application/json'})