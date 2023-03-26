#!/bin/sh
../../start.sh
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /part1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../mapreduce-test-data/hdfstest1/nyc_parking_violations_data.csv /part1/input/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../bonus/part1/mapper.py -mapper ../../bonus/part1/mapper.py  \
-file ../../bonus/part1/reducer.py -reducer ../../bonus/part1/reducer.py \
-input /part1/input/* -output /part1/output/
/usr/local/hadoop/bin/hdfs dfs -cat /part1/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part1/output/
../../stop.sh
