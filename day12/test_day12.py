import unittest

import day12.day12_data as data

import day12.day12 as challenges



class TestDay12(unittest.TestCase):

    def test_hill_climbing_algorithm(self):

        hca = challenges.HillClimbing()

        self.assertEqual(hca.find_pahts_iterative(data.hill_climbing_grid_simple),31)
        self.assertEqual(hca.first_a, 29)




if __name__ == '__main__':

    unittest.main()