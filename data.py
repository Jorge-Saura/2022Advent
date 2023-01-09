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

monkeys_attrs_simple = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""


hill_climbing_grid_simple = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


signal_simple = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


regolith_simple = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4"""


regolith_basic = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

regolith_wall = """498,4 -> 502,4"""


regolith_basic1 = """491,57 -> 506,57 -> 506,56
469,142 -> 473,142
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
497,29 -> 497,32 -> 493,32 -> 493,38 -> 507,38 -> 507,32 -> 501,32 -> 501,29
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
506,84 -> 506,79 -> 506,84 -> 508,84 -> 508,80 -> 508,84 -> 510,84 -> 510,82 -> 510,84 -> 512,84 -> 512,75 -> 512,84
475,142 -> 479,142
470,154 -> 475,154
506,89 -> 511,89
497,29 -> 497,32 -> 493,32 -> 493,38 -> 507,38 -> 507,32 -> 501,32 -> 501,29
492,18 -> 492,20 -> 489,20 -> 489,26 -> 497,26 -> 497,20 -> 495,20 -> 495,18
488,51 -> 488,44 -> 488,51 -> 490,51 -> 490,47 -> 490,51 -> 492,51 -> 492,43 -> 492,51 -> 494,51 -> 494,48 -> 494,51
493,119 -> 493,114 -> 493,119 -> 495,119 -> 495,114 -> 495,119 -> 497,119 -> 497,115 -> 497,119 -> 499,119 -> 499,109 -> 499,119 -> 501,119 -> 501,109 -> 501,119
505,60 -> 505,63 -> 499,63 -> 499,71 -> 509,71 -> 509,63 -> 508,63 -> 508,60
466,151 -> 471,151
480,127 -> 480,130 -> 475,130 -> 475,136 -> 494,136 -> 494,130 -> 486,130 -> 486,127
506,84 -> 506,79 -> 506,84 -> 508,84 -> 508,80 -> 508,84 -> 510,84 -> 510,82 -> 510,84 -> 512,84 -> 512,75 -> 512,84
506,84 -> 506,79 -> 506,84 -> 508,84 -> 508,80 -> 508,84 -> 510,84 -> 510,82 -> 510,84 -> 512,84 -> 512,75 -> 512,84
497,29 -> 497,32 -> 493,32 -> 493,38 -> 507,38 -> 507,32 -> 501,32 -> 501,29
496,91 -> 501,91
506,84 -> 506,79 -> 506,84 -> 508,84 -> 508,80 -> 508,84 -> 510,84 -> 510,82 -> 510,84 -> 512,84 -> 512,75 -> 512,84
503,91 -> 508,91
488,51 -> 488,44 -> 488,51 -> 490,51 -> 490,47 -> 490,51 -> 492,51 -> 492,43 -> 492,51 -> 494,51 -> 494,48 -> 494,51
488,51 -> 488,44 -> 488,51 -> 490,51 -> 490,47 -> 490,51 -> 492,51 -> 492,43 -> 492,51 -> 494,51 -> 494,48 -> 494,51
500,93 -> 505,93
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
492,18 -> 492,20 -> 489,20 -> 489,26 -> 497,26 -> 497,20 -> 495,20 -> 495,18
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
495,14 -> 495,15 -> 508,15 -> 508,14
506,84 -> 506,79 -> 506,84 -> 508,84 -> 508,80 -> 508,84 -> 510,84 -> 510,82 -> 510,84 -> 512,84 -> 512,75 -> 512,84
488,51 -> 488,44 -> 488,51 -> 490,51 -> 490,47 -> 490,51 -> 492,51 -> 492,43 -> 492,51 -> 494,51 -> 494,48 -> 494,51
480,127 -> 480,130 -> 475,130 -> 475,136 -> 494,136 -> 494,130 -> 486,130 -> 486,127
495,14 -> 495,15 -> 508,15 -> 508,14
454,163 -> 458,163
480,127 -> 480,130 -> 475,130 -> 475,136 -> 494,136 -> 494,130 -> 486,130 -> 486,127
493,119 -> 493,114 -> 493,119 -> 495,119 -> 495,114 -> 495,119 -> 497,119 -> 497,115 -> 497,119 -> 499,119 -> 499,109 -> 499,119 -> 501,119 -> 501,109 -> 501,119
506,84 -> 506,79 -> 506,84 -> 508,84 -> 508,80 -> 508,84 -> 510,84 -> 510,82 -> 510,84 -> 512,84 -> 512,75 -> 512,84
472,139 -> 476,139
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
493,119 -> 493,114 -> 493,119 -> 495,119 -> 495,114 -> 495,119 -> 497,119 -> 497,115 -> 497,119 -> 499,119 -> 499,109 -> 499,119 -> 501,119 -> 501,109 -> 501,119
488,51 -> 488,44 -> 488,51 -> 490,51 -> 490,47 -> 490,51 -> 492,51 -> 492,43 -> 492,51 -> 494,51 -> 494,48 -> 494,51
506,84 -> 506,79 -> 506,84 -> 508,84 -> 508,80 -> 508,84 -> 510,84 -> 510,82 -> 510,84 -> 512,84 -> 512,75 -> 512,84
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
514,93 -> 519,93
506,84 -> 506,79 -> 506,84 -> 508,84 -> 508,80 -> 508,84 -> 510,84 -> 510,82 -> 510,84 -> 512,84 -> 512,75 -> 512,84
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
466,145 -> 470,145
457,160 -> 461,160
493,119 -> 493,114 -> 493,119 -> 495,119 -> 495,114 -> 495,119 -> 497,119 -> 497,115 -> 497,119 -> 499,119 -> 499,109 -> 499,119 -> 501,119 -> 501,109 -> 501,119
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
456,154 -> 461,154
506,84 -> 506,79 -> 506,84 -> 508,84 -> 508,80 -> 508,84 -> 510,84 -> 510,82 -> 510,84 -> 512,84 -> 512,75 -> 512,84
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
488,51 -> 488,44 -> 488,51 -> 490,51 -> 490,47 -> 490,51 -> 492,51 -> 492,43 -> 492,51 -> 494,51 -> 494,48 -> 494,51
502,87 -> 507,87
460,163 -> 464,163
453,157 -> 458,157
478,145 -> 482,145
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
497,29 -> 497,32 -> 493,32 -> 493,38 -> 507,38 -> 507,32 -> 501,32 -> 501,29
488,51 -> 488,44 -> 488,51 -> 490,51 -> 490,47 -> 490,51 -> 492,51 -> 492,43 -> 492,51 -> 494,51 -> 494,48 -> 494,51
493,93 -> 498,93
467,157 -> 472,157
463,166 -> 467,166
492,18 -> 492,20 -> 489,20 -> 489,26 -> 497,26 -> 497,20 -> 495,20 -> 495,18
493,119 -> 493,114 -> 493,119 -> 495,119 -> 495,114 -> 495,119 -> 497,119 -> 497,115 -> 497,119 -> 499,119 -> 499,109 -> 499,119 -> 501,119 -> 501,109 -> 501,119
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
487,53 -> 487,54 -> 500,54 -> 500,53
505,60 -> 505,63 -> 499,63 -> 499,71 -> 509,71 -> 509,63 -> 508,63 -> 508,60
493,119 -> 493,114 -> 493,119 -> 495,119 -> 495,114 -> 495,119 -> 497,119 -> 497,115 -> 497,119 -> 499,119 -> 499,109 -> 499,119 -> 501,119 -> 501,109 -> 501,119
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
488,51 -> 488,44 -> 488,51 -> 490,51 -> 490,47 -> 490,51 -> 492,51 -> 492,43 -> 492,51 -> 494,51 -> 494,48 -> 494,51
451,166 -> 455,166
492,18 -> 492,20 -> 489,20 -> 489,26 -> 497,26 -> 497,20 -> 495,20 -> 495,18
493,119 -> 493,114 -> 493,119 -> 495,119 -> 495,114 -> 495,119 -> 497,119 -> 497,115 -> 497,119 -> 499,119 -> 499,109 -> 499,119 -> 501,119 -> 501,109 -> 501,119
492,18 -> 492,20 -> 489,20 -> 489,26 -> 497,26 -> 497,20 -> 495,20 -> 495,18
472,145 -> 476,145
506,84 -> 506,79 -> 506,84 -> 508,84 -> 508,80 -> 508,84 -> 510,84 -> 510,82 -> 510,84 -> 512,84 -> 512,75 -> 512,84
507,93 -> 512,93
460,157 -> 465,157
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
484,123 -> 484,124 -> 501,124
462,148 -> 467,148
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
459,151 -> 464,151
480,127 -> 480,130 -> 475,130 -> 475,136 -> 494,136 -> 494,130 -> 486,130 -> 486,127
506,84 -> 506,79 -> 506,84 -> 508,84 -> 508,80 -> 508,84 -> 510,84 -> 510,82 -> 510,84 -> 512,84 -> 512,75 -> 512,84
497,29 -> 497,32 -> 493,32 -> 493,38 -> 507,38 -> 507,32 -> 501,32 -> 501,29
493,119 -> 493,114 -> 493,119 -> 495,119 -> 495,114 -> 495,119 -> 497,119 -> 497,115 -> 497,119 -> 499,119 -> 499,109 -> 499,119 -> 501,119 -> 501,109 -> 501,119
505,60 -> 505,63 -> 499,63 -> 499,71 -> 509,71 -> 509,63 -> 508,63 -> 508,60
487,53 -> 487,54 -> 500,54 -> 500,53
487,53 -> 487,54 -> 500,54 -> 500,53
493,119 -> 493,114 -> 493,119 -> 495,119 -> 495,114 -> 495,119 -> 497,119 -> 497,115 -> 497,119 -> 499,119 -> 499,109 -> 499,119 -> 501,119 -> 501,109 -> 501,119
480,127 -> 480,130 -> 475,130 -> 475,136 -> 494,136 -> 494,130 -> 486,130 -> 486,127
488,51 -> 488,44 -> 488,51 -> 490,51 -> 490,47 -> 490,51 -> 492,51 -> 492,43 -> 492,51 -> 494,51 -> 494,48 -> 494,51
480,127 -> 480,130 -> 475,130 -> 475,136 -> 494,136 -> 494,130 -> 486,130 -> 486,127
488,51 -> 488,44 -> 488,51 -> 490,51 -> 490,47 -> 490,51 -> 492,51 -> 492,43 -> 492,51 -> 494,51 -> 494,48 -> 494,51
505,60 -> 505,63 -> 499,63 -> 499,71 -> 509,71 -> 509,63 -> 508,63 -> 508,60
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
495,14 -> 495,15 -> 508,15 -> 508,14
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
457,166 -> 461,166
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
488,51 -> 488,44 -> 488,51 -> 490,51 -> 490,47 -> 490,51 -> 492,51 -> 492,43 -> 492,51 -> 494,51 -> 494,48 -> 494,51
493,119 -> 493,114 -> 493,119 -> 495,119 -> 495,114 -> 495,119 -> 497,119 -> 497,115 -> 497,119 -> 499,119 -> 499,109 -> 499,119 -> 501,119 -> 501,109 -> 501,119
493,119 -> 493,114 -> 493,119 -> 495,119 -> 495,114 -> 495,119 -> 497,119 -> 497,115 -> 497,119 -> 499,119 -> 499,109 -> 499,119 -> 501,119 -> 501,109 -> 501,119
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
493,119 -> 493,114 -> 493,119 -> 495,119 -> 495,114 -> 495,119 -> 497,119 -> 497,115 -> 497,119 -> 499,119 -> 499,109 -> 499,119 -> 501,119 -> 501,109 -> 501,119
510,91 -> 515,91
463,154 -> 468,154
493,119 -> 493,114 -> 493,119 -> 495,119 -> 495,114 -> 495,119 -> 497,119 -> 497,115 -> 497,119 -> 499,119 -> 499,109 -> 499,119 -> 501,119 -> 501,109 -> 501,119
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
474,157 -> 479,157
480,127 -> 480,130 -> 475,130 -> 475,136 -> 494,136 -> 494,130 -> 486,130 -> 486,127
491,57 -> 506,57 -> 506,56
499,89 -> 504,89
492,18 -> 492,20 -> 489,20 -> 489,26 -> 497,26 -> 497,20 -> 495,20 -> 495,18
484,123 -> 484,124 -> 501,124
505,60 -> 505,63 -> 499,63 -> 499,71 -> 509,71 -> 509,63 -> 508,63 -> 508,60
505,60 -> 505,63 -> 499,63 -> 499,71 -> 509,71 -> 509,63 -> 508,63 -> 508,60
497,29 -> 497,32 -> 493,32 -> 493,38 -> 507,38 -> 507,32 -> 501,32 -> 501,29
492,18 -> 492,20 -> 489,20 -> 489,26 -> 497,26 -> 497,20 -> 495,20 -> 495,18
493,119 -> 493,114 -> 493,119 -> 495,119 -> 495,114 -> 495,119 -> 497,119 -> 497,115 -> 497,119 -> 499,119 -> 499,109 -> 499,119 -> 501,119 -> 501,109 -> 501,119
505,60 -> 505,63 -> 499,63 -> 499,71 -> 509,71 -> 509,63 -> 508,63 -> 508,60
485,106 -> 485,96 -> 485,106 -> 487,106 -> 487,103 -> 487,106 -> 489,106 -> 489,98 -> 489,106 -> 491,106 -> 491,96 -> 491,106 -> 493,106 -> 493,105 -> 493,106 -> 495,106 -> 495,100 -> 495,106 -> 497,106 -> 497,102 -> 497,106
497,29 -> 497,32 -> 493,32 -> 493,38 -> 507,38 -> 507,32 -> 501,32 -> 501,29"""


sensors_beacons = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

sensors_beacons1 = """Sensor at x=2924811, y=3544081: closest beacon is at x=3281893, y=3687621
Sensor at x=2719183, y=2520103: closest beacon is at x=2872326, y=2415450
Sensor at x=3754787, y=3322726: closest beacon is at x=3281893, y=3687621
Sensor at x=1727202, y=1485124: closest beacon is at x=1329230, y=1133797
Sensor at x=2517008, y=2991710: closest beacon is at x=2454257, y=2594911
Sensor at x=1472321, y=3123671: closest beacon is at x=2216279, y=3414523
Sensor at x=3456453, y=3959037: closest beacon is at x=3281893, y=3687621
Sensor at x=3997648, y=2624215: closest beacon is at x=4401794, y=2000000
Sensor at x=463281, y=967584: closest beacon is at x=1329230, y=1133797
Sensor at x=2395529, y=1897869: closest beacon is at x=2454257, y=2594911
Sensor at x=3094466, y=3888307: closest beacon is at x=3281893, y=3687621
Sensor at x=2737812, y=3928154: closest beacon is at x=2744537, y=4159197
Sensor at x=813538, y=3874308: closest beacon is at x=2216279, y=3414523
Sensor at x=822358, y=1997263: closest beacon is at x=1329230, y=1133797
Sensor at x=3993754, y=3951321: closest beacon is at x=3281893, y=3687621
Sensor at x=2585409, y=3541887: closest beacon is at x=2216279, y=3414523
Sensor at x=3269796, y=3730504: closest beacon is at x=3281893, y=3687621
Sensor at x=3075750, y=2873879: closest beacon is at x=2872326, y=2415450
Sensor at x=1357, y=2747918: closest beacon is at x=-1077481, y=3057204
Sensor at x=2256257, y=344800: closest beacon is at x=1854450, y=-900998
Sensor at x=2779742, y=2308087: closest beacon is at x=2872326, y=2415450
Sensor at x=867692, y=64146: closest beacon is at x=1329230, y=1133797
Sensor at x=3454465, y=966419: closest beacon is at x=4401794, y=2000000
Sensor at x=1902550, y=2398376: closest beacon is at x=2454257, y=2594911"""


valves_paths = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""

valves_paths1 = """Valve IK has flow rate=6; tunnels lead to valves EU, XY, AD, SC, CH
Valve YW has flow rate=11; tunnels lead to valves HD, MW, ID, JD, BJ
Valve HD has flow rate=0; tunnels lead to valves YW, AA
Valve LZ has flow rate=0; tunnels lead to valves CR, IT
Valve LO has flow rate=0; tunnels lead to valves CH, YB
Valve PM has flow rate=0; tunnels lead to valves EN, YB
Valve ME has flow rate=0; tunnels lead to valves VP, TX
Valve CK has flow rate=0; tunnels lead to valves MD, LL
Valve RM has flow rate=0; tunnels lead to valves TX, AA
Valve MU has flow rate=0; tunnels lead to valves MD, BX
Valve WK has flow rate=0; tunnels lead to valves HG, IP
Valve MT has flow rate=0; tunnels lead to valves ZZ, CR
Valve EN has flow rate=0; tunnels lead to valves JE, PM
Valve AD has flow rate=0; tunnels lead to valves JE, IK
Valve IT has flow rate=8; tunnels lead to valves RY, LZ, KC
Valve JD has flow rate=0; tunnels lead to valves MD, YW
Valve RY has flow rate=0; tunnels lead to valves IT, YB
Valve FS has flow rate=10; tunnels lead to valves QQ, IP, VG, VP, LL
Valve VT has flow rate=0; tunnels lead to valves TX, MW
Valve WF has flow rate=0; tunnels lead to valves JE, HJ
Valve CH has flow rate=0; tunnels lead to valves LO, IK
Valve PZ has flow rate=17; tunnels lead to valves NZ, HJ
Valve SS has flow rate=18; tunnel leads to valve BJ
Valve MW has flow rate=0; tunnels lead to valves YW, VT
Valve JE has flow rate=16; tunnels lead to valves AD, JG, EN, ZZ, WF
Valve AA has flow rate=0; tunnels lead to valves LQ, NG, RM, CA, HD
Valve DS has flow rate=21; tunnel leads to valve PB
Valve QQ has flow rate=0; tunnels lead to valves FS, ID
Valve HG has flow rate=20; tunnels lead to valves QF, WK
Valve ID has flow rate=0; tunnels lead to valves QQ, YW
Valve WL has flow rate=0; tunnels lead to valves KI, EU
Valve OT has flow rate=0; tunnels lead to valves CR, KI
Valve KI has flow rate=14; tunnels lead to valves OT, UN, WL, XU, KC
Valve ZZ has flow rate=0; tunnels lead to valves MT, JE
Valve VD has flow rate=0; tunnels lead to valves CR, RI
Valve PB has flow rate=0; tunnels lead to valves DS, MD
Valve XU has flow rate=0; tunnels lead to valves KI, SQ
Valve CR has flow rate=7; tunnels lead to valves OT, MT, XY, VD, LZ
Valve QF has flow rate=0; tunnels lead to valves HG, NZ
Valve JG has flow rate=0; tunnels lead to valves JE, QL
Valve VP has flow rate=0; tunnels lead to valves FS, ME
Valve HJ has flow rate=0; tunnels lead to valves WF, PZ
Valve MD has flow rate=12; tunnels lead to valves CK, MU, CA, JD, PB
Valve SQ has flow rate=22; tunnel leads to valve XU
Valve XY has flow rate=0; tunnels lead to valves CR, IK
Valve VG has flow rate=0; tunnels lead to valves LQ, FS
Valve YB has flow rate=13; tunnels lead to valves RI, RY, LO, UN, PM
Valve LQ has flow rate=0; tunnels lead to valves AA, VG
Valve BX has flow rate=0; tunnels lead to valves MU, TX
Valve KC has flow rate=0; tunnels lead to valves IT, KI
Valve IP has flow rate=0; tunnels lead to valves FS, WK
Valve SC has flow rate=0; tunnels lead to valves NG, IK
Valve BJ has flow rate=0; tunnels lead to valves SS, YW
Valve NZ has flow rate=0; tunnels lead to valves QF, PZ
Valve TX has flow rate=3; tunnels lead to valves RM, QL, BX, ME, VT
Valve EU has flow rate=0; tunnels lead to valves WL, IK
Valve QL has flow rate=0; tunnels lead to valves TX, JG
Valve CA has flow rate=0; tunnels lead to valves MD, AA
Valve LL has flow rate=0; tunnels lead to valves FS, CK
Valve UN has flow rate=0; tunnels lead to valves KI, YB
Valve RI has flow rate=0; tunnels lead to valves YB, VD
Valve NG has flow rate=0; tunnels lead to valves SC, AA"""







