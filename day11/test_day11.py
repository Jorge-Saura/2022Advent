import unittest

import day11.day11 as challenges
import day11.day11_data as data

class TestDay11(unittest.TestCase):

    def test_monkeys_business(self):

        mb = challenges.MonkeyBusiness()
        monkey_atrrs = mb._decode_input(data.monkeys_attrs_simple)

        self.assertEqual(len(monkey_atrrs),4)

        self.assertEqual(mb.get_business(data.monkeys_attrs_simple,20),10605)

        self.assertEqual(mb.get_business2(data.monkeys_attrs_simple,10000),52166 * 52013)



if __name__ == "__main__":

    unittest.main()