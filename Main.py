# Note that all single-line comments are referencing the line/lines directly above them, whereas block comments are
# referencing the function directly below them.
import random, time
# Imports the necessary modules into the code


'''
This function reads the title ASCII art from a text file, and prints it nicely, line by line.
'''


def asciiart():
    art = open('ascii.txt', 'r')
    # Opens the ASCII art file in read mode
    lines = art.readlines()
    # defines the contents of the file in a list
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
    # Nicely prints the list line by line


'''
The following function is the main body of my code, as it creates the tables based on the parameters that are imported.
An entirely random table is generated based on the parameters inputted in this function, with random words (selected
out of a specific word list that is specified in the parameters), and a random selection of letters from the alphabet.
'''


def createtable(listofnums, wordamount, letteramount, sidelength, difficulty):
    # Function is defined with the 5 Parameters needed
    easywords = []
    usedindexes = []
    wordchoices = []
    forbiddenyvalues = []
    # Empty lists are defined for later use
    for x in range(0, wordamount):
        # For loop that chooses the words to be used in the crossword table, parameter is amount of words
        words = open(difficulty, 'r')
        morewords = words.readlines()
        # opens the specified text document containing the needed words based on a parameter, and defines it as a list
        y = random.randint(0, 59)
        # Defines y as a random value that is equal to an index in the word document's list
        while y in forbiddenyvalues:
            y = random.randint(0, 59)
            # Makes sure that the selected y is not already used in a previous iteration of the loop, redefines it if it
            # is already used until it gets a y value that is not already used
        forbiddenyvalues.append(y)
        # appends the selected y value into the list of used y values, so that it will not get used again
        wordchoices.append(morewords[y].strip())
        # appends the word that corresponds to the selected y value into the wordchoices list.
    for x in range(0, letteramount):
        # for loop that picks random letters and appends them into the list that will be made into the table
        # runs for as many times as needed depending on how many letters are needed in the list (how large the table is)
        letter = open('alphabet.txt', 'r')
        letters = letter.readlines()
        # opens the text document containing the alphabet and defines it's lines as a list
        y = random.randint(0, 25)
        # picks a random index from 0 to 25 and defines it as y
        easywords.append(letters[y].strip())
        # appends the randomly selected letter into the list that will make up the table eventually
    words = 0
    # defines 'words' as zero to be used in the following for loop to append words into the list
    for x in range(0, wordamount):
        # for loop that adds chosen words into the list that this function is building
        y = int(random.choice(listofnums))
        # picks a y value to start the word at, and append the rest of the word on from that y value
        while y in usedindexes:
            y = int(random.choice(listofnums))
            # defensive while loop that makes sure the selected y value is not occupied by part of a word, and if it is,
            # redefines y until it gets an unused index
        chosenword = wordchoices[words]
        # defines chosenword as the first word in the list of chosen words from the text file
        isitbackwards = random.randint(0, 2)
        # random 1 in 3 chance that the word will get reversed
        words += 1
        # adds 1 to the 'words' variable so a different word will be targeted on the next iteration of this loop
        appendword = list(chosenword)
        # turns the chosen word into a list
        if isitbackwards == 2:
            appendword.reverse()
            # if the random 1 in 3 chance for making the word backwards is 2, reverses the list so that the word will
            # be appended into the main list backwards
        z = 0
        # defines z as zero so that the amount of times gone through the append loop can be tracked and changes.
        wordlen = len(appendword)
        # figures out how long the word is so it knows how many times to go though the following loop
        for r in range(0, wordlen):
            # loop that appends all the letters from the chosen word individually into the selected indexes of the list.
            easywords.insert(y + r, appendword[z])
            # inserts the targeted letter from the chosen word into the main list
            del easywords[y + r + 1]
            # deleted the randomly generated letter from the spot in the list that the letter from the chosen word is
            # now occupying
            usedindexes.append(y + r)
            # appends the used index into the usedindexes list
            z += 1
            # moves the targeted letter one further in the chosen word's list, so the next letter can be targeted in
            # the loop's next iteration
        for r in range(0, wordlen - 1):
            # for loop that appends all the indexes that the word's letters were inserted at into the usedindexes list
            y -= 1
            # changes the y value so as to target another index and be able to append it
            usedindexes.append(y)
    k = 0
    m = 0
    # defines the 'k' and 'm' variables to be used in the following loop
    for l in range(0, sidelength):
        # For loop that prints the rows of the table
        for r in range(0, sidelength):
            # for loop that prints the contents of the rows of the table
            print(easywords[k + m], end=" ")
            # prints the row contents without going down a line
            m += 1
        print("")
        # moves the printing cursor down a line to be used in the next printing of a row
        m = 0
        k += sidelength
    return wordchoices
    # returns wordchoices to wherever this function is called to the player can interact with the list of words that
    # will appear in the table.


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
    print('Words may appear reversed, and the length of words will vary\n')
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
