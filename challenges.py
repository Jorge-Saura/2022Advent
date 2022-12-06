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

