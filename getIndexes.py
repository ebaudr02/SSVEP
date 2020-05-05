#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 09:59:36 2020

@author: Estelle Baudry
"""
import pandas as pd
def getIndexes(df, value):
    ''' 
    Get index positions of value in a dataframe.
    
    Parameters
    ----------
    1. df (pandas Dataframe)
    2. value, can be either
        - single integer
        - single string
        - pandas Series such as:
            index: column in which to look for
            value: value to look for
        - list
    
    Returns
    ----------
    List of tuples indicating the positions of value in the dataframe : [(row,col)]
    
    '''
 
    IndList = list()
    
    if isinstance(value, pd.Series):
        for col, val in value.iteritems():
            rows = list(df[col][df[col] == val].index)
            for row in rows:
                IndList.append((row, col)) 
    
    elif isinstance(value, list):
        for val in value:
            for col in df.columns:
                rows = list(df[col][df[col] == val].index)
                for row in rows:
                    IndList.append((row, col))

    else:        
        for col in df.columns:
            rows = list(df[col][df[col] == value].index)
            for row in rows:
                IndList.append((row, col))


    return IndList
