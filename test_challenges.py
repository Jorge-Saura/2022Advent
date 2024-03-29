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





if __name__ == '__main__':

    unittest.main()
