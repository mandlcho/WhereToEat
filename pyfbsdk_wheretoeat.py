# import pyfbsdk as fb
# import pyfbsdk_additions as fba

# import sys
# from PyQt4 import QtGui

import random as rand

# app = QtGui.QApplication(sys.argv)

# window = QtGui.QWidget()
# window.setGeometry(0,0,500,300)
# window.setWindowTitle("Where To Eat!")

# # define buttons
# btnGenerous = fb.FBButton()
# btnBroke = fb.FBButton()

lFoodLocations = ["DailyCut",
                  "Subway", 
                  "Pho", 
                  "iSteaks",
                  "Carls Jr",
                  "FoodBarn",
                  "TwoChefs",
                  "Red"]

lCheapFoodLocations = ["Downstairs",
                       "Guest La Mian",
                       "Grass",
                       "Bread",
                       "Koufu",
                       "FoodMaster"]

def WhereToEat(pBudgetValue):
    if pBudgetValue <= 10:
        lCheapListCount = lCheapFoodLocations[:-1]
        cheapnum = len(lCheapListCount)
        cheapPlaceRandomIdx = rand.randint(0,cheapnum)
        cheapLocation = lCheapFoodLocations[cheapPlaceRandomIdx]
        # places that cost 10 or below
        # fb.FBMessageBox("Eat Cheap la", cheapLocation, "lets go")
        print cheapLocation

    if pBudgetValue >= 11:
        # places that cost 11 or more
        lExListCount = lFoodLocations[:-1]
        exnum = len(lExListCount)
        exPlaceRandomIdx = rand.randint(0,exnum)
        exLocation = lFoodLocations[exPlaceRandomIdx]
        print exLocation
        # fb.FBMessageBox("Feeling Generous eh?", exLocation, "lets go")

        # pass

WhereToEat(5)
# window.show()
