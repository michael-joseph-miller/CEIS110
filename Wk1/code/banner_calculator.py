# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Party Calculator - Michael J. Miller
# Date: Aug 29, 2022

print("Welcome to the Party Banner Calculator")
bannerWidth = float(input("Please input banner width: "))
bannerLength = float(input("Please input banner length: "))
costPerSqInch = float(input("Please input banner cost per square inch: "))
totalCost = bannerWidth * bannerLength * costPerSqInch
print("The total cost of the banner is: ", totalCost)
