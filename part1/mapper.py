#!/usr/bin/python
import sys

street_codes=['34510','10030','34050']
#Filter Vehicle colors values found in the range of data, there can be more values options
black_colors= ["BLK","BK","BLACK","B K","BLAK","BLCK","BC"]

for line in sys.stdin:

    #Remove commas and splits
    line=line.strip(',').split(',')
    line_length=len(line)

    # Checking if the length is 43 is a way to ensure the data point has all 43 attributes
    if line_length==43:
        continue

    if line[33] not in black_colors:
        prob_ticket="No"
    else:
        prob_ticket="Yes"

    if line[9] in street_codes or line[10] in street_codes or line[11] in street_codes:
        print(prob_ticket+"\t"+"1")