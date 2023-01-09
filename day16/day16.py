#--- Day 16: Proboscidea Volcanium ---

class ValvesController:

    valves = None
    valves_links = None

    def _decode_input(self, input:str):
        lines = input.split('\n')
        self.valves = dict()
        self.valves_links = dict()

        for line in lines:
            valve, links = line.split(';')

            key = valve.split()[1]
            value = int(valve[valve.index('=') + 1:])
            self.valves[key] = value

            links = links.replace(' tunnels lead to valves ','').replace(' tunnel leads to valve ','').split(', ')
            self.valves_links[key] = links
            
    def _get_all_paths(self) -> dict[str,int]:

        nodes = list(self.valves.keys())

        paths = dict()
       
        for node in nodes:
            for path in self.valves_links[node]:
                paths[node + path] = 1

        for _ in range(len(nodes)-1):
            for node in nodes:
                node_sons = self.valves_links[node]
                for path in node_sons:
                    paths_in_node_son = [key for key in paths.keys() if key.startswith(path) and key[-2:] != node]
                    for p in paths_in_node_son:
                        value = paths[p] + 1
                        key = node + p[-2:]
                        if key not in paths:
                            paths[key] = value
                        else:
                            paths[key] = min(paths[key], value)

        return paths
                
    def find_max_path(self, input:str, time:int, starting_node:str) -> int:
        self._decode_input(input)

        all_paths = self._get_all_paths()
        pressures_after_time = set()

        power_nodes = [x for x in self.valves.keys() if self.valves[x] > 0]

        ### First node can free pressure or not
        nodes = [(x,time,0) if x == starting_node else (x,time - all_paths[starting_node + x],0) for x in power_nodes] 

        while nodes:
            current = nodes.pop(0)
            current_path = current[0]
            current_node = current_path[-2:]
            current_time = current[1]
            current_pressure = current[2]

            current_time -= 1 # power on
            current_pressure += current_time * self.valves[current_node] # add all pressure
            pressures_after_time.add(current_pressure)
            
            for n in power_nodes:
                
                if current_path.find(n) == -1:
                    new_path = current_path + '>' + n
                    new_time = current_time - all_paths.get(current_node +  n, 0)
                    if new_time > 0:
                        nodes.append((new_path, new_time, current_pressure))

        return max(pressures_after_time)

    def find_max_in_concurrent_paths(self, input:str, time:int, starting_node:str, num_concurrents:int) -> int:
        self._decode_input(input)

        all_paths = self._get_all_paths()
        power_nodes = [x for x in self.valves.keys() if self.valves[x] > 0]
        nodes = [(x,time,0) if x == starting_node else (x,time - all_paths[starting_node + x],0) for x in power_nodes] 

        all_possible_paths =[]

        while nodes:
                current = nodes.pop(0)
                current_path = current[0]
                current_node = current_path[-2:]
                current_time = current[1]
                current_pressure = current[2]

                current_time -= 1 # power on
                current_pressure += current_time * self.valves[current_node] # add all pressure
                all_possible_paths.append((current_path, current_pressure))
                
                for n in power_nodes:
                    
                    if current_path.find(n) == -1:
                        new_path = current_path + '>' + n
                        new_time = current_time - all_paths.get(current_node +  n, 0)
                        if new_time > 0:
                            nodes.append((new_path, new_time, current_pressure))


        all_possible_paths.sort(key=lambda x: x[1], reverse=True)
        
        finded_value = 0
        all_results = set()
        while all_possible_paths:
            path = all_possible_paths.pop(0)
            nodes = path[0].split('>')
            
            for p_path in all_possible_paths:
                if p_path[1] + path[1] > finded_value:
                    if all(p_path[0].find(node) ==-1 for node in nodes):
                        all_results.add((path, p_path, path[1] + p_path[1]))
                        finded_value = path[1] + p_path[1]
                else:
                    break


        return finded_value


