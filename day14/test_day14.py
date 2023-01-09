import unittest

import day14.day14_data as data

import day14.day14 as challenges



class TestDay14(unittest.TestCase):

    
    def test_regolith_source(self):

        rs = challenges.RegolithSource()

        result = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (10, 4), (10, 3), (10, 2), (10, 1), (10, 0), (9, 0), (8, 0), (8, 1), (8, 2)]
        self.assertCountEqual(rs._get_points('0,0 -> 5,0 -> 5,5 -> 10,5 -> 10,0 -> 8,0 -> 8,2'), result)
        self.assertCountEqual(rs._get_points('498,4 -> 498,6 -> 496,6'),[(498,4), (498,5), (498,6), (497,6), (496,6)])

        self.assertCountEqual(rs._decode_input(data.regolith_simple),[(498,4), (498,5), (498,6), (497,6), (496,6), (503,4), (502,4)])

        self.assertEqual(rs.get_sand_packets(data.regolith_basic), 24)

        self.assertEqual(rs.get_sand_packets(data.regolith_basic1), 672)

        self.assertEqual(rs.get_sand_packets_with_floor(data.regolith_basic), 93)

        self.assertEqual(rs.get_sand_packets_with_floor(data.regolith_basic1), 26831)






if __name__ == '__main__':

    unittest.main()