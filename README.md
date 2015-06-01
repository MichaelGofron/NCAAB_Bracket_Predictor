# NCAAB_Bracket_Prector

This program was created by Juan David Dominguez and Michael Gofron.
We created this program for our Machine Learning class, EECS 349 at Northwestern University

The program uses machine learning algorithms based on the statistics in the 
regular season of the college basketball season in order to determine what 
bracket a person should pick in order to maximize their chance of getting a perfect bracket.

dataman.py:
Converts raw data obtained from scrapping program (scrapped from https://github.com/rodzam/ncaab-stats-scraper) into a data format that scikit machine learning algorithms can properly take in and output.

dTreeMM.py:
Creates machine learning algorithm that analyzes formatted data. This machine learning algorithm is later used in BracketMaker to develop a proper NCAA bracket.


BracketMaker.py:
Using saved machine learning algorithm it will compute the ideal bracket.
The different conferences and seeds are hard-coded and you will need to modify them
at the top in the MW, W, E, S conference arrays which are ordered by seeding where
MW[0] = #1 seed of the midwest conference. MW[1] = #2 seed of the midwest conference and so on. Each element in the array is a team stored as its unique team ID.