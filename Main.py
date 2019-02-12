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


'''
The following function makes the list of possible indexes that can be used when putting words into the list that
forms my word search table. 
'''


def numberlist(sidelength, positive, negative):
    # Function is defined with necessary parameters
    listofnums = []
    # empty listofnums is defined
    y = 0
    # y is defined as zero, to be changed with each loop through the function
    for x in range(0, sidelength):
        # uses the size of the table as the first range repeat
        for l in range(0, positive):
            # uses the second parameter, positive, as the second range repeat
            listofnums.append(y)
            # appends the y value to the listofnums
            y += 1
            # brings the y value up with each loop
        y += negative
        # skips the values that are not allowed to be inserted in the list, then runs through the loop again
    return listofnums
    # returns the completed listofnums


'''
The following function is the guessing function, and it is what allows the user to guess the values in the word search
and confirms or denies if their guess is true based on the functions parameters.
'''


def guessing(wordchoices, wordamount):
    # Function is defined with proper parameters
    timesguessed = 0
    wordsguessed = 0
    # needed variables are defined
    wordchoices = list(wordchoices)
    # wordchoices is redefined as a list
    while wordsguessed != wordamount:
        # while loop that all the guessing is contained inside
        print('\nWhat is your word guess')
        guess = input('>>>')
        # user guess is inputted
        if guess in wordchoices:
            print('\nYou have guessed a word correctly!')
            # if guess is correct, informs the user that they guessed correctly
            wordsguessed += 1
            timesguessed += 1
            # brings wordsguessed and timesguessed up by one for this iteration of the loop
            wordchoices.remove(guess)
            # removes the guessed word from the wordchoices list
            wordsleft = len(wordchoices)
            print(f'You have {wordsleft} words left to guess.\n')
            # finds the amount of words left and informs the user
        elif guess == 'quit':
            areyousure = input('Are you sure you want to quit? (y/n): ')
            # if the user inputs 'quit', asks them again if they are sure
            if areyousure.lower() == 'y':
                print('\nThanks for playing!\n')
                quit()
                # quits the code if they want to quit
            else:
                continue
                # continues the loop if they dont want to quit
        else:
            print('\nThat was not a correct guess, try again!')
            timesguessed += 1
            print('times guessed:', timesguessed)
            continue
            # if the user guesses wrong, informs them so and adds one to timesguessed.


'''
The following function calls the createtable function based on what difficulty the user has selected and inputs
the proper parameters to create the correct table
'''


def hardness(type):
    # defines the function with the parameter for the proper mode
    if type == 'easy':
        # if statement if the function is called with the type 'easy'
        listofnums = numberlist(7, 3, 4)
        # defines listofnums as the numberlist function with the correct parameters
        wordamount = 5
        letteramount = 49
        sidelength = 7
        difficulty = 'easywords.txt'
        # defines the proper parameters for the specified mode
        wordchoices = createtable(listofnums, wordamount, letteramount, sidelength, difficulty)
        # calls the createtable function with the proper parameters for the specified mode, and gets the returned
        # list of words to be returned
        return wordchoices
    elif type == 'medium':
        # elif statement if the function is called with the type 'medium'
        listofnums = numberlist(10, 5, 5)
        # defines listofnums as the numberlist function with the correct parameters
        wordamount = 10
        letteramount = 100
        sidelength = 10
        difficulty = 'mediumwords.txt'
        # defines the proper parameters for the specified mode
        wordchoices = createtable(listofnums, wordamount, letteramount, sidelength, difficulty)
        # calls the createtable function with the proper parameters for the specified mode, and gets the returned
        # list of words to be returned
        return wordchoices
    elif type == 'hard':
        # elif statement if the function is called with the type 'hard'
        listofnums = numberlist(15, 7, 8)
        # defines listofnums as the numberlist function with the correct parameters
        wordamount = 15
        letteramount = 225
        sidelength = 15
        difficulty = 'hardwords.txt'
        # defines the proper parameters for the specified mode
        wordchoices = createtable(listofnums, wordamount, letteramount, sidelength, difficulty)
        # calls the createtable function with the proper parameters for the specified mode, and gets the returned
        # list of words to be returned
        return wordchoices


'''
The following function is the main way that the user interacts with my program, and it is the only function that you
need to call in order to run the code. it informs the user all about the game, and calls all the proper functions
in the correct order for the game to run functionally.
'''


def interfacing():
    print('Welcome to...\n')
    time.sleep(0.5)
    asciiart()
    print('\nBy Liam Seagram\n\n')
    # prints the welcome screen with the ascii art function
    time.sleep(0.5)
    print('There are 3 difficulties to this minigame: Easy, Medium, and Hard.\n')
    time.sleep(0.5)
    print('In easy mode, you will be presented with a 7x7 of letters that includes 5 words, each with a max length of '
          '5 letters.\n')
    time.sleep(1)
    print('In medium mode, you will be presented with a 10x10 of letters that includes 10 words, each with a max '
          'length of 6 letters.\n')
    time.sleep(1)
    print('In hard mode, you will be presented with a 15x15 fo letters that includes 15 words, each with a max '
          'length of eight characters.\n')
    time.sleep(1)
    print('Words may appear reversed, and the length of words will vary.\n')
    time.sleep(1)
    # Informs the user about the game's modes, and how it works
    while True:
        # infinite while loop that can be broken with 'break'
        print('\nWhat mode would you like to play? you may also quit the program at any time by inputting "quit".')
        response = input('(Easy, Medium, Hard, Quit): ')
        # gets the users's input on what mode they desire to play, they may also input 'quit'
        if response.lower() == 'easy':
            # if statement if the user inputs 'easy'
            print('\n  Generating easy table... \n')
            time.sleep(0.5)
            # informs the user that an easy table is being generated
            wordchoices = hardness('easy')
            # generates the table with the appropriate function call
            guessing(wordchoices, 5)
            # runs the guessing module with the proper parameters so the user can play the created word search
            print("\n Congratulations, you have completed an easy mode table!\n")
            # once the module has completed its course, informs the user that they have completed the word search
        elif response.lower() == 'medium':
            # elif statement if the user inputs 'medium'
            print('\n  Generating medium table... \n')
            time.sleep(0.5)
            # informs the user that a medium table is being generated
            wordchoices = hardness('medium')
            # generates the table with the appropriate function call
            guessing(wordchoices, 10)
            # runs the guessing module with the proper parameters so the user can play the created word search
            print("\n Congratulations, you have completed a medium mode table!\n")
            # once the module has completed its course, informs the user that they have completed the word search
        elif response.lower() == 'hard':
            # elif statement if the user inputs 'hard'
            print('\n  Generating hard table... \n')
            time.sleep(0.5)
            # informs the user that a hard table is being generated
            wordchoices = hardness('hard')
            # generates the table with the appropriate function call
            guessing(wordchoices, 15)
            # runs the guessing module with the proper parameters so the user can play the created word search
            print("\n Congratulations, you have completed a hard mode table!\n")
        elif response.lower() == 'quit':
            # elif statement for if the user inputs 'quit'
            print('\nThanks for playing!\n')
            break
            # breaks the infinite loop
        else:
            print('That was not one of the options!\n')
            # defensive programming for if the user inputs something that was not one of the options


interfacing()
# calls the interfacing function
