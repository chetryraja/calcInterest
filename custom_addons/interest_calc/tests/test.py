from odoo.tests.common import TransactionCase

class TestInterestCalculation(TransactionCase):

    def test_simple_interest_calculation(self):
        interest_calculation = self.env['interest.calculation'].create({
            'principal_amount': 1000.0,
            'interest_rate': 5.0,
            'time_period': 2,
            'interest_type': 'simple'
        })
        self.assertAlmostEqual(interest_calculation.simple_interest, 100.0, places=2)

    def test_compound_interest_calculation(self):
        interest_calculation = self.env['interest.calculation'].create({
            'principal_amount': 1000.0,
            'interest_rate': 5.0,
            'time_period': 2,
            'interest_type': 'compound'
        })
        self.assertAlmostEqual(interest_calculation.compound_interest, 102.50, places=2)
