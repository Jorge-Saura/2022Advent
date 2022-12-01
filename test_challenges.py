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



if __name__ == '__main__':

    unittest.main()