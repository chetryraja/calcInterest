from odoo import models, fields, api

class InterestCalculation(models.Model):
    _name = 'interest.calculation'
    _description = 'Interest Calculation'

    principal_amount = fields.Float(string='Principal Amount', required=True)
    interest_rate = fields.Float(string='Interest Rate (%)', required=True)
    time_period = fields.Integer(string='Time Period (years)', required=True)
    interest_type = fields.Selection([
        ('simple', 'Simple Interest'),
        ('compound', 'Compound Interest')
    ], string='Interest Type', required=True, default='simple')
    simple_interest = fields.Float(string='Simple Interest', compute='_compute_interest', store=True)
    compound_interest = fields.Float(string='Compound Interest', compute='_compute_interest', store=True)

    @api.depends('principal_amount', 'interest_rate', 'time_period', 'interest_type')
    def _compute_interest(self):
        for record in self:
            if record.interest_type == 'simple':
                record.simple_interest = (record.principal_amount * record.interest_rate * record.time_period) / 100
                record.compound_interest = 0.0
            elif record.interest_type == 'compound':
                record.simple_interest = 0.0
                record.compound_interest = record.principal_amount * ((1 + (record.interest_rate / 100)) ** record.time_period - 1)
