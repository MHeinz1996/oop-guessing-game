import random

# Define your GuessingGame class here...
class GuessingGame():
    def __init__(self, num) -> None:
      self.num = num
      self.correct = False

    def guess(self, guess):
      if(int(guess) > self.num):
        return f"High"
      elif(int(guess) < self.num):
        return f"Low"
      elif(int(guess) == self.num):
        self.correct = True

    def solved(self):
      return self.correct == True
        

# ----- DRIVER CODE -----
game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

while game.solved() == False:
  if last_guess != None: 
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = input("Enter your guess: ")
  last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")