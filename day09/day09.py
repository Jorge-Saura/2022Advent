#--- Day 9: Rope Bridge ---

class Rope:
    initial_state = None
    no_move = [
            (-1,1),(0,1),(1,1),
            (-1,0),(0,0),(1,0),
            (-1,-1),(0,-1),(1,-1)
            ]

    def _decode_movements(self, input:str) -> list[tuple]:
        lines = input.split('\n')
        result = []
        for line in lines:
            dir, mov = line.split()
            mov = int(mov)
            result.append((dir,mov))

        return result

    def _diff_head_tail(self, head:tuple, tail:tuple) -> tuple:
        return (head[0]-tail[0],head[1]-tail[1])

    def _move_head(self, direction:str, head_last_point:tuple) -> tuple:
        current_point = None
        if direction == 'U':
            current_point = (head_last_point[0],head_last_point[1]+1)
        if direction == 'D':
            current_point = (head_last_point[0],head_last_point[1]-1)
        if direction == 'L':
            current_point = (head_last_point[0]-1,head_last_point[1])
        if direction == 'R':
            current_point = (head_last_point[0]+1,head_last_point[1])
        
        return current_point

    # (x,y). x: left or right, y: up or down
    def move_rope(self, input:str) -> int:
        head_moves = self._decode_movements(input)

        tail_visited = set()

        head_last_point = (0,0)
        tail_last_point = head_last_point
        tail_visited.add((0,0))
        for move in head_moves:

            for _ in range(move[1]):
                dir = move[0]
                current_point = self._move_head(dir,head_last_point)
                diff = self._diff_head_tail(current_point,tail_last_point)
                
                if diff not in self.no_move:
                    tail_last_point = head_last_point
                    tail_visited.add(tail_last_point)
                    
                head_last_point = current_point

        return len(tail_visited)

    def move_rope_10_knots(self, input:str) -> int:
        head_moves = self._decode_movements(input)

        tail_visited = set()

        rope = [(0,0)] *10
        tail_visited.add((0,0))
        for move in head_moves:
            for _ in range(move[1]):
                dir = move[0]
                rope[0] = self._move_head(dir,rope[0])
                for idx,point in enumerate(rope[1:],1):
                    if point == rope[idx-1]:
                        pass
                    else:
                        diff = self._diff_head_tail(rope[idx-1],point)
                        if diff not in self.no_move:
                            if diff[0] > 1 and diff[1]==0: diff = (1,0)
                            if diff[0] < -1 and diff[1]==0: diff = (-1,0)
                            if diff[1] > 1 and diff[0]==0: diff = (0,1)
                            if diff[1] <-1 and diff[0]==0: diff = (0,-1)
                            if diff[0] > 0 and diff[1] > 0: diff = (1,1)
                            if diff[0] < 0 and diff[1] > 0: diff = (-1,1)
                            if diff[0] > 0 and diff[1] < 0: diff = (1,-1)
                            if diff[0] <0 and diff[1] < 0: diff = (-1,-1)
                            rope[idx] = (point[0] + diff[0],point[1] + diff[1])
                        if idx == 9:
                            tail_visited.add((rope[idx][0], rope[idx][1]))


        return len(tail_visited)
