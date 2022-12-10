calories ="1000\n" \
            "2000\n" \
            "3000\n" \
            "\n" \
            "4000\n" \
            "\n" \
            "5000\n" \
            "6000\n" \
            "\n" \
            "7000\n" \
            "8000\n" \
            "9000\n" \
            "\n" \
            "10000"

rps_gambles = """A Y
B X
C Z"""

rp_elements = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

clean_data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


supply_stacks = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

filesystem_simple="""$ cd /
$ cd a
4 a
$ cd b
2 b
3 c"""


filesystem = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


tree_grid_simple = """111
101
111"""

tree_grid = """30373
25512
65332
33549
35390"""

rope_move_up = "U 1"

rope_moves = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

rope_moves1 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


cpu_instructions_simple = """noop
addx 3
addx -5"""


cpu_instructions = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""


screen = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""


screen_one_line = """##..##..##..##..##..##..##..##..##..##..###...###...###...###...###...###...###.####....####....####....####....####....#####.....#####.....#####.....#####.....######......######......######......###########.......#######.......#######....."""



cpu_instructions1 = """addx 2
addx 3
noop
noop
addx 1
addx 5
addx -1
addx 5
addx 1
noop
noop
addx 4
noop
noop
addx 5
addx -5
addx 6
addx 3
addx 1
addx 5
addx 1
noop
addx -38
addx 41
addx -22
addx -14
addx 7
noop
noop
addx 3
addx -2
addx 2
noop
addx 17
addx -12
addx 5
addx 2
addx -16
addx 17
addx 2
addx 5
addx 2
addx -30
noop
addx -6
addx 1
noop
addx 5
noop
noop
noop
addx 5
addx -12
addx 17
noop
noop
noop
noop
addx 5
addx 10
addx -9
addx 2
addx 5
addx 2
addx -5
addx 6
addx 4
noop
noop
addx -37
noop
noop
addx 17
addx -12
addx 30
addx -23
addx 2
noop
addx 3
addx -17
addx 22
noop
noop
noop
addx 5
noop
addx -10
addx 11
addx 4
noop
addx 5
addx -2
noop
addx -6
addx -29
addx 37
addx -30
addx 27
addx -2
addx -22
noop
addx 3
addx 2
noop
addx 7
addx -2
addx 2
addx 5
addx -5
addx 6
addx 2
addx 2
addx 5
addx -25
noop
addx -10
noop
addx 1
noop
addx 2
noop
noop
noop
noop
addx 7
addx 1
addx 4
addx 1
noop
addx 2
noop
addx 3
addx 5
addx -1
noop
addx 3
addx 5
addx 2
addx 1
noop
noop
noop
noop"""


























