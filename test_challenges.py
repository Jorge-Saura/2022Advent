import unittest

import challenges 
import data

class TestChallenges(unittest.TestCase):
    def test_counting_calories(self):
        cc = challenges.CaloriesService()
        calories = data.calories
        result = cc.getMaxCalories(calories)
        self.assertEqual(result,24000)    

        result = cc.get3MaxCalories(calories)
        self.assertEqual(result,45000)    

    def test_rps_counting(self):
        rps = challenges.RPSGame()
        gambles = data.rps_gambles
        self.assertEqual(rps.get_gambles_score(gambles),15)
        gambles = data.rps_gambles
        self.assertEqual(rps.get_gambles_with_decription(gambles),12)

    def test_find_repeated(self):
        fr = challenges.Rucksack()
        self.assertEqual(fr._find_repeated('vJrwpWtwJgWrhcsFMMfFFhFp'),'p')
        self.assertEqual(fr._find_repeated('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'),'L')
        self.assertEqual(fr._find_repeated('pTsdppTMPtqqdbnlNVzJVbSSnbZR'),'b')

        self.assertEqual(fr._find_repeated('aaabbb'),'')

        self.assertEqual(fr._find_all_repeated(data.rp_elements),['p','L','P','v','t','s'])

        self.assertEqual(fr._get_element_priority('a'),1)
        self.assertEqual(fr._get_element_priority('z'),26)
        self.assertEqual(fr._get_element_priority('A'),27)
        self.assertEqual(fr._get_element_priority('Z'),52)

        self.assertEqual(fr.get_rearrange_priority(data.rp_elements),157)

        self.assertEqual(fr._find_all_repetead_in_groups_3(data.rp_elements),['r','Z'])
        self.assertEqual(fr.get_badges_priority(data.rp_elements),70)

    def test_clean_pairs(self):
        r_inside_r = challenges.RangeInsideRange()
        c_inside = challenges.Cleanup(r_inside_r)
        self.assertEqual(c_inside._extract_pairs("2-6,3-5"),[[2,6],[3,5]])
        self.assertEqual(c_inside.count_sections_inside(data.clean_data),2)

        r_overlap_r = challenges.RangeOverlapRange()
        c_overlap = challenges.Cleanup(r_overlap_r)
        self.assertEqual(c_overlap.count_sections_inside(data.clean_data),4)

    def test_supply_stacks(self):
        cc = challenges.CargoCrane()
        self.assertEqual(cc._is_empty_line(""),True)
        self.assertEqual(cc._is_empty_line(" "),True)
        self.assertEqual(cc._is_empty_line("algo"),False)

        cc._decode_input("stack\n\ninstructions")
        self.assertEqual(cc.stacks, ['stack'])
        self.assertEqual(cc.instructions, ['instructions'])

        #decode cargo streams
        cargo = ["           ",
                 " 1   2   3 "]
        self.assertEqual(cc._get_stacks(cargo),[[],[],[]])

        cargo = ["[1]     [3]",
                 " 1   2   3 "]
        self.assertEqual(cc._get_stacks(cargo),[['1'],[],['3']])

        cargo = ["[1]     [2]",
                 "[3] [4] [5]",
                 " 1   2   3 "]
        self.assertEqual(cc._get_stacks(cargo),[['3','1'],['4'],['5','2']])

        #decode instructions
        m = cc._get_instructions(["move 2 from 4 to 6"])
        self.assertEqual(m[0].num_blocks,2)
        self.assertEqual(m[0].from_pos,3)
        self.assertEqual(m[0].to_pos,5)

        l = [['3','1'],['4'],['5','2']]
        m = challenges.Move(1,0,2)
        self.assertEqual(cc._exectue_instruction(l,m), [['3'],['4'],['5','2','1']])

        l = [['3','1'],['4'],['5','2']]
        m = challenges.Move(2,0,2)
        self.assertEqual(cc._exectue_instruction(l,m), [[],['4'],['5','2','1','3']])

        result = cc.move_cargo(data.supply_stacks,cc._exectue_instruction)
        self.assertEqual(result,'CMZ')

        result = cc.move_cargo(data.supply_stacks,cc._exectue_instruction_new_crane)
        self.assertEqual(result,'MCD')

    def test_find_start_packet_marker(self):
        cc = challenges.MarkerDifferentChars(4)
        self.assertEqual(cc.get_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb'),7)
        self.assertEqual(cc.get_marker('bvwbjplbgvbhsrlpgdmjqwftvncz'),5)
        self.assertEqual(cc.get_marker('nppdvjthqldpwncqszvftbrmjlhg'),6)
        self.assertEqual(cc.get_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'),10)
        self.assertEqual(cc.get_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'),11)

        cc = challenges.MarkerDifferentChars(14)
        self.assertEqual(cc.get_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb'),19)
        self.assertEqual(cc.get_marker('bvwbjplbgvbhsrlpgdmjqwftvncz'),23)
        self.assertEqual(cc.get_marker('nppdvjthqldpwncqszvftbrmjlhg'),23)
        self.assertEqual(cc.get_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'),29)
        self.assertEqual(cc.get_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'),26)
        
    def test_find_dirs_size(self):

        f = challenges.FileSysteNavigator()
        f.get_directory_folders(data.filesystem_simple)
        self.assertEqual(f.sum_sizes_directories_over_size(5),5)

        f.get_directory_folders(data.filesystem)
        self.assertEqual(f.sum_sizes_directories_over_size(100000),95437)

        f.get_directory_folders(data.filesystem)
        self.assertEqual(f.get_smallest_deletable_directory(30000000),24933642)

    def test_tree_visibility(self):

        tv = challenges.TreeVisibility()

        grid = tv._decode_data(data.tree_grid_simple)

        self.assertEqual(tv._is_visible_horizontally(2,grid,(1,1)), True)
        self.assertEqual(tv._is_visible_horizontally(0,grid,(1,1)), False)

        self.assertEqual(tv.get_number_of_visible_trees(data.tree_grid_simple),8)
        self.assertEqual(tv.get_number_of_visible_trees(data.tree_grid),21)

        self.assertEqual(tv._get_scenic_score((2,1)),4)
        self.assertEqual(tv._get_scenic_score((2,3)),8)
        self.assertEqual(tv.get_best_scenic_score(data.tree_grid),8)

    def test_rope_bridge(self): 

        r = challenges.Rope()

        self.assertEqual(r._decode_movements("U 1\nL 3"),[('U',1),('L',3)])
        
        self.assertEqual(r.move_rope(data.rope_moves),13)

        self.assertEqual(r.move_rope_10_knots(data.rope_moves),1)

        self.assertEqual(r.move_rope_10_knots(data.rope_moves1),36)

    def test_cathode_ray_tube(self):

        crt = challenges.CathodeRayTube()
        noop = crt._decode_instruction("noop")
        expected = challenges.Instruction('noop',1,0)
        self.assertEqual(noop.type_op, expected.type_op), self.assertEqual(noop.duration, expected.duration), self.assertEqual(noop.value, expected.value)
        addx = crt._decode_instruction("addx 5")
        expected = challenges.Instruction('addx',2,5)
        self.assertEqual(addx.type_op, expected.type_op), self.assertEqual(addx.duration, expected.duration), self.assertEqual(addx.value, expected.value)

        self.assertEqual(crt.execute_program(data.cpu_instructions),13140)

        self.assertEqual(crt.execute_program2(data.cpu_instructions),data.screen)

    def test_monkeys_business(self):

        mb = challenges.MonkeyBusiness()
        monkey_atrrs = mb._decode_input(data.monkeys_attrs_simple)

        self.assertEqual(len(monkey_atrrs),4)

        self.assertEqual(mb.get_business(data.monkeys_attrs_simple,20),10605)

        self.assertEqual(mb.get_business2(data.monkeys_attrs_simple,10000),52166 * 52013)

    def test_hill_climbing_algorithm(self):

        hca = challenges.HillClimbing()

        self.assertEqual(hca.find_pahts_iterative(data.hill_climbing_grid_simple),31)
        self.assertEqual(hca.first_a, 29)

    def test_distress_signal(self):
            
            ds = challenges.DistressSignal()

            self.assertEqual(ds._transforn_to_list("[1]"),[1])       
            self.assertEqual(ds._transforn_to_list("[1,2,3,4]"),[1,2,3,4])
            self.assertEqual(ds._transforn_to_list("[[1],2,3,4]"),[[1],2,3,4])    
            self.assertEqual(ds._transforn_to_list("[[4,4],4,4]"),[[4,4],4,4])   
            self.assertEqual(ds._transforn_to_list("[[4,4],4,4]"),[[4,4],4,4]) 
            self.assertEqual(ds._transforn_to_list("[[[]]]"),[[[]]]) 
            self.assertEqual(ds._transforn_to_list("[1,[2,[3,[4,[5,6,7]]]],8,9]"),[1,[2,[3,[4,[5,6,7]]]],8,9])
            self.assertEqual(ds._transforn_to_list("[[[[[4]],4]],4,4]"),[[[[[4]],4]],4,4]) 
            
            l1, l2= [1,1,3,1,1], [1,1,5,1,1]
            self.assertEqual(ds._check_right_order(l1,l2), True)

            l1, l2= [[1],[2,3,4]], [[1],4]
            self.assertEqual(ds._check_right_order(l1,l2), True)
            
            l1, l2= [[4,4],4,4], [[4,4],4,4,4]
            self.assertEqual(ds._check_right_order(l1,l2), True)

            l1, l2= [[],4,4], [[0],4,4,4]
            self.assertEqual(ds._check_right_order(l1,l2), True)

            l1 = [[[[0, 3, 7], 3, [4, 0], [6, 2, 0], 4], 1, [[3, 4, 7], 8, [1]], 2]]
            l2 = [[0, 6, [[6, 9, 6], 9, [0], [2, 10]], 4]]
            self.assertEqual(ds._check_right_order(l1,l2), False)

            l1 = [[[[], 9, [8, 8, 9, 10, 9]], [], 10, 10], [10, [], 0]]
            l2 = [[0, [], 6, 3, [[], []]], [7, [8]], [[[4, 3, 3, 2, 9], 10, 4, []], 5], []]
            self.assertEqual(ds._check_right_order(l1,l2), True)

            self.assertEqual(ds.sum_indexes_right_order(data.signal_simple), 13)

            self.assertEqual(ds.get_decoder_key(data.signal_simple), 140)

    def test_regolith_source(self):

        rs = challenges.RegolithSource()

        result = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5), (10, 5), (10, 4), (10, 3), (10, 2), (10, 1), (10, 0), (9, 0), (8, 0), (8, 1), (8, 2)]
        self.assertCountEqual(rs._get_points('0,0 -> 5,0 -> 5,5 -> 10,5 -> 10,0 -> 8,0 -> 8,2'), result)
        self.assertCountEqual(rs._get_points('498,4 -> 498,6 -> 496,6'),[(498,4), (498,5), (498,6), (497,6), (496,6)])

        self.assertCountEqual(rs._decode_input(data.regolith_simple),[(498,4), (498,5), (498,6), (497,6), (496,6), (503,4), (502,4)])

        self.assertEqual(rs.get_sand_packets(data.regolith_basic), 24)

        self.assertEqual(rs.get_sand_packets(data.regolith_basic1), 672)

        self.assertEqual(rs.get_sand_packets_with_floor(data.regolith_basic), 93)

        self.assertEqual(rs.get_sand_packets_with_floor(data.regolith_basic1), 26831)




        


if __name__ == '__main__':

    unittest.main()
