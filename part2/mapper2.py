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

def euclidean_distance(C1, C2):
  return math.sqrt(sum(pow(c1-c2,2) for c1, c2 in zip(C1[:], C2[:])))

def Euclidean_distance_centriods(data,centroids,k):
  centroids_distances = {}

  for i in range(0,k):
    centroids_distances[i+1] = euclidean_distance(data, centroids[i+1])
  return centroids_distances

lower_limit = 51; upper_limit = 71; precint18 = 18; precint20= 20; 
lincoln_regex = re.compile('w[5-7][0-9]') 
assigned_time = '10A' 
violation_regex = re.compile('[A-Za-z0-9]*stand+[A-Za-z0-9]*|[A-Za-z0-9]*park+[A-Za-z0-9]*')

zones = sys.argv[1]
k = eval(sys.argv[2])
centroids = [eval(dp) for dp in zones.split('C')[1].strip('_').split('_')]

# Creating Dict for centroids values
centroids_values=centroids_dict(centroids,k)


for line in sys.stdin:
    line = line.strip(',').split(',')
    line_len = len(line)
    if line_len == 43:
        try:
            st_1 = line[9]
            st_2 = line[10]
            st_3 = line[11]
            precint = eval(line[14].strip())
            violation_time = line[19].strip()
            violation_time = violation_time[:2]+violation_time[-1]
            street_name = line[24]
            street_name = re.sub('\W+','',street_name.strip()).lower()
            street_name = ''.join(street_name.split(' '))
            street_name = eval(''.join(lincoln_regex.findall(street_name))[1:])
            st_1 = float(st_1.strip())
            st_2 = float(st_2.strip())
            st_3 = float(st_3.strip())

            # Narrow data within requested time, street & precint
            if violation_time == assigned_time and (precint == precint18 or precint == precint20) and street_name >= lower_limit and street_name <= upper_limit:
               
                data = [st_1, st_2, st_3]
                
                # Creating new centroids after calculating the euclidean distance
                data_centroids_distances = Euclidean_distance_centriods(data,centroids_values, k) 
                
    
                min_distance_key = min(data_centroids_distances, key = data_centroids_distances.get) #argmin
                details_of_violation = re.sub('\W+','',line[39]).lower()
                park_violation_regex = violation_regex.search(details_of_violation)
                violation_value = '1' if park_violation_regex else '0'

                print('{}\t{}'.format(min_distance_key, violation_value))

        except:
            continue