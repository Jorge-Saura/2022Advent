#--- Day 9: Rope Bridge ---

import unittest

import day09.day09 as challenges
import day09.day09_data as data

class TestDay09(unittest.TestCase):

    def test_rope_bridge(self): 

        r = challenges.Rope()

        self.assertEqual(r._decode_movements("U 1\nL 3"),[('U',1),('L',3)])
        
        self.assertEqual(r.move_rope(data.rope_moves),13)

        self.assertEqual(r.move_rope_10_knots(data.rope_moves),1)

        self.assertEqual(r.move_rope_10_knots(data.rope_moves1),36)



if __name__ == "__main__":

    unittest.main()