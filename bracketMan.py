# -*- coding: utf-8 -*-
mw = [334,328,513,392,768,87,782,140,559,306,703,86,735,500,472,270]
w = [796,29,51,457,31,812,740,529,521,518,430,2915,275,254,699,149]
e = [739,746,522,367,504,556,416,490,365,257,175,811,109,14,14927,342]
s = [193,260,311,251,732,663,312,626,603,173,110,676,207,9,493,579]


#checkB(l, '2015', conf = 's')
mw32= [0,1,2,3,4,5,6,7]
w32 = [0,7,4,3,5,13,9,1]
e32 = [0,7,4,3,10,2,6,1]
s32 = [0,7,4,3,10,13,6,1]

mw16 = [0,4,2,6]
w16 = [0,3,5,1]
e16 = [7,3,2,6]
s16 = [0,4,10,1]

mw8 = [0,2]
w8 = [0,1]
e8 = [3,6]
s8 = [0,1]

mw4 = [0]
w4 = [0]
e4 = [6]
s4 = [0]

def rT(mw,w,e,s):
    return [mw,w,e,s]

t64 = rT(mw, w, e, s)
t32 = rT(mw32, w32, e32,s32)
t16 = rT(mw16, w16, e16, s16)
t8 = rT(mw8, w8, e8, s8)
t4 = rT(mw4, w4, e4, s4)
t2 = [193, 796]
t1 = [193]

regionals = [t64, t32, t16, t8, t4]


def createWinningBracket(regionalR, r2, r1):
    roundWinners = []
    for i in xrange(1,len(regionalR)):
        roundWinners.append(createWinningRound(regionalR[0],regionalR[i]))
    roundWinners.append(r2)
    roundWinners.append(r1)
    return roundWinners

def createWinningRound(allRegions,regionRound):
    roundWinner = []
    for i in range(len(allRegions)):
        curr = allRegions[i]
        currN = regionRound[i]
        for j in currN:
            roundWinner.append(curr[j])
    return roundWinner


l =  createWinningBracket(regionals, t2, t1)
for r in l:
    print len(r)

def checkB(inlist, syear, conf = None):
    pass

"""d = {finals : {1: [intTeam], 2: [intTeam], 4: [intTeam,...]},
        conf: {2: {s: [intTeam, intTeam], w: [intTeam...], e:...,mw...}, 
        4: { s: [....], }}}
   d = {finals : [[4], [2], [1]]
   
   [[32], [16], [8], [4], [2], [1]]"""
   
def checkRegLvl(picks,year):
    pass
    """
    This function will check a regional level in the NCAA tournament
    and return a score indicating how well the picks for that level performed
    """
    