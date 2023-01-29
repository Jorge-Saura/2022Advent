import unittest
import time

import day21.day21 as challenges
import day21.day21_data as data

class TestDay21(unittest.TestCase):

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))        


    def test_monkey_yelling(self):

        mm = challenges.MonkeyMath()

        value = mm.calculate_math(data.monkeys_basic_yelling, 'root')
        self.assertEqual(value, 152)

        value = mm.calculate_math(data.monkeys_complex_yelling, 'root')
        self.assertEqual(value, 110181395003396)


        value = mm.calculate_math2(data.monkeys_basic_yelling, 'root')
        self.assertEqual(value, 301)

        value = mm.calculate_math2(data.monkeys_complex_yelling, 'root')
        self.assertEqual(value, 3721298272959)






if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(TestDay21)
    unittest.TextTestRunner(verbosity=0).run(suite)    

