import random
number = random.randint(1,10)
# print number
#Works in Python2

player_name = input("Hello Winner! What's your first name?")
player_question = input ("Want to try my new game?")
#Works in Python3

number_of_guesses = 0

print('What up ' + player_name + ' Lets get started' + ' I am thinking of a number between 1 and 10:')
#while loop
while number_of_guesses < 5:
    #python's inbuilt method
    guess = int(input())
    #number of total guesses
    number_of_guesses += 1
    if guess < number:
        print('Try again you guessed too low'),
    if guess >number:
        print('Try again you guessed too high'),
    if guess == number:
        break

        #string
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))
