import random
from colorama import Fore, Style
try:
    x = int(input('enter the beggining of your range:'))
    y = int(input('enter the end of your range:'))
except:
    print(Fore.RED +'ValueError: only numbers allowed')
    print(Style.RESET_ALL)
    quit()
#_________________________________________________________

my_range = range(x, y)
if len(my_range) <= 20:
    Tries = round(len(my_range)/10*3)
elif len(my_range) > 20 and len(my_range) <= 100 :
    Tries = round(len(my_range)/10*1.5)
elif len(my_range) > 100 and len(my_range) <= 500 :
    Tries = round(len(my_range)/10*0.25)
else:
    Tries = round(len(my_range)/10*0.1)
guess_number = random.randint(x, y)
my_guess = 777777777777777
#__________________________________________________________

while guess_number != my_guess :
    if Tries == 0 :
        print('your tries are over')
        quit()
    print(f'{Fore.CYAN} you have {Tries} of tries left ')
    print(Style.RESET_ALL)
    try:
        my_guess = int(input(f'guess a number between {x} and {y} :'))
    except:
        print(Fore.RED +'ValueError: only numbers allowed')
        print(Style.RESET_ALL)

    if my_guess not in my_range: 
        print('you are out of your range')
        quit()
    elif my_guess < guess_number and Tries != 1 :
        print(Fore.LIGHTYELLOW_EX +'    Try again but HIGHER    ')
        print(Style.RESET_ALL)
    elif guess_number < my_guess and Tries != 1 :
        print(Fore.LIGHTYELLOW_EX +'    Try again but LOWER    ')
        print(Style.RESET_ALL)
    Tries -= 1
#_____________________________________________________________________
    
print(Fore.LIGHTGREEN_EX +'congartulatoins!! you guessed the correct number')
print(Style.RESET_ALL)
















