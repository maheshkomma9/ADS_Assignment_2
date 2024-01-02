#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 22:29:50 2024

@author: maheshroyal
"""

#import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#defining the function 
def read_file(file_name):
    my_data_frame = pd.read_excel(file_name)
    my_data_frame.set_index('Indicator Name', inplace=True)
    
    req_data = my_data_frame.select_dtypes(include=['number'])
    print(req_data.describe())
    
    #plot the graph
    plt.figure(figsize=(12,8))
    sns.heatmap(req_data, annot = True, cmap = 'Pastel1',linewidths = 0.5)
    
    #labelling the plot
    plt.title('Canada')
    plt.show()
    
# declaring the file name
file_name = '/Users/maheshroyal/Downloads/Canada.xlsx'
print(read_file(file_name))



