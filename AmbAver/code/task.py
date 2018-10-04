from psychopy import visual, core, event, gui, data, sound, logging
import sys
import os
import glob
import csv
import datetime
import random
import numpy as np
import pandas as pd


# Path to working directory
timer = core.Clock()
directory = os.getcwd()

# Timings
itiDuration = 1
decisionDuration = 3
postChoiceDuration = 1
tryFasterDuration = 1
thankYouScreenDuration = 1.5

# Trial data initlization
#Hard-Coded stuff
Machine_color=["slot_red.jpg","slot_green.jpg","slot_blue.jpg"]
Machine_color=random.sample(Machine_color,len(Machine_color))
Machine_color.append("Sure.jpg")
Machine_color=np.array(Machine_color)
moneyTypes=np.array([1.50,3.00,5.00])
percentageTypes=np.array([00,10,20,30,40,50,60,70,80,90,100])
wide_d=np.array([0,0,0,0,1,1,1,2,2,3,7,8,8,9,9,9,10,10,10,10])
narrow_d=np.array([2,3,3,4,4,4,5,5,5,5,5,5,5,5,6,6,6,7,7,8])
skew_d=np.array([4,5,5,6,6,6,7,7,7,7,7,7,7,7,8,8,8,9,9,10])
wide_m=np.array([0,1,2,1,0,1,2,0,2,1,2,1,0,0,1,2,0,1,2,1])
narrow_m=np.array([1,0,2,0,1,2,0,1,2,0,1,2,0,1,0,1,0,2,0,1])
skew_m=narrow_m
hand_index=np.random.permutation(20)

#make empty trial df
header_list=['leftMachineTypes','leftMachinePercentages','leftMachineMoneyAmounts','rightMachineTypes','rightMachinePercentages','rightMachineMoneyAmounts']
N_trials=pd.DataFrame(columns=header_list)
W_trials=pd.DataFrame(columns=header_list)
S_trials=pd.DataFrame(columns=header_list)
# Defining all of the narrow trials where risk is on the left
hand_index=np.random.permutation(len(narrow_d))
N_trials=pd.DataFrame({'leftMachineTypes':[Machine_color[0]]*10,
              'leftMachinePercentages':percentageTypes[narrow_d][hand_index[range(10)]],
              'leftMachineMoneyAmounts':moneyTypes[narrow_m][hand_index[range(10)]],
              'rightMachineTypes':[Machine_color[3]]*10,
              'rightMachinePercentages':[""]*10,
              'rightMachineMoneyAmounts':moneyTypes[[0]*10]})
#defines all of the narrow trials where risk is on the right
df2=pd.DataFrame({'rightMachineTypes':[Machine_color[0]]*10,
              'rightMachinePercentages':percentageTypes[narrow_d][hand_index[range(10,20)]],
              'rightMachineMoneyAmounts':moneyTypes[narrow_m][hand_index[range(10,20)]],
              'leftMachineTypes':[Machine_color[3]]*10,
              'leftMachinePercentages':[""]*10,
              'leftMachineMoneyAmounts':moneyTypes[[0]*10]})
#puts the two together and shuffle the order
N_trials=N_trials.append(df2,ignore_index=True)
#N_trials= N_trials.sample(frac=1).reset_index(drop=True)

# Defining all of the wide trials where risk is on the left
hand_index=np.random.permutation(len(narrow_d))
W_trials=pd.DataFrame({'leftMachineTypes':[Machine_color[1]]*10,
              'leftMachinePercentages':percentageTypes[wide_d][hand_index[range(10)]],
              'leftMachineMoneyAmounts':moneyTypes[wide_m][hand_index[range(10)]],
              'rightMachineTypes':[Machine_color[3]]*10,
              'rightMachinePercentages':[""]*10,
              'rightMachineMoneyAmounts':moneyTypes[[0]*10]})
#defines all of the wide trials where risk is on the right
df2=pd.DataFrame({'rightMachineTypes':[Machine_color[1]]*10,
              'rightMachinePercentages':percentageTypes[wide_d][hand_index[range(10,20)]],
              'rightMachineMoneyAmounts':moneyTypes[wide_m][hand_index[range(10,20)]],
              'leftMachineTypes':[Machine_color[3]]*10,
              'leftMachinePercentages':[""]*10,
              'leftMachineMoneyAmounts':moneyTypes[[0]*10]})
#puts the two together and shuffle the order
W_trials=W_trials.append(df2,ignore_index=True)
#W_trials= N_trials.sample(frac=1).reset_index(drop=True)

# Defining all of the Skewed trials where risk is on the left
hand_index=np.random.permutation(len(narrow_d))
S_trials=pd.DataFrame({'leftMachineTypes':[Machine_color[2]]*10,
              'leftMachinePercentages':percentageTypes[skew_d][hand_index[range(10)]],
              'leftMachineMoneyAmounts':moneyTypes[skew_m][hand_index[range(10)]],
              'rightMachineTypes':[Machine_color[3]]*10,
              'rightMachinePercentages':[""]*10,
              'rightMachineMoneyAmounts':moneyTypes[[0]*10]})
#defines all of the Skewed trials where risk is on the right
df2=pd.DataFrame({'rightMachineTypes':[Machine_color[2]]*10,
              'rightMachinePercentages':percentageTypes[skew_d][hand_index[range(10,20)]],
              'rightMachineMoneyAmounts':moneyTypes[skew_m][hand_index[range(10,20)]],
              'leftMachineTypes':[Machine_color[3]]*10,
              'leftMachinePercentages':[""]*10,
              'leftMachineMoneyAmounts':moneyTypes[[0]*10]})
#puts the two together and shuffle the order
S_trials=S_trials.append(df2,ignore_index=True)
#S_trials= N_trials.sample(frac=1).reset_index(drop=True)
T_trials=pd.concat([N_trials,W_trials,S_trials])
T_trials=df = T_trials.sample(frac=1).reset_index(drop=True)

#Define the RiskyChoice Trials
def riskychoice(left_image,right_image,left_money,right_money,left_percent,right_percent,duration):
    #Assign images to the correct objects.
    LeftImage.setImage("images/%s"%(left_image))
    RightImage.setImage("images/%s"%(right_image))
    # Draw the jpegs to the window's back buffer
    LeftImage.draw(window)untitled1
    RightImage.draw(window)
    #Flush the key buffer and mouse movements
    event.clearEvents()
    #Put the image on the screen
    window.flip()
    #Reset our clock to zero  - I think this call should take less time than window.flip, so resetting after the flip should be slightly more accurate.
    clock.reset()
    #Wait two seconds.  Tie up the CPU the entire time (this is more accurate than letting other processes go)
    core.wait(TrialDuration,TrialDuration)
    #Get a list of all keys that were pressed during our wait.  Tell it to give also give us the amount of time since our clock was reset when the key was pressed (reaction time).
    keypresses = event.getKeys(None,clock)
    return keypresses










