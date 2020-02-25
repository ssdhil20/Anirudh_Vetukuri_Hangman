word = "Anir"
updatedSpaces = []
def checkLetter():
    letter = str(raw_input())
    global updatedSpaces
    list(word)
    lives = 5
    if letter in word:
        letterPlacement = word.index(letter) 
        updatedSpaces.replace([letterPlacement], letter)
        '''
        replace[letterPlacement].updatedSpaces(letter)
        '''
    else:
        '''
        lives = lives - 1
        if lives != 0:
            getLetter()
        else:    
            print("Sorry, game over")        
            '''
    print(updatedSpaces)
    print(word)