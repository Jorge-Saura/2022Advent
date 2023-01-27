#--- Day 20: Grove Positioning System ---


class DecrypterOperator:

    
    def _decode_input(self, input:str) -> list[int]:
        
        lines = input.split('\n')
        numbers = list()
        for line in lines:
            numbers.append(int(line))

        return numbers

    def newMod(self, a, b):
        res = a%b
        return res if not res else res-b if a<0 else res

    def decrypt(self, numbers:list[int]) -> list[int]:

        pairs = [[idx, num] for idx, num in enumerate(numbers)]
        length = len(pairs) - 1


        for p in pairs:
            idx, num = p
            if num == 0:
                continue

            movement = idx + num
          
            if num > 0:
                new_index = ((movement -1) % length) + 1
                if new_index > idx:
                    for i,x in enumerate(pairs):
                        current_idx, _ = x
                        pairs[i][0] = current_idx - 1 if idx < current_idx <= new_index else current_idx
                elif new_index < idx :
                    for i,x in enumerate(pairs):
                        current_idx, _ = x
                        pairs[i][0] = current_idx + 1 if new_index <= current_idx < idx else current_idx

            elif num < 0:
                if movement < 0:
                    real_mov = self.newMod(movement,length)
                    new_index = length + real_mov 
                elif movement == 0:
                    new_index = length
                else:
                    new_index = movement

                if new_index > idx:
                    for i,x in enumerate(pairs):
                        current_idx, _ = x
                        pairs[i][0] = current_idx - 1 if idx < current_idx <= new_index else current_idx
                    
                elif new_index < idx :
                    for i,x in enumerate(pairs):
                        current_idx, _ = x
                        pairs[i][0] = current_idx + 1 if new_index <= current_idx < idx else current_idx
            
            p[0] = new_index

        pairs.sort(key = lambda x: x[0])
        
        return [x for idx, x in pairs]


    def decrypt2(self, numbers:list[list[int]]) -> list[list[int]]:

        numbers.sort(key= lambda x: x[2])
        length = len(numbers)


        for triplet in numbers:
            idx, num, order = triplet

            new_index = (idx + num) % length
            # new_index = new_index if new_index >= 0 else length-new_index
            

            for x in numbers:
                current_idx, _, _ = x
                if new_index > idx:
                    x[0] = current_idx - 1 if idx < current_idx <= new_index else current_idx
                if new_index < idx:
                    x[0] = current_idx + 1 if new_index <= current_idx <= idx else current_idx
            triplet[0] = new_index

        numbers.sort(key = lambda x: x[0])
        
        return numbers



    def get_coordenates(self, input:str) -> int:
        numbers = self._decode_input(input)

        decrypted_numbers = self.decrypt(numbers)
        length = len(decrypted_numbers)
        zero_idx = decrypted_numbers.index(0)
        first_coor = decrypted_numbers[(zero_idx + 1000) % length]
        second_coor = decrypted_numbers[(zero_idx + 2000) % length]
        third_coor = decrypted_numbers[(zero_idx + 3000) % length]

        return first_coor + second_coor + third_coor


    def get_coordenates2(self, input:str) -> int:
        numbers = self._decode_input(input)
        decrypted_numbers = [[idx, x * 811589153, idx] for idx, x in enumerate(numbers)]
        # decrypted_numbers = self.decrypt2(numbers)
        for _ in range(10):
            decrypted_numbers = self.decrypt2(decrypted_numbers)
        
        length = len(decrypted_numbers)
        zero_idx = decrypted_numbers.index(0)
        first_coor = decrypted_numbers[(zero_idx + 1000) % length]
        second_coor = decrypted_numbers[(zero_idx + 2000) % length]
        third_coor = decrypted_numbers[(zero_idx + 3000) % length]

        return first_coor + second_coor + third_coor
 