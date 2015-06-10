# -*- coding: utf-8 -*-
import pickle as p
playoffsDirectory = "./Data/playoffs/"
regDirectory = "./Data/reg_data/"
teamDirectory = "./Data/team_data/"
playoffsPrepend = "playoff_game_data_"
regPrepend = "reg_data_"
teamPrepend = "team_data_"
nameDictDir = "./DictionariesOfTeamNames/"
nameDictPrepend = 'dTNames_'
pickleFIleEnding = '.p'
tupleDataDir = './tupleData/'
tupleDataFName = 'tupleData_'
statsDictDir = './DictionariesOfTeamStats/'
statsDictFName = "dTeam_"
numGamesP = 63
lOfTeamData = 60
doNotDivideL = [2, 5, 8, 10, 14,22, 25, 28, 30, 34]
"""
Game Info:
0. game_id	1.game_date	2.away_team_id 	3.away_team_name	4.away_team_minutes	5.away_team_fgm	
6.away_team_fga	7.away_team_three_fgm	8.away_team_three_fga	9.away_team_ft 	10.away_team_fta
	11.away_team_pts	12.away_team_offreb	13.away_team_defreb	14.away_team_totreb	
 15. away_team_ast 16.away_team_to	17.away_team_stl	18.away_team_blk	19.away_team_fouls	
 20.home_team_id	 21.home_team_name	 22.home_team_minutes	23.home_team_fgm	24.home_team_fga	
 25.home_team_three_fgm 26.home_team_three_fga	27.home_team_ft	28.home_team_fta	29.home_team_pts	
 30.home_team_offreb 31.home_team_defreb	32.home_team_totreb	33.home_team_ast	34.home_team_to	
 35.home_team_stl	36.home_team_blk 37. home_team_fouls	 38.neutral_site
 
 
 Team Info:
 ['team_id', 'team_name', 'team_minutes', 'team_fgm', 'team_fga', 'team_fgpct',
 'team_three_fgm', 'team_three_fga', 'team_three_fgpct', 'team_ft', 'team_fta',
 'team_ftpct', 'team_pts', 'team_ptsavg', 'team_offreb', 'team_defreb', 
 'team_totreb', 'team_rebavg', 'team_ast', 'team_to', 'team_stl', 'team_blk', 
 'team_fouls', 'team_dbldbl', 'team_trpdbl', 'opp_team_minutes', 
 'opp_team_fgm', 'opp_team_fga', 'opp_team_fgpct', 'opp_team_three_fgm', 
 'opp_team_three_fga', 'opp_team_three_fgpct', 'opp_team_ft', 'opp_team_fta', 
 'opp_team_ftpct', 'opp_team_pts', 'opp_team_ptsavg', 'opp_team_offreb', 
 'opp_team_defreb', 'opp_team_totreb', 'opp_team_rebavg', 'opp_team_ast', 
 'opp_team_to', 'opp_team_stl', 'opp_team_blk', 'opp_team_fouls', 
 'opp_team_dbldbl', 'opp_team_trpdbl']
 
 ['ATeam [ 0 ] team_fgm', 'ATeam [ 1 ] team_fga', 'ATeam [ 2 ] team_fgpct', 
'ATeam [ 3 ] team_three_fgm', 'ATeam [ 4 ] team_three_fga', 
'ATeam [ 5 ] team_three_fgpct', 'ATeam [ 6 ] team_ft', 
'ATeam [ 7 ] team_fta', 'ATeam [ 8 ] team_ftpct', 'ATeam [ 9 ] team_pts', 
'ATeam [ 10 ] team_ptsavg', 'ATeam [ 11 ] team_offreb', 
'ATeam [ 12 ] team_defreb', 'ATeam [ 13 ] team_totreb', 
'ATeam [ 14 ] team_rebavg', 'ATeam [ 15 ] team_ast', 'ATeam [ 16 ] team_to', 
'ATeam [ 17 ] team_stl', 'ATeam [ 18 ] team_blk', 'ATeam [ 19 ] team_fouls', 
'ATeam [ 20 ] opp_team_fgm', 'ATeam [ 21 ] opp_team_fga', 
'ATeam [ 22 ] opp_team_fgpct', 'ATeam [ 23 ] opp_team_three_fgm', 
'ATeam [ 24 ] opp_team_three_fga', 'ATeam [ 25 ] opp_team_three_fgpct', 
'ATeam [ 26 ] opp_team_ft', 'ATeam [ 27 ] opp_team_fta', 
'ATeam [ 28 ] opp_team_ftpct', 'ATeam [ 29 ] opp_team_pts', 
'ATeam [ 30 ] opp_team_ptsavg', 'ATeam [ 31 ] opp_team_offreb', 
'ATeam [ 32 ] opp_team_defreb', 'ATeam [ 33 ] opp_team_totreb', 
'ATeam [ 34 ] opp_team_rebavg', 'ATeam [ 35 ] opp_team_ast', 
'ATeam [ 36 ] opp_team_to', 'ATeam [ 37 ] opp_team_stl', 
'ATeam [ 38 ] opp_team_blk', 'ATeam [ 39 ] opp_team_fouls',  
 

tGamesPlayed = round(float('ATeam [ 9 ] team_pts')/ 'ATeam [ 10 ] team_ptsavg')


 ['ATeam [ 0 ] team_fgm'/tGamePlayes, 'ATeam [ 1 ] team_fga' /tGampePlayed, 'ATeam [ 2 ] team_fgpct', 
'ATeam [ 3 ] team_three_fgm'/tGamesPlayed, 'ATeam [ 4 ] team_three_fga' /tGamesPlayed, 
'ATeam [ 5 ] team_three_fgpct', 'ATeam [ 6 ] team_ft'/tGamesPlayed, 
'ATeam [ 7 ] team_fta'/tGamesPlayed, 'ATeam [ 8 ] team_ftpct', 'ATeam [ 9 ] team_pts', 
'ATeam [ 10 ] team_ptsavg', 'ATeam [ 11 ] team_offreb'/tGamesPlayed, 
'ATeam [ 12 ] team_defreb'/tGamesPlayed, 'ATeam [ 13 ] team_totreb', 
'ATeam [ 14 ] team_rebavg', 'ATeam [ 15 ] team_ast'/tGamesPlayed, 'ATeam [ 16 ] team_to'/tGamesPlayed, 
'ATeam [ 17 ] team_stl'/tGamesPlayed, 'ATeam [ 18 ] team_blk'/tGamesPlayed, 'ATeam [ 19 ] team_fouls'/tGamesPlayed, 
'ATeam [ 20 ] opp_team_fgm' /tGamesPlayed, 'ATeam [ 21 ] opp_team_fga'/tGamesPlayed, 
'ATeam [ 22 ] opp_team_fgpct', 'ATeam [ 23 ] opp_team_three_fgm'/tGamesPlayed, 
'ATeam [ 24 ] opp_team_three_fga'/tGamesPlayed, 'ATeam [ 25 ] opp_team_three_fgpct', 
'ATeam [ 26 ] opp_team_ft'/tGamesPlayed, 'ATeam [ 27 ] opp_team_fta'/tGamesPlayed, 
'ATeam [ 28 ] opp_team_ftpct', 'ATeam [ 29 ] opp_team_pts', 
'ATeam [ 30 ] opp_team_ptsavg', 'ATeam [ 31 ] opp_team_offreb'/tGamesPlayed, 
'ATeam [ 32 ] opp_team_defreb'/tGamesPlayed, 'ATeam [ 33 ] opp_team_totreb', 
'ATeam [ 34 ] opp_team_rebavg', 'ATeam [ 35 ] opp_team_ast'/tGamesPlayed, 
'ATeam [ 36 ] opp_team_to'/tGamesPlayed, 'ATeam [ 37 ] opp_team_stl'/tGamesPlayed, 
'ATeam [ 38 ] opp_team_blk'/tGamesPlayed, 'ATeam [ 39 ] opp_team_fouls'/tGamesPlayed, 

differentiate all

 
 
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
        if len(lInstances) != numGamesP:
            print "numGames == ",len(lInstances)
            print lInstances
            raise ValueError("There are not 63 playoff games")
    if len(lInstances[0]) != lOfTeamData * 2:
        raise ValueError("Not same number of team stats")
    if len(lInstances)!=len(lOutput):
        raise ValueError("In number of instances not equal to number of outputs")
    return assertAllSameL(lInstances)
    
def createTupleData(gameFile, dTeam, stringYear, isPlayOff = False):
    table = convertTSVToData(gameFile)
    lGames = manipulateGameData(table)
    tupleData = mapDTeamLWins(dTeam, lGames)
    assertGameTeamMatch(tupleData, isPlayOff)
    prePend = 'r-'
    if isPlayOff:
        prePend = 'p-'
    fileName = tupleDataDir + tupleDataFName + prePend + stringYear + '.p'
    p.dump(tupleData, open(fileName, 'wb'))
    return tupleData


def avgDiffStats(teamDict):
    for k in teamDict:
        teamList = teamDict[k]
        lenList = len(teamList)
        tGamesPlayed = float(round(float(teamList[9])/teamList[10]))
        oppTeamInd = lenList/2
        for i in xrange(lenList):
            if i not in doNotDivideL:
                teamList[i] = teamList[i]/tGamesPlayed
        ownTeamData = teamList[:oppTeamInd]
        oppTeamData = teamList[oppTeamInd:lenList]
        diff = [x - y for x,y in zip(ownTeamData, oppTeamData) ]
        teamList.extend(diff)
        teamDict[k] = teamList
    return teamDict

def saveTeamDict(teamFile,stringYear):
    team = convertTSVToData(teamFile)
    teamDict = manipulateTeamData(team)
    dTeam = avgDiffStats(teamDict)
    fileName = statsDictDir + statsDictFName + stringYear + ".p"
    p.dump(dTeam,open(fileName,'wb'))
    
def saveAllTeams():
    for year in xrange(2010,2016):
        teamFile = teamDirectory + teamPrepend + str(year) + ".tsv"
        saveTeamDict(teamFile,str(year))

def generateDataForAllYears():
    for year in xrange(2010,2016):
        dTeamFile = statsDictDir + statsDictFName + str(year) + pickleFIleEnding
        regFile = regDirectory + regPrepend + str(year) + ".txt"
        playoffFile = playoffsDirectory + playoffsPrepend + str(year) + ".tsv"
        dTeam = loadFile(dTeamFile)
        createTupleData(regFile,dTeam,str(year))
        createTupleData(playoffFile,dTeam,str(year),True)

def createIDNameDict(sYear):
    fileName = teamDirectory + teamPrepend + sYear + '.tsv'
    team = convertTSVToData(fileName)
    team.pop(0)
    dTeam = {}
    for t in team:
        dTeam[int(t[0])] = t[1]
    return dTeam

def createDNames():
    for x in xrange(2010, 2016):
        d = createIDNameDict(str(x))
        fileName = nameDictDir + nameDictPrepend + str(x) + pickleFIleEnding
        p.dump(d, open(fileName, 'wb'))
    print 'done'

def loadFile(fileName):
    ret = p.load(open(fileName, 'rb'))
    return ret
def generateDataPPriorvPCurrent():
    priorPlayoffInstances = []
    priorPlayoffWins = []
    tFile = tupleDataDir + tupleDataFName + 'p-'
    for yr in xrange(2010, 2015):
        currTFile = tFile + str(yr) + '.p'
        tData = p.load(open(currTFile, 'rb'))
        priorPlayoffInstances.extend(tData[0])
        priorPlayoffWins.extend(tData[1])
    tupleData = (priorPlayoffInstances, priorPlayoffWins)
    p.dump(tupleData, open(tFile + '2010-2015.p', 'wb'))

generateDataPPriorvPCurrent()