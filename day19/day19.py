#--- Day 19: Not Enough Minerals ---

from __future__ import annotations


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

        self.max_robots = 5
        self.max_ore = max([ore_robot[0], clay_robot[0], obsidian_robot[0], geode_robot[0]])

        self.max_clay = max([ore_robot[1], clay_robot[1], obsidian_robot[1], geode_robot[1]])

        self.max_obsidian = max([ore_robot[2], clay_robot[2], obsidian_robot[2], geode_robot[2]])

        self.max_geode = max([ore_robot[3], clay_robot[3], obsidian_robot[3], geode_robot[3]])

    def _copy(self) -> Blueprint:
        b = Blueprint(self.id, self.ore_robot, self.clay_robot, self.obsidian_robot, self.geode_robot)
        b.robots = self.robots
        b.resources = self.resources
        b.minutes = self.minutes

        return b



    def can_create_robot(self, material_needed:list[int]) -> bool:
        if material_needed == self.ore_robot and self.robots[0] > self.max_ore:
            return False
        if material_needed == self.clay_robot and self.robots[1] > self.max_clay:
            return False
        if material_needed == self.obsidian_robot and self.robots[2] > self.max_geode:
            return False

        #

        return all(True if m <= r else False for m, r in zip(material_needed, self.resources))

    def create_ore_robot(self) -> list[int]:
        ore, clay, obs, geo = self.robots
        ore += 1

        self.resources = [re - ro for re, ro in zip(self.resources, self.ore_robot)]
        return [ore, clay, obs, geo]

    def create_clay_robot(self) -> list[int]:
        ore, clay, obs, geo = self.robots
        clay += 1

        self.resources = [re - ro for re, ro in zip(self.resources, self.clay_robot)]
        return [ore, clay, obs, geo]

    def create_obsidian_robot(self) -> list[int]:
        ore, clay, obs, geo = self.robots
        obs += 1

        self.resources = [re - ro for re, ro in zip(self.resources, self.obsidian_robot)]
        return [ore, clay, obs, geo]

    def create_geode_robot(self) -> list[int]:
        ore, clay, obs, geo = self.robots
        geo += 1

        self.resources = [re - ro for re, ro in zip(self.resources, self.geode_robot)]
        return [ore, clay, obs, geo]

    def update_resources(self): # [#ore, #clay, #obsidian, #geode]
        self.resources = [r + p for r, p in zip(self.resources, self.robots)]

    def produce_resources(self) -> list[int]: # [#ore, #clay, #obsidian, #geode]
        #devolvemos los recursos generados en 1 minuto que se deben sumar a los recursos generales
        pass

class BlueprintsController:

    
    def _decode_input(self, input:str) -> list[Blueprint]:
        
        lines = input.split('\n')
        blueprints = list()
#Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
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
        finished_ways = list()
        max_geodes = 0 


        while ways:
            current = ways.pop(0)

            if current.minutes == 0:
                max_geodes = max(max_geodes, current.resources[3])
                finished_ways.append(current)
                continue
            
            #espera para construir una geoda
            # si recursos de obsidian + produccion de obsidiana >= obsidiana para geoda
            # no gastes en otra cosa 
            if current.resources[2] + current.robots[2] >= current.geode_robot[2]:
                current.update_resources()
                current.minutes -= 1
                ways.append(current)
                continue

            #espera para construir una obsidiana
            # si recursos de barro + produccion de barro >= barro para obsidiana
            # no gastes en otra cosa 
            if current.resources[1] + current.robots[1] >= current.obsidian_robot[1]:
                current.update_resources()
                current.minutes -= 1
                ways.append(current)
                continue

            # geode robot
            if current.can_create_robot(current.geode_robot):
                # create robot
                new_blueprint = current._copy()
                new_production = new_blueprint.create_geode_robot()
                new_blueprint.update_resources()
                new_blueprint.robots = new_production
                new_blueprint.minutes -= 1
                ways.append(new_blueprint)


            # obsidian robot
            if current.can_create_robot(current.obsidian_robot):
                # create robot
                new_blueprint = current._copy()
                new_production = new_blueprint.create_obsidian_robot()
                new_blueprint.update_resources()
                new_blueprint.robots = new_production
                new_blueprint.minutes -=1
                ways.append(new_blueprint)

            # clay robot
            if current.can_create_robot(current.clay_robot):
                # create robot
                new_blueprint = current._copy()
                new_production = new_blueprint.create_clay_robot()
                new_blueprint.update_resources()
                new_blueprint.robots = new_production
                new_blueprint.minutes -= 1
                ways.append(new_blueprint)

            # ore robot
            if current.can_create_robot(current.ore_robot):
                # create robot
                new_blueprint = current._copy()
                new_production = new_blueprint.create_ore_robot()
                new_blueprint.update_resources()
                new_blueprint.robots = new_production
                new_blueprint.minutes -= 1
                ways.append(new_blueprint)


            # Si tengo los recursos necesarios para construir he de construir, no hacerlo no es mejor jugada que hacerlo
            # if current.resources[0] < current.max_ore and current.resources[1] < current.max_clay and current.resources[2] < current.max_obsidian:
            current.update_resources()
            current.minutes -= 1
            ways.append(current)






        max_b = max(finished_ways,key= lambda x: x.resources[3])
        return max_b.resources[3]


    def geode_generator(self, input:str) -> int:

        bps = self._decode_input(input)
        max_bps = list()

        for b in bps:
            max_b = self._get_blueprint_production(b)
            max_bps.append(max_b)

        m = max(max_bps)
        return m







