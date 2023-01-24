import unittest

import day13.day13_data as data

import day13.day13 as challenges



class TestDay13(unittest.TestCase):

    
    def test_distress_signal(self):
            
            ds = challenges.DistressSignal()

            self.assertEqual(ds._transforn_to_list("[1]"),[1])       
            self.assertEqual(ds._transforn_to_list("[1,2,3,4]"),[1,2,3,4])
            self.assertEqual(ds._transforn_to_list("[[1],2,3,4]"),[[1],2,3,4])    
            self.assertEqual(ds._transforn_to_list("[[4,4],4,4]"),[[4,4],4,4])   
            self.assertEqual(ds._transforn_to_list("[[4,4],4,4]"),[[4,4],4,4]) 
            self.assertEqual(ds._transforn_to_list("[[[]]]"),[[[]]]) 
            self.assertEqual(ds._transforn_to_list("[1,[2,[3,[4,[5,6,7]]]],8,9]"),[1,[2,[3,[4,[5,6,7]]]],8,9])
            self.assertEqual(ds._transforn_to_list("[[[[[4]],4]],4,4]"),[[[[[4]],4]],4,4]) 
            
            l1, l2= [1,1,3,1,1], [1,1,5,1,1]
            self.assertEqual(ds._check_right_order(l1,l2), True)

            l1, l2= [[1],[2,3,4]], [[1],4]
            self.assertEqual(ds._check_right_order(l1,l2), True)
            
            l1, l2= [[4,4],4,4], [[4,4],4,4,4]
            self.assertEqual(ds._check_right_order(l1,l2), True)

            l1, l2= [[],4,4], [[0],4,4,4]
            self.assertEqual(ds._check_right_order(l1,l2), True)

            l1 = [[[[0, 3, 7], 3, [4, 0], [6, 2, 0], 4], 1, [[3, 4, 7], 8, [1]], 2]]
            l2 = [[0, 6, [[6, 9, 6], 9, [0], [2, 10]], 4]]
            self.assertEqual(ds._check_right_order(l1,l2), False)

            l1 = [[[[], 9, [8, 8, 9, 10, 9]], [], 10, 10], [10, [], 0]]
            l2 = [[0, [], 6, 3, [[], []]], [7, [8]], [[[4, 3, 3, 2, 9], 10, 4, []], 5], []]
            self.assertEqual(ds._check_right_order(l1,l2), True)

            self.assertEqual(ds.sum_indexes_right_order(data.signal_simple), 13)

            self.assertEqual(ds.get_decoder_key(data.signal_simple), 140)








if __name__ == '__main__':

    unittest.main()