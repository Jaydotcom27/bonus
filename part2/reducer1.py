#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys

result_value = {}

for line in sys.stdin:
    k, v = line.split('\t')
    v = eval(v)
    result_value[int(k)] = [v[1][0]/v[0], v[1][1]/v[0], v[1][2]/v[0]]

result_string = ''
for k, vals in result_value.items():
  for v in vals:
    result_string = result_string + '_' +str(v)
result_string = 'C' + result_string[1:]
print(result_string)