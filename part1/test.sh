#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /part1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/hdfstest2/shot_logs.csv /part1/input/
-file ../../bonus/part1/mapper1.py -mapper ../../bonus/part1/mapper1.py  \
-file ../../bonus/part1/reducer1.py -reducer ../../bonus/part1/reducer1.py \
-input /part1/input/* -output /part1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /part1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1/output/
../../stop.sh
