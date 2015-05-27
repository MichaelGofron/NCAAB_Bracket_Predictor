# -*- coding: utf-8 -*-
playoffsDirectory = "./Data/playoffs/"
regDirectory = "./Data/reg_data/"
teamDirectory = "./Data/team_data/"
playoffsPrepend = "playoff_game_data_"
regPrepend = "reg_data_"
teamPrepend = "team_data_"

"""
0. game_id	1.game_date	2.away_team_id 	3.away_team_name	4.away_team_minutes	5.away_team_fgm	
6.away_team_fga	7.away_team_three_fgm	8.away_team_three_fga	9.away_team_ft 	10.away_team_fta
	11.away_team_pts	12.away_team_offreb	13.away_team_defreb	14.away_team_totreb	
 15. away_team_ast 16.away_team_to	17.away_team_stl	18.away_team_blk	19.away_team_fouls	
 20.home_team_id	 21.home_team_name	 22.home_team_minutes	23.home_team_fgm	24.home_team_fga	
 25.home_team_three_fgm 26.home_team_three_fga	27.home_team_ft	28.home_team_fta	29.home_team_pts	
 30.home_team_offreb 31.home_team_defreb	32.home_team_totreb	33.home_team_ast	34.home_team_to	
 35.home_team_stl	36.home_team_blk 37. home_team_fouls	 38.neutral_site
"""

def isConvertableFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
        
def cTeamMappingsToWins(dataTable):
    """Create Binary Win or Loss identifier
    Go through each element in the array subtract [11] - [29], away_team_pts - home_team_pts
    if > 0 then set new [39] to 1, away team win
    if < 0 then set new [39] to 0, away team loss"""
    listOfGames =[] #List of Games
                #Games = [awayteam_id, hometeam_id, boolIfAwayTeamWon]
    for game in dataTable:
        g = [int(game[2]), int(game[20])]
        winOrLoss = game[11] - game[29]
        if winOrLoss > 0: # away team win
            g.append(1)
        else: # away team loss, Note: does not error handle for ties
            g.append(0)
        listOfGames.append(g)
    return listOfGames
            
"""Convert String to Decimal"""
def strListToNumList(dataTable):
    for subList in range(0,len(dataTable)):
        for statVal in range(0,len(dataTable[subList])):
            if isConvertableFloat(dataTable[subList][statVal]):
                dataTable[subList][statVal] = float(dataTable[subList][statVal])

"""Stripping of tab spaces and forming new arrays on carriage returns"""
def convertTSVToData(filePath):
    file = open(filePath,'rbU')
    table = [row.strip().split('\t') for row in file]
    return table


def manipulateGameData(dataTable):
    dataTable.pop(0)
    strListToNumList(dataTable)
    lGameWins = cTeamMappingsToWins(dataTable)
    return lGameWins

def isNotEqualToTab(string):
    return string!='\xc2\xa0'

def removeCommas(string):
    c = ','
    if c in string:
        return string.replace(c, '')
    else:
        return string

def isNotString(obj):
    return not isinstance(obj, str)

def manipulateTeamData(listOfTeams):
    listOfTeams.pop(0)
    lOfTeamsNoCommas = [map(removeCommas, x) for x in listOfTeams]
    lOfTeamsNoTabs = [filter(isNotEqualToTab, x) for x in lOfTeamsNoCommas]
    strListToNumList(lOfTeamsNoTabs)
    listOfTeams = [filter(isNotString, x) for x in lOfTeamsNoTabs]
    dTeam = {}
    for team in listOfTeams:
        dTeam[int(team[0])] = team[1:]
    return dTeam

def mapDTeamLWins(dTeam, lWins):
    #Not tested
    #Might not exist error handeling needed
    lOfInstances = []
    lOfOutputs = []
    for score in lWins:
        awayTeam = score[0]
        homeTeam = score[1]
        binWin = score[2]
        try:
            teams = dTeam[awayTeam] + dTeam[homeTeam]
            lOfInstances.append(teams)
            lOfOutputs.append(binWin)
        except:
            pass
    return (lOfInstances, lOfOutputs)

def assertAllSameL(inList):
    sizeFirst = len(inList[0])
    for x in inList:
        if sizeFirst != len(x):
            raise ValueError("Some instances not the same length")
    return True
    
def assertGameTeamMatch(tupleData, isPlayoff = False):
    lInstances = tupleData[0]
    lOutput = tupleData[1]
    if isPlayoff:
        if len(lInstances) != 63:
            raise ValueError("There are not 63 playoff games")
    if len(lInstances[0]) != 80:
        raise ValueError("Not same number of team stats")
    if len(lInstances)!=len(lOutput):
        raise ValueError("In number of instances not equal to number of outputs")
    return assertAllSameL(lInstances)
    
    

table2010 = convertTSVToData(regDirectory + regPrepend + "2010.txt")
team2010 = convertTSVToData(teamDirectory + teamPrepend + "2010.tsv")        

dTeam2010 = manipulateTeamData(team2010)
lGames2010 = manipulateGameData(table2010)
tupleData = mapDTeamLWins(dTeam2010, lGames2010)

playoffTable2010 = convertTSVToData(playoffsDirectory + playoffsPrepend + "2010.tsv")
lPlayoff2010 = manipulateGameData(playoffTable2010)
playoffTupleData = mapDTeamLWins(dTeam2010,lPlayoff2010)
assertGameTeamMatch(playoffTupleData, True)    
    