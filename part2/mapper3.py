#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys
for entry in sys.stdin:
    k_zone, v_probability = entry.split('\t')
    try:
        v_probability = eval(v_probability)
        if float(v_probability[1]) == 1 and float(v_probability[0]) == 0:
            continue
        else:
            v_probability = float(v_probability[0])/float(v_probability[1])
    except:
        pass
    print(k_zone+'\t'+str(v_probability))
