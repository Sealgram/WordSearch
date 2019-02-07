import random


def createtable(listofnums, wordamount, letteramount, sidelength, difficulty):
    easywords = []
    usedindexes = []
    wordchoices = []
    forbiddenyvalues = []
    for x in range(0, wordamount):
        words = open(difficulty, 'r')
        morewords = words.readlines()
        y = random.randint(0, 59)
        while y in forbiddenyvalues:
            y = random.randint(0, 59)
        forbiddenyvalues.append(y)
        wordchoices.append(morewords[y].strip())
    for x in range(0, letteramount):
        letter = open('alphabet.txt', 'r')
        letters = letter.readlines()
        y = random.randint(0, 25)
        easywords.append(letters[y].strip())
    words = 0
    for x in range(0, wordamount):
        y = int(random.choice(listofnums))
        while y in usedindexes:
            y = int(random.choice(listofnums))
        chosenword = wordchoices[words]
        isitbackwards = random.randint(0, 2)
        words += 1
        appendword = list(chosenword)
        if isitbackwards == 2:
            appendword.reverse()
        z = 0
        wordlen = len(appendword)
        for r in range(0, wordlen):
            easywords.insert(y + r, appendword[z])
            del easywords[y + r + 1]
            usedindexes.append(y + r)
            z += 1
        for r in range(0, wordlen - 1):
            y -= 1
            usedindexes.append(y)
    k = 0
    m = 0
    for l in range(0, sidelength):
        for r in range(0, sidelength):
            print(easywords[k + m], end=" ")
            m += 1
        print("")
        m = 0
        k += sidelength
    return wordchoices


def hardness(type):
    if type == 'easy':
        listofnums = [0, 1, 2, 7, 8, 9, 14, 15, 16, 21, 22, 23, 28, 29, 30, 35, 36, 37, 42, 43, 44]
        wordamount = 5
        letteramount = 49
        sidelength = 7
        difficulty = 'easywords.txt'
        wordchoices = createtable(listofnums, wordamount, letteramount, sidelength, difficulty)
        return wordchoices
    elif type == 'medium':
        listofnums = []
        y = 0
        for x in range(0, 9):
            for l in range(0, 3):
                    listofnums.append(y)
                    y += 1
            y += 6
        print(listofnums)
        wordamount = 9
        letteramount = 81
        sidelength = 9
        difficulty = 'mediumwords.txt'
        wordchoices = createtable(listofnums, wordamount, letteramount, sidelength, difficulty)
        return wordchoices
    elif type == 'hard':
        print("hard")


print(hardness('medium'))
