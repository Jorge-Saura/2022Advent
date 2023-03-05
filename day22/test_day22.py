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


    def test_pointer_movement(self):

        p = challenges.pointer()

        p.move('R')
        self.assertEqual(p.direction_index, 1)

        p.direction_index = 3
        p.move('R')
        self.assertEqual(p.direction_index, 0)
        
        p.move('L')
        self.assertEqual(p.direction_index, 3)
        p.move('L')
        self.assertEqual(p.direction_index, 2)

        # simple right movement with wall in front
        p = challenges.pointer()
        grid_rows = [challenges.gridRow(1,6,[5]),challenges.gridRow(1,6,[4])]
        p.grid_rows = grid_rows
        p.move(10)
        self.assertEqual(p.x,4, 'simple movement with wall in front')

        # simple right movement between two walls
        p = challenges.pointer()
        grid_rows = [challenges.gridRow(1,6,[2,6]),challenges.gridRow(1,6,[4])]
        p.x = 3
        p.grid_rows = grid_rows
        p.move(10)
        self.assertEqual(p.x,5,'simple movement between two walls')

        # simple right movement with no walls
        p = challenges.pointer()
        grid_rows = [challenges.gridRow(1,6,[]),challenges.gridRow(1,6,[4])]
        p.grid_rows = grid_rows
        p.move(3)
        self.assertEqual(p.x,4, 'simple movement with no walls')
        
        # turn back right movement with  walls at beginning of the line
        p = challenges.pointer()
        grid_rows = [challenges.gridRow(1,6,[1]),challenges.gridRow(1,6,[4])]
        p.grid_rows = grid_rows
        p.move(10)
        self.assertEqual(p.x,6,'turn back movement with  walls at beginning of the line')
        
        # turn back right movement without  walls at beginning of the wall
        p = challenges.pointer()
        grid_rows = [challenges.gridRow(1,6,[]),challenges.gridRow(1,6,[4])]
        p.grid_rows = grid_rows
        p.move(10)
        self.assertEqual(p.x,5, 'turn back movement without  walls at beginning of the wall')
        p.x= 1
        p.move(18)
        self.assertEqual(p.x,1, 'turn back movement without  walls at beginning of the wall')
        # turn back left movement with no walls
        # p = challenges.pointer()
        # grid_rows = [challenges.gridRow(1,6,[]),challenges.gridRow(1,6,[4])]
        # p.x = 2
        # p.direction_index = 2
        # p.grid_rows = grid_rows
        # p.move(5)
        # self.assertEqual(p.x,3, 'turn back left movement with no walls')
       

        # mm.get_path_password(data.force_field)
        







if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(TestDay22)
    unittest.TextTestRunner(verbosity=0).run(suite)    

