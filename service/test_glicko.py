from unittest import TestCase
from popo import Player
import glicko

# Test players, values derived from Glicko document
player_1 = Player("pool", 1500, 200, 0.8442, 1, "one", "one")
player_2 = Player("pool", 1400, 30, 0.9955, 2, "one", "one")
player_3 = Player("pool", 1550, 100, 0.9531, 3, "one", "one")
player_4 = Player("pool", 1700, 300, 0.7242, 4, "one", "one")


class Test(TestCase):
    def test_calculate_new_rating(self):
        self.fail()

    def test_calculate_rd_time(self):
        self.fail()

    def test_calculate_rd_prime(self):
        self.fail()

    def test_calculate_g_of_rd(self):
        self.assertAlmostEqual(glicko.calculate_g_of_rd(player_2.deviation), player_2.g_of_rd, 4)
        self.assertAlmostEqual(glicko.calculate_g_of_rd(player_3.deviation), player_3.g_of_rd, 4)
        self.assertAlmostEqual(glicko.calculate_g_of_rd(player_4.deviation), player_4.g_of_rd, 4)

    def test_calculate_expected_outcome(self):
        self.assertAlmostEqual(glicko.calculate_expected_outcome(player_1.rating, player_2.rating, player_2.g_of_rd),
                               0.639, 3)
        self.assertAlmostEqual(glicko.calculate_expected_outcome(player_1.rating, player_3.rating, player_3.g_of_rd),
                               0.432, 3)
        self.assertAlmostEqual(glicko.calculate_expected_outcome(player_1.rating, player_4.rating, player_4.g_of_rd),
                               0.303, 3)
