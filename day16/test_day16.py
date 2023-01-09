import unittest

import day16.day16_data as data

import day16.day16 as challenges



class TestDay16(unittest.TestCase):

    
    def test_proboscidea_volcanium(self):

        pv =  challenges.ValvesController()
        pv._decode_input('Valve AA has flow rate=0; tunnels lead to valves DD, II, BB')
        keys = list(pv.valves.keys())
        self.assertEqual(keys[0], 'AA')

        pv._decode_input(data.valves_paths)
        paths = pv._get_all_paths()
        self.assertEqual(len(paths),90)

        self.assertEqual(pv.find_max_path(data.valves_paths,30,'AA'), 1651)

        self.assertEqual(pv.find_max_path(data.valves_paths1,30,'AA'), 1580) 

        self.assertEqual(pv.find_max_in_concurrent_paths(data.valves_paths,26,'AA',2), 1707)
        self.assertEqual(pv.find_max_in_concurrent_paths(data.valves_paths1,26,'AA',2), 2213)





if __name__ == '__main__':

    unittest.main()