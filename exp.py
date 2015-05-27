# -*- coding: utf-8 -*-
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

print lConcat