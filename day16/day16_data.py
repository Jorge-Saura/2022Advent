#--- Day 16: Proboscidea Volcanium ---

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



