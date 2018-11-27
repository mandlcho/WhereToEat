# =========================================================== #
# Name: Mandl
# Description:
# Simple Python 8-ball script to decide where to go for lunch
# Updated: 26 Nov 2018
# =========================================================== #

import random as rand
import json

budget = int(input("Tell me your budget in $!"))

with open('locations.json')




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
        # places that cost 10 or less
        lCheapListCount = lCheapFoodLocations[:-1]
        cheapnum = len(lCheapListCount)
        cheapPlaceRandomIdx = rand.randint(0,cheapnum)
        cheapLocation = lCheapFoodLocations[cheapPlaceRandomIdx]
        print(cheapLocation)

    if pBudgetValue >= 11:
        # places that cost 11 or more
        lExListCount = lFoodLocations[:-1]
        exnum = len(lExListCount)
        exPlaceRandomIdx = rand.randint(0,exnum)
        exLocation = lFoodLocations[exPlaceRandomIdx]
        print(exLocation)

WhereToEat(budget)
