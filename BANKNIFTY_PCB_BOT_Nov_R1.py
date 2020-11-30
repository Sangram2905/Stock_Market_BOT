# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 10:36:10 2020

@author: Sangram Phadke
"""

# Perent Contribution

"""
Name Percent Contri to BN
0AXIS Bank Ltd	14.95
1Bandhan Bank Ltd	2.58
2Bank of Baroda Ltd	0.66
3Federal Bank Ltd.	1.33
4HDFC Bank Ltd	28.39
5ICICI Bank Ltd	19.48
6IDFC First Bank Ltd	0.85
7IndusInd Bank Ltd.	4.37
8Kotak Mahindra Bank Ltd.	16.31
9Punjab National Bank	0.46
10RBL Bank Ltd	1.06
11State Bank Of India	9.56
12 nifty bank

"""
#Importing the libraries
import numpy as np
import pandas as pd
import math
from datetime import datetime


Starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull start time
Pst = datetime.now().strftime("%H:%M")
Day = datetime.now().strftime("%A")
Daydate = datetime.now().strftime("%d")
pdate = datetime.now().strftime("%d-%m-%Y")
textdate = datetime.now().strftime("%d%m%Y")


## For Current values Importing the dataset from file NF_VIX_BN.csv from "in.investing.com"
## Manual process need to automated

#COLUMN_NAMES = ['Name', 'Symbol', 'Last', 'Open', 'High', 'Low', 'Chg.', 'Chg. %','Vol.', 'Time']
BN_file = 'BankNifty_Watchlist_'+textdate+'.csv'

cvdataset = pd.read_csv(BN_file) # CSV file
df_cvdataset1 = cvdataset.replace('\,','', regex=True)
df_cvdataset = df_cvdataset1.replace('\%','', regex=True)
df_cvdataset['Chg. %'].astype(float) # converting in to float
df_cvdataset['Chg.'].astype(float) # converting in to float

#Axis_value = float(df_cvdataset.iloc[0][2])+float(df_cvdataset.iloc[0][3])+float(df_cvdataset.iloc[0][4])+float(df_cvdataset.iloc[0][5])

def BNcurrentvalue(CurrentLOC):
    CurrentValue = (float(df_cvdataset.iloc[CurrentLOC][2])+float(df_cvdataset.iloc[CurrentLOC][3])+float(df_cvdataset.iloc[CurrentLOC][4])+float(df_cvdataset.iloc[CurrentLOC][5]))/4
    return CurrentValue

Axis_value = BNcurrentvalue(0)
Bandhan_value = BNcurrentvalue(1)
Baroda_value = BNcurrentvalue(2)
Federal_value = BNcurrentvalue(3)
HDFC_value = BNcurrentvalue(4)
ICICI_value = BNcurrentvalue(5)
IDFC_value = BNcurrentvalue(6)
IndusInd_value = BNcurrentvalue(7)
Kotak_value = BNcurrentvalue(8)
Punjab_value = BNcurrentvalue(9)
RBL_value = BNcurrentvalue(10)
SBI_value = BNcurrentvalue(11)

#BankNifty
Bnltpv = float(df_cvdataset.iloc[12][2])
Bnov = float(df_cvdataset.iloc[12][3])
Bnhv = float(df_cvdataset.iloc[12][4])
Bnlv = float(df_cvdataset.iloc[12][5])
bnvalue = (Bnltpv+Bnov+Bnhv+Bnlv)/4

stockPCtoBN = [14.95,2.58,0.66,1.33,28.39,19.48,0.85,4.37,16.31,0.46,1.06,9.56]
stockValues = [Axis_value,Bandhan_value,Baroda_value,Federal_value,HDFC_value,ICICI_value,IDFC_value,IndusInd_value,Kotak_value,Punjab_value,RBL_value,SBI_value]


## Need to add Bank nifty PCB as well

def pvaluesfun ():
    pvnList = []
    pvpList = []
    pvBNvalue = []
    for mulVal in range(12):
        pvalueby2d5 = float(df_cvdataset.iloc[mulVal][6])/2.5
        pvaluemul2d5 = float(df_cvdataset.iloc[mulVal][6])*2.5
        if  float(df_cvdataset.iloc[mulVal][7]) > 0:
            pvn = (stockValues[mulVal] - pvalueby2d5)*(stockPCtoBN[mulVal]/100)
            pvp = (stockValues[mulVal] + pvaluemul2d5)*(stockPCtoBN[mulVal]/100)
        elif float(df_cvdataset.iloc[mulVal][7]) < 0:
            pvn = (stockValues[mulVal] + pvalueby2d5)*(stockPCtoBN[mulVal]/100)
            pvp = (stockValues[mulVal] - pvaluemul2d5)*(stockPCtoBN[mulVal]/100)
        pvnList.append(pvn) 
        pvpList.append(pvp)
        
    pvnListm = bnvalue-(bnvalue*(((sum(pvnList)/1000))/100))
    pvpListm = bnvalue+(bnvalue*(((sum(pvpList)/1000))/100))
    pvBNvalue.append(pvnListm)
    pvBNvalue.append(pvpListm)
    return pvBNvalue


bn_pvalueList = pvaluesfun()

print("For Todays BankNifty Range at support {} and Resistance {}".format(format(bn_pvalueList[0],'.2f'),format(bn_pvalueList[1],'.2f')))
print(('BankNifty_PCB,{},{},{},{},{},{}'.format(pdate,format(bn_pvalueList[0],'.2f'),bnvalue,format(bn_pvalueList[1],'.2f'),0,0)),file=open("BN_Support_Resistance_data.csv", "a"))

## IDR program




