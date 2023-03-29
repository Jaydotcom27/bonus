#!/usr/bin/python

import sys

prediction = dict()

for line in sys.stdin:
    line = line.split("\t")
    probability = line[0]
    counter = float(line[1])
    prediction[probability] = prediction.get(probability,0) + counter


prob_yes = prediction['yes']
prod_yes_no = prediction['yes'] + prediction['no']
final_probalility = prob_yes/(prob_yes+prod_yes_no)

print("The Probability of Black vehicless parking illegally is:",final_probalility)