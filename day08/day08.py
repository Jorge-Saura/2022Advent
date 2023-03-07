#--- Day 8: Treetop Tree House ---

import numpy as np

class TreeVisibility:
    
    tree_grid = None
    tree_grid_transposed = NotImplementedError
    
    def _decode_data(self, input:str)-> list[str]:
        result = []
        lines = input.split('\n')
        for line in lines:
            result.append(list(line))
        return result
    
    def _is_visible_horizontally(self, tree:int, tree_grid:list[str], point:tuple()) -> bool:
        idx_h, idx_v = point

        max_left = int(max(tree_grid[idx_v][0:idx_h]))
        if max_left < tree:
            return True

        max_right = int(max(tree_grid[idx_v][idx_h+1:]))
        if max_right < tree:
            return True

        return False

    def _is_visible_vertically(self, tree:int, tree_grid:list[str], point:tuple()) -> bool:
        point = (point[1],point[0])
        return self._is_visible_horizontally(tree, tree_grid,point)

    def get_number_of_visible_trees(self, input:str) -> int:

        self.tree_grid = self._decode_data(input)
        self.tree_grid_transposed = np.transpose(self.tree_grid).tolist()
        num_visible_trees = (len(self.tree_grid) + len(self.tree_grid[0]) -2 ) * 2 # the edges

        for idx_v, line in enumerate(self.tree_grid [1:-1]):
            for idx_h, tree in enumerate(line[1:-1]):
                point = (idx_h+1, idx_v+1)
                if self._is_visible_horizontally(int(tree), self.tree_grid,point):
                    num_visible_trees += 1
                elif self._is_visible_vertically(int(tree), self.tree_grid_transposed,point):
                   num_visible_trees += 1
        
        return num_visible_trees

    def _get_scenic_score(self, point:tuple()) -> int:
        line_h = self.tree_grid[point[1]]
        line_v = self.tree_grid_transposed[point[0]]

        tree = self.tree_grid[point[1]][point[0]]
        score_left = 0
        for idx in range(point[0]-1,-1,-1):
            score_left +=1
            if(line_h[idx]>=tree):
                break
        score_right = 0
        for ele in line_h[point[0]+1:]:
            score_right +=1
            if(ele>=tree):
                break

        score_up = 0
        for idx in range(point[1]-1,-1,-1):
            score_up +=1
            if(line_v[idx]>=tree):
                break
        score_down = 0
        for ele in line_v[point[1]+1:]:
            score_down +=1
            if(ele>=tree):
                break

        return score_up * score_down * score_left * score_right

    def get_best_scenic_score(self, input:str) -> int:

        self.tree_grid = self._decode_data(input)
        self.tree_grid_transposed = np.transpose(self.tree_grid).tolist()
        best_score = 0

        for idx_v, line in enumerate(self.tree_grid [1:-1]):
            for idx_h, tree in enumerate(line[1:-1]):
                point = (idx_h+1, idx_v+1)

                curent_score = self._get_scenic_score(point)
                best_score = max(curent_score, best_score )
        
        return best_score
