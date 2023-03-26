#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys
count_total_value = {}
for line in sys.stdin:
    d, c = line.split('\t')
    try:
        c = int(c)
        count_total_value[d] = [count_total_value.get(d, [0,0])[0] + c, count_total_value.get(d, [0,0])[1]+1]
    except ValueError:
        pass

for k, v in count_total_value.items():
    print(k+'\t'+str(v))