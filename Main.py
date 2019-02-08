import random, time


def asciiart():
    art = open('ascii.txt', 'r')
    lines = art.readlines()
    print(lines[0].strip())
    print(lines[1].strip())
    time.sleep(0.5)
    print(lines[2].strip())
    print(lines[3].strip())
    time.sleep(0.5)
    print(lines[4].strip())
    print(lines[5].strip())
    time.sleep(0.5)
    print(lines[6].strip())
    print(lines[7].strip())
    time.sleep(0.5)
    print(lines[8].strip())


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


def numberlist(sidelength, positive, negative):
    listofnums = []
    y = 0
    for x in range(0, sidelength):
        for l in range(0, positive):
            listofnums.append(y)
            y += 1
        y += negative
    return listofnums


def guessing(wordchoices, wordamount):
    timesguessed = 0
    wordsguessed = 0
    wordchoices = list(wordchoices)
    while wordsguessed != wordamount:
        print('\nWhat is your word guess')
        guess = input('>>>')
        if guess in wordchoices:
            print('\nYou have guessed a word correctly!')
            wordsguessed += 1
            timesguessed += 1
            wordchoices.remove(guess)
            wordsleft = len(wordchoices)
            print(f'You have {wordsleft} words left to guess.\n')
        elif guess == 'quit':
            areyousure = input('\nAre you sure you want to quit? (y/n): ')
            if areyousure.lower == 'y':
                print('\nThanks for playing!\n')
                break
            else:
                continue
        else:
            print('\nThat was not a correct guess, try again!')
            timesguessed += 1
            print('times guessed:', timesguessed)
            continue


def hardness(type):
    if type == 'easy':
        listofnums = numberlist(7, 3, 4)
        wordamount = 5
        letteramount = 49
        sidelength = 7
        difficulty = 'easywords.txt'
        wordchoices = createtable(listofnums, wordamount, letteramount, sidelength, difficulty)
        return wordchoices
    elif type == 'medium':
        listofnums = numberlist(10, 5, 5)
        wordamount = 10
        letteramount = 100
        sidelength = 10
        difficulty = 'mediumwords.txt'
        wordchoices = createtable(listofnums, wordamount, letteramount, sidelength, difficulty)
        return wordchoices
    elif type == 'hard':
        listofnums = numberlist(15, 7, 8)
        wordamount = 15
        letteramount = 225
        sidelength = 15
        difficulty = 'hardwords.txt'
        wordchoices = createtable(listofnums, wordamount, letteramount, sidelength, difficulty)
        return wordchoices


def interfacing():
    print('welcome to...\n')
    time.sleep(0.5)
    asciiart()
    print('\nBy Liam Seagram\n\n')
    time.sleep(0.5)
    print('There are 3 difficulties to this minigame: Easy, Medium, and Hard.\n')
    time.sleep(0.5)
    print('In easy mode, you will be presented with a 7x7 of letters that includes 5 words, each with a max length of '
          '5 letters.\n')
    time.sleep(1)
    print('In medium mode, you will be presented with a 10x10 of letters that includes 10 words, each with a max'
          'length of 6 letters.\n')
    time.sleep(1)
    print('In hard mode, you will be presented with a 15x15 fo letters that includes 15 words, each with a max'
          'length of eight characters.\n')
    time.sleep(1)
    print('Words may appear reversed, and the length of words will vary.su\n')
    time.sleep(1)
    while True:
        print('\nWhat mode would you like to play? you may also quit the program at any time by inputting "quit".')
        response = input('(Easy, Medium, Hard, Quit): ')
        if response.lower() == 'easy':
            print('\n  Generating easy table... \n')
            time.sleep(0.5)
            wordchoices = hardness('easy')
            guessing(wordchoices, 5)
            print("\n Congratulations, you have completed an easy mode table!\n")
        elif response.lower() == 'medium':
            print('\n  Generating medium table... \n')
            time.sleep(0.5)
            wordchoices = hardness('medium')
            guessing(wordchoices, 10)
            print("\n Congratulations, you have completed a medium mode table!\n")
        elif response.lower() == 'hard':
            print('\n  Generating hard table... \n')
            time.sleep(0.5)
            wordchoices = hardness('hard')
            guessing(wordchoices, 15)
        elif response.lower() == 'quit':
            print('\nThanks for playing!\n')
            break
        else:
            print('That was not one of the options!\n')


interfacing()
