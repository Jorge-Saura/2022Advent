# --- Day 1: Calorie Counting ---

class CaloriesService:
    def getMaxCalories(self, input:str) -> int:
        l = self._get_calories(input)
        return max(l)

    def get3MaxCalories(self, input:str) -> int:
        l = self._get_calories(input)
        l.sort()
        return sum(l[-3:])

    def _get_calories(self, input:str) -> list:
        grouped_calories = list()
        lines = input.split('\n')

        current_calories = 0
        for line in lines:
            if line:
                current_calories += int(line)
            else:
                grouped_calories.append(current_calories)
                current_calories = 0
        grouped_calories.append(current_calories)

        return grouped_calories


#--- Day 2: Rock Paper Scissors ---

class RPSGame:
    gambles_score ={"A X":3
                    ,"A Y":6
                    ,"A Z":0
                    ,"B Y":3
                    ,"B Z":6
                    ,"B X":0
                    ,"C Z":3
                    ,"C X":6
                    ,"C Y":0}

    moves_score = {"X":1
                  ,"Y":2
                  ,"Z":3}

    gamble_result = {"X":0
                    ,"Y":3
                    ,"Z":6}

    move_results = {"A":{0:"Z", 3:"X", 6:"Y"}
                ,"B":{0:"X", 3:"Y", 6:"Z"}
                ,"C":{0:"Y", 3:"Z", 6:"X"}}


    def get_gambles_score(self, gambles:str) -> int:
        gambles = self._get_gambles_list(gambles)
        result = 0

        for gamble in gambles:
            result += self._get_simple_score(gamble)

        return result

    def get_gambles_with_decription(self, gambles:str) -> int:
        gambles = self._get_gambles_list(gambles)
        result = 0

        for gamble in gambles:
            result += self._get_decrypted_score(gamble)
            
        return result

    def _get_gambles_list(self, gambles:str) -> list:
        return gambles.split("\n")
    
    def _get_simple_score(self, gamble:str) -> int:
        return self.gambles_score[gamble] + self.moves_score[gamble[2]]
    
    def _get_decrypted_score(self, gamble:str) -> int:
        current_result = self.gamble_result[gamble[2]]
        possible_moves = self.move_results[gamble[0]]
        good_move = possible_moves[current_result]
        return current_result + self.moves_score[good_move]


#--- Day 3: Rucksack Reorganization ---

class Rucksack:
    def _find_repeated(self, elements:str) -> str:
        length = len(elements)
        center = int(length/2)
        comp1, comp2 = elements[:center], elements[center:]

        item = [x for x in comp1 if x in comp2]

        return item[0] if item else ''
    
    def _find_all_repeated(self, input: str) -> list[str]:
        lines = input.split("\n")

        repeated_elements = []
        for line in lines:
            ele = self._find_repeated(line)
            if ele:
                repeated_elements.append(ele)
            else:
                print(line)

        return repeated_elements

    def _get_element_priority(self, e:str) -> int:
        
        return ord(e)-96 if e.islower() else ord(e)-65+27

    def get_rearrange_priority(self, input:str) -> int:

        rep_elements = self._find_all_repeated(input)
        result = sum([self._get_element_priority(x) for x in rep_elements])

        return result

    def _find_all_repetead_in_groups_3(self, input:str) -> list[str]:
        lines = input.split("\n")

        repeated_elements = []
        idx = 0 
        while idx < len(lines):
            l1, l2, l3 = lines[idx], lines[idx+1], lines[idx+2]

            
            item = [x for x in l1 if x in l2 and x in l3]
            repeated_elements.append(item[0])

            idx += 3

        return repeated_elements        

    def get_badges_priority(self, input:str) -> int:
        rep_elements = self._find_all_repetead_in_groups_3(input)
        result = sum([self._get_element_priority(x) for x in rep_elements])

        return result

    
#--- Day 4: Camp Cleanup ---

class RangeInRange:
    def is_range_inside_range(self, r1:list[int], r2:list[int]) -> bool:
        pass

class RangeInsideRange(RangeInRange):
    def is_range_inside_range(self, r1:list[int], r2:list[int]) -> bool:
        return r1[0] >= r2[0] and r1[1] <= r2[1]

class RangeOverlapRange(RangeInRange):
    def is_range_inside_range(self, r1:list[int], r2:list[int]) -> bool:
        return (r2[0] <= r1[0] <= r2[1]) or (r2[0] <= r1[1] <= r2[1])

class Cleanup:
    range_checker = None

    def __init__(self, rangeChecker:RangeInRange):
        self.range_checker = rangeChecker

    def _get_pairs(self, input:str) -> list[str]:
        pairs = input.split("\n")

        return pairs
    
    def _extract_pairs(self, pair:str) -> list:
        p1,p2 = pair.split(",")

        elf1 = [int(x) for x in p1.split('-')]
        elf2 = [int(x) for x in p2.split('-')]

        return [elf1,elf2]

    def count_sections_inside(self, input:str) -> int:

        pairs = self._get_pairs(input)

        result = 0
        for pair in pairs:
            sections = self._extract_pairs(pair)
            s1, s2 = sections[0], sections[1]

            result += self.range_checker.is_range_inside_range(s1,s2) or self.range_checker.is_range_inside_range(s2,s1)

        return result


#--- Day 5: Supply Stacks ---

class Move:
    num_blocks = 0
    from_pos = 0
    to_pos = 0

    def __init__(self, n_blocks, from_pos, to_pos) -> None:
        self.num_blocks = n_blocks
        self.from_pos = from_pos
        self.to_pos = to_pos

class CargoCrane:
    stacks = []
    instructions = []
    
    def _is_empty_line(self, line:str) -> bool:
        line = line.strip()
        return False if line else True

    def _decode_input(self, input:str):
        self.stacks = []
        self.instructions = []

        lines = input.split('\n')

        change_flagg = 0 # when empty line change to instructions
        for line in lines:
            if self._is_empty_line(line):
                change_flagg = 1
            elif not change_flagg:
                self.stacks.append(line)
            elif change_flagg:
                self.instructions.append(line)

    def _get_stacks(self, stacks_text:list[str])-> list[str]:
        # [P] [L]     [C] [V] [W] [W] [H] [L]
        # [G] [B] [V] [R] [L] [N] [G] [P] [F]
        # [R] [T] [S] [S] [S] [T] [D] [L] [P]
        # [N] [J] [M] [L] [P] [C] [H] [Z] [R]
        #  1   2   3   4   5   6   7   8   9 

        num_stacks = len(stacks_text[-1].split())
        stacks_list = [ [] for _ in range(num_stacks) ] 
        stacks_text = stacks_text[:-1]
        stacks_text.reverse()
        for line in stacks_text:
            idx_line = 1
            pointer_move = 4
            for idx_vector in range(num_stacks):
                c = line[idx_line]
                if c != ' ':
                    stacks_list[idx_vector].append(c)
                idx_line += pointer_move
        return stacks_list


    def _get_instructions(self, instructions:list[str])-> list[Move]:
        # example: move 2 from 4 to 6
        moves = []

        for line in instructions:
            words = line.split()
            move = Move(int(words[1]), int(words[3])-1, int(words[5])-1)
            moves.append(move)

        return moves


    def _exectue_instruction(self,stacks:list, instruction:Move) -> list:

        blocks_to_move = stacks[instruction.from_pos][-instruction.num_blocks:]
        blocks_to_move.reverse()

        stacks[instruction.to_pos] = stacks[instruction.to_pos] + blocks_to_move
        stacks[instruction.from_pos] = stacks[instruction.from_pos][:-instruction.num_blocks]

        return stacks

    def _exectue_instruction_new_crane(self,stacks:list, instruction:Move) -> list:

        blocks_to_move = stacks[instruction.from_pos][-instruction.num_blocks:]

        stacks[instruction.to_pos] = stacks[instruction.to_pos] + blocks_to_move
        stacks[instruction.from_pos] = stacks[instruction.from_pos][:-instruction.num_blocks]

        return stacks

    def move_cargo(self, input: str, crane) -> str:
        self._decode_input(input)

        stacks = self._get_stacks(self.stacks)
        instructions = self._get_instructions(self.instructions)

        for instruction in instructions:
            stacks = crane(stacks, instruction)

        top_cargo = ''.join([stream[-1] for stream in stacks])
        return top_cargo


#--- Day 6: Tuning Trouble ---

class MarkerFinder:
    def get_marker(self, input:str) -> int:
        pass

class MarkerDifferentChars(MarkerFinder):
    diffChars = 4
    def __init__(self, diffChars: int) -> None:
        super().__init__()
        self.diffChars = diffChars
        
    def get_marker(self, input:str) -> int:
        marker = ''
        idx = 0
        lenght = len(input)
        while len(marker) < self.diffChars and idx < lenght:
            char = input[idx]
            marker += char

            if char in marker[:-1]:
                i = marker.index(char)
                marker = marker[i+1:]

            idx += 1

        return idx


#--- Day 7: No Space Left On Device ---

class FileSysteNavigator:

    root = None
    all_dirs = None

    def _get_input_lines(self, input:str) -> list[str]:
        return input.split('\n')

    def get_directory_folders(self, input: str):
        self.all_dirs = dict()
        lines = self._get_input_lines(input)
        current_dir = None
        for line in lines:
            if line.startswith('$ cd /'):
                current_dir = 'root'
                self.all_dirs[current_dir]  = 0
            elif line.startswith('$ cd ..'):
                current_dir = current_dir[:current_dir.rindex('/')]
            elif line.startswith('$ cd'):
                current_dir = current_dir + '/' + line.replace('$ cd ','').strip()
                self.all_dirs[current_dir]  = 0
            elif line.startswith("$ ls") or line.startswith("dir"):
                pass
            else:
                size,name = line.split()
                self.all_dirs[current_dir] += int(size)
                path_dirs = current_dir
                while path_dirs != 'root':
                    path_dirs = path_dirs[:path_dirs.rindex('/')]
                    self.all_dirs[path_dirs] += int(size)
        
    def sum_sizes_directories_over_size(self,size:int = 0) -> int:
        
        return sum([x for x in self.all_dirs.values() if x <= size])

    def get_smallest_deletable_directory(self,size:int = 0) -> int:
        total_system_space = 70000000
        min_space_required = size
        space_ocuppied = self.all_dirs['root'] 
        if total_system_space - space_ocuppied < min_space_required:
            return min([x for x in self.all_dirs.values() if total_system_space - (space_ocuppied - x) >= min_space_required])


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


#--- Day 9: Rope Bridge ---

class Rope:
    initial_state = None
    no_move = [
            (-1,1),(0,1),(1,1),
            (-1,0),(0,0),(1,0),
            (-1,-1),(0,-1),(1,-1)
            ]

    def _decode_movements(self, input:str) -> list[tuple]:
        lines = input.split('\n')
        result = []
        for line in lines:
            dir, mov = line.split()
            mov = int(mov)
            result.append((dir,mov))

        return result

    def _diff_head_tail(self, head:tuple, tail:tuple) -> tuple:
        return (head[0]-tail[0],head[1]-tail[1])

    def _move_head(self, direction:str, head_last_point:tuple) -> tuple:
        current_point = None
        if direction == 'U':
            current_point = (head_last_point[0],head_last_point[1]+1)
        if direction == 'D':
            current_point = (head_last_point[0],head_last_point[1]-1)
        if direction == 'L':
            current_point = (head_last_point[0]-1,head_last_point[1])
        if direction == 'R':
            current_point = (head_last_point[0]+1,head_last_point[1])
        
        return current_point

    # (x,y). x: left or right, y: up or down
    def move_rope(self, input:str) -> int:
        head_moves = self._decode_movements(input)

        tail_visited = set()

        head_last_point = (0,0)
        tail_last_point = head_last_point
        tail_visited.add((0,0))
        for move in head_moves:

            for _ in range(move[1]):
                dir = move[0]
                current_point = self._move_head(dir,head_last_point)
                diff = self._diff_head_tail(current_point,tail_last_point)
                
                if diff not in self.no_move:
                    tail_last_point = head_last_point
                    tail_visited.add(tail_last_point)
                    
                head_last_point = current_point

        return len(tail_visited)

    def move_rope_10_knots(self, input:str) -> int:
        head_moves = self._decode_movements(input)

        tail_visited = set()

        rope = [(0,0)] *10
        tail_visited.add((0,0))
        for move in head_moves:
            for _ in range(move[1]):
                dir = move[0]
                rope[0] = self._move_head(dir,rope[0])
                for idx,point in enumerate(rope[1:],1):
                    if point == rope[idx-1]:
                        pass
                    else:
                        diff = self._diff_head_tail(rope[idx-1],point)
                        if diff not in self.no_move:
                            if diff[0] > 1 and diff[1]==0: diff = (1,0)
                            if diff[0] < -1 and diff[1]==0: diff = (-1,0)
                            if diff[1] > 1 and diff[0]==0: diff = (0,1)
                            if diff[1] <-1 and diff[0]==0: diff = (0,-1)
                            if diff[0] > 0 and diff[1] > 0: diff = (1,1)
                            if diff[0] < 0 and diff[1] > 0: diff = (-1,1)
                            if diff[0] > 0 and diff[1] < 0: diff = (1,-1)
                            if diff[0] <0 and diff[1] < 0: diff = (-1,-1)
                            rope[idx] = (point[0] + diff[0],point[1] + diff[1])
                        if idx == 9:
                            tail_visited.add((rope[idx][0], rope[idx][1]))


        return len(tail_visited)
