file = "C:\\Users\mg\Desktop\Big Data\BDProjekt\\ratebeer2.json"

import re
import json
wszystkie_recenzje = []
stop_word = {"yet", "y", "without", "l", "flavor", "head", "aroma", "bottle", "nice", "beer", "pours", "body", "good", "oz", "like", "almost", "color", "finish", "ale", "one", "much", "thanks", "taste", "notes", "nose", "bit", "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"}


with open(file, 'r') as aa:
    for line in aa:
        #data = re.findall("text\":\"(.*?)\.\"\}", line)
        data = json.loads(line)
        if data["beerId"] == 51:
            #print(data["beerId"])
            #print(data["text"])
            word_only = re.findall("[a-zA-Z]+", data["text"])
            for poz in word_only:
                if poz.lower() not in stop_word:
                    wszystkie_recenzje.append(poz.lower())

aa.close()

#print(wszystkie_recenzje)
#print(len(wszystkie_recenzje))

#print(sorted(wszystkie_recenzje))

word_count = {}
last_word = None
sum = 1
i = 1
for word in sorted(wszystkie_recenzje):
    if word == last_word:
        sum += 1
    else:
        sum = 1
        last_word = word
        word_count[word] = 1
    word_count[word] = sum
word_count_sorted = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print(word_count_sorted)


print(len(word_count_sorted))
if len(word_count_sorted) < 30:
    print("----")
elif 30 <= len(word_count_sorted) < 200:
    print(word_count_sorted[0:3])
elif 200 <= len(word_count_sorted) < 700:
    print(word_count_sorted[0:8])
elif 700 <= len(word_count_sorted) < 1000:
    print(word_count_sorted[0:12])
else:
    print(word_count_sorted[0:15])