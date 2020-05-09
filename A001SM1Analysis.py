# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28

Exploration of data set recorded during SSVEP experience.

@author: Estelle Baudry
"""
import pandas as pd
import re
import matplotlib.pyplot as plt
from getIndexes import getIndexes
import seaborn as sn
import numpy as np
import os


def getMaxPeak(df):
    listMax = pd.DataFrame(df.max(0))
    listMax['Channel'] = listMax.index
    # print('Max peak and channel : \n', listMax[listMax[0]==listMax[0].max()].values.tolist(), '\n')
    return(listMax[listMax[0]==listMax[0].max()].values.tolist())

def getMinMaxCorrelation(df):
    correlMatrix = df.corr().where(np.tril(np.ones(df.corr().shape),-1).astype(np.bool))
    # sn.heatmap(correlMatrix)
    # plt.show()
    
    maxCorrelations =pd.DataFrame({'Max' : correlMatrix.max(0), 'Electrode1' : correlMatrix.idxmax(0)})
    minCorrelations =pd.DataFrame({'Min' : correlMatrix.min(0), 'Electrode1' : correlMatrix.idxmin(0)})
    maxCorrelations['Electrode2'] = maxCorrelations.index
    minCorrelations['Electrode2'] = minCorrelations.index
    # print('Correlation matrix max: \n', maxCorrelations, "\n")
    # print('Correlation matrix min: \n', minCorrelations, "\n")
    
    minCorrelation = minCorrelations['Min'].idxmin(skipna=True)
    minCorrData = minCorrelations.loc[minCorrelation]
    # print("Min corr data : \n", minCorrData, "\n")
    
    maxCorrelation = maxCorrelations['Max'].idxmax(skipna=True)
    maxCorrData = maxCorrelations.loc[maxCorrelation]
    # print("Max corr data : \n", maxCorrData, "\n")
    return(minCorrData, maxCorrData)




fileList = [f for f in os.listdir('.') if re.match('.*.csv',f)]
# print(fileList)

allMaxVoltages = []
allMinCorrelationData = pd.DataFrame()

for file in fileList:

    #OPEN AND CLEAN DATA
    data = pd.read_csv(file)
    data.shape
    # data = df.iloc[:,3:]
    
    #GET THE CHANNEL AND VALUE OF MAX VOLTAGE
    for item in getMaxPeak(data):
        item.append(file)
        allMaxVoltages.append(item)
        
        
    #PLOT GRAPH ALL CHANNELS/TIME
    fig = plt.figure(figsize=(13,13))
    for (colName, colData) in data.iteritems():
        if (bool(re.match('F',colName))):
            plt.plot(data.index/128, colData.values, label=colName, linestyle='dashed')
        else:
            plt.plot(data.index/128, colData.values, label=colName)
    plt.title("All channels - " + file)
    plt.xlabel('Time (s)')
    plt.ylabel('mHz')
    plt.legend()
    
    #ANALYSE MIN AND MAX CORRELATIONS
    minCorrData, maxCorrData  = getMinMaxCorrelation(data)
    allMinCorrelationData[file] = minCorrData
    allMaxCorrelationData[file] = maxCorrData

print('All max voltages : ', *allMaxVoltages, sep='\n')
print('All min correlation data : \n', allMinCorrelationData)
print('All max correlation data : \n', allMaxCorrelationData)

# #PLOT DATA
# #graph of each channel, mHz per time
# for (colName, colData) in data.iteritems():
#     fig = plt.figure()
#     plt.plot(data.index/128, colData.values, label=colName)
#     plt.title(colName)
#     plt.xlabel('Time (s)')
#     plt.ylabel('mHz')
#     plt.legend()
    






#time the max happens for each channel
# channelTimeOfMax = getIndexes(data,listMax)
# channelTimeOfMax.sort()
# print('Channel time max : ', channelTimeOfMax)

# #Channels mean voltage distribution
# fig = plt.figure()
# plt.hist(data.mean(0))
# plt.title('Channels mean voltage distribution')
# plt.xlabel('mHz')


