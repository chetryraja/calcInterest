from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import serialize_exception


class InterestCalculationController(http.Controller):

    @http.route('/interest_calculation/create', type='json', auth='user')
    @serialize_exception
    def create_interest_calculation(self, principal_amount, interest_rate, time_period, interest_type):
        interest_calculation = request.env['interest.calculation'].create({
            'principal_amount': principal_amount,
            'interest_rate': interest_rate,
            'time_period': time_period,
            'interest_type': interest_type
        })
        return {'id': interest_calculation.id}

    @http.route('/interest_calculation/<int:calculation_id>', type='json', auth='user')
    @serialize_exception
    def get_interest_calculation(self, calculation_id):
        interest_calculation = request.env['interest.calculation'].sudo().browse(calculation_id)
        return {
            'principal_amount': interest_calculation.principal_amount,
            'interest_rate': interest_calculation.interest_rate,
            'time_period': interest_calculation.time_period,
            'interest_type': interest_calculation.interest_type,
            'simple_interest': interest_calculation.simple_interest,
            'compound_interest': interest_calculation.compound_interest
        }

    @http.route('/interest_calculations', type='json', auth='user')
    @serialize_exception
    def list_interest_calculations(self):
        interest_calculations = request.env['interest.calculation'].sudo().search([])
        result = []
        for calculation in interest_calculations:
            result.append({
                'id': calculation.id,
                'principal_amount': calculation.principal_amount,
                'interest_rate': calculation.interest_rate,
                'time_period': calculation.time_period,
                'interest_type': calculation.interest_type,
                'simple_interest': calculation.simple_interest,
                'compound_interest': calculation.compound_interest
            })
        return result
