#--- Day 21: Monkey Math ---

# make a dictionary of lambda functions???

class MonkeyMath:

    def _decode_input(self, input:str) -> list[str]:

        lines = input.split('\n')

        return lines
    
    def _get_operation(self, operation:str, operations:dict) -> callable:
        operation = operation.strip()
        vars = operation.split(' ')

        if len(vars) == 1:
            return lambda: int(vars[0])
        else:
            if operation.find('+') > 0:
                return lambda : operations[vars[0]]() + operations[vars[2]]()
            elif operation.find('-') > 0:
                return lambda : operations[vars[0]]() - operations[vars[2]]()
            elif operation.find('*') > 0:
                return lambda : operations[vars[0]]() * operations[vars[2]]()
            elif operation.find('/') > 0:
                return lambda : operations[vars[0]]() / operations[vars[2]]()

 


    def calculate_math(self, input:str, root:str) -> float:
        lines = self._decode_input(input)
        operations = dict()

        for line in lines:
            variable, operation = line.split(':')
            operations[variable] = self._get_operation(operation, operations)


        return operations[root]()


    def calculate_math2(self, input:str, root:str) -> float:
        lines = self._decode_input(input)
        operations = dict()
        f1 = None
        f2 = None

        for line in lines:
            variable, operation = line.split(':')

            if variable == root:
                operation = operation.strip()
                vars = operation.split(' ')
                f1 = vars[0]
                f2 = vars[2]
            else:
                operations[variable] = self._get_operation(operation, operations)

        value = 1
        adding = 1000000000000
        operations['humn'] = lambda : value
        f1 = operations[f1]
        f2 = operations[f2]

        
        val1 = f1()
        val2 = f2()
        vector = None

        if val1 > val2:
            vector = 'desc'
            value = 2
            operations['humn'] = lambda : value
            next_val1 = f1()
            if val1 < next_val1:
                adding = -adding
        elif  val1 < val2:
            vector = 'asc'
            value = 2
            operations['humn'] = lambda : value
            next_val1 = f1()
            if val1 > next_val1:
                adding = -adding
        elif  val1 == val2:
            return value

        while val1 != val2:

            if vector == 'desc':
                if val1 < val2: # he soprepasado y tengo que subir
                    adding = adding / 10
                    adding = adding * -1
                    vector = 'asc'
            elif vector == 'asc':
                if val1 > val2: # he soprepasado y tengo que subir
                    adding = adding / 10
                    adding = adding * -1
                    vector = 'desc'
          
            value += adding
            val1 = f1()
            val2 = f2()
        
        return value
