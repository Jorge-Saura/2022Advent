#--- Day 22: Monkey Map ----

# Our gridLines starts in position 1.
class gridRow:

    def __init__(self, limit_left:int, limit_right:int, walls_positions:list[int]) -> None:
        self.left = limit_left
        self.right = limit_right
        self.walls = walls_positions


class pointer:
    directions = ['R','D','L','U']

    def __init__(self) -> None:
        self.x = 1
        self.y = 1
        self.direction_index = 0 # R -> right, L -> left, U -> up, D -> down
        self.grid_rows = list()


    def _move_right(self, row:gridRow, movement: int) ->  int:

        next_position = self.x + movement
        # we have walls en the line
        if row.walls:
                # I have at least one wall in my wall.
                if row.walls[-1] > self.x:
                    next_wall = next(x for x in row.walls if x > self.x)
                    return min(next_position, next_wall - 1)
                # I dont have wall between my position and the end of the line
                else:
                    # I dont reach the end of the line
                    if next_position <= row.right:
                        return next_position
                    # I have to turn around to the beginning of the line
                    else:
                        # first position is a wall, I can not move beyond the end of the grid
                        if row.left == row.walls[0]:
                            return row.right
                        else:
                            self.x = row.left
                            movement = next_position - (row.right + 1)
                            return self._move_right(row,movement)
                        
        # there is no wall        
        else:
            next_position = next_position % (row.right - row.left + 1)
            return next_position
            
    def _move_left(self, row:gridRow, movement: int) ->  int:

        next_position = self.x - movement
        # we have walls en the line
        if row.walls:
                # I have at least one wall in my line.
                if row.walls[0] < self.x:

                    next_wall = next(x for x in row.walls[::-1] if x < self.x)
                    return max(next_position, next_wall + 1)
                # I dont have wall between my position and the beginning of the line
                else:
                    # I dont reach the beginning of the line
                    if next_position >= row.left:
                        return next_position
                    # I have to turn around to the end of the line
                    else:
                        # last position is a wall, I can not move beyond the beginning of the grid
                        if row.right == row.walls[-1]:
                            return row.left
                        else:
                            movement = movement + - 1 - (self.x - row.left)
                            self.x = row.right
                            return self._move_left(row,movement)
                        
        # there is no wall        
        else:
            if next_position > 0:
                return next_position
            else:
                next_position = abs(next_position) % (row.right - row.left + 1)
                return row.right - next_position
            


    def move(self, movement) -> None:
        if isinstance(movement,str):
            #gira
            if movement == 'R': self.direction_index = self.direction_index + 1 if self.direction_index < 3 else 0 
            if movement == 'L': self.direction_index = self.direction_index - 1 if self.direction_index > 0 else 3 

        if isinstance(movement,int):
            row = self.grid_rows[self.y - 1]


            if self.direction_index == 0: #RIGHT direction 
                self.x = self._move_right(row, movement)
            if self.direction_index == 2: #LEFT direction 
                self.x = self._move_left(row, movement)
            






class MonkeyMap:

    # def __init__(self) -> None:
    #     # self.grid_rows  = list()

    def find_all(self, complete_string:str, substring:str) -> list[str]:
        start = 0
        while True:
            start = complete_string.find(substring, start)
            if start == -1: return
            yield start + 1
            start += len(substring) # use start += 1 to find overlapping matches

    def _decode_input(self, input:str) -> list[str]:

        
        grid_str, path = input.split('\n\n')

        grid_lines = grid_str.split('\n')
        grid_rows = list()
        for line in grid_lines:
            position_left = (min(line.index('.'), line.index('#')) + 1) if '#' in line else line.index('.')
            line_length = len(line)
            line_rvs = line[::-1]
            position_right = max(line_length - line_rvs.index('.'), line_length - line_rvs.index('')) if '#' in line else line_length - line_rvs.index('.')

            walls_postions = list(self.find_all(line,'#'))

            grid_row = gridRow(position_left,position_right,walls_postions)
            grid_rows.append(grid_row)

        return grid_rows, path

    def get_path_password(self, input:str):

        grid_rows, path = self._decode_input(input)



        pass


