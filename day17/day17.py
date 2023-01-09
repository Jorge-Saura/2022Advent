#--- Day 17: Pyroclastic Flow --

import math
class Rock:
    lines = None
    rock_type = None
    
    
    # def move_horizontal(self, value:int): 
    #     left = 127 # 1000000
    #     right = 1  # 0000001

    #     comparator = left if value < 0 else right
    #     for _ in range(abs(value)):
    #         for idx, line in self.lines:
    #             if any([x & comparator for x in self.lines]):
    #                 pass
    #             else:
    #                 self.lines[idx] = line << 1 if value < 0 else line >> 1

    def move_horizontal(self, movements:list[int]):


        left = 127 # 1000000
        right = 1  # 0000001
    
        for move in movements:
            if move > 0:
                right_spaces = min([int(math.log2(x & -x) + 1) for x in self.lines]) - 1
                movements = min(move , right_spaces)
                self.lines = [line >> movements for line in self.lines]
                
            else:
                left_spaces = 7 - max([int(math.log2(x))+1 for x in self.lines])
                movements = min (abs(move), left_spaces)
                self.lines = [line << movements for line in self.lines]



    def move_vertically(self, value:int, destination_line:int):

        for idx, line in self.lines:
            self.lines[idx] = line << 1

class RockHorizontal(Rock):

    def __init__(self) -> None:
        super().__init__()

        # 30 -> 0011110
        self.lines = [30]
        self.rock_type = 0

class RockCross(Rock):

    def __init__(self) -> None:
        super().__init__()

        self.lines = [8, 28, 8]
        self.rock_type = 1

class RockSimetricL(Rock):

    def __init__(self) -> None:
        super().__init__()
        
        self.lines = [28, 4, 4]
        self.rock_type = 2

class RockVertical(Rock):

    def __init__(self) -> None:
        super().__init__()

        self.lines = [16, 16, 16, 16] 
        self.rock_type = 3

class RockSquare(Rock):

    def __init__(self) -> None:
        super().__init__()

        self.lines = [24,24]
        self.rock_type = 4

class RocksGenerator:
    step = -1

    def create_rock(self) -> Rock:
        
        self.step += 1
        rock_type = self.step % 5

        if rock_type == 0: return RockHorizontal()
        if rock_type == 1: return RockCross()
        if rock_type == 2: return RockSimetricL()
        if rock_type == 3: return RockVertical()
        if rock_type == 4: return RockSquare()

class Chamber:
    levels = None

    def __init__(self) -> None:
         level0 = 127 # 1111111
         self.levels = list()
         self.levels.append(level0)
         
    def get_max_level(self) -> int:
        return len(self.levels) - 1

    def save_snapshot(self):
        mode = 'w' 

        with open('FloorBinary.txt', mode) as f:
            inversed = self.levels.copy()
            inversed.reverse()
            f.write('\n\n')
            for idx, num in enumerate(inversed):

                text_level = f"{num:07b}".replace('0','.').replace("1","#")
                if idx == len(inversed)-1:
                    text_level = '+-------+' + '\n'
                else:
                    text_level = '|' + text_level + '|' + '\n'
                f.write(text_level) 

class ChamberController:

    def _check_collision(self, chamber:list[int], rock:list[int]) -> bool:

        length = min([len(chamber),len(rock)])
        for i in range(length):
            if chamber[i] & rock[i]:
                return True

        return False

    def fall_rocks(self, num_rocks:int, gas:str, print_snapshot:bool = False) -> int:

        chamber =  Chamber()
        generator = RocksGenerator()
        
        gas_values = [-1 if x == '<' else 1 for x in gas ]
        gas_index = 0
        gas_length= len(gas)

        sequences = dict()
        height = dict()

        # we gonna try to find repetead sequences. if this happens we can calculate total height
        height_before_seq1 = 0
        height_seq1 = 0
        num_of_seq1 = 0
        height_after_seq1 = 0



        for idx in range(num_rocks):
            
            rock = generator.create_rock()
                
            movements = [gas_values[gas_index % gas_length], gas_values[(gas_index + 1)  % gas_length], gas_values[(gas_index + 2)  % gas_length], gas_values[(gas_index + 3)  % gas_length]]
            gas_index += 4

            rock.move_horizontal(movements)
            chamber_max_level = chamber.get_max_level()
            if chamber_max_level >=385:
                z = 0
            chamber_index = chamber_max_level
            chamber_chunk_to_test = chamber.levels[chamber_index:chamber_index + 3]
            while not self._check_collision(chamber_chunk_to_test, rock.lines):
                # move rock horizontally
                movement = gas_values[gas_index % gas_length]
                gas_index += 1
                rock.move_horizontal([movement])
                if self._check_collision(chamber_chunk_to_test, rock.lines):
                    rock.move_horizontal([-movement])
                
                # prepare for check the next level
                chamber_index -= 1
                chamber_chunk_to_test = chamber.levels[chamber_index:]

            for line in rock.lines:
                if chamber_index < chamber_max_level:
                    #'or' lines
                    chamber.levels[chamber_index + 1] = chamber.levels[chamber_index + 1] | line
                    chamber_index += 1
                    
                else:
                    #add line
                    chamber.levels.append(line)
            
            current_seq = sequences.get((rock.rock_type, gas_index % gas_length),[])
            current_seq.append(idx)
            sequences[(rock.rock_type, gas_index % gas_length)] = current_seq
            height[idx] = chamber.get_max_level()

            if len(current_seq) > 2: # possible repeat
                start, middle, end = current_seq[-3:]

                seq1 = chamber.levels[height[start + 1]:height[middle]]
                seq2 = chamber.levels[height[middle + 1]:height[end]]

                if seq1 == seq2:
                    height_before_seq1 = height[start]
                    height_seq1 = height[middle] - height[start]

                    start_seq_rocks = num_rocks - start
                    num_of_seq1 = start_seq_rocks // (middle - start)
                    remaining_rocks = start_seq_rocks % (middle - start)

                    height_after_seq1 = height[start + remaining_rocks -1] - height[start]


                    break
                
        if print_snapshot:
            chamber.save_snapshot()

        total_height = chamber.get_max_level()
        if num_of_seq1 != 0:
            total_height = height_before_seq1 + (height_seq1 * num_of_seq1) + height_after_seq1
            
        return total_height

