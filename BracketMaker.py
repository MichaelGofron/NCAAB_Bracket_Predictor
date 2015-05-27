# -*- coding: utf-8 -*-
"""
Created on Wed May 27 14:25:48 2015

@author: Juan David Dominguez & Michael Gofron
"""
import dataman as dman
import dTreeMM as dT
import pickle as p

MW2015 = [334,328,513,392,768,87,782,140,559,306,703,86,735,500,472,270]
W2015 = [796,29,51,457,31,812,740,529,521,518,430,2915,275,254,699,149]
E2015 = [739,746,522,367,504,556,416,490,365,257,175,811,109,14,14927,342]
S2015 = [193,260,311,251,732,663,312,626,603,173,110,676,207,9,493,579]

def winner(awayID,homeID,year,dTree):
    awayTeamInfo = getTeamData(awayID,year)
    homeTeamInfo = getTeamData(homeID,year)
    teamsInfo = awayTeamInfo + homeTeamInfo
    winArr = dTree.predict(teamsInfo)
    win = winArr[0]
    return win
    
def getTeamData(teamID,year):
    dTeamFile = "dTeam_" + str(year) + ".p"
    dTeam = p.load(open(dTeamFile, 'rb'))
    teamInfo = dTeam[teamID]
    return teamInfo
    
def seedTeams(inTeams):
    seededTeams = []
    if len(inTeams) != 16:
        raise ValueError("Not given 16 teams to seed")
    for i in xrange(len(inTeams)):
        seededTeams.append((i+1, inTeams[i]))
    return seededTeams

    
def regionalTournament(ltSeedsIds,year,dTree):
    if len(ltSeedsIds) == 1:
        return ltSeedsIds[0][1]
    matchedTeams = matchSeeds(ltSeedsIds)
    lWinningTeams = []
    for mTeam in matchedTeams:
        lWinningTeams.append(mTeam[not winner(mTeam[0][1], mTeam[1][1], year, dTree)])
    return regionalTournament(lWinningTeams, year, dTree)
        
        
def matchSeeds(inTeams):
    numTeams = len(inTeams)
    if numTeams == 1:
        return inTeams
    elif numTeams % 2 == 1:
        raise ValueError("Teams for Matched seeds is not even")
    else:
        halfTeams = numTeams/2 
        matchedTeams = []
        for team in xrange(halfTeams):
            matchedTeam = [inTeams[team], inTeams[numTeams - 1 - team]]
            matchedTeams.append(matchedTeam)
        return matchedTeams
        
def NCAATournament(year,dTree):
    MWseed = seedTeams(MW2015)
    Wseed = seedTeams(W2015)
    Eseed = seedTeams(E2015)
    Sseed = seedTeams(S2015)
    MW = regionalTournament(MWseed,2015,dTree)
    W = regionalTournament(Wseed,2015,dTree)
    E = regionalTournament(Eseed,2015,dTree)
    S = regionalTournament(Sseed,2015,dTree)
    # MW vs E, W vs S
    MWvsE = E
    if winner(MW,E,year,dTree):
        MWvsE = MW
    WvsS = S
    if winner(W,S,year,dTree):
        WvsS = W
    finalWinner = WvsS
    if winner(MWvsE,WvsS,year,dTree):
        finalWinner = MWvsE
    return finalWinner
            
            
        
t = dT.produceDecisionTree(["r-2015"], []) 
sTeams = seedTeams(MW2015)
print NCAATournament(2015,t)