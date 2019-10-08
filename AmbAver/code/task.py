#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This script plays a 2 alt Force choice game for risk lotteries and Ambiguous Lotteries
#This cell imports out library and sets some global variables

from psychopy import visual, core, event, data, logging, gui
import sys
import os
import csv
import random
import numpy as np
import pandas as pd
#I want two different things to run for risk and Amb so we'll need 2 different data
#Risk should need Lottery_RL|Lottery %| Lottery $|Lottery_color| Sure $
# Ambiguity should need Amb_RL|Amb_type|Amb$|Risk%|Risk$
lot_color=['red','green','blue']
random.shuffle(lot_color)
Prizes=[8]
sure_prize=[5]
Lot_pers=np.array([0,10,20,30,40,50,60,70,80,90,100])
# Distribution of lotteries
wide_d=[0,0,0,0,1,1,1,1,2,2,8,8,9,9,9,9,10,10,10,10]
narrow_d=[3,3,4,4,4,4,5,5,5,5,5,5,5,5,6,6,6,6,7,7]
skew_d=[x+3 for x in narrow_d]
left=[0]*np.divide(len(wide_d),2)+[1]*np.divide(len(wide_d),2)


# In[2]:


#This cell sets up the risky lotteries
#left is shuffled each time so that there is a random order of left vs right and equal number for each color lot
# The data frames then get combined later
random.shuffle(left)
W_trials=pd.DataFrame({'LotisLeft':left,
                       'Lot_per':Lot_pers[wide_d],
                      'Lot_mon':Prizes[0],
                      'Lot_color':lot_color[0],
                      'Sure_mon':sure_prize[0]})
W_trials['dist']='wide'
random.shuffle(left)
N_trials=pd.DataFrame({'LotisLeft':left,
                       'Lot_per':Lot_pers[narrow_d],
                      'Lot_mon':Prizes[0],
                      'Lot_color':lot_color[1],
                      'Sure_mon':sure_prize[0]})
N_trials['dist']='Narrow'

random.shuffle(left)
S_trials=pd.DataFrame({'LotisLeft':left,
                       'Lot_per':Lot_pers[skew_d],
                      'Lot_mon':Prizes[0],
                      'Lot_color':lot_color[2],
                      'Sure_mon':sure_prize[0]})
S_trials['dist']='Skew'
random.shuffle(left)



# In[3]:


from sklearn.utils import shuffle
R_trials=pd.concat([N_trials,W_trials,S_trials])
R_trials=R_trials.sample(frac=1).reset_index(drop=True)
R_trials.head()

aa_data=[[l,r,m,c] for l in left for r in Lot_pers for m in [8] for c in lot_color]
A_trials=pd.DataFrame(data=aa_data,columns=['RiskisLeft','Risk_per','Money','Color'])
A_trials=A_trials.sample(frac=1).reset_index(drop=True)
A_trials.head()


# In[57]:


response_R_trials=pd.DataFrame(columns=['Keypress','RT'])
timer = core.Clock()
win=visual.Window(fullscr=False,
                  size=[5000,1000],
                  units="pix")


# In[ ]:


#Here we defined the risky choices
def risk_choice(lot_col,lot_m,lot_p,lot_left,sure_m):
    event.clearEvents()

    print([lot_left,lot_p,lot_m,lot_col,sure_m])
    if lot_col=='red':
        col_code=[1,0,0]
    elif lot_col=='green':
        col_code=[0,1,0]
    else:
        col_code=[0,0,1]
    
    if lot_left:
        lot_pos=-300
        sure_pos=(300,0)
    else:
        lot_pos=300
        sure_pos=(-300,0)
        
    tmp_div=np.divide(lot_p,100.00)
    shade=np.multiply(360.00,tmp_div)+1
    print shade
    
    Lot_a=visual.RadialStim(win=win,units="pix",name='Lot', color=col_code,opacity=1,
                          angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
                          ori= -90.0,pos=(lot_pos,0), size=(300,300),visibleWedge=(0.0, shade))
    
    rad2 = visual.RadialStim( win=win, name='rad2', color=col_code,opacity=0.3,
                                angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
                                ori= 45.0, pos=(lot_pos,0), size=(300,300))
    rad2.draw()
    Lot_a.draw()
    
    
    SureMoney=visual.TextStim(win=win,text="$ %s"%(sure_m),pos=sure_pos,bold=True)
    SureMoney.draw()
    
    Lot_per=visual.TextStim(win=win,text="%s %%"%(lot_p),pos=(lot_pos,-50),bold=True)
    Lot_Money=visual.TextStim(win=win,text="$ %s"%(lot_m),pos=(lot_pos,50),bold=True)
    Lot_per.draw()
    Lot_Money.draw()
    focus=visual.TextStim(win=win,text='+')
    
   
    focus.draw()
   
    win.flip()
    timer.reset()
    
    
    core.wait(1)
    keys=event.waitKeys(keyList=['f', 'j','escape'],maxWait=5)
    RT=timer.getTime()

        
    if not keys:
        keys='No_resp'
        RT=10

            
   
    wait_sec=10-RT
    focus.draw()
    win.flip()   
    core.wait(wait_sec)
    core.wait(0.5)
    return keys,RT


# In[ ]:


#Here we define the Ambiguous choices
def Amb_choice(lot_left,lot_p,money,lot_col):
    event.clearEvents()

    print([lot_left,lot_p,money,lot_col])
    if lot_col=='red':
        col_code=[1,0,0]
    elif lot_col=='green':
        col_code=[0,1,0]
    else:
        col_code=[0,0,1]
    
    if lot_left:
        lot_pos=-300
        sure_pos=300
    else:
        lot_pos=300
        sure_pos=-300
        
    tmp_div=np.divide(lot_p,100.00)
    shade=np.multiply(360.00,tmp_div)+1
    
    print shade
    
    Lot_a=visual.RadialStim(win=win,units="pix",name='Lot', color=col_code,opacity=1,
                          angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
                          ori= -90.0,pos=(lot_pos,0), size=(300,300),visibleWedge=(0.0,shade))
    rad2 = visual.RadialStim( win=win, name='rad2', color=col_code,opacity=0.3,
                                angularCycles = 0, radialCycles = 0, radialPhase = 0.5, colorSpace = 'rgb', 
                                ori= 45.0, pos=(lot_pos,0), size=(300,300))
    rad2.draw()
    Lot_a.draw()
    
    rad3 = visual.RadialStim( win=win, name='rad2', color=col_code,
                                angularCycles = 2, radialCycles = 2, radialPhase = 0.5, colorSpace = 'rgb', 
                                ori= 45.0, pos=(sure_pos,0), size=(300,300))
    rad3.draw()
    AmbMoney=visual.TextStim(win=win,text="$ %s"%(money),pos=(sure_pos,50),bold=True)
    AmbMoney.draw()
    AmbPer=visual.TextStim(win=win,text="???",pos=(sure_pos,-50),bold=True)
    AmbPer.draw()
    
    
    Lot_per=visual.TextStim(win=win,text="%s %%"%(lot_p),pos=(lot_pos,-50),bold=True)
    Lot_Money=visual.TextStim(win=win,text="$ %s"%(money),pos=(lot_pos,50),bold=True)
    Lot_per.draw()
    Lot_Money.draw()
    focus=visual.TextStim(win=win,text='+')
    
   
    focus.draw()
   
    win.flip()
    timer.reset()
    
    
    core.wait(0.5)
    keys=event.waitKeys(keyList=['f', 'j','escape'],maxWait=3)
    RT=timer.getTime()
    print(RT)
    
    if lot_col==lot_color[0]:
        dist='wide'
    elif lot_col==lot_color[1]:
        dist='narrow'
    elif lot_col==lot_color[2]:
        dist='skew'
        
        
    
    if not keys:
        keys='No_resp'
        RT=3
        
    wait_sec=10-RT
    focus.draw()
    win.flip()   
    core.wait(wait_sec)
    core.wait(0.5)
    return keys,RT,dist



# In[ ]:


#Here we define instructions
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
    win.flip
    


# In[ ]:


Stimdir="Stim/"

responses=[]
subjDlg = gui.Dlg(title="JOCN paper - rate items")
subjDlg.addField('Enter Subject ID: ')
subjDlg.show()
subj_id=subjDlg.data[0]

R_inst=["img1.png","img2.png","img3.png","img4.png","img5.png","img6.png",]
A_inst=["img7.png","img8.png","img9.png",]

if len(subj_id) < 1: # Make sure participant entered name
    core.quit()
# Lets participant quit at any time by pressing escape button
for page in R_inst:
    instruction(page)
#len(R_trials)
#for i in range(2):
for i in range(len(R_trials)):
    row=R_trials.iloc[i]
    print(row)
    resp,RT=risk_choice(row[0],row[1],row[2],row[3],row[4])
    responses.append(np.concatenate([row,[resp,RT]]))
    print resp,RT
    if 'escape' in resp:
        win.close()
        core.quit()
R_resp=pd.DataFrame(data=responses,columns=np.concatenate([R_trials.columns.to_list(),['response','RT']]))
R_resp.to_csv("../data/sub-%s_task-risk_events.csv"%(subj_id))
        
for page in A_inst:
    instruction(page)

responses=[]
#for i in range(2):
for i in range(len(A_trials)):
    row=A_trials.iloc[i]
    print(row)
    resp,RT,dist=Amb_choice(row[0],row[1],row[2],row[3])
    responses.append(np.concatenate([row,[resp,RT,dist]]))
    print resp,RT
    if 'escape' in resp:
        win.close()
        core.quit()
A_resp=pd.DataFrame(data=responses,columns=np.concatenate([A_trials.columns.to_list(),['response','RT','dist']]))
A_resp.to_csv("../data/sub-%s_task-ambiguity_events.csv"%(subj_id))

win.close()
core.quit()

