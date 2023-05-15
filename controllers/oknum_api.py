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
    def orderCreate(self, **kw):
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
    def orderCreate(self, id, **kw):
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
    
    # @http.route('/api/sales/createOrder', auth='user', methods=["POST"], csrf=False, cors="*", website=False)
    # def orderCreate(self, **kw):
    #     r2
    
    # @http.route('/api/sales/createOrder', auth='user', methods=["POST"], csrf=False, cors="*", website=False)
    # def orderCreate(self, **kw):
    #     u

    # @http.route('/api/sales/createOrder', auth='user', methods=["POST"], csrf=False, cors="*", website=False)
    # def orderCreate(self, **kw):
    #     d