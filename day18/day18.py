#--- Day 18: Boiling Boulders ---

class BouldersController:

    def _decode_input(self, input:str):
        lines = input.split('\n')

        coordinates = list()

        for line in lines:
            x, y, z = [int(num) for num in line.split(',')]
            coordinates.append((x, y, z))

        return coordinates

    def _sum_tuple(self, point1:tuple[int], point2:tuple[int]) -> tuple[int]:
        return tuple(i+j for i,j in zip(point1,point2))

    def _get_sides(self, point:tuple[int]) -> list[tuple[tuple[int]]]:
        # 6 sides
        sides = list()

        # first side
        # 0,0,0 | 0,1,0 | 1,1,0 | 1,0,0
        side1 = (point, self._sum_tuple(point, (0,1,0)), self._sum_tuple(point, (1,1,0)), self._sum_tuple(point, (1,0,0)))

        # second side
        # 1,0,0 | 1,1,0 | 1,1,1 | 1,0,1
        side2 = (self._sum_tuple(point, (1,0,0)), self._sum_tuple(point, (1,1,0)), self._sum_tuple(point, (1,1,1)), self._sum_tuple(point, (1,0,1)))

        # third side
        # 0,0,1 | 0,1,1 | 1,1,1 | 1,0,1
        side3 = (self._sum_tuple(point, (0,0,1)), self._sum_tuple(point, (0,1,1)), self._sum_tuple(point, (1,1,1)), self._sum_tuple(point, (1,0,1)))

        # fouth side
        # 0,0,0 | 0,1,0 | 0,1,1 | 0,0,1
        side4 = (self._sum_tuple(point, (0,0,0)), self._sum_tuple(point, (0,1,0)), self._sum_tuple(point, (0,1,1)), self._sum_tuple(point, (0,0,1)))

        # fith side
        # 0,1,0 | 1,1,0 | 1,1,1 | 0,1,1
        side5 = (self._sum_tuple(point, (0,1,0)), self._sum_tuple(point, (1,1,0)), self._sum_tuple(point, (1,1,1)), self._sum_tuple(point, (0,1,1)))

        # sixth side
        # 0,0,0 | 1,0,0 | 1,0,1 | 0,0,1
        side6 = (self._sum_tuple(point, (0,0,0)), self._sum_tuple(point, (1,0,0)), self._sum_tuple(point, (1,0,1)), self._sum_tuple(point, (0,0,1)))

        return [side1, side2, side3, side4, side5, side6]

    def count_areas(self, input:str) -> int:
        cubes = self._decode_input(input)

        all_cubes = {c:6 for c in cubes}

        for cube, sides in all_cubes.items():
            sides = sides - 1 if (cube[0]-1,cube[1],cube[2]) in all_cubes.keys() else sides
            sides = sides - 1 if (cube[0]+1,cube[1],cube[2])  in all_cubes.keys() else sides

            sides = sides - 1 if (cube[0],cube[1]-1,cube[2]) in all_cubes.keys() else sides
            sides = sides - 1 if (cube[0],cube[1]+1,cube[2]) in all_cubes.keys() else sides

            sides = sides - 1 if (cube[0],cube[1],cube[2]-1)  in all_cubes.keys() else sides
            sides = sides - 1 if (cube[0],cube[1],cube[2]+1)  in all_cubes.keys() else sides

            all_cubes[cube] = sides

        return sum(all_cubes.values())

    def count_superficial_areas(self, input:str) -> int:
        cubes = self._decode_input(input)

        droplet = dict()
        min_x, max_x, min_y, max_y, min_z, max_z = 1000, 0, 1000, 0, 1000, 0 
        for cube in cubes: 
            min_x = min(min_x, cube[0])
            max_x = max(max_x, cube[0])

            min_y = min(min_y, cube[1])
            max_y = max(max_y, cube[1])

            min_z = min(min_z, cube[2])
            max_z = max(max_z, cube[2])

        max_x += 1
        max_y += 1
        max_z += 1

        min_x -= 1
        min_y -= 1
        min_z -= 1

        positions = [(max_x, max_y, max_z)]
        visited = set()
        visited.add((max_x, max_y, max_z))
        while positions:
            current = positions.pop(0)

            new_positions = [(current[0]-1,current[1],current[2]), (current[0]+1,current[1],current[2]), (current[0],current[1]-1,current[2]),
                            (current[0],current[1]+1,current[2]), (current[0],current[1],current[2]+1), (current[0],current[1],current[2]-1)]
            
            for new_position in new_positions:
                if new_position in cubes:
                    droplet[new_position] = droplet.get(new_position, 0) + 1
                else:
                    x,y,z = new_position
                    if min_x <= x <= max_x and min_y <= y <= max_y and min_z <= z <= max_z and new_position not in visited:
                        positions.append(new_position)
                        visited.add(new_position)
            
        return sum(droplet.values())



        
