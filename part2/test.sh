#!/bin/sh
centroids=C_34790_10810_10910_34930_10910_11010_34970_11710_44990_35050_11710_44990_35090_14510_15710_35170_11710_44990
zones="0"
new_zones=""
k=6


for i in {0..10}; do
    if [[ $zones == $new_zones ]]; then
        break
    elif [[ $new_zones != "" ]]; then
        zones=$new_zones
    else
        zones=$centroids
    fi
    
    new_zones=`cat /Project1/data/parking_violations_2023.csv | python3 mapper1.py "$zones" "$k" | python3 reducer1.py`
	echo "Iterations Number: $i"
	echo "Centroids: $new_zones"
done

echo "Initiating Pipeline"

../../start.sh

/usr/local/hadoop/bin/hdfs dfs -rm -r /part2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part2/output/
/usr/local/hadoop/bin/hdfs dfs -mkdir -p /part2/input/
/usr/local/hadoop/bin/hdfs dfs -copyFromLocal ../../data/parking_violations_2023.csv /part2/input/
/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../bonus/part2/mapper2.py -mapper "../../bonus/part2/mapper2.py "$new_zones" "$k" "  \
-file ../../bonus/part2/reducer2.py -reducer ../../bonus/part2/reducer2.py \
-input /part2/input/* -output /part2/output/

/usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar \
-file ../../bonus/part2/mapper3.py -mapper ../../bonus/part2/mapper3.py \
-file ../../bonus/part2/reducer3.py -reducer ../../bonus/part2/reducer3.py \
-input /part2/output/* -output /part2-2/output/

/usr/local/hadoop/bin/hdfs dfs -cat /part2-2/output/part-00000
/usr/local/hadoop/bin/hdfs dfs -rm -r /part2/input/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part2/output/
/usr/local/hadoop/bin/hdfs dfs -rm -r /part2-2/output/
../../stop.sh
