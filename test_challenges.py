import unittest

import challenges 
import data

class TestChallenges(unittest.TestCase):
    def test_counting_calories(self):
        cc = challenges.CaloriesService()
        calories = data.calories
        result = cc.getMaxCalories(calories)
        self.assertEqual(result,24000)    

        result = cc.get3MaxCalories(calories)
        self.assertEqual(result,45000)    

    def test_rps_counting(self):
        rps = challenges.RPSGame()
        gambles = data.rps_gambles
        self.assertEqual(rps.get_gambles_score(gambles),15)
        gambles = data.rps_gambles
        self.assertEqual(rps.get_gambles_with_decription(gambles),12)


if __name__ == '__main__':

    unittest.main()