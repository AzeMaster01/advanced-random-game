import random               
def game():
   global user_choice                                                           #yourself working
   a = 999
   user_choice = input("Do you want to play yourself(Y) or AI(A) : ")
   def user():
         number = random.randint(1, a)
         print("You can abort program whenvere you want with typing '0'")
         count = 1
         guess = int(input('Guess the number from 1 to ' +str(a)+ ': '))
         while number != guess:
             print()
             if guess == 0:
                 count -= 1
                 confirmation = input("Are you sure? (y/n): ")
                 if confirmation == 'y':
                     print("You left the game!")
                     break
                 if confirmation == 'n':
                     print()
             if guess < number:
                 count += 1
                 print('Try again! You guessed too small')
                 print()
                 guess = int(input('Guess the number from 1 to ' +str(a)+ ': '))
             elif guess > number:
                 count += 1
                 print('Try again! You guessed too large')
                 print()
                 guess = int(input('Guess the number from 1 to ' +str(a)+ ': '))
             elif guess == number:
                 break
         else:
             print()  
             print('You found it! Answer was: ' +str(number))
             print('You did it in', count, 'tries')

   def AI():
         number = int(input('Choose a number from 1 to ' +str(a)+ ': '))
         count = 1
         low = 1
         high = 999
         computer = random.randint(1, a)
         print()
         while number != computer:
             print('Machine guessed', computer)
             print("You can abort program whenever you want with typing '0'")
             count += 1
             reply = str(input("If it is big type B/b, if it is small type S/s, if it is true type F/f :  "))
             if reply.lower() == "b":
                 if number < computer:
                     high = computer - 1
                     print('You guessed too large! Try again')
                     print()
                     computer = random.randint(low, high)
             if reply.lower() == "s":
                 if number > computer:        
                     low = computer + 1
                     print('You guessed too small! Try again')
                     print()
                     computer = random.randint(low, high)
             if reply == "0":
                 count -= 1
                 confirmation = input("Are you sure? (y/n): ")
                 if confirmation == "y":
                     print("You left the game!")
                     break
                 if confirmation == "n":
                     print()
             print()  
         while computer == number:
             print("Machine guessed", computer)
             reply = str(input("If it is big type B/b, if it is small type S/s, if it is true type F/f :  "))
             if reply.lower() == "f":
                 print("Machnie found it! Answer was", number)
                 break
           
   while True:
       if user_choice.lower() == "y":
             user()
             break
       elif user_choice.lower() == "a":
             AI()
             break
game()
while True:
    again = input("Do you want to play again? (Y/N): ")
    if again.lower() == "y":
        print("Let's start!")
        print()
        game()
    elif again.lower() == "n":
     print("Have a good day!")
     break