#--- Day 15: Beacon Exclusion Zone ---

class SensorBeacon:
    s_x = 0
    s_y = 0
    b_x = 0
    b_y = 0

    distance = 0

    def __init__(self, s_x:int, s_y:int, b_x:int, b_y:int) -> None:
        self.s_x = s_x
        self.s_y = s_y
        self.b_x = b_x
        self.b_y = b_y

        self.distance = abs(s_x - b_x) + abs(s_y - b_y)

    def __eq__(self, __o: object) -> bool:

        return self.s_x == __o.s_x and self.s_y == __o.s_y and self.b_x == __o.b_x and self.b_y == __o.b_y and self.distance == __o.distance

class BeaconExclusiveZone:
    
    def _decode_input(self, input:str) -> list[SensorBeacon]:
        lines = input.split('\n') 

        result = list()

        for line in lines:
            sensor, beacon = line.split(':')

            s_x, s_y = sensor.split(',')
            s_x = int(s_x.replace('Sensor at x=', ''))
            s_y = int(s_y.replace(' y=', ''))

            b_x, b_y = beacon.split(',')
            b_x = int(b_x.replace(' closest beacon is at x=', ''))
            b_y = int(b_y.replace(' y=', ''))

            pair = SensorBeacon(s_x, s_y, b_x, b_y)
            result.append(pair)

        return result

    def _line_in_range(self, line_index:int, pair:SensorBeacon) -> bool:
        return abs(pair.s_y - line_index) <= pair.distance

    def _get_points(self, line_index:int, pair:SensorBeacon, beacons: set[int]) -> list[int]:
        
        result =list()
        if self._line_in_range(line_index, pair):
            if (pair.s_x) not in beacons: result.append(pair.s_x)
            distance = pair.distance - abs(line_index - pair.s_y)
            for i in range(1, distance + 1):
                if (pair.s_x + i) not in beacons: result.append(pair.s_x + i)
                if (pair.s_x - i) not in beacons: result.append(pair.s_x - i) 

        return result

    def check_line(self, input:str, line_index:int) -> int:
        
        pairs = self._decode_input(input)

        beacons = {b.b_x for b in pairs if b.b_y == line_index}
        points_covered = set()

        for pair in pairs:
            points = self._get_points(line_index, pair, beacons)
            points_covered.update(points)

        return len(points_covered)

    def _is_point_in_range(self, x:int, y:int, pairs:list[SensorBeacon]) -> bool:

        for pair in pairs:
            if pair.distance >= abs(x - pair.s_x) + abs(y - pair.s_y):
                return True
        
        return False
        
    def check_free_position(self, input:str, range_min:int, range_max:int) -> int:

        # There is only 1 free position so it must be surronding one of the sensors scope.

        pairs = self._decode_input(input)
        x, y = -1, -1
        exist_point = False
        for idx, pair in enumerate(pairs):

            current_x, current_y = pair.s_x, pair.s_y
            dist = pair.distance + 1

            # get the points
            for i in range(0, dist + 1):

                
                x,y = current_x + i, current_y + dist - i
                # check the points againts the other Sensors
                if range_min <= x <= range_max and  range_min <= y <= range_max and not self._is_point_in_range(x,y, pairs[:idx] + pairs[idx+1:]):
                    exist_point = True
                    break
                x,y = current_x - i, current_y - dist + i
                if range_min <= x <= range_max and  range_min <= y <= range_max and not self._is_point_in_range(x,y, pairs[:idx] + pairs[idx+1:]):
                    exist_point = True
                    break
                x,y = current_x + dist - i, current_y + i
                if range_min <= x <= range_max and  range_min <= y <= range_max and not self._is_point_in_range(x,y, pairs[:idx] + pairs[idx+1:]):
                    exist_point = True
                    break
                x,y = current_x - dist + i, current_y - i
                if range_min <= x <= range_max and  range_min <= y <= range_max and not self._is_point_in_range(x,y, pairs[:idx] + pairs[idx+1:]):
                    exist_point = True
                    break
            if(exist_point):
                break

        return (x * 4000000) + y

    