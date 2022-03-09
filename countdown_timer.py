#import time library
import time

#define countdown function and passing a parameter
def countdown(t):
    while t:
        #setting time to seconds
        mins, secs = divmod(t, 60)
        #converting seconds to minutes:seconds
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        #countdown operation
        t -= 1
#output message when countdown is done
    print("Time Up!!")

#take number of seconds from user
t = input("Enter Time is seconds: ")

#call to the countdown function
countdown(int(t))