import unittest

import day17.day17_data as data

import day17.day17 as challenges



class TestDay17(unittest.TestCase):

    def test_pyroclastic_flow_binary(self):
        
        cc = challenges.ChamberController()

        rock = challenges.RockHorizontal()
        rock.move_horizontal([-1])
        self.assertEqual(rock.lines,[60])
        rock.move_horizontal([-5])
        self.assertEqual(rock.lines,[120])

        rock.move_horizontal([1])
        self.assertEqual(rock.lines,[60])

        rock.move_horizontal([5])
        self.assertEqual(rock.lines,[15])


        rock = challenges.RockCross()
        chamber = [127]
        self.assertEqual(cc._check_collision(chamber, rock.lines),True)
            
        chamber = [0]
        self.assertEqual(cc._check_collision(chamber, rock.lines),False)

        chamber = [2]
        self.assertEqual(cc._check_collision(chamber, rock.lines),False)


        self.assertEqual(cc.fall_rocks(10, data.gas_pattern),17)
        self.assertEqual(cc.fall_rocks(2022, data.gas_pattern),3068)

        self.assertEqual(cc.fall_rocks(2022, data.gas_pattern1),3048)

        self.assertEqual(cc.fall_rocks(1000000000000, data.gas_pattern),1514285714288)

        self.assertEqual(cc.fall_rocks(1000000000000, data.gas_pattern1),1504093567249)



if __name__ == '__main__':

    unittest.main()