# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 15:54:34 2015

@author: jpaukov
"""

import numpy as np
import scipy 
import scipy.stats
import pandas

turnData = pandas.read_csv('C:\Users\jpaukov\Documents\Udacity\CurrentPath\Turnstile_data_master_with_weather.csv')

    
rain = turnData[turnData.rain == 1]["ENTRIESn_hourly"]
noRain = turnData[turnData.rain == 0]["ENTRIESn_hourly"]
withRainMean = np.mean(rain)
withoutRainMean = np.mean(noRain)
regResults = scipy.stats.mannwhitneyu(rain, noRain)
U = regResults[0]
p = regResults[1]


print withRainMean, withoutRainMean, U, p

print p * 2
    
    