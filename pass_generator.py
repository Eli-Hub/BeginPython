#import random library from python
import random


print('Welcome To Your Password Generator ')

#store all characters for password in a variable
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?0123456789'

#prompt user to input number passwords needed
number = input("Enter number of passwords to generate: ")

#convert the string input to an int
number=int(number)

#prompt user to enter length of the password
length = input("Enter password length: ")

#convert the string input to an int
length=int(length)

print('\n Here are your passwords: ')

#loop through the characters fro password
for pwd in range(number):
    passwords=''
    #loop and randomly pick characters to form password
    for c in range(length):
        passwords += random.choice(chars)

    #output results
    print(passwords)