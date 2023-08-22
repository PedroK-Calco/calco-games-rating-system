from unittest import TestCase
from popo import Player
from popo import Match
import glicko

# Test players, values derived from Glicko document
player_1 = Player("pool", 1500, 200, 0.8442, 1, "one", "one")
player_2 = Player("pool", 1400, 30, 0.9955, 2, "one", "one")
player_3 = Player("pool", 1550, 100, 0.9531, 3, "one", "one")
player_4 = Player("pool", 1700, 300, 0.7242, 4, "one", "one")

# Test matches, using the test Player objects
match_1_2 = Match(1, 1, 2, "pool", "22-08-2023", {
    1: glicko.calculate_expected_outcome(player_1.rating, player_2.rating, player_2.g_of_rd),
    2: glicko.calculate_expected_outcome(player_2.rating, player_1.rating, player_1.g_of_rd)
})
match_1_3 = Match(1, 1, 3, "pool", "22-08-2023", {
    1: glicko.calculate_expected_outcome(player_1.rating, player_3.rating, player_3.g_of_rd),
    2: glicko.calculate_expected_outcome(player_3.rating, player_1.rating, player_1.g_of_rd)
})
match_1_4 = Match(1, 1, 4, "pool", "22-08-2023", {
    1: glicko.calculate_expected_outcome(player_1.rating, player_4.rating, player_4.g_of_rd),
    2: glicko.calculate_expected_outcome(player_4.rating, player_1.rating, player_1.g_of_rd)
})
# Assign a match outcome to the Match object indicating player 1 as the winner
match_1_2.outcome = 1
match_1_3.outcome = 1
match_1_4.outcome = 1


class Test(TestCase):
    def test_calculate_new_rating(self):
        self.assertEqual(glicko.calculate_new_rating(player_1, player_2, match_1_2), 1563)
        self.assertEqual(glicko.calculate_new_rating(player_1, player_3, match_1_3), 1596)
        self.assertEqual(glicko.calculate_new_rating(player_1, player_4, match_1_4), 1601)

    def test_calculate_rd_time(self):
        self.fail()

    def test_calculate_rd_prime(self):
        self.assertEqual(glicko.calculate_rd_prime(player_1.deviation, player_2.g_of_rd, match_1_2.expected_outcome[1]),
                         175)
        self.assertEqual(glicko.calculate_rd_prime(player_1.deviation, player_3.g_of_rd, match_1_3.expected_outcome[1]),
                         175)
        self.assertEqual(glicko.calculate_rd_prime(player_1.deviation, player_4.g_of_rd, match_1_4.expected_outcome[1]),
                         186)

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
