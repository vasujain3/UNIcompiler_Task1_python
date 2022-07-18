import random

random_number = random.randint(1, 100)
userGuess = None
guesses = 0
score = 0

while(userGuess != random_number):
    print(f"----------------------------------------------------")     
    userGuess = int(input("Enter your guess:"))
    guesses += 1
    print(f'guesses left : {10-guesses}')
    if(userGuess == random_number):
       print("You guessed the right Number")
    elif(userGuess > random_number):
        print("Your guessed number is too high")
    else:
        print("Your guessed number is too low")
        
        
    if(random_number%2 == 0):
      print('Number you are guessing is divisible of 2 and it is even number')   
    elif(random_number%3==0):
        print('And Number you are guessing is divisible of 3 and it is odd number') 
    elif(random_number%5==0):
        print('And Number you are guessing is divisible of 5 ') 
    else:
        print("Number is prime")    
    
    print(f"----------------------------------------------------")
    print(f"------------------Code by Vasu Jain-----------------")     
        
print(f'You guessed no. in {guesses} guesses')
score = 10-guesses 
print(f'Your score is {score*10}%')