#--- Day 8: Treetop Tree House ---

import unittest

import day08.day08 as challenges
import day08.day08_data as data

class TestDay08(unittest.TestCase):

    def test_tree_visibility(self):

        tv = challenges.TreeVisibility()

        grid = tv._decode_data(data.tree_grid_simple)

        self.assertEqual(tv._is_visible_horizontally(2,grid,(1,1)), True)
        self.assertEqual(tv._is_visible_horizontally(0,grid,(1,1)), False)

        self.assertEqual(tv.get_number_of_visible_trees(data.tree_grid_simple),8)
        self.assertEqual(tv.get_number_of_visible_trees(data.tree_grid),21)

        self.assertEqual(tv._get_scenic_score((2,1)),4)
        self.assertEqual(tv._get_scenic_score((2,3)),8)
        self.assertEqual(tv.get_best_scenic_score(data.tree_grid),8)



if __name__ == "__main__":

    unittest.main()