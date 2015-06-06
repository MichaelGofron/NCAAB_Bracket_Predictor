# -*- coding: utf-8 -*-

l = [26.166666666666668, 55.93333333333333, 46.78, 5.533333333333333, 16.233333333333334, 34.09, 17.033333333333335, 23.966666666666665, 71.07, 74.9, 74.9, 13.1, 25.433333333333334, 38.53333333333333, 38.53, 15.033333333333333, 10.766666666666667, 6.733333333333333, 6.9, 17.2, 18.866666666666667, 54.1, 34.87, 4.633333333333334, 17.166666666666668, 26.99, 11.166666666666666, 17.266666666666666, 64.67, 53.53333333333333, 53.53, 11.9, 19.3, 31.2, 31.2, 7.633333333333334, 14.333333333333334, 4.966666666666667, 2.3, 19.966666666666665, 7.300000000000001, 1.8333333333333286, 11.910000000000004, 0.8999999999999995, -0.9333333333333336, 7.100000000000005, 5.866666666666669, 6.699999999999999, 6.3999999999999915, 21.366666666666674, 21.370000000000005, 1.1999999999999993, 6.133333333333333, 7.333333333333332, 7.330000000000002, 7.3999999999999995, -3.5666666666666664, 1.7666666666666666, 4.6000000000000005, -2.7666666666666657]
print len(l)

"""
lAway = ['team_fgm', 
'team_fga', 'team_fgpct', 'team_three_fgm', 'team_three_fga', 
'team_three_fgpct', 'team_ft', 'team_fta', 'team_ftpct', 
'team_pts', 'team_ptsavg', 'team_offreb', 'team_defreb', 
'team_totreb', 'team_rebavg', 'team_ast', 'team_to', 
'team_stl', 'team_blk', 'team_fouls', 'opp_team_fgm', 'opp_team_fga', 
'opp_team_fgpct', 'opp_team_three_fgm', 'opp_team_three_fga', 
'opp_team_three_fgpct', 'opp_team_ft', 'opp_team_fta', 'opp_team_ftpct', 
'opp_team_pts', 'opp_team_ptsavg', 'opp_team_offreb', 'opp_team_defreb', 
'opp_team_totreb', 'opp_team_rebavg', 'opp_team_ast', 'opp_team_to', 'opp_team_stl', 
'opp_team_blk', 'opp_team_fouls']

lHome = lAway[:]
print len(lAway)
def appendSpot(inList, offset = 0, s = ''):
    for x in xrange(len(inList)):
        inList[x] = s + '[ ' + str(x + offset) + ' ]' + ' ' + inList[x]
    return inList
lConcat = appendSpot(lAway, s = 'ATeam ') + appendSpot(lHome, len(lAway), s = 'HTeam ')

print lConcat"""