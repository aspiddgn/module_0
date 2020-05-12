# "Predict the Number" Game 0.01a
# Initial options
import numpy as np

highpassnumber = 100    # the maximum number to guess
guesstimes = 3  # Number to try prediction in one turn
tries = 0   # Initial number of tries
found = False   # Found flag
ranges = [1,highpassnumber]

def doprediction(rmin,rmax): # Will guess "guesstimes" times and guess the number in "rmin" and "rmax" range
    trythree = [x*0 for x in range(guesstimes)] #initialize the guesses list (fills with zeros)
    print("Reading Your mind...It seems to be..", end='')
    for i in range(0,guesstimes):
        trythree[i] = np.random.randint(rmin, rmax+1)   #get the random guess in defined range
        global tries
        tries += 1  #overal tries count
        if trythree[i] == number:   # checking the number is correct
            print(trythree[i],end=' ')
            found = True
            print("Yess!")
            return(found)
        else:
            print(trythree[i],end=' ')

    print("No.. ")
    return


print("Hello, username! Let's play a Game! I'm The Predictor, the first and only!")
print("I can predict the number, that You guess... But I will ask You the clues! :)")
number = int(input("Enter the Number from 1 to {} >>".format(highpassnumber)))
#number = 33

while found != True: # While we didn't find the number do guessing..

    if input("Is Your number equals or higher then {}? y/n:".format((ranges[0]+ranges[1])//2)) in 'yY':
        ranges[0] = (ranges[0]+ranges[1])//2    #set the ranges for guessing random numbers if the number is in upper part of the range
        found = doprediction(ranges[0],ranges[1])
    else:
        ranges[1] = (ranges[0]+ranges[1])//2    #set the ranges for guessing random numbers if the number is in lower part of the range
        found = doprediction(ranges[0], ranges[1])
    if found == True:
        print("Gotcha! {} is Your number! It was {}-th try.".format(number,tries))
        break
    if tries >= highpassnumber:     # emergency stop
        break


