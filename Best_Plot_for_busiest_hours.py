# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 08:40:51 2015

@author: jpaukov
"""


import pandas
from ggplot import *



turnData = pandas.read_csv('C:\Users\jpaukov\Documents\Udacity\Project1\Udacity_Project_1_2429\Turnstiledatamasterwithweather.csv')

wkDay2 = turnData['DATEn'].str[8:]
wkDay2 = wkDay2.astype('float')
inHour = turnData['ENTRIESn_hourly']
wHour = turnData['Hour']

gg = ggplot(turnData, aes('wkDay2', 'wHour', size='inHour')) + geom_point(color= 'coral') \
+ labs(title="May Daily Ridership Per Hour") +\
 scale_y_continuous(name="Hour-24h", limits=(-1,24)) + scale_x_continuous(name="Day Of Month", limits=(0,31))


print gg



