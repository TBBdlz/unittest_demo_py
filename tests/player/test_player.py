import unittest
from game.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("lena", "lena@gmail.com", "mage") # level 1

    def test_to_string(self):
        expected_str = (
            f"Player(user_id={self.player.user_id}, name=lena, email=lena@gmail.com, "
            f"game_class=mage, level=1)"
        )
        self.assertEqual(
            str(self.player),
            expected_str,
            "Player.__str__ is incorrect",
        )

    def test_level_up_normal(self):
        self.player.level_up()
        self.assertEqual(self.player.level, 2, "Player.level_up is incorrect")

    def test_level_up_step(self):
        self.player.level_up(5)
        self.assertEqual(
            self.player.level, 6, "Player.level_up with step argument is incorrect"
        )


if __name__ == "__main__":
    unittest.main()
