# -*- coding: utf-8 -*-
"""
Created on Sat May 28 09:12:26 2016

@author: roosv_000
"""

from IO import Output
import pandas as pd
from evaluation import logloss
predsdf = pd.read_pickle(r'C:\Users\roosv_000\Desktop\pkl files\predictions_valset_HOG_8_16_1_linear_SVC.pkl')
#Write outputfile
check = predsdf
predsdf = check
Output.to_outputfile(check,1,'linearSVC_trainset_HOG_8_16_1',clean=False, validation=True )


[df_filenames, df_data]=logloss.load_data('..\Outputfiles_validationset\Old\outputfile_20160602_1_linearSVC_trainset_HOG_8_16_1.csv')
Score=logloss.compute_logloss(df_filenames,df_data)