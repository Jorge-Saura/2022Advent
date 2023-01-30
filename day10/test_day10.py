import unittest

import day11.day11 as challenges
import day11.day11_data as data

class TestDay11(unittest.TestCase):

    def test_cathode_ray_tube(self):

        crt = challenges.CathodeRayTube()
        noop = crt._decode_instruction("noop")
        expected = challenges.Instruction('noop',1,0)
        self.assertEqual(noop.type_op, expected.type_op), self.assertEqual(noop.duration, expected.duration), self.assertEqual(noop.value, expected.value)
        addx = crt._decode_instruction("addx 5")
        expected = challenges.Instruction('addx',2,5)
        self.assertEqual(addx.type_op, expected.type_op), self.assertEqual(addx.duration, expected.duration), self.assertEqual(addx.value, expected.value)

        self.assertEqual(crt.execute_program(data.cpu_instructions),13140)

        self.assertEqual(crt.execute_program2(data.cpu_instructions),data.screen)




if __name__ == "__main__":

    unittest.main()