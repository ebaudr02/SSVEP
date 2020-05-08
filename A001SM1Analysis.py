# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28

Exploration of data set recorded during SSVEP experience.
Input file: A001SM1_1

@author: Estelle Baudry
"""
import pandas as pd
import re
import matplotlib.pyplot as plt
from getIndexes import getIndexes
import seaborn as sn
import numpy as np
import os

#OPEN AND CLEAN DATA
df = pd.read_csv("A001SM1_1.csv")
df.shape
data = df.iloc[:,3:]

fileList = [f for f in os.listdir('.') if re.match('.*.csv',f)]
print(fileList)

# #PLOT DATA
# #graph of each channel, mHz per time
# for (colName, colData) in data.iteritems():
#     fig = plt.figure()
#     plt.plot(data.index/128, colData.values, label=colName)
#     plt.title(colName)
#     plt.xlabel('Time (s)')
#     plt.ylabel('mHz')
#     plt.legend()
    
# #graph of all channels to compare the time difference in response
# fig = plt.figure(figsize=(13,13))
# for (colName, colData) in data.iteritems():
#     if (bool(re.match('F',colName))):
#         plt.plot(data.index/128, colData.values, label=colName, linestyle='dashed')
#     else:
#         plt.plot(data.index/128, colData.values, label=colName)
# plt.title("All channels")
# plt.xlabel('Time (s)')
# plt.ylabel('mHz')
# plt.legend()

#EXTREME VALUES AND CENTRAL TENDENCY
#channel where max response is seen
listMax = data.max(0)
dataMax = listMax.max()
print('Channel for max voltage {}, {} Hz.'.format(listMax[listMax==dataMax].index.value, dataMax))

#time the max happens for each channel
channelTimeOfMax = getIndexes(data,listMax)
channelTimeOfMax.sort()
print('Channel time max : ', channelTimeOfMax)

# #Channels mean voltage distribution
# fig = plt.figure()
# plt.hist(data.mean(0))
# plt.title('Channels mean voltage distribution')
# plt.xlabel('mHz')


#MIN AND MAX CORRELATION
correlMatrix = data.corr().where(np.tril(np.ones(data.corr().shape),-1).astype(np.bool))
# sn.heatmap(correlMatrix)
# plt.show()
# print('Correlation matrix triled: \n', correlMatrix, "\n")

maxCorrelations =pd.DataFrame({'Max' : correlMatrix.max(0), 'Electrode1' : correlMatrix.idxmax(0)})
minCorrelations =pd.DataFrame({'Min' : correlMatrix.min(0), 'Electrode1' : correlMatrix.idxmin(0)})
maxCorrelations['Electrode2'] = maxCorrelations.index
minCorrelations['Electrode2'] = minCorrelations.index
# print('Correlation matrix max: \n', maxCorrelations, "\n")
# print('Correlation matrix min: \n', minCorrelations, "\n")

minCorrelation = minCorrelations['Min'].idxmin(skipna=True)
minCorrData = minCorrelations.loc[minCorrelation]
# minCorrData.name = filename
print("Min corr data : \n", minCorrData, "\n")

maxCorrelation = maxCorrelations['Max'].idxmax(skipna=True)
maxCorrData = maxCorrelations.loc[maxCorrelation]
print("Max corr data : \n", maxCorrData, "\n")