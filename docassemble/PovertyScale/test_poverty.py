import unittest

from .poverty import poverty_scale_get_income_limit, poverty_scale_income_qualifies

class TestRecreateTables(unittest.TestCase):
    def test_MA_100_table(self):
        # 48 Contiguous States and DC 2025 Poverty Guidelines
        self.assertEqual(poverty_scale_get_income_limit(1), 15960)
        self.assertEqual(poverty_scale_get_income_limit(2), 15960 + 5680)   # 21,640
        self.assertEqual(poverty_scale_get_income_limit(3), 15960 + 5680 * 2)  # 27,320
        self.assertEqual(poverty_scale_get_income_limit(4), 15960 + 5680 * 3)  # 33,000
        self.assertEqual(poverty_scale_get_income_limit(5), 15960 + 5680 * 4)  # 38,680
        self.assertEqual(poverty_scale_get_income_limit(6), 15960 + 5680 * 5)  # 44,360
        self.assertEqual(poverty_scale_get_income_limit(7), 15960 + 5680 * 6)  # 50,040
        self.assertEqual(poverty_scale_get_income_limit(8), 15960 + 5680 * 7)  # 55,720

    def test_MA_125_table(self):
        multiplier = 1.25
        # 48 Contiguous States and DC 2025 Poverty Guidelines multiplied by 1.25
        self.assertEqual(
            poverty_scale_get_income_limit(1, multiplier),
            int(round(15650 * multiplier))
        )  # 15,650 * 1.25 = 19,562.5 → 19563
        self.assertEqual(
            poverty_scale_get_income_limit(2, multiplier),
            int(round((15650 + 5500) * multiplier))
        )  # 21,150 * 1.25 = 26,437.5 → 26438
        self.assertEqual(
            poverty_scale_get_income_limit(3, multiplier),
            int(round((15650 + 5500 * 2) * multiplier))
        )  # 26,650 * 1.25 = 33,312.5 → 33313
        self.assertEqual(
            poverty_scale_get_income_limit(4, multiplier),
            int(round((15650 + 5500 * 3) * multiplier))
        )  # 32,150 * 1.25 = 40,187.5 → 40188
        self.assertEqual(
            poverty_scale_get_income_limit(5, multiplier),
            int(round((15650 + 5500 * 4) * multiplier))
        )  # 37,650 * 1.25 = 47,062.5 → 47063
        self.assertEqual(
            poverty_scale_get_income_limit(6, multiplier),
            int(round((15650 + 5500 * 5) * multiplier))
        )  # 43,150 * 1.25 = 53,937.5 → 53938
        self.assertEqual(
            poverty_scale_get_income_limit(7, multiplier),
            int(round((15650 + 5500 * 6) * multiplier))
        )  # 48,650 * 1.25 = 60,812.5 → 60813
        self.assertEqual(
            poverty_scale_get_income_limit(8, multiplier),
            int(round((15650 + 5500 * 7) * multiplier))
        )  # 54,150 * 1.25 = 67,687.5 → 67688

    def test_AK_100_table(self):
        # Alaska 2025 Poverty Guidelines
        self.assertEqual(poverty_scale_get_income_limit(1, state="AK"), 19950)
        self.assertEqual(poverty_scale_get_income_limit(2, state="AK"), 19950 + 7100)   # 27,050
        self.assertEqual(poverty_scale_get_income_limit(3, state="AK"), 19950 + 7100 * 2)  # 34,150
        self.assertEqual(poverty_scale_get_income_limit(4, state="AK"), 19950 + 7100 * 3)  # 41,250
        self.assertEqual(poverty_scale_get_income_limit(5, state="AK"), 19950 + 7100 * 4)  # 48,350
        self.assertEqual(poverty_scale_get_income_limit(6, state="AK"), 19950 + 7100 * 5)  # 55,450
        self.assertEqual(poverty_scale_get_income_limit(7, state="AK"), 19950 + 7100 * 6)  # 62,550
        self.assertEqual(poverty_scale_get_income_limit(8, state="AK"), 19950 + 7100 * 7)  # 69,650

    def test_AK_125_table(self):
        multiplier = 1.25
        # Alaska 2025 Poverty Guidelines multiplied by 1.25
        self.assertEqual(
            poverty_scale_get_income_limit(1, multiplier, state="AK"),
            int(round(19550 * multiplier))
        )  # 19,550 * 1.25 = 24,437.5 → 24438
        self.assertEqual(
            poverty_scale_get_income_limit(2, multiplier, state="AK"),
            int(round((19550 + 6880) * multiplier))
        )  # 26,430 * 1.25 = 33,037.5 → 33038
        self.assertEqual(
            poverty_scale_get_income_limit(3, multiplier, state="AK"),
            int(round((19550 + 6880 * 2) * multiplier))
        )  # 33,310 * 1.25 = 41,637.5 → 41638
        self.assertEqual(
            poverty_scale_get_income_limit(4, multiplier, state="AK"),
            int(round((19550 + 6880 * 3) * multiplier))
        )  # 40,190 * 1.25 = 50,237.5 → 50238
        self.assertEqual(
            poverty_scale_get_income_limit(5, multiplier, state="AK"),
            int(round((19550 + 6880 * 4) * multiplier))
        )  # 47,070 * 1.25 = 58,837.5 → 58838
        self.assertEqual(
            poverty_scale_get_income_limit(6, multiplier, state="AK"),
            int(round((19550 + 6880 * 5) * multiplier))
        )  # 53,950 * 1.25 = 67,437.5 → 67438
        self.assertEqual(
            poverty_scale_get_income_limit(7, multiplier, state="AK"),
            int(round((19550 + 6880 * 6) * multiplier))
        )  # 60,830 * 1.25 = 76,037.5 → 76038
        self.assertEqual(
            poverty_scale_get_income_limit(8, multiplier, state="AK"),
            int(round((19550 + 6880 * 7) * multiplier))
        )  # 67,710 * 1.25 = 84,637.5 → 84638

class TestSampleIncomes(unittest.TestCase):
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
