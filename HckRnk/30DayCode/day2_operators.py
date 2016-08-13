import sys

mealCost = float(raw_input())
tip = int(raw_input())
tax = int(raw_input())

mealCost = round(mealCost + (mealCost*tip/100.0) + (mealCost*tax/100.0))
print "The total meal cost is %d dollars." % mealCost