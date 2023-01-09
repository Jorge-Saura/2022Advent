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

