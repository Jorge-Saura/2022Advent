import unittest

import day15.day15_data as data

import day15.day15 as challenges



class TestDay15(unittest.TestCase):

    
    def test_beacon_exclusive_zone(self):

        bez = challenges.BeaconExclusiveZone()
        pairs = bez._decode_input(data.sensors_beacons)
        self.assertEqual(len(pairs),14)
        pair = pairs[0]
        self.assertTrue(pair == challenges.SensorBeacon(2, 18, -2, 15))

        pair = challenges.SensorBeacon(1, 1, 3, 3)
        self.assertEqual(bez._line_in_range(0, pair), True)
        self.assertEqual(bez._line_in_range(-1, pair), True)
        self.assertEqual(bez._line_in_range(-4, pair), False)
        self.assertEqual(bez._line_in_range(4, pair), True)
        self.assertEqual(bez._line_in_range(-5, pair), False)
        self.assertEqual(bez._line_in_range(6, pair), False)

        self.assertCountEqual(bez._get_points(1, pair, [12]),[1, 2, 0, 3, -1, 4, -2, 5, -3])

        pair = challenges.SensorBeacon(0, 11, 2, 10)
        self.assertCountEqual(bez._get_points(10, pair, [15]),[0, 1, -1, 2, -2])
        self.assertCountEqual(bez._get_points(10, pair, [1,-2]),[0, -1, 2])

        self.assertEqual(bez.check_line(data.sensors_beacons,10), 26)
        self.assertEqual(bez.check_line(data.sensors_beacons1,2000000), 5040643)
        sensors = [challenges.SensorBeacon(0, 0, 2, 2)]
        self.assertEqual(bez._is_point_in_range(1,1, sensors), True)

        sensors = [challenges.SensorBeacon(0, 0, 2, 2), challenges.SensorBeacon(2, 1, 5, 5)]
        self.assertEqual(bez._is_point_in_range(0, 5, sensors), True)
        self.assertEqual(bez._is_point_in_range(8, 8, sensors), False)


        self.assertEqual(bez.check_free_position(data.sensors_beacons, 0, 20)  , 56000011)
        self.assertEqual(bez.check_free_position(data.sensors_beacons1, 0, 4000000)  , 11016575214126)




if __name__ == '__main__':

    unittest.main()