#!/usr/bin/python

import sys
Street = ["34510", "10030", "34050"]
colors = ["Black", "BLK", "BK", "BK.", "BLAC", "BK/","BCK","BLK.","B LAC","BC"]


for line in sys.stdin:

    line = line.strip()
    line = line.split(',')
    len_line = len(line)
    
    if len_line == 43:
        continue
    

    if line[33] in colors:
        probalility = "yes"
    else:
        probalility = "no"

    if line[9] in Street or line[10] in Street or line[11] in Street:

        print(probalility+"\t"+"1")