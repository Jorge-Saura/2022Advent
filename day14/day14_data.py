#--- Day 14: Regolith Reservoir ---

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
