import unittest
from decimal import Decimal

from fixture import get_path

from bricklane_platform.local_runner import main


class TestMain(unittest.TestCase):

    def test_card(self):

        expected = (
            "customer_id,shares\r\n"
            "123,735.0\r\n"
            "456,3430.0\r\n"
        )

        result = main(get_path("card_payments_mixed.csv"), "card", Decimal("1.2"))

        self.assertEqual(result, expected)

    def test_bank(self):

        expected = (
            "customer_id,shares\r\n"
            "345,735.0\r\n"
            "789,735.0\r\n"
        )

        result = main(get_path("bank_payments_mixed.csv"), "card", Decimal("1.2"))

        self.assertEqual(result, expected)
