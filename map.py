#!/usr/bin/env python
import sys
import json
#from langdetect import detect

def map(lines):
    for line in lines:
        data = json.loads(line)
        recenzja = data["text"]
        #lang = detect(recenzja)
        lang = "en"

        words = recenzja.split(" ")
        aaa = [data["beerId"], lang, []]
        for word in words:
            if len(word) > 3:
                aaa[2].append("{0}\t{1}".format(word.strip(), 1))

if __name__ == "__main__":
    map(sys.stdin)


