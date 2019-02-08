word2 = open('easywords.txt', 'r')
word3 = word2.readlines()
word4 = []
y = 0
for w in word3:
    word4.append(word3[y].strip())
    y += 1
print(word3)
print(word4)
