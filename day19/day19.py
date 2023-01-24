#--- Day 19: Not Enough Minerals ---

from __future__ import annotations


import math



class Blueprint:
    id = 0
    ore_robot = None # [#ore, #clay, #obsidian]
    clay_robot = None # [#ore, #clay, #obsidian]
    obsidian_robot = None # [#ore, #clay, #obsidian]
    geode_robot = None # [#ore, #clay, #obsidian]

    robots = None # [#ore, #clay, #obsidian, #geode]
    resources = None # [#ore, #clay, #obsidian, #geode]
    
    minutes = 24

    def __init__(self, id:int, ore_robot:list[int], clay_robot:list[int], obsidian_robot:list[int], geode_robot:list[int]) -> None:
        self.id = id
        self.ore_robot = ore_robot
        self.clay_robot = clay_robot
        self.obsidian_robot = obsidian_robot
        self.geode_robot = geode_robot
        self.robots =  [1, 0, 0, 0] # you always start with 1 ore robot
        self.resources = [0, 0, 0, 0]

        # self.max_robots = 5
        self.max_ore = max([ore_robot[0], clay_robot[0], obsidian_robot[0], geode_robot[0]])

        self.max_clay = max([ore_robot[1], clay_robot[1], obsidian_robot[1], geode_robot[1]])

        self.max_obsidian = max([ore_robot[2], clay_robot[2], obsidian_robot[2], geode_robot[2]])

        self.max_geode = max([ore_robot[3], clay_robot[3], obsidian_robot[3], geode_robot[3]])

    def _copy(self) -> Blueprint:
        b = Blueprint(self.id, self.ore_robot, self.clay_robot, self.obsidian_robot, self.geode_robot)
        b.robots = self.robots.copy()
        b.resources = self.resources.copy()
        b.minutes = self.minutes

        return b

    def __str__(self) -> str:
        return f"{str(self.minutes)}_{str(self.resources)}_{str(self.robots)}"



class BlueprintsController:

    
    def _decode_input(self, input:str) -> list[Blueprint]:
        
        lines = input.split('\n')
        blueprints = list()
        for line in lines:
            sentences = line.split('.')
            
            identificator, sentences[0] = sentences[0].split(':')
            
            b_id = int(identificator.replace('Blueprint ',''))

            b_ore = [int(sentences[0].replace(' Each ore robot costs ','').replace(' ore', '')), 0, 0, 0]
            b_clay = [int(sentences[1].replace(' Each clay robot costs ','').replace(' ore', '')), 0, 0, 0]
            resources = sentences[2].replace(' Each obsidian robot costs ','').replace(' ore and', '').replace(' clay', '').split(' ')
            b_obsidian = [int(resources[0]), int(resources[1]), 0, 0]
            resources = sentences[3].replace(' Each geode robot costs ','').replace(' ore and', '').replace(' obsidian', '').split(' ')
            b_geode = [int(resources[0]), 0, int(resources[1]), 0]

            b = Blueprint(b_id, b_ore, b_clay, b_obsidian, b_geode)

            blueprints.append(b)


        return blueprints

    def _get_blueprint_production(self, blueprint:Blueprint) -> int:
            
            ways = [blueprint]
            visited_ways = set()
            max_geodes = 0 


            while ways:
                current = ways.pop(0)

                ore_r, clay_r, obsidian_r, geode_r = current.robots

                current_total_geodes = current.resources[3] + (current.minutes * current.robots[3])
                max_geodes = max(max_geodes, current_total_geodes)

                current_max_total_geodes = current_total_geodes + ((current.minutes * (current.minutes-1))//2)
                if current_max_total_geodes < max_geodes:
                    continue


                # option 1. wait to create new geode robot. First because it helps us to prune other blueprints
                if  obsidian_r > 0: # Only check if is possible build geode robot, but buil all than you can
                    geode_resources_ore = current.resources[0] # we need ore resources to create obsidian robot
                    geode_resources_obs = current.resources[2] # we need clay resources to create obsidian robot
                    ore_robot_cost = current.geode_robot[0]
                    obs_robot_cost = current.geode_robot[2]
                    

                    time_to_create_new_robot = 1 # robot creation takes 1 min
                    if ore_robot_cost > geode_resources_ore or obs_robot_cost > geode_resources_obs:
                        time_to_create_new_robot_ore = math.ceil((ore_robot_cost - geode_resources_ore) / ore_r) # minutes neede to reach the resources
                        time_to_create_new_robot_obs = math.ceil((obs_robot_cost - geode_resources_obs) / obsidian_r) # minutes neede to reach the resources
                        time_to_create_new_robot += max(time_to_create_new_robot_ore, time_to_create_new_robot_obs)

                    if current.minutes > time_to_create_new_robot:                    
                        new_blueprint = current._copy()

                        new_blueprint.minutes -= time_to_create_new_robot
                        new_blueprint.resources = [new_blueprint.resources[0] + (ore_r*time_to_create_new_robot), new_blueprint.resources[1] + (clay_r*time_to_create_new_robot), new_blueprint.resources[2] + (obsidian_r*time_to_create_new_robot), new_blueprint.resources[3] + (geode_r*time_to_create_new_robot)]
                        new_blueprint.robots[3] += 1 # adding the created resource
                        new_blueprint.resources[0] -= ore_robot_cost # substracting the robot cost
                        new_blueprint.resources[2] -= obs_robot_cost # substracting the robot cost
                        if str(new_blueprint) not in visited_ways:
                            ways.append(new_blueprint)
                            visited_ways.add(str(new_blueprint))

                # option 2. wait to create new obsidian robot
                if  clay_r > 0 and obsidian_r < current.max_obsidian: # Not over the maximum production necesary
                    obsidian_resources_ore = current.resources[0] # we need ore resources to create obsidian robot
                    obsidian_resources_clay = current.resources[1] # we need clay resources to create obsidian robot
                    ore_robot_cost = current.obsidian_robot[0]
                    clay_robot_cost = current.obsidian_robot[1]
                    

                    time_to_create_new_robot = 1 # robot creation takes 1 min
                    if ore_robot_cost > obsidian_resources_ore or clay_robot_cost > obsidian_resources_clay:
                        time_to_create_new_robot_ore = math.ceil((ore_robot_cost - obsidian_resources_ore) / ore_r) # minutes neede to reach the resources
                        time_to_create_new_robot_clay = math.ceil((clay_robot_cost - obsidian_resources_clay) / clay_r) # minutes neede to reach the resources
                        time_to_create_new_robot += max(time_to_create_new_robot_ore, time_to_create_new_robot_clay)

                    if current.minutes > time_to_create_new_robot:                    
                        new_blueprint = current._copy()

                        new_blueprint.minutes -= time_to_create_new_robot
                        new_blueprint.resources = [new_blueprint.resources[0] + (ore_r*time_to_create_new_robot), new_blueprint.resources[1] + (clay_r*time_to_create_new_robot), new_blueprint.resources[2] + (obsidian_r*time_to_create_new_robot), new_blueprint.resources[3] + (geode_r*time_to_create_new_robot)]
                        new_blueprint.robots[2] += 1 # adding the created resource
                        new_blueprint.resources[0] -= ore_robot_cost # substracting the robot cost
                        new_blueprint.resources[1] -= clay_robot_cost # substracting the robot cost
                        if str(new_blueprint) not in visited_ways:
                            ways.append(new_blueprint)
                            visited_ways.add(str(new_blueprint))

                # option 3. wait to create new clay robot
                if clay_r < current.max_clay: # Not over the maximum production necesary
                    ore_resources = current.resources[0] # we need ore resources to create clay robot
                    clay_robot_cost = current.clay_robot[0]
                    

                    time_to_create_new_robot = 1 # robot creation takes 1 min
                    if clay_robot_cost > ore_resources:
                        time_to_create_new_robot += math.ceil((clay_robot_cost - ore_resources) / ore_r) # minutes neede to reach the resources

                    if current.minutes > time_to_create_new_robot:
                        new_blueprint = current._copy()

                        new_blueprint.minutes -= time_to_create_new_robot
                        new_blueprint.resources = [new_blueprint.resources[0] + (ore_r*time_to_create_new_robot), new_blueprint.resources[1] + (clay_r*time_to_create_new_robot), new_blueprint.resources[2] + (obsidian_r*time_to_create_new_robot), new_blueprint.resources[3] + (geode_r*time_to_create_new_robot)]
                        new_blueprint.robots[1] += 1 # adding the created resource
                        new_blueprint.resources[0] -= clay_robot_cost # substracting the robot cost
                        if str(new_blueprint) not in visited_ways:
                            ways.append(new_blueprint)
                            visited_ways.add(str(new_blueprint))
               
                # option 4. wait to create new ore robot
                if ore_r < current.max_ore: # Not over the maximum production necesary
                    ore_resources = current.resources[0]
                    ore_robot_cost = current.ore_robot[0]
                    
                    time_to_create_new_robot = 1 # robot creation takes 1 min
                    if ore_robot_cost > ore_resources:
                        time_to_create_new_robot += math.ceil((ore_robot_cost - ore_resources) / ore_r) # minutes neede to reach the resources


                    if current.minutes > time_to_create_new_robot:
                        new_blueprint = current._copy()

                        new_blueprint.minutes -= time_to_create_new_robot
                        new_blueprint.resources = [new_blueprint.resources[0] + (ore_r*time_to_create_new_robot), new_blueprint.resources[1] + (clay_r*time_to_create_new_robot), new_blueprint.resources[2] + (obsidian_r*time_to_create_new_robot), new_blueprint.resources[3] + (geode_r*time_to_create_new_robot)]
                        new_blueprint.robots[0] += 1 # adding the created resource
                        new_blueprint.resources[0] -= ore_robot_cost # substracting the robot cost
                        if str(new_blueprint) not in visited_ways:
                            ways.append(new_blueprint)
                            visited_ways.add(str(new_blueprint))



            return max_geodes





    def geode_generator(self, input:str) -> int:

        bps = self._decode_input(input)
        max_bps = list()

        for idx, b in enumerate(bps,1):
            max_b = self._get_blueprint_production(b)
            max_bps.append(idx * max_b)

        m = sum(max_bps)
        return m


    def geode_generator2(self, input:str) -> int:

        bps = self._decode_input(input)
        max_bps = 1

        for idx, b in enumerate(bps,1):
            if idx > 3:
                break

            b.minutes = 32
            max_b = self._get_blueprint_production(b)
            max_bps = max_bps * max_b

            

        
        return max_bps





