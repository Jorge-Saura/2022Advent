import unittest

import day19.day19 as challenges
import day19.day19_data as data

class TestDay19(unittest.TestCase):

    def test_blueprints(self):

        bc = challenges.BlueprintsController()
        b = bc._decode_input(data.blueprints_basic)
        b1 = b[0]
        self.assertEqual(b1.id, 1)
        self.assertEqual(b1.ore_robot, [4,0,0,0])

        self.assertEqual(str(b1),"24_[0, 0, 0, 0]_[1, 0, 0, 0]")

        bp = challenges.Blueprint(1,[1,1,2,1],[1,1,2,1],[1,1,2,1],[1,1,2,1])
 
        new_bp = bp._copy()
        self.assertEqual(new_bp.id, bp.id)
        self.assertEqual(new_bp.ore_robot, bp.ore_robot)

        
        max = bc.geode_generator(data.blueprints_basic)
        self.assertEqual(max, 33)

        max = bc.geode_generator(data.blueprints_complex)
        self.assertEqual(max, 1725)

        max = bc.geode_generator2(data.blueprints_basic)
        self.assertEqual(max, 56*62)

        max = bc.geode_generator2(data.blueprints_complex)
        self.assertEqual(max, 15510)

if __name__ == "__main__":

    unittest.main()