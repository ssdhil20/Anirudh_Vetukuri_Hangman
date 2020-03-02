word = ("Anir")
wordList = list(word.lower())
updatedSpaces = []
wordLen = len(word)
lives = 5
letter = " "

for i in range (0, int(wordLen)):
    updatedSpaces.append("_")
    
def getLetter():
    global letter
    letter = raw_input ("Enter a letter guess    ")

def check():
    global updatedSpaces
    master
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
    
import random
WORDLIST = [""]
updatedWord = ""

def initialize():
    global updatedWord
    global SECRET
    WORDLIST = ['one','two','three','four','five','six','seven','eight','nine','ten']
    SECRET = random.choice(WORDLIST)
    updatedWord = [('_'*len(SECRET))]
   
    print(updatedWord)
    print SECRET

def getLetter():
    global letter
    letter = str(raw_input('ENTER YOUR GUESS: '))
    print ('YOUR GUESS: ' + letter)

def fillLetter():
    pos = SECRET.find(letter)
    updatedWord[pos] = letter
    
def ifWon():
    if updatedWord == SECRET:
        print ('You Won!')
    else: 
        getLetter()
        
def main():
    
    initialize()
    getLetter()
    
    
=======
    global lives
    global letter
    for x in range(0, int(wordLen)):
        if letter == wordList[x]:
            updatedSpaces[x] = wordList[x]
            print(updatedSpaces)
            print("You have:   ", lives, "   lives left!")
            checklist = "".join(updatedSpaces)
            master = "".join(wordList)
            if checklist == master:
                print("Congrats you solved the word!    ")
                #break
            else:
                getLetter()
        else:
            lives -= 1
            if lives != 0:
                print("You have:  " + str(lives) + "  lives left!")
                print(updatedSpaces)
                getLetter()
            else:
                print("Game Over   ")
                
def game():
    getLetter()
    check()
    
game()   
  master
