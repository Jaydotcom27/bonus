#!/bin/sh
../../start.sh


/usr/local/hadoop/bin/hdfs dfs -rm -r /bonus/part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /bonus/part1/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /bonus/part1/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../mapreduce-test-data/hdfstest1/nyc_parking_violations_data.csv  /part1/input/


/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file mapper.py -mapper mapper.py \
-file reducer.py -reducer reducer.py \
-input /bonus/part1/input/* -output /bonus/part1/output/

echo "--------------------------- Question: What is the probability that it will get an ticket?? ---------------------------" 

/usr/local/hadoop/bin/hdfs dfs -cat /bonus/part1/output/part-00000

/usr/local/hadoop/bin/hdfs dfs -rm -r /bonus/part1/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /bonus/part1/output/
../../stop.sh

