
##############################
#                            #
# Created by: Daniel Aguirre #
# Date: 2019/05/07           #
#                            #
##############################

# Imports
import numpy as np
import matplotlib.pyplot as plt
import time

# USER´S VARIABLES
folds = 16

# Program variables
## Directions: right=0, up=1, left=2, down=3
a = [0]
a_n = [a]

# Fold/Unfold the dragon curve for a given number of iterations(folds)
def iterate(folds):
    for i in range(folds):  
        print("Fold number: " + str(i))  
        a_i = a_n[-1]            
        inv = a_i[::-1] # Calculate array inverse
        for j in range(len(inv)):      
            inv[j] = inv[j] + 1 # Sum +1 to "turn" the direction 90 degrees
            if (inv[j] >3):
                inv[j] = 0    
        a_i = a_i + inv    
        a_n.append(a_i)


    
#Prepare data to be plotted
def plotCurve():
    a_i = a_n[-1]

    x = np.array([0],dtype=int)
    y = np.array([0],dtype=int)

    for i in range(len(a_i)):
        val = a_i[i]
        if (val == 0): #Moves RIGHT
            new_xpos = x[-1] + 1
            new_ypos = y[-1]
            x = np.append(x, new_xpos)
            y = np.append(y, new_ypos)

        elif (val == 1): #Moves UP
            new_xpos = x[-1] 
            new_ypos = y[-1] + 1
            x = np.append(x, new_xpos)
            y = np.append(y, new_ypos)
            
        elif (val == 2): #Moves LEFT
            new_xpos = x[-1] - 1 
            new_ypos = y[-1]
            x = np.append(x, new_xpos)
            y = np.append(y, new_ypos)
        
        elif (val == 3): #Moves DOWN
            new_xpos = x[-1] 
            new_ypos = y[-1] - 1
            x = np.append(x, new_xpos)
            y = np.append(y, new_ypos)
        else:        
            print("There are some values wrong in the matrix!")

    fig = plt.figure()
    ax = plt.axes()
    ax.set_title('Folds: ' + str(folds))
    ax.set_axis_off()
    lines, = ax.plot(x,y)
    plt.show()

# Main program´s logic
def main():
    start = time.time()
    print("Started")
    iterate(folds)
    end = time.time()
    print("Elapsed time: " + str(end - start))
    plotCurve()
    print("Finished")

# EXECUTE program
main()






    
