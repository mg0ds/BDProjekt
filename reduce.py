#!/usr/bin/env python

import sys

def reduce(lines):
    lastKey = None
    sum = 0
    for line in lines:
        for poz in line[2]:
            key, value = poz.split("\t")
            if key != lastKey and lastKey is not None:
               print("{0}\t{1}".format(lastKey, sum))
               sum = 0

            sum += int(value)
            lastKey = key

if __name__ == "__main__":
   reduce(sys.stdin)

#hadoop-streaming -input /user/hadoop -output /tmp/m -mapper ./map.py -reducer ./reduce.py -file ./reduce.py -file ./map.py