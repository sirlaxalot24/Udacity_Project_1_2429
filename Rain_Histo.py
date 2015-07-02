# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 12:51:56 2015

@author: jpaukov
"""

import numpy as np
import pandas
import matplotlib.pyplot as plt

turnData = pandas.read_csv('C:\Users\jpaukov\Documents\Udacity\Project1\Udacity_Project_1_2429\Turnstile_weather_v2.csv')

rain = turnData[turnData.rain == 1]["ENTRIESn_hourly"]
noRain = turnData[turnData.rain == 0]["ENTRIESn_hourly"]


noRain.plot(kind= 'hist', bins= 100)
rain.plot(kind= 'hist', bins= 100)
plt.xlabel("Entries Hourly")
plt.ylabel("# of Records")
plt.title("Rain vs. No Rain")
plt.axis([0, 6000, 0, 10000])

print plt
