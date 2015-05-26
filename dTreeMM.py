# -*- coding: utf-8 -*-
import dataman as dm
from sklearn import tree
# python print decision tree
from sklearn.externals.six import StringIO  
import pydot


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


print dm.playoffTupleData

regSeasonIn = dm.tupleData[0]
regSeasonOut = dm.tupleData[1]

pIn = dm.playoffTupleData[0]
pOut = dm.playoffTupleData[1]

t = tree.DecisionTreeClassifier()
t = t.fit(regSeasonIn, regSeasonOut)
c = t.predict(pIn)
print c
print len(c)
print pOut
print len(pOut)
print percentCorrect(c, pOut)
print t

with open("dtree.dot", 'w') as f:
    f = tree.export_graphviz(t, out_file = f)
