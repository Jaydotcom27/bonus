#!/usr/bin/env python
# coding: utf-8
#!/usr/bin/python3

import sys
import re
import math

# Fucntions

def centroids_dict(centroids,k):
  centroids_dict = {}

  for i in range(0,k):
    centroids_dict[i+1] = centroids[i*3:(i+1)*3]
  return centroids_dict


def get_result_dict_mapper(k):
  mapper_result = {}

  for i in range(0,k):
    mapper_result[i+1] =[0,[0,0,0]]
  return mapper_result


def euclidean_distance(C1, C2):
  return math.sqrt(sum(pow(c1-c2,2) for c1, c2 in zip(C1[:], C2[:])))


def Euclidean_distance_centriods(data,centroids,k):
  centroids_distances = {}

  for i in range(0,k):
    centroids_distances[i+1] = euclidean_distance(data, centroids[i+1])
  return centroids_distances



centroids = sys.argv[1]
# Zones within 0.5 miles of LC 
k = eval(sys.argv[2])
lower_limit = 51; upper_limit = 71; precint18 = 18; precint20= 20; 
lincoln_regex = re.compile('w[5-7][0-9]') # Pattern for streets from 51 to 71

# Getting Centroid from bash file and spliting by "_"
centroids = [eval(dp) for dp in centroids.split('C')[1].strip('_').split('_')]

# Creating Dict for centroids values
centroids_values=centroids_dict(centroids,k)

# Creating empty dict to get mapper results
mapper_result = get_result_dict_mapper(k)




for line in sys.stdin:
  line = line.strip(',').split(',')
  line_len = len(line)
  if line_len == 43:
    try:
      st_1 = line[9]
      st_2 = line[10]
      st_3 = line[11]
      precint = eval(line[14].strip())
      street_name = line[24]
      street_name = re.sub('\W+','',street_name.strip()).lower()
      street_name = ''.join(street_name.split(' '))
      street_name = eval(''.join(lincoln_regex.findall(street_name))[1:])
      st_1 = float(st_1.strip())
      st_2 = float(st_2.strip())
      st_3 = float(st_3.strip())
      if (precint == precint18 or precint == precint20) and street_name >= lower_limit and street_name <= upper_limit: # removing streets not in 0.5 miles Radius
        data = [st_1, st_2, st_3]

        # Creating new centroids after calculating the euclidean distance
        data_centroids_distances = Euclidean_distance_centriods(data,centroids_values, k)  

        # Getting smallest distance to obtain new centroids
        min_distance_key = min(data_centroids_distances, key = data_centroids_distances.get) #argmin
        mapper_result[min_distance_key][0] += 1 
        # Sum of all street codes 1, 2 & 3
        mapper_result[min_distance_key][1][0] += data[0] # street_code_1
        mapper_result[min_distance_key][1][1] += data[1] # street_code_2
        mapper_result[min_distance_key][1][2] += data[2] # street_code_3
    except:
      continue

input_for_reducer = mapper_result
for key, values in input_for_reducer.items():
  print('{key}\t{values}'.format(key=key, values=values))