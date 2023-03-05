#--- Day 22: Monkey Map ----

# Our gridLines starts in position 1.
class gridRow:

    def __init__(self, limit_left:int, limi_right:int, walls_positions:list[int]) -> None:
        self.left = limit_left
        self.right = limi_right
        self.walls = walls_positions

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

        return 1


