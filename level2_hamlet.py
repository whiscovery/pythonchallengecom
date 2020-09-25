words = {}

with open('./hamlet.txt', "r") as f:
    for line in f: # 라인으로 자르고
        for word in line.lower().strip().split(): # 라인을 소문자로 바꾸고, 양쪽 공백 제거하고, 빈칸으로 분리하면 다시 리스트가 되서 돌고
            if word in words: # 단어 모음에 있다면
                words[word] += 1 # 갯수 증가
            else:
                words[word] = 1 # 없다면 1

print(type(words))
words_list = sorted(words.items(), key=lambda x: x[1], reverse=True)
print(type(words_list))
print(words_list[:10]) # 상위 열개 출력