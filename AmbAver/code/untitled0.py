#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 10:01:41 2018

@author: strange_lorenz
"""

from psychopy import visual, core, event, gui, data, sound, logging
import sys
import os
import glob
import csv
import datetime
import random
import numpy as np
import pandas as pd

Stimdir="Stim"

# Path to working directory
timer = core.Clock()
directory = os.getcwd()

R_inst=["instructions1.jpg","instructions2.jpg","instructions3.jpg","instructions4.jpg","instructions5.jpg","instructions6.jpg",]
A_inst=["instructions7.jpg","instructions8.jpg","instructions9.jpg",]

# Trial data initlization
#Hard-Coded stuff
Machine_color=["slot_red.jpg","slot_green.jpg","slot_blue.jpg"]
Machine_color=random.sample(Machine_color,len(Machine_color))
Machine_color.append("Sure.jpg")
Machine_color=np.array(Machine_color)
moneyTypes=np.array([1.50,3.00,5.00])
percentageTypes=np.array([00,10,20,30,40,50,60,70,80,90,100,"??"])
wide_d=np.array([0,0,0,0,1,1,1,2,2,3,7,8,8,9,9,9,10,10,10,10])
narrow_d=np.array([2,3,3,4,4,4,5,5,5,5,5,5,5,5,6,6,6,7,7,8])
skew_d=np.array([4,5,5,6,6,6,7,7,7,7,7,7,7,7,8,8,8,9,9,10])
wide_m=np.array([0,1,2,1,0,1,2,0,2,1,2,1,0,0,1,2,0,1,2,1])
narrow_m=np.array([1,0,2,0,1,2,0,1,2,0,1,2,0,1,0,1,0,2,0,1])
skew_m=narrow_m


#make empty trial df
header_list=['leftMachineTypes','leftMachinePercentages','leftMachineMoneyAmounts','rightMachineTypes','rightMachinePercentages','rightMachineMoneyAmounts']

A_trials=pd.DataFrame(columns=header_list)
#

#hand_index=np.random.permutation(len(percentageTypes)-1)
#A_trials=pd.DataFrame({'leftMachineTypes':Machine_color[0,1,2]*5,
 #             'leftMachinePercentages':percentageTypes[hand_index[range(5)]],
  #            'leftMachineMoneyAmounts':moneyTypes[[1]*10],
   #           'rightMachineTypes':Machine_color[0,1,2]*5,
    #          'rightMachinePercentages':["??"]*15,
     #         'rightMachineMoneyAmounts':moneyTypes[[1]*10]})
#defines all of the narrow trials where risk is on the right
#df2=pd.DataFrame({'rightMachineTypes':Machine_color[0,1,2]*5,
 #             'rightMachinePercentages':percentageTypes[hand_index[range(5,11)]],
  #            'rightMachineMoneyAmounts':moneyTypes[[1]*10],
   #           'leftMachineTypes':Machine_color[0,1,2]*5,
    #          'leftMachinePercentages':["??"]*10,
     #         'leftMachineMoneyAmounts':moneyTypes[[1]*10]
      #        })
print(Machine_color[[0,1,2,0,1,2]])
print([Machine_color[[0,1,2]*2]])
print(len(percentageTypes))