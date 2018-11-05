# Ambiguity through learned second order distributions
from psychopy import visual, core, event, gui, data, sound, logging
import sys
import os
import csv
import random
import numpy as np
import pandas as pd


Stimdir="Stim/"

# Path to working directory
timer = core.Clock()
directory = os.getcwd()

R_inst=["Instructions1.jpg","Instructions2.jpg","Instructions3.jpg","Instructions4.jpg","Instructions5.jpg","Instructions6.jpg",]
A_inst=["Instructions7.jpg","Instructions8.jpg","Instructions9.jpg",]

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
A_trials=pd.DataFrame(columns=header_list)
# Defining all of the narrow trials where risk is on the left
hand_index=np.random.permutation(len(narrow_d))
N_trials=pd.DataFrame({'leftMachineTypes':[Machine_color[0]]*10,
              'leftMachinePercentages':percentageTypes[narrow_d][hand_index[range(10)]],
              'leftMachineMoneyAmounts':moneyTypes[narrow_m][hand_index[range(10)]],
              'rightMachineTypes':[Machine_color[3]]*10,
              'rightMachinePercentages':["Safe"]*10,
              'rightMachineMoneyAmounts':moneyTypes[[0]*10]})
#defines all of the narrow trials where risk is on the right
df2=pd.DataFrame({'rightMachineTypes':[Machine_color[0]]*10,
              'rightMachinePercentages':percentageTypes[narrow_d][hand_index[range(10,20)]],
              'rightMachineMoneyAmounts':moneyTypes[narrow_m][hand_index[range(10,20)]],
              'leftMachineTypes':[Machine_color[3]]*10,
              'leftMachinePercentages':["Safe"]*10,
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
              'rightMachinePercentages':["Safe"]*10,
              'rightMachineMoneyAmounts':moneyTypes[[0]*10]})
#defines all of the wide trials where risk is on the right
df2=pd.DataFrame({'rightMachineTypes':[Machine_color[1]]*10,
              'rightMachinePercentages':percentageTypes[wide_d][hand_index[range(10,20)]],
              'rightMachineMoneyAmounts':moneyTypes[wide_m][hand_index[range(10,20)]],
              'leftMachineTypes':[Machine_color[3]]*10,
              'leftMachinePercentages':["Safe"]*10,
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
              'rightMachinePercentages':["Safe"]*10,
              'rightMachineMoneyAmounts':moneyTypes[[0]*10]})
#defines all of the Skewed trials where risk is on the right
df2=pd.DataFrame({'rightMachineTypes':[Machine_color[2]]*10,
              'rightMachinePercentages':percentageTypes[skew_d][hand_index[range(10,20)]],
              'rightMachineMoneyAmounts':moneyTypes[skew_m][hand_index[range(10,20)]],
              'leftMachineTypes':[Machine_color[3]]*10,
              'leftMachinePercentages':["Safe"]*10,
              'leftMachineMoneyAmounts':moneyTypes[[0]*10]})
#puts the two together and shuffle the order
S_trials=S_trials.append(df2,ignore_index=True)
#S_trials= N_trials.sample(frac=1).reset_index(drop=True)
R_trials=pd.concat([N_trials,W_trials,S_trials])
R_trials=R_trials.sample(frac=1).reset_index(drop=True)

np.random.shuffle(percentageTypes)
A_trials=pd.DataFrame({'leftMachineTypes':Machine_color[[0,1,2]*5],
              'leftMachinePercentages':percentageTypes[[0,0,0,1,1,1,2,2,2,3,3,3,4,4,4]],
              'leftMachineMoneyAmounts':moneyTypes[[1]*15],
              'rightMachineTypes':Machine_color[[0,1,2]*5],
              'rightMachinePercentages':["??"]*15,
              'rightMachineMoneyAmounts':moneyTypes[[1]*15]})
#defines all of the narrow trials where risk is on the right
df2=pd.DataFrame({'rightMachineTypes':Machine_color[[0,1,2]*6],
              'rightMachinePercentages':percentageTypes[[5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10]],
              'rightMachineMoneyAmounts':moneyTypes[[1]*18],
              'leftMachineTypes':Machine_color[[0,1,2]*6],
              'leftMachinePercentages':["??"]*18,
              'leftMachineMoneyAmounts':moneyTypes[[1]*18]
              })

#puts the two together and shuffle the order
A_trials=A_trials.append(df2,ignore_index=True)
A_trials=A_trials.sample(frac=1).reset_index(drop=True)

response_R_trials=pd.DataFrame(columns=['Keypress','RT'])
response_A_trials=pd.DataFrame(columns=['Keypress','RT'])

win=visual.Window(
        size=[1200,1800],
        units="pix",
        fullscr=False
        )
#define instructions set
def instruction(instructions):
    if any(instructions.endswith(x) for x in ('.jpg','.gif','.png','.bmp')):
        Inst_IMG=visual.ImageStim(win=win, image=Stimdir+instructions)
        Inst_IMG.draw()
        win.flip()
    else:
        Inst_text=visual.TextStim(win=win,text=instructions)
        Inst_text.draw()
        win.flip()
    event.waitKeys()

#Define the Choice Trials
def choice(left_image,right_image,left_money,right_money,left_percent,right_percent,duration):
    focus=visual.TextStim(win=win, text="+")
    #Assign images to the correct objects.
        # Draw the jpegs to the window's back buffer
    focus.draw()
    win.flip()
    if np.logical_or(isinstance(left_percent,int),left_percent=="??"):
        LeftPercentage=visual.TextStim(win=win,text="%s %%"%(left_percent),pos=(-200,300),color=[-1,-1,-1],bold=True)
        LeftImage=visual.ImageStim(image=Stimdir+left_image,win=win,pos=[-200,200])
        LeftMoney=visual.TextStim(win=win,text="$ %s"%(left_money),pos=(-200,00),bold=True)
        LeftImage.draw()
    else:
        LeftPercentage=visual.TextStim(win=win,text="%s"%(left_percent),pos=(-200,300),bold=True)
        LeftMoney=visual.TextStim(win=win,text="$ %s"%(left_money),pos=(-200,00),bold=True)
   
    if np.logical_or(isinstance(right_percent,int),right_percent=="??"):
        RightPercentage=visual.TextStim(win=win,text="%s %%"%(right_percent),pos=(200,300),color=[-1,-1,-1],bold=True)
        RightImage=visual.ImageStim(image=Stimdir+right_image,win=win,pos=[200,200])
        RightMoney=visual.TextStim(win=win,text="$ %s"%(right_money),pos=(200,00),bold=True)
        RightImage.draw()
    else:
        RightPercentage=visual.TextStim(win=win,text="%s" %(right_percent),pos=(200,300),bold=True)
        RightMoney=visual.TextStim(win=win,text="$ %s"%(right_money),pos=(200,00),bold=True)

    core.wait(np.round(random.uniform(1,3),decimals=2))

    LeftMoney.draw()
    RightMoney.draw()
    LeftPercentage.draw()
    RightPercentage.draw()
    win.flip()
    timer.reset()
    core.wait(6)
    #Flush the key buffer and mouse movements
    event.clearEvents()
    #Put the image on the screen
    win.flip()
    keypresses = event.getKeys()
    RT=timer.getTime()
    return keypresses,RT
    

# Get subjID
subjDlg = gui.Dlg(title="JOCN paper - rate items")
subjDlg.addField('Enter Subject ID: ')
subjDlg.show()
subj_id=subjDlg.data[0]

if len(subj_id) < 1: # Make sure participant entered name
    core.quit()
# Lets participant quit at any time by pressing escape button
if 'escape' in event.waitKeys():
    core.quit()

for page in R_inst:
    instruction(page)
for i in range(len(R_trials)):
    keypress,RT=choice(left_image=R_trials.leftMachineTypes[i],right_image=R_trials.rightMachineTypes[i],
       left_money=R_trials.leftMachineMoneyAmounts[i],right_money=R_trials.rightMachineMoneyAmounts[i],
       left_percent=R_trials.leftMachinePercentages[i],right_percent=R_trials.rightMachinePercentages[i],
       duration=6)
    response_R_trials=response_R_trials.append([keypress,RT],columns=['keypress','RT'])
    
for page in A_inst:
    instruction(page)
for i in range(len(A_trials)):
    keypress,RT=choice(left_image=A_trials.leftMachineTypes[i],right_image=A_trials.rightMachineTypes[i],
       left_money=A_trials.leftMachineMoneyAmounts[i],right_money=A_trials.rightMachineMoneyAmounts[i],
       left_percent=A_trials.leftMachinePercentages[i],right_percent=A_trials.rightMachinePercentages[i],
       duration=6)
    response_A_trials=response_A_trials.append([keypress,RT],columns=['keypress','RT'])

instruction("Thank you for playing and giving your best please go get an experimenter and finish the session")

win.close()
quit()