#--- Day 20: Grove Positioning System ---


class DecrypterOperator:

    
    def _decode_input(self, input:str) -> list[int]:
        
        lines = input.split('\n')
        numbers = list()
        for line in lines:
            numbers.append(int(line))

        return numbers


    def decrypt(self, numbers:list[int]) -> list[int]:

        pairs = [[idx, num] for idx, num in enumerate(numbers)]
        length = pairs[-1][0]


        for p in pairs:
            idx, num = p

            new_index = (idx + num) % length
            new_index = new_index if new_index > 0 else length-new_index
            

            for x in pairs:
                current_idx, _ = x
                if new_index > idx:
                    x[0] = current_idx - 1 if idx < current_idx <= new_index else current_idx
                if new_index < idx:
                    x[0] = current_idx + 1 if new_index <= current_idx <= idx else current_idx
            p[0] = new_index

        pairs.sort(key = lambda x: x[0])
        
        return [x for idx, x in pairs]


    def get_coordenates(self, input:str) -> int:
        numbers = self._decode_input(input)

        decrypted_numbers = self.decrypt(numbers)
        length = len(decrypted_numbers)
        zero_idx = decrypted_numbers.index(0)
        first_coor = decrypted_numbers[(zero_idx + 1000) % length]
        second_coor = decrypted_numbers[(zero_idx + 2000) % length]
        third_coor = decrypted_numbers[(zero_idx + 3000) % length]

        return first_coor + second_coor + third_coor


