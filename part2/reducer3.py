#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys

min_prob = 100
min_zone = ''
for entry in sys.stdin:

    k_zone, v_probability = entry.split('\t')
    v_probability = float(v_probability) 

    if v_probability < min_prob:
        min_prob = v_probability 
        min_zone = k_zone
    else:
        continue

print('Park at zone '+str(min_zone))