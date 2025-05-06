import random 

secret_number = random.randint(0,100)
attempts = 6 

print ("welcome to the number guessing game!")
print (f"you have {attempts} to guessing the correct number (0,100)")

won = 0
for i in range(1,attempts+1):
    guess = int (input(f"round({i}): guess a number:"))
    if(guess < secret_number ):
          print("your chosen number is lower.")
    elif(guess > secret_number):
          print("your chosen number is higher.")
    else:  
        print("you win")
        won = 1
        break
if won == 0:
  print("sorry you loss.")



print (secret_number)