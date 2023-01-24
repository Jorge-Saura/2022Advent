
#--- Day 12: Hill Climbing Algorithm ---

from collections import deque

class HillClimbing:
    
    grid = None
    startPoint = None
    endPoint = None

    first_a = None

    def _decode_input(self, input:str) -> list[list[int]]:
        lines = input.split('\n')

        self.grid = []
        for idx_v,line in enumerate(lines):
            horizontal = []
            for idx_h,letter in enumerate(line):
                
                if letter == 'S':
                    self.startPoint = (idx_h,idx_v)
                    horizontal.append(0) # --> a = 0
                elif letter == 'E':
                    self.endPoint = (idx_h,idx_v)
                    horizontal.append(25) # --> z = 25
                else:
                    horizontal.append(ord(letter)-97)
            
            self.grid.append(horizontal)
        
        print(self.grid)


    def _get_possible_points(self, point:tuple, visited_points:set[tuple]) -> list[tuple]:
        result = list()
        
        value = self.grid[point[1]][point[0]]

        #up 
        if (point[1] - 1) >= 0 :
            value_up = self.grid[point[1] - 1][point[0]]
            if (point[0], point[1] - 1) not in visited_points and (value - value_up) <= 1:
                result.append((point[0], point[1] - 1))

        #down
        if (point[1] + 1)  < len(self.grid):
            value_down = self.grid[point[1] + 1][point[0]]
            if (point[0], point[1] + 1) not in visited_points and (value - value_down) <= 1:
                result.append((point[0], point[1] + 1))
           
        #right
        if (point[0] + 1) < len(self.grid[0]):
            value_right = self.grid[point[1]][point[0] + 1]
            if (point[0] + 1, point[1]) not in visited_points and (value - value_right) <= 1:
                result.append((point[0] + 1, point[1]))
            
        #left
        if (point[0] - 1) >= 0 :
            value_left = self.grid[point[1]][point[0] - 1]
            if (point[0] - 1, point[1]) not in visited_points and value - value_left <= 1:
                result.append((point[0] - 1, point[1]))

        return result

    def find_pahts_iterative(self, input:str) -> int:

        self._decode_input(input)
        results = []
        
        visited_points = set()
        possible_paths = list()
        possible_paths.append((self.endPoint,1))

        while possible_paths:

            current_point = possible_paths[0][0]
            current_length = possible_paths[0][1]


            if current_point not in visited_points:
                
                visited_points.add(current_point)
                possible_points = self._get_possible_points(current_point, visited_points)
    
                if possible_points:
                    for point in possible_points:
                        if point == self.startPoint:
                            results.append(current_length)
                        else:
                            if (self.grid[point[1]][point[0]]==0 and not self.first_a):
                                self.first_a = current_length

                            possible_paths.append((point,current_length+1))


            possible_paths.pop(0)
        
        results = min(results)

        return results


