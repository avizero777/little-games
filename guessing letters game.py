import random
import string
from colorama import Fore, Style
guess_letter = (random.choice(string.ascii_letters)).lower()

list1 = ["a", "z", "e", "r", "t", "y", "u", "i", "o","p"]
list2 = ["q", "s", "d", "f", "g", "h", "j", "k", "l","m"]
list3 = ["w", "x", "c", "v", "b"]
 
my_tries = 5
my_guess = 0

print("french keyboard:")
print(f'the first row: {Fore.LIGHTBLUE_EX}{list1}')
print(Style.RESET_ALL)
print(f'the second row:{Fore.LIGHTBLUE_EX}{list2}')
print(Style.RESET_ALL)
print(f'the third row: {Fore.LIGHTBLUE_EX}{list3}')
print(Style.RESET_ALL)

while my_guess != guess_letter:
    if my_tries == 0:
        print(Fore.RED +'GAME OVER')
        print(Style.RESET_ALL)
        quit()
    my_guess = input('guess a letter:').lower().strip()
    if my_guess in list1 and guess_letter in list1 and my_guess != guess_letter:
        print(Fore.LIGHTYELLOW_EX +'you are in the correct row')
        print(Style.RESET_ALL)
    elif my_guess in list2 and guess_letter in list2 and my_guess != guess_letter:
        print(Fore.LIGHTYELLOW_EX +'you are in the correct row')
        print(Style.RESET_ALL)
    elif my_guess in list3 and guess_letter in list3 and my_guess != guess_letter:
        print(Fore.LIGHTYELLOW_EX +'you are in the correct row')
        print(Style.RESET_ALL)
    
    elif guess_letter in list2 and my_guess in list1:
        print(Fore.LIGHTYELLOW_EX +'DOWN')
        print(Style.RESET_ALL)
    elif guess_letter in list2 and my_guess in list3:
        print(Fore.LIGHTYELLOW_EX +'UP')
        print(Style.RESET_ALL)

    elif guess_letter in list1 and my_guess in list2:
        print(Fore.LIGHTYELLOW_EX +'UP')
        print(Style.RESET_ALL)
    elif guess_letter in list1 and my_guess in list3:
        print(Fore.LIGHTYELLOW_EX +'UP')
        print(Style.RESET_ALL)
        
    elif guess_letter in list3 and my_guess in list1:
        print(Fore.LIGHTYELLOW_EX +'DOWN')
        print(Style.RESET_ALL)
    elif guess_letter in list3 and my_guess in list2:
        print(Fore.LIGHTYELLOW_EX +'DOWN')
        print(Style.RESET_ALL)
    elif my_guess not in list1 and my_guess not in list2 and my_guess not in list3:
        print(Fore.RED +'only letters allowed')
        print(Style.RESET_ALL)
    my_tries -= 1


print(Fore.LIGHTGREEN_EX +'congartulation you guessed the correct letter')
print(Style.RESET_ALL)
