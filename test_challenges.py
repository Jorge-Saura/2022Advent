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

    def test_find_repeated(self):
        fr = challenges.Rucksack()
        self.assertEqual(fr._find_repeated('vJrwpWtwJgWrhcsFMMfFFhFp'),'p')
        self.assertEqual(fr._find_repeated('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'),'L')
        self.assertEqual(fr._find_repeated('pTsdppTMPtqqdbnlNVzJVbSSnbZR'),'b')

        self.assertEqual(fr._find_repeated('aaabbb'),'')

        self.assertEqual(fr._find_all_repeated(data.rp_elements),['p','L','P','v','t','s'])

        self.assertEqual(fr._get_element_priority('a'),1)
        self.assertEqual(fr._get_element_priority('z'),26)
        self.assertEqual(fr._get_element_priority('A'),27)
        self.assertEqual(fr._get_element_priority('Z'),52)

        self.assertEqual(fr.get_rearrange_priority(data.rp_elements),157)

        self.assertEqual(fr._find_all_repetead_in_groups_3(data.rp_elements),['r','Z'])
        self.assertEqual(fr.get_badges_priority(data.rp_elements),70)

    def test_clean_pairs(self):
        r_inside_r = challenges.RangeInsideRange()
        c_inside = challenges.Cleanup(r_inside_r)
        self.assertEqual(c_inside._extract_pairs("2-6,3-5"),[[2,6],[3,5]])
        self.assertEqual(c_inside.count_sections_inside(data.clean_data),2)

        r_overlap_r = challenges.RangeOverlapRange()
        c_overlap = challenges.Cleanup(r_overlap_r)
        self.assertEqual(c_overlap.count_sections_inside(data.clean_data),4)






if __name__ == '__main__':

    unittest.main()