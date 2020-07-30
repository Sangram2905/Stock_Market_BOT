# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:34:18 2020

@author: Sangram Phadke
"""

# Importing the libraries
import numpy as np
import pandas as pd
import math
from datetime import datetime
from nsetools import Nse
   
# Importing the NIFTY dataset from NSE live site / portel 

nse = Nse()  # NSE object creation
print('AI Result Start Time')
print('Main Program')
print('',file=open("NSEmarket.txt", "a"))
print('')

# Capital letter words / variable which are not appre in data variable box to reduce the display data frames and clean program view

Nf_n50 = nse.get_index_quote("nifty 50") 

N50 = Nf_n50['lastPrice']
#N50 = 11000 # Sample test data
N50p = int(50 * round(float(N50)/50))
n50f = format(N50p,'.2f')

BN_bank = nse.get_index_quote("nifty bank") 
#BN = 22000 # Sample test data
BN = BN_bank['lastPrice']
BNp = int(50 * round(float(BN)/50))
bnf = format(BNp,'.2f')


# Importing the Option dataset from Files stored in same folder
## Run the specific files on 9:45  12 and 1:30 each day and save on exit 

COLUMN_NAMES=['CallOI','CallLTP','CallNetChange','Strike Price','PutNetChange','PutLTP','PutOI']


# Option data


############################################### Bank Nifty ####################################
##Data Slicing for BankNifty

Dr_banknifty = pd.read_excel ('BankNifty-Option-Chain-Automated-Data-Extractor.xlsm' , sheet_name='Option Chain')

Dr_banknifty1 = Dr_banknifty.iloc[6:,[1,5,6,11,16,17,21]]

Dr_banknifty1.columns = COLUMN_NAMES

Dr_banknifty2 = Dr_banknifty1.dropna()

df_banknifty = Dr_banknifty2.replace(to_replace = ['- ','-'], value =0)

## Collect Higest and 2nd highest Open intrest from call and Put side

"""
## Exact value functions
# BNCH1OI = df_banknifty['CallOI'].max() # Returns a max value
# BNCH1OI_loc = df_banknifty['CallOI'].idxmax() # Returns a index location max value
"""
# Call values

BNCH1OI,BNCH2OI = df_banknifty['CallOI'].nlargest(2,keep='last')  # Returns a max and 2nd max values

BNCH1OI_loc,BNCH2OI_loc = df_banknifty['CallOI'].nlargest(2,keep='last').index # Returns location of a max and 2nd max values


# Put values

BNPH1OI,BNPH2OI = df_banknifty['PutOI'].nlargest(2,keep='last')  # Returns a max and 2nd max values

BNPH1OI_loc,BNPH2OI_loc = df_banknifty['PutOI'].nlargest(2,keep='last').index # Returns location of a max and 2nd max values


## Calculate the range which is same as Higest and 2nd highest Open intrest from call and Put side
# Call
BNCH1OI_SP = df_banknifty.iloc[BNCH1OI_loc]['Strike Price'] # Returns a Strick price 
BNCH2OI_SP = df_banknifty.iloc[BNCH2OI_loc]['Strike Price'] # Returns a Strick price 

# Put
BNPH1OI_SP = df_banknifty.iloc[BNPH1OI_loc]['Strike Price'] # Returns a Strick price 
BNPH2OI_SP = df_banknifty.iloc[BNPH2OI_loc]['Strike Price'] # Returns a Strick price 

## Calculate the High Put Call ratio (PCR)

BNHPCR = BNPH1OI/BNCH1OI
bnhpcr = format(BNHPCR,'.2f')


print('BankNifty Higest Open Intrest PCR ratio ',bnhpcr,file=open("NSEmarket.txt", "a"))
print('')
print('',file=open("NSEmarket.txt", "a"))

## Calculate the total Put Call ratio

BNCallOI_sum = df_banknifty['CallOI'].sum()  # Returns a sum of Call Open intrest values

BNPutOI_sum = df_banknifty['PutOI'].sum()  # Returns a sum of  Put Open intrest values

BNTPCR = BNPutOI_sum / BNCallOI_sum

bntpcr = format(BNTPCR,'.2f')


print('BankNifty Total Open Intrest PCR ratio ',bntpcr,file=open("NSEmarket.txt", "a"))
print('')
print('',file=open("NSEmarket.txt", "a"))

# PUT call Ratio  PCR
# avrage is 0.7

# A rising put-call ratio, or a ratio greater than .7 or exceeding 1, means that equity traders are buying more puts than calls. It suggests that bearish sentiment is building in the market. Investors are either speculating that the market will move lower or are hedging their portfolios in case there is a sell-off.
if  BNTPCR > 0.7:
    print('It suggests that bearish sentiment is building in the market.',file=open("NSEmarket.txt", "a"))
    if  BNTPCR > 1.5:
        print("Over purchased Put Options",file=open("NSEmarket.txt", "a"))



# A falling put-call ratio, or below .7 and approaching .5, is considered a bullish indicator. It means more calls are being bought versus puts.

if  BNTPCR < 0.9:
    print("This considered a bullish indicator.",file=open("NSEmarket.txt", "a"))
    if  BNTPCR < 0.6:
        print("Over purchased Call Options",file=open("NSEmarket.txt", "a"))


print('',file=open("NSEmarket.txt", "a"))


## Main Logic Bank Nifty

print('OI Resistance 2 ',BNCH1OI_SP,file=open("NSEmarket.txt", "a"))

print('OI Resistance 1 ',BNCH2OI_SP,file=open("NSEmarket.txt", "a"))

print('BankNifty SP    ',bnf,file=open("NSEmarket.txt", "a"))

print('OI Support 1    ',BNPH1OI_SP,file=open("NSEmarket.txt", "a"))

print('OI Support 2    ',BNPH2OI_SP,file=open("NSEmarket.txt", "a"))



print('')


print('',file=open("NSEmarket.txt", "a"))

###################################### NIFTY 50 ###########################################

##Data Slicing for Nifty 50
Dr_nifty50 = pd.read_excel ('Nifty-Option-Chain-Automated-Data-Extractor.xlsm' , sheet_name='Option Chain')

Dr_nifty501 = Dr_nifty50.iloc[6:,[1,5,6,11,16,17,21]]

Dr_nifty501.columns = COLUMN_NAMES

Dr_nifty502 = Dr_nifty501.dropna()

df_nifty50 = Dr_nifty502.replace(to_replace = ['- ','-'], value =0)


## Collect Higest and 2nd highest Open intrest from call and Put side
# Call values

NFCH1OI,NFCH2OI = df_nifty50['CallOI'].nlargest(2,keep='last')  # Returns a max and 2nd max values

NFCH1OI_loc,NFCH2OI_loc = df_nifty50['CallOI'].nlargest(2,keep='last').index # Returns location of a max and 2nd max values


# Put values

NFPH1OI,NFPH2OI = df_nifty50['PutOI'].nlargest(2,keep='last')  # Returns a max and 2nd max values

NFPH1OI_loc,NFPH2OI_loc = df_nifty50['PutOI'].nlargest(2,keep='last').index # Returns location of a max and 2nd max values


## Calculate the range which is same as Higest and 2nd highest Open intrest from call and Put side
# Call
NFCH1OI_SP = df_nifty50.iloc[NFCH1OI_loc]['Strike Price'] # Returns a Strick price 
NFCH2OI_SP = df_nifty50.iloc[NFCH2OI_loc]['Strike Price'] # Returns a Strick price 

# Put
NFPH1OI_SP = df_nifty50.iloc[NFPH1OI_loc]['Strike Price'] # Returns a Strick price 
NFPH2OI_SP = df_nifty50.iloc[NFPH2OI_loc]['Strike Price'] # Returns a Strick price 

## Calculate the High Put Call ratio (PCR)

NFHPCR = NFPH1OI/NFCH1OI
nfhpcr = format(NFHPCR,'.2f')

print('Nifty Higest Open Intrest PCR ratio ',nfhpcr,file=open("NSEmarket.txt", "a"))
print('')
print('',file=open("NSEmarket.txt", "a"))

## Calculate the total Put Call ratio

NFCallOI_sum = df_nifty50['CallOI'].sum()  # Returns a sum of Call Open intrest values

NFPutOI_sum = df_nifty50['PutOI'].sum()  # Returns a sum of  Put Open intrest values

NFTPCR = NFPutOI_sum / NFCallOI_sum

nftpcr = format(NFTPCR,'.2f')

print('Nifty Total Open Intrest PCR ratio ',nftpcr,file=open("NSEmarket.txt", "a"))
print('')
print('',file=open("NSEmarket.txt", "a"))

# PUT call Ratio  PCR
# avrage is 0.7

# A rising put-call ratio, or a ratio greater than .7 or exceeding 1, means that equity traders are buying more puts than calls. It suggests that bearish sentiment is building in the market. Investors are either speculating that the market will move lower or are hedging their portfolios in case there is a sell-off.
if  NFTPCR > 0.7:
    print('It suggests that bearish sentiment is building in the market.',file=open("NSEmarket.txt", "a"))
    if NFTPCR > 1.5:
        print("Over purchased Put Options",file=open("NSEmarket.txt", "a"))



# A falling put-call ratio, or below .7 and approaching .5, is considered a bullish indicator. It means more calls are being bought versus puts.

if  NFTPCR < 0.9:
    print("This considered a bullish indicator.",file=open("NSEmarket.txt", "a"))
    if NFTPCR < 0.6:
        print("Over purchased Call Options",file=open("NSEmarket.txt", "a"))

print('',file=open("NSEmarket.txt", "a"))




## Main Logic Nifty

print('OI Resistance 2 ',NFCH1OI_SP,file=open("NSEmarket.txt", "a"))

print('OI Resistance 1 ',NFCH2OI_SP,file=open("NSEmarket.txt", "a"))

print('Nifty SP        ',n50f,file=open("NSEmarket.txt", "a"))

print('OI Support 1    ',NFPH1OI_SP,file=open("NSEmarket.txt", "a"))

print('OI Support 2    ',NFPH2OI_SP,file=open("NSEmarket.txt", "a"))

print('')
print('',file=open("NSEmarket.txt", "a"))



################################### End of BOT ############################################
print('#############################################################################',file=open("NSEmarket.txt", "a"))
print('',file=open("NSEmarket.txt", "a"))
print('End of BOT Read text file "NSEmarket" for results generated / saved at same folder as prrogram')

####################################### End Program ######################################################