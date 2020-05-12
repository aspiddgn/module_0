# "Predict the Number" Game 0.01a
# Initial options
import numpy as np

highpassnumber = 100    # the maximum number to guess
guesstimes = 3  # Number to try prediction in one turn
tries = 0   # Initial number of tries
vector = 0  # Pointer for guessing
index = 0   # Pointer pin
numberlist = [x for x in range(1,101)]

def doprediction(rmin,rmax): # Will guess "guesstimes"
    trythree = []
    for i in range(0,guesstimes):
        print(i,np.random.randint(rmin, rmax+1))
        trythree.append(np.random.randint(rmin, rmax+1))
    return(False)

def askhelp():
    return


print("Hello, username! Let's play a Game! I'm The Predictor, the first and only!")
print("I can predict the number, that You guess... But I will ask You the clues! :)")
#number = input("Enter the Number from 1 to {} >>".format(highpassnumber))
number = 33

while doprediction(1,100) == False:
    print("test")
    if tries >= highpassnumber:
        break
else:
    print("Yes! {} is Your number!".format(index))
