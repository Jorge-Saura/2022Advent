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

# for each line:
# def factory(line):

#    def operation(line):
#       if line.operation() == sum:
#           return lambda: line.arg1() + line.arg()