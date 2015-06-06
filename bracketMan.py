# -*- coding: utf-8 -*-
MW2015 = [334,328,513,392,768,87,782,140,559,306,703,86,735,500,472,270]
W2015 = [796,29,51,457,31,812,740,529,521,518,430,2915,275,254,699,149]
E2015 = [739,746,522,367,504,556,416,490,365,257,175,811,109,14,14927,342]
S2015 = [193,260,311,251,732,663,312,626,603,173,110,676,207,9,493,579]

tot2015 = [MW2015, W2015, E2015, S2015]

l = [334,328,513,392,768,87,782,140]

#checkB(l, '2015', conf = 's')
lmw2015_32= [0,1,2,3,4,5,6,7]
lw2015_32 = [0,7,4,3,5,13,9,1]
le2015_32 = [0,7,4,3,10,2,6,1]
ls2015_32 = [0,7,4,3,10,13,6,1]

totNext2015_32 = [lmw2015_32, lw2015_32, le2015_32, ls2015_32]

NCAABracket2015 = []

tempL = []
for i in range(len(tot2015)):
    curr = tot2015[i]
    currN = totNext2015_32[i]
    for j in currN:
        tempL.append(curr[j])
print tempL



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
    