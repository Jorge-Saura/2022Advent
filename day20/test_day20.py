import unittest
import time

import day20.day20 as challenges
import day20.day20_data as data

class TestDay20(unittest.TestCase):

    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))        


    def test_decryption(self):

        do = challenges.DecrypterOperator()
        l = do._decode_input(data.encrypted_basic)
        self.assertEqual(do.decrypt(l), [1, 2, -3, 4, 0, 3, -2])
       
        self.assertEqual(do.get_coordenates(data.encrypted_basic), 3)

        self.assertEqual(do.get_coordenates(data.encrypted_file), 10763)



if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(TestDay20)
    unittest.TextTestRunner(verbosity=0).run(suite)    
