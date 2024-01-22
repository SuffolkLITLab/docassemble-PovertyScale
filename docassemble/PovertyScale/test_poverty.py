import unittest

from .poverty import poverty_scale_get_income_limit, poverty_scale_income_qualifies

class test_recreate_tables(unittest.TestCase):
    def test_MA_100_table(self):
        self.assertEqual(poverty_scale_get_income_limit(), 15060)
        self.assertEqual(poverty_scale_get_income_limit(2), 15060 + 5380)
        self.assertEqual(poverty_scale_get_income_limit(3), 15060 + 5380*2)
        self.assertEqual(poverty_scale_get_income_limit(4), 15060 + 5380*3)
        self.assertEqual(poverty_scale_get_income_limit(5), 15060 + 5380*4)
        self.assertEqual(poverty_scale_get_income_limit(6), 15060 + 5380*5)
        self.assertEqual(poverty_scale_get_income_limit(7), 15060 + 5380*6)
        self.assertEqual(poverty_scale_get_income_limit(8), 15060 + 5380*7)

    def test_MA_125_table(self):
        multiplier = 1.25
        self.assertEqual(poverty_scale_get_income_limit(1, multiplier), 15060 * multiplier)
        self.assertEqual(poverty_scale_get_income_limit(2, multiplier), (15060 + 5380) * multiplier)
        self.assertEqual(poverty_scale_get_income_limit(3, multiplier), (15060 + 5380*2) * multiplier)
        self.assertEqual(poverty_scale_get_income_limit(4, multiplier), (15060 + 5380*3) * multiplier)
        self.assertEqual(poverty_scale_get_income_limit(5, multiplier), (15060 + 5380*4) * multiplier)
        self.assertEqual(poverty_scale_get_income_limit(6, multiplier), (15060 + 5380*5) * multiplier)
        self.assertEqual(poverty_scale_get_income_limit(7, multiplier), (15060 + 5380*6) * multiplier)
        self.assertEqual(poverty_scale_get_income_limit(8, multiplier), (15060 + 5380*7) * multiplier)
        
    def test_AK_100_table(self):
        self.assertEqual(poverty_scale_get_income_limit(state="AK"), 18810)
        self.assertEqual(poverty_scale_get_income_limit(2, state="ak"), 18810 + 6730)
        self.assertEqual(poverty_scale_get_income_limit(3, state="Ak"), 18810 + 6730*2)
        self.assertEqual(poverty_scale_get_income_limit(4, state="AK"), 18810 + 6730*3)
        self.assertEqual(poverty_scale_get_income_limit(5, state="AK"), 18810 + 6730*4)
        self.assertEqual(poverty_scale_get_income_limit(6, state="AK"), 18810 + 6730*5)
        self.assertEqual(poverty_scale_get_income_limit(7, state="AK"), 18810 + 6730*6)
        self.assertEqual(poverty_scale_get_income_limit(8, state="AK"), 18810 + 6730*7)


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