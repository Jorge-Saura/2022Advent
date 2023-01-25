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

