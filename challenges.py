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