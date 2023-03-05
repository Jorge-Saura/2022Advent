import unittest
import time

import day22.day22 as challenges
import day22.day22_data as data

class TestDay22(unittest.TestCase):

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))        


    def test_monkey_map(self):

        mm = challenges.MonkeyMap()
        







if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(TestDay22)
    unittest.TextTestRunner(verbosity=0).run(suite)    

