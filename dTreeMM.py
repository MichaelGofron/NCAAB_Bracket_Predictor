# -*- coding: utf-8 -*-
from sklearn import tree
# python print decision tree
from sklearn.externals.six import StringIO  
import pydot
import pickle as p
"""['ATeam [ 0 ] team_fgm', 'ATeam [ 1 ] team_fga', 'ATeam [ 2 ] team_fgpct', 
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
'HTeam [ 40 ] team_fgm', 'HTeam [ 41 ] team_fga', 'HTeam [ 42 ] team_fgpct', 
'HTeam [ 43 ] team_three_fgm', 'HTeam [ 44 ] team_three_fga', 
'HTeam [ 45 ] team_three_fgpct', 'HTeam [ 46 ] team_ft', 
'HTeam [ 47 ] team_fta', 'HTeam [ 48 ] team_ftpct', 'HTeam [ 49 ] team_pts', 
'HTeam [ 50 ] team_ptsavg', 'HTeam [ 51 ] team_offreb', 
'HTeam [ 52 ] team_defreb', 'HTeam [ 53 ] team_totreb', 
'HTeam [ 54 ] team_rebavg', 'HTeam [ 55 ] team_ast', 'HTeam [ 56 ] team_to', 
'HTeam [ 57 ] team_stl', 'HTeam [ 58 ] team_blk', 'HTeam [ 59 ] team_fouls', 
'HTeam [ 60 ] opp_team_fgm', 'HTeam [ 61 ] opp_team_fga', 
'HTeam [ 62 ] opp_team_fgpct', 'HTeam [ 63 ] opp_team_three_fgm', 
'HTeam [ 64 ] opp_team_three_fga', 'HTeam [ 65 ] opp_team_three_fgpct', 
'HTeam [ 66 ] opp_team_ft', 'HTeam [ 67 ] opp_team_fta', 
'HTeam [ 68 ] opp_team_ftpct', 'HTeam [ 69 ] opp_team_pts', 
'HTeam [ 70 ] opp_team_ptsavg', 'HTeam [ 71 ] opp_team_offreb', 
'HTeam [ 72 ] opp_team_defreb', 'HTeam [ 73 ] opp_team_totreb', 
'HTeam [ 74 ] opp_team_rebavg', 'HTeam [ 75 ] opp_team_ast', 
'HTeam [ 76 ] opp_team_to', 'HTeam [ 77 ] opp_team_stl', 
'HTeam [ 78 ] opp_team_blk', 'HTeam [ 79 ] opp_team_fouls']"""
def percentCorrect(cBin, vBin):
    #cBin = Classification binary list , ie our guesses
    #vBin = verification binary list, ie truth
    labeledCorrectlyCount = 0
    labeledIncorrectlyCount = 0
    for i in xrange(len(cBin)):
        if cBin[i] == vBin[i]:
            labeledCorrectlyCount += 1
        else:
            labeledIncorrectlyCount += 1
    return float(labeledCorrectlyCount)/len(cBin)
 
def loadTupleData(lString):
    instances = []
    outBin = []
    for each in lString:
        fileName = 'tupleData_' + each + '.p'
        tData = p.load(open(fileName, 'rb'))
        instances = instances + tData[0]
        outBin = outBin + tData[1]
    return (instances, outBin)


def produceDecisionTree(sLTrain, LDTVars):
    #Do more with SlDTVars
    tTrain = loadTupleData(sLTrain)
    t = tree.DecisionTreeClassifier()
    t = t.fit(tTrain[0], tTrain[1])
    return t

def evaluatePerformance(sLTest, dTree):
    tTest = loadTupleData(sLTest)
    c = dTree.predict(tTest[0])
    return percentCorrect(c, tTest[1])
    
def generatePDF(PDFName,dTree):
    dot_data = StringIO() 
    tree.export_graphviz(dTree, out_file=dot_data) 
    graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
    graph.write_pdf(PDFName + ".pdf")
    
def driver(sLTrain, sLTest, LDTVars,PDFName):
    t = produceDecisionTree(sLTrain, LDTVars)
    print "Performance of tree: ", evaluatePerformance(sLTest, t)
    generatePDF(PDFName,t)

def regVsPlay(sARTName, sIRTName, lDTVars = []):
    regPrepend = 'r-'
    playPrepend = 'p-'
    allReg = []
    allPlay = []
    for year in xrange(2010, 2016):
        sReg = [regPrepend + str(year)]
        sPlay = [playPrepend + str(year)]
        allReg = allReg + sReg
        allPlay = allPlay + sPlay
        driver(sReg, sPlay, lDTVars, sIRTName  + str(year))
    driver(allReg, allPlay, lDTVars, sARTName)

regVsPlay('AllReg', 'dTreeReg')