import random

def userGuess():
  blank = "-" * len(wordSecret)
  attemptsRemaining = 6
#print("Game Over! The mystery word was " + word + ". Maybe next time!")
 
  while attemptsRemaining > -1 and not blank == wordSecret:
    print(blank)
    #print (str(attemptsRemaining))
    print ("Attempts remaining: " + (str(attemptsRemaining)))
    guess = input("Please guess a letter:")
    
    if len(guess) != 1:
      print ("Please try again")
      
    elif guess in wordSecret:
      print ("Woohoo, that letter is in the sectret word")
      blank = blanksUpdate(wordSecret, blank, guess)
      
    else:
      print ("Please try again")
      attemptsRemaining -= 1
    
  if attemptsRemaining < 0:
    print ("Game over the word was: " + str(wordSecret))
  
  else:
    print ("Welldone, the word was: " + str(wordSecret))
    
def blanksUpdate(secret, currentArray, latestGuess):
  result = ""
  
  for i in range(len(secret)):
    if secret[i] == latestGuess:
      result = result + latestGuess  
      
    else:
      result = result + currentArray[i]
      
  return result
    
words = ["football", "swimming", "tennis", "soccer", "volleyball"]

wordSecret = random.choice(words)
userGuess()