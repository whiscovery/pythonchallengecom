words = {}

with open('./hamlet.txt', "r", encoding="utf8") as f:
    for row in f:
        rows = row.split('\n')
        for blank in rows:
            blank = blank.split(' ')
            words[blank] = f.count(blank)

print(sorted(words.items(), key=lambda x: x[1], reverse=True))