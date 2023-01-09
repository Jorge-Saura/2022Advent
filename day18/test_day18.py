import unittest

import day18.day18_data as data

import day18.day18 as challenges



class TestDay18(unittest.TestCase):

    def test_boiling_boulders(self):

        bc = challenges.BouldersController()
        coords = bc._decode_input(data.obsidian_cubes)
        self.assertEqual(len(coords),13)
        self.assertEqual(coords[0],(2,2,2))

        self.assertEqual(bc._sum_tuple((0,1,0),(0,1,1)),(0,2,1))

        self.assertEqual(bc.count_areas(data.obsidian_simple), 10)

        self.assertEqual(bc.count_areas(data.obsidian_cubes), 64)
        self.assertEqual(bc.count_areas(data.obsidian_empty_cube), 204)
        self.assertEqual(bc.count_areas(data.obsidian_empty_star), 36)
        self.assertEqual(bc.count_areas(data.obsidian_complex), 3396)

        self.assertEqual(bc.count_superficial_areas(data.obsidian_empty_cube), 150)
        self.assertEqual(bc.count_superficial_areas(data.obsidian_empty_star), 30)
        self.assertEqual(bc.count_superficial_areas(data.obsidian_cubes), 58)
        self.assertEqual(bc.count_superficial_areas(data.obsidian_complex), 2044)


if __name__ == '__main__':

    unittest.main()