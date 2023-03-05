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
        self.grid_columns = list()


    def _move_right(self, row:gridRow, movement: int, starting_postion:int) ->  int:

        next_position = starting_postion + movement
        # we have walls en the line
        if row.walls:
                # I have at least one wall in my wall.
                if row.walls[-1] > starting_postion:
                    next_wall = next(x for x in row.walls if x > starting_postion)
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
                            starting_postion = row.left
                            movement = next_position - (row.right + 1)
                            return self._move_right(row, movement, starting_postion)
                        
        # there is no wall        
        else:
            next_position = (movement + (self.x - row.right - 1)) % (row.right - row.left + 1) 
            return next_position + row.left
            
    def _move_left(self, row:gridRow, movement: int, starting_postion:int) ->  int:

        next_position = starting_postion - movement
        # we have walls en the line
        if row.walls:
                # I have at least one wall in my line.
                if row.walls[0] < starting_postion:

                    next_wall = next(x for x in row.walls[::-1] if x < starting_postion)
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
                            movement = movement + - 1 - (starting_postion - row.left)
                            starting_postion = row.right
                            return self._move_left(row, movement, starting_postion)
                        
        # there is no wall        
        else:
            if next_position > 0:
                return next_position
            else:
                next_position = (movement - (self.x - row.left + 1)) % (row.right - row.left + 1)
                return row.right - next_position
            
    def move(self, movement) -> None:
        if isinstance(movement,str):
            #gira
            if movement == 'R': self.direction_index = self.direction_index + 1 if self.direction_index < 3 else 0 
            if movement == 'L': self.direction_index = self.direction_index - 1 if self.direction_index > 0 else 3 

        if isinstance(movement,int):
            row = self.grid_rows[self.y - 1]

            column = self.grid_columns[self.x - 1]


            if self.direction_index == 0: #RIGHT direction 
                self.x = self._move_right(row, movement, self.x)
            if self.direction_index == 2: #LEFT direction 
                self.x = self._move_left(row, movement, self.x)

            if self.direction_index == 1: #DOWN direction 
                self.y = self._move_right(column, movement, self.y)
            if self.direction_index == 3: #UP direction 
                self.y = self._move_left(column, movement, self.y)
            






class MonkeyMap:

    # def __init__(self) -> None:
    #     # self.grid_rows  = list()

    def _find_all(self, complete_string:str, substring:str) -> list[str]:
        start = 0
        while True:
            start = complete_string.find(substring, start)
            if start == -1: return
            yield start + 1
            start += len(substring) # use start += 1 to find overlapping matches

    def _get_gridRow_from_line(self, line:str) -> gridRow:

        position_left = (min(line.index('.'), line.index('#'))) + 1 if '#' in line else line.index('.') + 1
        line_length = len(line)
        line_rvs = line[::-1]
        position_right = max(line_length - line_rvs.index('.'), line_length - line_rvs.index('#')) if '#' in line else line_length - line_rvs.index('.')

        walls_postions = list(self._find_all(line,'#'))

        grid_row = gridRow(position_left,position_right,walls_postions)

        return grid_row

    def _decode_path(self, path:str) -> list:
        decoded_path = list()
        temp = ''
        for c in path:
            if c in['R','L']:
                decoded_path.append(int(temp))
                decoded_path.append(c)
                temp = ''
            else:
                temp += c
        decoded_path.append(int(temp))
        return decoded_path

    def _decode_input(self, input:str) -> list[str]:

        
        grid_str, path = input.split('\n\n')

        # rows of the grid
        grid_lines = grid_str.split('\n')

        max_line_length = 0        
        grid_rows = list()
        for line in grid_lines:
            max_line_length = max(max_line_length, len(line))
            grid_rows.append(self._get_gridRow_from_line(line))

        grid_columns = list()

        # columns of the grid
        grid_vertical_lines = [''] * max_line_length
        for line in grid_lines:
            line_with_padding = line
            if len(line_with_padding) < max_line_length:
                line_with_padding = f"{line_with_padding:{max_line_length}}"
            grid_vertical_lines = [x + y for x,y in zip(grid_vertical_lines, line_with_padding)]        
        
        
        for line in grid_vertical_lines:
            grid_columns.append(self._get_gridRow_from_line(line))

        path = self._decode_path(path)

        return grid_rows, grid_columns, path

    def get_path_password(self, input:str):

        grid_rows, grid_columns, path = self._decode_input(input)

        grid_pointer = pointer()
        grid_pointer.grid_columns = grid_columns
        grid_pointer.grid_rows = grid_rows

        grid_pointer.x = grid_rows[0].left

        
        for item in path:
            grid_pointer.move(item)

        result = (grid_pointer.y * 1000) + (grid_pointer.x * 4) + grid_pointer.direction_index

        return result





        



        pass


