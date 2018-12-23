# =========================================================== #
# Name: Mandl
# Description:
# Simple Python3 script to decide where to go for lunch
# Comments? Feedback? http://github.com/mandlcho
# Updated: 4th Dec 2018
# =========================================================== #

import sys
import random as rand

# ui imports
import wheretoeatdesign
from PyQt4 import QtCore,QtGui

# argparse import for adding arguments : https://stackoverflow.com/questions/20063/whats-the-best-way-to-parse-command-line-arguments
import argparse


# data ======================================================= #

lFoodLocations = ["DailyCut",
                  "Subway",
                  "Pho",
                  "iSteaks",
                  "Carls Jr",
                  "FoodBarn",
                  "TwoChefs",
                  "Red",
                  "Bismillah Briyani",
                  "Omo Omo Don",
                  "Eighteen Chefs"]

lCheapFoodLocations = ["Air",
                       "Grass",
                       "Timbre+",
                       "Bread",
                       "Koufu",
                       "FoodMaster",
                       "CoffeeHive"]

testLocationList = []

# =========================================================== #

class WhereToEatApp(QtGui.QMainWindow, wheretoeatdesign.Ui_MainWindow):
    def __init__(self, parent=None):
        super(WhereToEatApp, self).__init__(parent)
        self.showUI()

        # -----------------------------------------------------------------------------------------------*

    def printHello(self):
        print('code is working')

    def showUI(self):
        self.setupUi(self)
        self.btn_Tellme.clicked.connect(self.showDialog)
        self.btn_Surpriseme.clicked.connect(self.SurpriseMe)
        self.btn_browse.clicked.connect(self.BrowseFile)

    def updateUI(self, pOutput):
        self.Le_showresult.setText(pOutput)

    def showDialog(self):
        pBudgetValue, UserInput = QtGui.QInputDialog.getInt(self,"Input Budget","Enter it here")
        if UserInput:
            self.updateUI(WhereToEat(pBudgetValue))

    def BrowseFile(self):
        # https://www.youtube.com/watch?v=trklFGA1CKQ&feature=youtu.be
        filePath = QtGui.QFileDialog.getOpenFileName(self,
                                                     'Single File',
                                                     "~/Users/Mandl/Desktop",
                                                     '*.json')
        print('filePath',filePath,'\n')
        fileHandle = open(filePath,'r')
        locationList = fileHandle.readlines()
        print(fileHandle)
        for eachline in locationList:
            # print(eachline)
            testLocationList.append(eachline)
            print(len(testLocationList))

    def SurpriseMe(self):
        IRandomBudget = rand.randint(1, 25)
        SurpriseLoc = WhereToEat(IRandomBudget)
        print(SurpriseLoc)
        self.updateUI(SurpriseLoc)


def WhereToEat(pBudgetValue):
    if pBudgetValue == 0:
        cheapLocation = lCheapFoodLocations[0]
        return cheapLocation

    if pBudgetValue <= 10:
        # places that cost 10 or less
        lCheapListCount = lCheapFoodLocations[:-1]
        cheapnum = len(lCheapListCount)
        cheapPlaceRandomIdx = rand.randint(0, cheapnum)
        cheapLocation = lCheapFoodLocations[cheapPlaceRandomIdx]
        return cheapLocation

    if pBudgetValue >= 11:
        # places that cost 11 or more
        lExListCount = lFoodLocations[:-1]
        exnum = len(lExListCount)
        exPlaceRandomIdx = rand.randint(0, exnum)
        exLocation = lFoodLocations[exPlaceRandomIdx]
        return exLocation

def main():
    # initialise the parser -------------------------------------------------------------------------*
    parser = argparse.ArgumentParser(description="Helps you decide on a place to eat if you cant!")
    parser.add_argument('budget', type=int, nargs='?', help='budget input')  # this is where you add the additional / required arguments.

    args = vars(parser.parse_args())  # Parse the args
    inputArg = args['budget']

    if inputArg is not None:
        print(WhereToEat(inputArg))
        print(args)
    else:
        app = QtGui.QApplication(sys.argv)
        form = WhereToEatApp()
        form.show()
        app.exec_()

if __name__ == '__main__':
    main()