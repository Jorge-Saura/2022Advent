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


#--- Day 10: Cathode-Ray Tube ---

class Instruction:
    type_op = 'noop'
    duration = 1
    value = 0 
    
    def __init__(self, type_op:str, duration:int, value:int) -> None:
        self.type_op = type_op
        self.duration = duration
        self.value = value

class CathodeRayTube:

    def _decode_instruction(self, input:str) -> Instruction:
        if input.startswith("noop"):
            return Instruction("noop",1,0)
        
        if input.startswith("addx"):
            instruction, value = input.split()
            return Instruction(instruction,2,int(value))

    def _decode_instructions(self, input:str) -> list[Instruction]:
        lines = input.split('\n')
        instructions = []

        for line in lines:
            instruction = self._decode_instruction(line)
            if instruction.type_op == 'addx':
                instructions.append(Instruction('noop',1,0))
                instructions.append(Instruction('add',1,instruction.value))
            else:
                instructions.append(instruction)

        return instructions

    def execute_program(self, input:str) -> int:
        program = self._decode_instructions(input)

        cycle = 1
        X_value = 1

        cycles_inspected = dict()
        next_cycle_to_inspect = 20
        sum_cycles = 40

        for ins in program:
            if cycle == next_cycle_to_inspect:
                cycles_inspected[cycle] = X_value
                next_cycle_to_inspect += sum_cycles

            cycle += 1
            if ins.type_op == 'add':
                X_value += ins.value

        return sum(x*y for x,y in cycles_inspected.items()) if cycles_inspected else 0


    def execute_program2(self, input:str) -> int:
        program = self._decode_instructions(input)

        cycle = 1
        X_value = 1

        sprite = [1,2,3]
        line  = ''
        screen = ''

        for ins in program:

            if cycle in sprite:
                line += '#'
            else:
                line += '.'

            cycle += 1
            if ins.type_op == 'add':
                X_value += ins.value
                sprite = [X_value, X_value + 1, X_value + 2]

            if (cycle-1) % 40 == 0:
                screen =  line if not screen else screen + '\n' + line 
                line = ''
                cycle = 1

        return screen


#--- Day 11: Monkey in the Middle ---

from math import lcm

class Monkey:
    id = 0
    items = None
    operation = None
    
    test = None
    test_number = None

    items_inspected = 0

    def __init__(self, id:int, items:list[int], operation:str, test:str) -> None:
        self.id= id
        self.items = items

        self.operation = self._set_operation(operation)

        self.test = self._set_test(test)


    def _set_operation(self, text:str) -> callable:
        
        num1, operation, num2 = text[text.index('=')+1:].strip().split()
        if num2 == 'old':
            if operation == '+':
                return lambda x: x + x
            else:
                return lambda x: x * x
        else:
            num2 = int(num2)
            if operation == '+':
                return lambda x: x + num2
            else:
                return lambda x: x * num2


    def _set_test(self, text:str) -> callable:

        line_test, line_true, line_false = text.split('\n')
        self.test_number = int(line_test.replace('Test: divisible by ','').strip())

        m_true = int(line_true.replace('If true: throw to monkey ','').strip())
        m_false = int(line_false.replace('If false: throw to monkey ','').strip())

        return lambda x: m_true if (x % self.test_number) == 0 else m_false

class MonkeyBusiness:

    def _decode_input(self, input:str) -> dict[Monkey]:
        monkey_descriptions = input.split('\n\n')
        monkeys_dict = dict()
        for monkey_desc in monkey_descriptions:
            line_id, line_starting, line_operation, line_test, line_true, line_false = monkey_desc.split('\n')
            m_id = int(line_id.strip(':').replace('Monkey ',''))
            m__starting = [int(x) for x in line_starting.replace('Starting items: ','').split(', ')]
            
            m_operation = line_operation
            m_test = '\n'.join([line_test,line_true, line_false])

            monkey = Monkey(m_id,m__starting,m_operation,m_test)
            
            monkeys_dict[monkey.id] = monkey
 
        return monkeys_dict

    def _proccess_monkeys(self, monkeys:dict[int, Monkey], worry_level:callable) -> dict[int, Monkey]:

        for id in monkeys.keys():
            monkey = monkeys[id]
            for item in monkey.items:
                monkey.items_inspected += 1
                item = monkey.operation(item)
                item = worry_level(item)
                next_monkey = monkey.test(item)

                monkeys[next_monkey].items.append(item)

            monkey.items = []
            monkeys[id] = monkey

        return monkeys

    def get_business(self, input:str, rounds:int) -> int:

        monkeys = self._decode_input(input)
        worry_level = lambda x: x//3
        for i in range(rounds):
            monkeys = self._proccess_monkeys(monkeys,worry_level)
        
        total_items_instpected = [x.items_inspected for x in monkeys.values()]
        total_items_instpected.sort(reverse=True)

        return total_items_instpected[0] * total_items_instpected[1]


    def get_business2(self, input:str, rounds:int) -> int:

        monkeys = self._decode_input(input)
        dividends = [monkey.test_number for monkey in monkeys.values()]
        multiple = lcm(*dividends)
        worry_level = lambda x: x % multiple

        for i in range(rounds):
            monkeys = self._proccess_monkeys(monkeys,worry_level)
        
        total_items_instpected = [x.items_inspected for x in monkeys.values()]
        total_items_instpected.sort(reverse=True)

        return total_items_instpected[0] * total_items_instpected[1]


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


#--- Day 13: Distress Signal ---

class DistressSignal:
    
    def _transforn_to_list(self, string:str) -> list:

        if string.isnumeric():
            return int(string)
        
        if string.startswith('['): string = string [1:]
        if string.endswith(']'): string = string [:-1]

        elements = list()
        
        while string:
            if string[0].isdigit():
                first_coma = string.find(',')
                if first_coma > 0:
                    num = string[:first_coma]
                    string = string.lstrip(num)
                else:
                    num = string
                    string = string.lstrip(num)
                elements.append(num)
            elif string[0] == '[':
                indexes = [i for i, ltr in enumerate(string) if ltr == ']']
                
                good_index = 0
                for idx in indexes:
                    part = string[:idx+1]
                    if part.count('[') == part.count(']'):
                        good_index = idx
                        break
                
                elements.append(string[:good_index + 1])
                string = string[good_index + 1:]
            elif string[0] == ',':
                string = string.lstrip(',')


        result = [self._transforn_to_list(x) for x in elements]
        return result

    def _decode_input(self, input:str)->list[tuple[list,list]]:
        pairs = input.split('\n\n')

        result = list()
        for pair in pairs:
            pair1, pair2 = pair.split('\n')

            list1 = self._transforn_to_list(pair1)
            list2 = self._transforn_to_list(pair2)

            result.append((list1,list2))

        return result

    def _get_first_item_in_nested_list(self, nested_list:list) -> int:

        while isinstance(nested_list,list):
            if nested_list:
                nested_list = nested_list[0]
            else:
                nested_list = None

        return nested_list

    def _check_right_order(self, list1:list, list2:list) -> bool:

        result = None

        for ele1, ele2 in zip(list1, list2): # If both are list lets checks this lists.
            if isinstance(ele1, list) and isinstance(ele2, list):
                result = self._check_right_order(ele1, ele2)

            elif isinstance(ele1, list) and isinstance(ele2, int): # If second element is int we transform it to list and check.
                result =  self._check_right_order(ele1, [ele2])

            elif isinstance(ele1, int) and isinstance(ele2, list):# If first element is int we transform it to list and check.
                result = self._check_right_order([ele1], ele2)
            
            elif isinstance(ele1, int) and isinstance(ele2, int):
                if ele1 < ele2:
                    result = True
                if ele1 > ele2:
                    result = False

            if result is not None:
                break

        if result is None:
            if len(list1) > len(list2):
                result = False
            if len(list1) < len(list2): 
                result = True

        return result

    def sum_indexes_right_order(self, input:str) -> int:
        list_pairs = self._decode_input(input)
        sum_of_index = 0
        for idx, pair in enumerate(list_pairs,1):
            list1, list2 = pair
            sum_of_index += idx if self._check_right_order(list1,list2) else 0
   
        return sum_of_index

    def _sort_values(self, values: list, is_lower_than:callable) -> list:
        # Basic bubble algorithm 
        for i in range(len(values)):
            for j in range(i + 1, len(values)):
                if not is_lower_than(values[i], values[j]):
                    values[i], values[j] = values[j], values[i]
        return values

    def get_decoder_key(self, input:str) -> int:
        list_pairs = self._decode_input(input)
        all_messages = [x for tupla in list_pairs for x in tupla]

        all_messages.append([[2]])
        all_messages.append([[6]])

        all_messages = self._sort_values(all_messages,self._check_right_order)
        first_key = all_messages.index([[2]]) + 1
        second_key = all_messages.index([[6]]) + 1

        return first_key * second_key


#--- Day 14: Regolith Reservoir ---

class RegolithSource:

    def _get_points(self, line:str) -> list[tuple[int,int]]:
        result = list()
        vertices = line.split(' -> ')
        for vertice in vertices:
            
            x, y = vertice.split(',')
            x, y = int(x), int(y)
 
            if  result:
                last_vertice = result[-1]
                last_x, last_y = last_vertice

                if x - last_x:
                    #horizontal
                    addition_sign = -1 if x - last_x < 0 else 1
                    for i in range(addition_sign, x - last_x + addition_sign, addition_sign):
                        result.append((last_x + i, last_y))
                elif y - last_y:
                    #vertical
                    addition_sign = -1 if y - last_y < 0 else 1
                    for i in range(addition_sign, y - last_y + addition_sign, addition_sign):
                        result.append((last_x, last_y + i))

            else: #first point
                result.append((x,y))

        return set(result)

    def _decode_input(self, input:str) -> list[tuple[int,int]]:
        lines = input.split('\n')
        result = list()
        
        for line in lines:
            
            points = self._get_points(line)

            result.extend(points)

        result = list(set(result))
        return result

    def _move_sand(self, point:tuple[int,int], points: list[tuple[int,int]]) -> tuple[int,int]:
        x, y = point
        if (x, y + 1) not in points:
            return (x, y + 1)
        elif (x - 1, y + 1) not in points:
            return (x - 1, y + 1)
        elif (x + 1, y + 1) not in points:
            return (x + 1, y + 1)

        return (-1, -1)

    def _print_walls(self, rocks:list[tuple[int,int]], snow:list[tuple[int,int]], last_path:list[tuple[int,int]]):
        points = rocks

        points.append((500,0))

        max_x = max(points + snow + last_path,key = lambda x: x[0])[0]
        min_x = min(points + snow + last_path,key = lambda x: x[0])[0]

        max_y = max(points + snow + last_path,key = lambda x: x[1])[1]
        min_y = min(points + snow + last_path,key = lambda x: x[1])[1]

        ancho = max_x - min_x + 3
        alto = max_y - min_y + 3

        m = [['.'] * ancho for _ in range(alto)] 

        for point in points:
            x,y = point
            x = x - min_x + 1
            m[y][x] = '#'

        for point in snow:
            x,y = point
            x = x - min_x + 1
            m[y][x] = 'o'

        for point in last_path:
            x,y = point
            x = x - min_x + 1
            m[y][x] = '~'

        with open('rockwall_day14.txt','w',encoding = 'utf-8') as f:
            for row in m:
                line = ''.join(row) + '\n'
                f.write(line)
        
        return m
   
    def _print_walls_with_floor(self, rocks:list[tuple[int,int]], free_points:list[tuple[int,int]]):
        points = rocks

        max_x = max(points + free_points,key = lambda x: x[0])[0]
        min_x = min(points + free_points,key = lambda x: x[0])[0]

        max_y = max(points + free_points,key = lambda x: x[1])[1]
        min_y = min(points + free_points,key = lambda x: x[1])[1]

        # ancho = max_x - min_x + 3
        alto = max_y + 2

        ancho = 1 + (2 *(alto - 1))

        m = [['.'] * ancho for _ in range(alto-1)] 
        m.append(['#'] * ancho)

        start = (ancho//2) 
        off_set = 500 - start
        
        for i in range(1, alto):
            m[i-1][start] = 'o'
            for j in range(1,i):
                m[i-1][start - j] = 'o'
                m[i-1][start + j] = 'o'

        for point in points:
            x,y = point
            x = x - off_set
            m[y][x] = '#'

        for point in free_points:
            x,y = point
            x = x - off_set
            m[y][x] = '.'


        with open('rockwall_with_floor_day14.txt','w',encoding = 'utf-8') as f:
            for row in m:
                line = ''.join(row) + '\n'
                f.write(line)
        
        return m

    def get_sand_packets(self, input:str) -> int:
        points = self._decode_input(input)
        rocks = points.copy()
        
        lowest_level = max(points, key = lambda x: x[1])[1]

        start = (500,0)
        current_point = start
        result = 0

        snow = list()
        last_path = list()

        while current_point[1] < lowest_level:
            current_point = start
            result += 1 
            
            last_path = []
            while (new_point:=self._move_sand(current_point, points)) != (-1,-1) and current_point[1] < lowest_level:
                last_path.append(new_point)
                current_point = new_point

            points.append(current_point)
            snow.append(current_point)
            
        self._print_walls(rocks, snow, last_path)

        return result - 1

    def get_sand_packets_with_floor(self, input:str) -> int:
        points = self._decode_input(input)
        points.sort(key=lambda x: (x[0], x[1]))
        rocks = points.copy()
        free_points = list()
        last_path = list()
        
        lowest_level = max(points, key = lambda x: x[1])[1] + 2
        
        all_sands = (lowest_level) * (lowest_level)

        for level in range(0,lowest_level):
            level_points = [x for x in points if x[1] == level]

            for point in level_points:
                x, y = point
                left_point = (x - 1, y)
                right_point = (x + 1, y)
                if left_point in points and right_point in points:
                    new_point = (x, y + 1)
                    if new_point not in points and new_point[1] < lowest_level:
                        points.append(new_point)
                        free_points.append(new_point)

       
        self._print_walls_with_floor(rocks, free_points)

        result = all_sands - len(rocks) - len(free_points)

        return result


#--- Day 15: Beacon Exclusion Zone ---

class SensorBeacon:
    s_x = 0
    s_y = 0
    b_x = 0
    b_y = 0

    distance = 0

    def __init__(self, s_x:int, s_y:int, b_x:int, b_y:int) -> None:
        self.s_x = s_x
        self.s_y = s_y
        self.b_x = b_x
        self.b_y = b_y

        self.distance = abs(s_x - b_x) + abs(s_y - b_y)

    def __eq__(self, __o: object) -> bool:

        return self.s_x == __o.s_x and self.s_y == __o.s_y and self.b_x == __o.b_x and self.b_y == __o.b_y and self.distance == __o.distance

class BeaconExclusiveZone:
    
    def _decode_input(self, input:str) -> list[SensorBeacon]:
        lines = input.split('\n') 

        result = list()

        for line in lines:
            sensor, beacon = line.split(':')

            s_x, s_y = sensor.split(',')
            s_x = int(s_x.replace('Sensor at x=', ''))
            s_y = int(s_y.replace(' y=', ''))

            b_x, b_y = beacon.split(',')
            b_x = int(b_x.replace(' closest beacon is at x=', ''))
            b_y = int(b_y.replace(' y=', ''))

            pair = SensorBeacon(s_x, s_y, b_x, b_y)
            result.append(pair)

        return result

    def _line_in_range(self, line_index:int, pair:SensorBeacon) -> bool:
        return abs(pair.s_y - line_index) <= pair.distance

    def _get_points(self, line_index:int, pair:SensorBeacon, beacons: set[int]) -> list[int]:
        
        result =list()
        if self._line_in_range(line_index, pair):
            if (pair.s_x) not in beacons: result.append(pair.s_x)
            distance = pair.distance - abs(line_index - pair.s_y)
            for i in range(1, distance + 1):
                if (pair.s_x + i) not in beacons: result.append(pair.s_x + i)
                if (pair.s_x - i) not in beacons: result.append(pair.s_x - i) 

        return result

    def check_line(self, input:str, line_index:int) -> int:
        
        pairs = self._decode_input(input)

        beacons = {b.b_x for b in pairs if b.b_y == line_index}
        points_covered = set()

        for pair in pairs:
            points = self._get_points(line_index, pair, beacons)
            points_covered.update(points)

        return len(points_covered)

    def _is_point_in_range(self, x:int, y:int, pairs:list[SensorBeacon]) -> bool:

        for pair in pairs:
            if pair.distance >= abs(x - pair.s_x) + abs(y - pair.s_y):
                return True
        
        return False
        
    def check_free_position(self, input:str, range_min:int, range_max:int) -> int:

        # There is only 1 free position so it must be surronding one of the sensors scope.

        pairs = self._decode_input(input)
        x, y = -1, -1
        exist_point = False
        for idx, pair in enumerate(pairs):

            current_x, current_y = pair.s_x, pair.s_y
            dist = pair.distance + 1

            # get the points
            for i in range(0, dist + 1):

                
                x,y = current_x + i, current_y + dist - i
                # check the points againts the other Sensors
                if range_min <= x <= range_max and  range_min <= y <= range_max and not self._is_point_in_range(x,y, pairs[:idx] + pairs[idx+1:]):
                    exist_point = True
                    break
                x,y = current_x - i, current_y - dist + i
                if range_min <= x <= range_max and  range_min <= y <= range_max and not self._is_point_in_range(x,y, pairs[:idx] + pairs[idx+1:]):
                    exist_point = True
                    break
                x,y = current_x + dist - i, current_y + i
                if range_min <= x <= range_max and  range_min <= y <= range_max and not self._is_point_in_range(x,y, pairs[:idx] + pairs[idx+1:]):
                    exist_point = True
                    break
                x,y = current_x - dist + i, current_y - i
                if range_min <= x <= range_max and  range_min <= y <= range_max and not self._is_point_in_range(x,y, pairs[:idx] + pairs[idx+1:]):
                    exist_point = True
                    break
            if(exist_point):
                break

        return (x * 4000000) + y

    
#--- Day 16: Proboscidea Volcanium ---

from itertools import permutations 

class ValvesController:

    valves = None
    valves_links = None

    def _decode_input(self, input:str):
        lines = input.split('\n')
        self.valves = dict()
        self.valves_links = dict()

        for line in lines:
            valve, links = line.split(';')

            key = valve.split()[1]
            value = int(valve[valve.index('=') + 1:])
            self.valves[key] = value

            links = links.replace(' tunnels lead to valves ','').replace(' tunnel leads to valve ','').split(', ')
            self.valves_links[key] = links
            
    def _get_all_paths(self) -> dict[str,int]:

        nodes = list(self.valves.keys())

        paths = dict()
       
        for node in nodes:
            for path in self.valves_links[node]:
                paths[node + path] = 1

        for _ in range(len(nodes)-1):
            for node in nodes:
                node_sons = self.valves_links[node]
                for path in node_sons:
                    paths_in_node_son = [key for key in paths.keys() if key.startswith(path) and key[-2:] != node]
                    for p in paths_in_node_son:
                        value = paths[p] + 1
                        key = node + p[-2:]
                        if key not in paths:
                            paths[key] = value
                        else:
                            paths[key] = min(paths[key], value)

        return paths
                
    def find_max_path(self, input:str, time:int, starting_node:str) -> int:
        self._decode_input(input)

        all_paths = self._get_all_paths()
        pressures_after_time = set()

        power_nodes = [x for x in self.valves.keys() if self.valves[x] > 0]

        ### First node can free pressure or not
        nodes = [(x,time,0) if x == starting_node else (x,time - all_paths[starting_node + x],0) for x in power_nodes] 

        while nodes:
            current = nodes.pop(0)
            current_path = current[0]
            current_node = current_path[-2:]
            current_time = current[1]
            current_pressure = current[2]

            current_time -= 1 # power on
            current_pressure += current_time * self.valves[current_node] # add all pressure
            pressures_after_time.add(current_pressure)
            
            for n in power_nodes:
                
                if current_path.find(n) == -1:
                    new_path = current_path + '>' + n
                    new_time = current_time - all_paths.get(current_node +  n, 0)
                    if new_time > 0:
                        nodes.append((new_path, new_time, current_pressure))

        return max(pressures_after_time)

    def find_max_in_concurrent_paths(self, input:str, time:int, starting_node:str, num_concurrents:int) -> int:
        self._decode_input(input)

        all_paths = self._get_all_paths()
        power_nodes = [x for x in self.valves.keys() if self.valves[x] > 0]
        nodes = [(x,time,0) if x == starting_node else (x,time - all_paths[starting_node + x],0) for x in power_nodes] 

        all_possible_paths =[]

        while nodes:
                current = nodes.pop(0)
                current_path = current[0]
                current_node = current_path[-2:]
                current_time = current[1]
                current_pressure = current[2]

                current_time -= 1 # power on
                current_pressure += current_time * self.valves[current_node] # add all pressure
                all_possible_paths.append((current_path, current_pressure))
                
                for n in power_nodes:
                    
                    if current_path.find(n) == -1:
                        new_path = current_path + '>' + n
                        new_time = current_time - all_paths.get(current_node +  n, 0)
                        if new_time > 0:
                            nodes.append((new_path, new_time, current_pressure))


        all_possible_paths.sort(key=lambda x: x[1], reverse=True)
        
        finded_value = 0
        all_results = set()
        while all_possible_paths:
            path = all_possible_paths.pop(0)
            nodes = path[0].split('>')
            
            for p_path in all_possible_paths:
                if p_path[1] + path[1] > finded_value:
                    if all(p_path[0].find(node) ==-1 for node in nodes):
                        all_results.add((path, p_path, path[1] + p_path[1]))
                        finded_value = path[1] + p_path[1]
                else:
                    break


        return finded_value

