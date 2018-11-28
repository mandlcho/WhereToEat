# =========================================================== #
# Name: Mandl
# Description:
# Simple Python 8-ball script to decide where to go for lunch
# Updated: 26 Nov 2018
# =========================================================== #

from PyQt4 import QtCore,QtGui
import wheretoeatdesign
import sys

import random as rand
import json

# budget = int(input("Tell me your budget in $!"))

# data ======================================================= #

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

# =========================================================== #

class WhereToEatApp(QtGui.QMainWindow, wheretoeatdesign.Ui_MainWindow):
    def __init__(self, parent=None):
        super(WhereToEatApp, self).__init__(parent)
        self.setupUi(self)
        self.btn_Tellme.clicked.connect(self.printHello)

    def printHello(self):
        print('code is working')

    def WhereToEat(pBudgetValue):
        if pBudgetValue <= 10:
            # places that cost 10 or less
            lCheapListCount = lCheapFoodLocations[:-1]
            cheapnum = len(lCheapListCount)
            cheapPlaceRandomIdx = rand.randint(0, cheapnum)
            cheapLocation = lCheapFoodLocations[cheapPlaceRandomIdx]
            print(cheapLocation)

        if pBudgetValue >= 11:
            # places that cost 11 or more
            lExListCount = lFoodLocations[:-1]
            exnum = len(lExListCount)
            exPlaceRandomIdx = rand.randint(0, exnum)
            exLocation = lFoodLocations[exPlaceRandomIdx]
            print(exLocation)

def main():
    app = QtGui.QApplication(sys.argv)
    form = WhereToEatApp()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()