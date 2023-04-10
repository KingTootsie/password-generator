import random

#Constitutes the sets of characters that will be combined together to be selected from.
lowers = 'abcdefghijklmnopqrstuvwxyz'
uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()-=[];:,.<>?' #Add more symbols if you'd like.

#Combines said sets together.
combination = lowers + uppers + numbers + symbols
combo_length = len(combination)

#Set the password length here.
length = 20

password = ""

#Combines randomly selected characters together to form a password.
for n in range(length):
    char = combination[random.randint(0, combo_length - 1)]

    password += char

#Prints the randomly generated password to terminal.
print(password) 
