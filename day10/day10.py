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


