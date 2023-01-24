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




