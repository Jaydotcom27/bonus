#!/usr/bin/python

import sys

dic=dict()
for line in sys.stdin:
    line = line.split("\t")
    #key: probability values yes or no depending of the color
    prob=line[0]
    #value
    value=line[1]
    dic[prob]=dic.get(prob,0)+value

prob_yes=dic['Yes']
total=dic['Yes']+dic['No']
result=prob_yes/total

print("Probability of a Black color vehicle parking is:",result)