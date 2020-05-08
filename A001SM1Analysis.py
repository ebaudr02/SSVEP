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

#OPEN AND CLEAN DATA
df = pd.read_csv("A001SM1_1.csv")
df.shape
data = df.iloc[:,3:]

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
# print('Channel for maximum value: ', list(listMax[listMax==dataMax]This.index))


#time the max happens for each channel
channelTimeOfMax = getIndexes(data,listMax)
channelTimeOfMax.sort()

# #Channels mean voltage distribution
# fig = plt.figure()
# plt.hist(data.mean(0))
# plt.title('Channels mean voltage distribution')
# plt.xlabel('mHz')


#STATISTICAL ANALYSIS
correlMatrix = data.corr().where(np.tril(np.ones(data.corr().shape),-1).astype(np.bool))
sn.heatmap(correlMatrix)
plt.show()
print('Correlation matrix triled: \n', correlMatrix)

correlMatrixMax =pd.DataFrame({'Max' : correlMatrix.max(0), 'Index of max' : correlMatrix.idxmax(0)})
correlMatrixMin =pd.DataFrame({'Min' : correlMatrix.min(0), 'Index of min' : correlMatrix.idxmin(0)})
print('Correlation matrix min: \n', correlMatrixMin)
print('Correlation matrix max: \n', correlMatrixMax)
