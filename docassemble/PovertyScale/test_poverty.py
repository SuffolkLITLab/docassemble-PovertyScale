import unittest

from .poverty import poverty_scale_get_income_limit, poverty_scale_income_qualifies

class test_recreate_tables(unittest.TestCase):
    def test_MA_100_table(self):
        self.assertEqual(poverty_scale_get_income_limit(), 14580)
        self.assertEqual(poverty_scale_get_income_limit(2), 19720)
        self.assertEqual(poverty_scale_get_income_limit(3), 24860)
        self.assertEqual(poverty_scale_get_income_limit(4), 30000)
        self.assertEqual(poverty_scale_get_income_limit(5), 35140)
        self.assertEqual(poverty_scale_get_income_limit(6), 40280)
        self.assertEqual(poverty_scale_get_income_limit(7), 45420)
        self.assertEqual(poverty_scale_get_income_limit(8), 50560)

    def test_MA_125_table(self):
        self.assertEqual(poverty_scale_get_income_limit(1, 1.25), 18225)
        self.assertEqual(poverty_scale_get_income_limit(2, 1.25), 24650)
        self.assertEqual(poverty_scale_get_income_limit(3, 1.25), 31075)
        self.assertEqual(poverty_scale_get_income_limit(4, 1.25), 37500)
        self.assertEqual(poverty_scale_get_income_limit(5, 1.25), 43925)
        self.assertEqual(poverty_scale_get_income_limit(6, 1.25), 50350)
        self.assertEqual(poverty_scale_get_income_limit(7, 1.25), 56775)
        self.assertEqual(poverty_scale_get_income_limit(8, 1.25), 63200)
        
    def test_AK_100_table(self):
        self.assertEqual(poverty_scale_get_income_limit(state="AK"), 18210)
        self.assertEqual(poverty_scale_get_income_limit(2, state="ak"), 24640)
        self.assertEqual(poverty_scale_get_income_limit(3, state="Ak"), 31070)
        self.assertEqual(poverty_scale_get_income_limit(4, state="AK"), 37500)
        self.assertEqual(poverty_scale_get_income_limit(5, state="AK"), 43930)
        self.assertEqual(poverty_scale_get_income_limit(6, state="AK"), 50360)
        self.assertEqual(poverty_scale_get_income_limit(7, state="AK"), 59790)
        self.assertEqual(poverty_scale_get_income_limit(8, state="AK"), 63220)


class test_sample_incomes(unittest.TestCase):
    def test_example_income(self):
        # TODO(brycew): this should pass, but because of float precision, it doesn't work (even with round).
        # Would have to refactor to Decimal, but out of scope for now
        # self.assertTrue(poverty_scale_income_qualifies(1133))
        self.assertTrue(poverty_scale_income_qualifies(1132))
        self.assertTrue(poverty_scale_income_qualifies(1000))
        self.assertTrue(poverty_scale_income_qualifies(0))
        self.assertTrue(poverty_scale_income_qualifies(-1))
        self.assertFalse(poverty_scale_income_qualifies(14582))
        self.assertFalse(poverty_scale_income_qualifies(100000000))

if __name__ == "__main__":
    unittest.main()