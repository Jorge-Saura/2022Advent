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


    def test_pointer_rotation(self):

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

    def test_pointer_right_movement(self):

        # simple right movement with wall in front
        p = challenges.pointer()
        grid_rows = [challenges.gridRow(1,6,[5]),challenges.gridRow(1,6,[4])]
        p.grid_rows = grid_rows
        p.move(10)
        self.assertEqual(p.x,4, 'simple movement with wall in front')

        # simple right movement between two walls
        grid_rows = [challenges.gridRow(1,6,[2,6]),challenges.gridRow(1,6,[4])]
        p.x = 3
        p.grid_rows = grid_rows
        p.move(10)
        self.assertEqual(p.x,5,'simple movement between two walls')

        # simple right movement with no walls
        grid_rows = [challenges.gridRow(1,6,[]),challenges.gridRow(1,6,[4])]
        p.x = 1
        p.grid_rows = grid_rows
        p.move(3)
        self.assertEqual(p.x,4, 'simple movement with no walls')
        
        # turn back right movement with  walls at beginning of the line
        grid_rows = [challenges.gridRow(1,6,[1]),challenges.gridRow(1,6,[4])]
        p.x = 1
        p.grid_rows = grid_rows
        p.move(10)
        self.assertEqual(p.x,6,'turn back movement with  walls at beginning of the line')
        
        # turn back right movement without  walls at beginning of the wall
        grid_rows = [challenges.gridRow(1,6,[]),challenges.gridRow(1,6,[4])]
        p.x = 1
        p.grid_rows = grid_rows
        p.move(10)
        self.assertEqual(p.x,5, 'turn back movement without  walls at beginning of the wall')
        p.x= 1
        p.move(18)
        self.assertEqual(p.x,1, 'turn back movement without  walls at beginning of the wall')
        
    def test_pointer_left_movement(self):

        
        p = challenges.pointer()
        p.direction_index = 2

        # simple left movement 0
        grid_rows = [challenges.gridRow(1,6,[]),challenges.gridRow(1,6,[4])]
        p.x = 4
        p.grid_rows = grid_rows
        p.move(0)
        self.assertEqual(p.x,4, 'simple left movement 0')
       
        # turn back left movement with no walls
        grid_rows = [challenges.gridRow(1,6,[]),challenges.gridRow(1,6,[4])]
        p.x = 2
        p.grid_rows = grid_rows
        p.move(10)
        self.assertEqual(p.x,4, 'turn back left movement with no walls')       

        # simple left movement with wall behind, not reaching the wall
        grid_rows = [challenges.gridRow(1,6,[2]),challenges.gridRow(1,6,[4])]
        p.grid_rows = grid_rows
        p.x = 6
        p.move(2)
        self.assertEqual(p.x,4, 'simple left movement with wall behind, not reaching the wall')

        # simple left movement with wall behind
        grid_rows = [challenges.gridRow(1,6,[2]),challenges.gridRow(1,6,[4])]
        p.grid_rows = grid_rows
        p.x = 5
        p.move(10)
        self.assertEqual(p.x,3, 'simple left movement with wall behind')

        # turn back left movement with wall at the end of the line
        grid_rows = [challenges.gridRow(1,6,[6]),challenges.gridRow(1,6,[4])]
        p.grid_rows = grid_rows
        p.x = 2
        p.move(4)
        self.assertEqual(p.x,1, 'turn back left movement with wall at the end of the line')

        # turn back left movement with wall at middle of the line but not reaching the wall
        grid_rows = [challenges.gridRow(1,6,[3]),challenges.gridRow(1,6,[4])]
        p.grid_rows = grid_rows
        p.x = 2
        p.move(3)
        self.assertEqual(p.x, 5, 'turn back left movement with wall at middle of the line but not reaching the wall')

        # turn back left movement with wall at middle of the line reaching the wall
        grid_rows = [challenges.gridRow(1,6,[3]),challenges.gridRow(1,6,[4])]
        p.grid_rows = grid_rows
        p.x = 2
        p.move(13)
        self.assertEqual(p.x, 4, 'turn back left movement with wall at middle of the line reaching the wall')

                # turn back left movement with wall at middle of the line reaching the wall
        grid_rows = [challenges.gridRow(6,11,[8]),challenges.gridRow(6,11,[8])]
        p.grid_rows = grid_rows
        p.x = 7
        p.move(13)
        self.assertEqual(p.x, 9, 'turn back left movement with wall at middle of the line reaching the wall')

    def test_decode_input(self):
        mm = challenges.MonkeyMap()

        path = mm._decode_path('10R1L')
        self.assertListEqual(path,[10,'R',1,'L'])

    def test_get_password(self):
        mm = challenges.MonkeyMap()
        result = mm.get_path_password(data.force_field)
        self.assertEqual(result, 6032)

        result = mm.get_path_password(data.force_field_full)
        self.assertEqual(result, 6032)

if __name__ == "__main__":

    suite = unittest.TestLoader().loadTestsFromTestCase(TestDay22)
    unittest.TextTestRunner(verbosity=0).run(suite)    

