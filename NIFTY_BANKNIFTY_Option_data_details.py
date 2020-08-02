#-*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:34:18 2020

@author: Sangram Phadke

Call Option Intrinsic Value=USC−CS
where:
    
USC=Underlying Stock’s Current Price

CS=Call Strike Price
​	 
﻿
Put Option Intrinsic Value=PS−USC
where:
PS=Put Strike Price
​Time Value=Option Price−Intrinsic Value



#PCR put call ratio 1.68 to 1.8

#highest est Open intrest strike price in put and call when NIFTY 50 reach at the strike price sell...



#PUT call Ratio  PCR
#avrage is 0.7
#A rising put-call ratio, or a ratio greater than .7 or exceeding 1, means that equity traders are buying more puts than calls. It suggests that bearish sentiment is building in the market. Investors are either speculating that the market will move lower or are hedging their portfolios in case there is a sell-off.
#A falling put-call ratio, or below .7 and approaching .5, is considered a bullish indicator. It means more calls are being bought versus puts.

#Over purchased options ce

#if PCR < 0.7
 
#if above condition meet price will fall after result


#if PCR > 0.7

#if above condition meet price will go up after result



"""

#Importing the libraries
import numpy as np
import pandas as pd
import math
from datetime import datetime
from nsetools import Nse
   
#Importing the NIFTY dataset from NSE live site / portel 

nse = Nse()  #NSE object creation


print('############################################################################',file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))
Starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull start time
Pst = datetime.now().strftime("%H:%M")
Day = datetime.now().strftime("%A")
Daydate = datetime.now().strftime("%d")
print('AI for Weekly Option data Start Time',Starttime,file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))
#Capital letter words / variable which are not appre in data variable box to reduce the display data frames and clean program view
 
#Nf_n50 = nse.get_index_quote("nifty 50") 
#print('NIFTY 50   index current value is {} and percent change is {} '.format(Nf_n50['lastPrice'],Nf_n50['pChange'])) 
#print('NIFTY 50   index current value is {} and percent change is {} '.format(Nf_n50['lastPrice'],Nf_n50['pChange']),file=open("Option_data.txt", "a"))


#Test data  / no internet program
N50 = 11000
print('')
#N50 = Nf_n50['lastPrice']
N50p = int(50 * round(float(N50)/50))
n50f = format(N50p,'.2f')

#Bf_bank = nse.get_index_quote("nifty bank") 
#print('NIFTY BANK index current value is {} and percent change is {} '.format(Bf_bank['lastPrice'],Bf_bank['pChange'])) 
print('')


#Test data / no internet program
BN = 21230

#BN = Bf_bank['lastPrice']
BNp = int(100 * round(float(BN)/100))
bnf = format(BNp,'.2f')


#Importing the Weekly Option dataset from Files stored in same folder
##Run the specific files on 9:45  12 and 1:30 each day and save on exit 

COLUMN_NAMES=['CallOI','CallLTP','CallNetChange','Strike Price','PutNetChange','PutLTP','PutOI']


#Weekly Option data


#######################################Bank Nifty ##########################################

print('#For BankNifty Option Data',file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))


##Data from CSV File
#Data Slicing for BankNifty

dr_banknifty = pd.read_excel('banknifty.xlsx',sheet_name = 'option-chain-equity-derivatives')
Dr_banknifty1 = dr_banknifty.iloc[:,[0,4,5,10,15,16,20]]
Dr_banknifty1.columns = COLUMN_NAMES
#dr_banknifty2 = (dr_banknifty1).dropna()
df_banknifty = Dr_banknifty1.replace(to_replace = ['- ','-'], value =0)


#Collect Higest and 2nd highest est Open intrest from call side

"""
Exact value functions
#BNCH1OI = df_banknifty['CallOI'].max() #Returns a max value
#BNCH1OI_loc = df_banknifty['CallOI'].idxmax() #Returns a index location max value
"""
#Call values
BNCH1OI,BNCH2OI = df_banknifty['CallOI'].nlargest(2,keep='last')  #Returns a max and 2nd max values

#Convert to Words for print only
BNCH1OI_Wd = format(BNCH1OI/100000,'.2f')
BNCH2OI_Wd = format(BNCH2OI/100000,'.2f')

#Returns location of a max and 2nd max values
BNCH1OI_loc,BNCH2OI_loc = df_banknifty['CallOI'].nlargest(2,keep='last').index 



#Collect Higest and 2nd highest est Open intrest from Put side
#Put values

BNPH1OI,BNPH2OI = df_banknifty['PutOI'].nlargest(2,keep='last')  #Returns a max and 2nd max values

#Convert to Words for print only
BNPH1OI_Wd = format(BNPH1OI/100000,'.2f')
BNPH2OI_Wd = format(BNPH2OI/100000,'.2f')

#Returns location of a max and 2nd max values
BNPH1OI_loc,BNPH2OI_loc = df_banknifty['PutOI'].nlargest(2,keep='last').index 


##Calculate / data of Stick price taken from Higest and 2nd highest Open intrest from call and Put side

#Call
BNCH1OI_SP = df_banknifty.iloc[BNCH1OI_loc]['Strike Price'] #Returns a Strick price 
BNCH2OI_SP = df_banknifty.iloc[BNCH2OI_loc]['Strike Price'] #Returns a Strick price 

#Put
BNPH1OI_SP = df_banknifty.iloc[BNPH1OI_loc]['Strike Price'] #Returns a Strick price 
BNPH2OI_SP = df_banknifty.iloc[BNPH2OI_loc]['Strike Price'] #Returns a Strick price 


##PCR Analysis
print('#BankNifty PCR Data Analysis',file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))
#Calculate the highest  Put Call ratio (PCR)
BNHPCR = BNPH1OI/BNCH1OI
bnhpcr = format(BNHPCR,'.2f')
print('1. BankNifty Higest Open Interest PCR ratio ',bnhpcr,file=open("Option_data.txt", "a"))

##Calculate the total Put Call ratio
BNCallOI_sum = df_banknifty['CallOI'].sum()  #Returns a sum of Call Open intrest values
BNPutOI_sum = df_banknifty['PutOI'].sum()  #Returns a sum of  Put Open intrest values
BNTPCR = BNPutOI_sum / BNCallOI_sum
bntpcr = format(BNTPCR,'.2f')
print('2. BankNifty Total  Open Interest PCR ratio ',bntpcr,file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))

#Append the Highest PCR value in CSV file and write it to PCR data frame
print(bnhpcr,file=open("BN_Option_data.csv", "a")) #Simple append function using print
Dr_BNPCR_list = pd.read_csv('BN_Option_data.csv')
df_BNPCR_list = pd.DataFrame(data=Dr_BNPCR_list)
#find the persent change in BN HPCR
BNPCR_PC = (100 * ((df_BNPCR_list.iloc[-1] - df_BNPCR_list.iloc[-2]) / df_BNPCR_list.iloc[-2])) 

if  float(BNPCR_PC) > 0.0:
    print('#A rising put-call ratio, means more Puts are being bought versus Calls.',file=open("Option_data.txt", "a"))

print('',file=open("Option_data.txt", "a"))

if  float(BNPCR_PC) < 0.0:
    print('#A falling put-call ratio, means more calls are being bought versus puts.',file=open("Option_data.txt", "a"))

print('',file=open("Option_data.txt", "a"))

if  float(BNTPCR) < 0.5:
    print("#BN: Over purchased Call Options",file=open("Option_data.txt", "a"))
if  float(BNTPCR) > 1.5:
    print("#BN: Over purchased Put Options",file=open("Option_data.txt", "a"))

print('',file=open("Option_data.txt", "a"))
print('')

##Open Interest Analysis

#Find the Call_OI & Put_OI for current BN Strick price 
BNCSPLOC = 0
for BNCSPLOC in range(len(df_banknifty)):
    if (df_banknifty['Strike Price'][(BNCSPLOC)]) == BNp:
        BNCSPCOI = df_banknifty.iloc[BNCSPLOC]['CallOI']
        BNCSPPOI = df_banknifty.iloc[BNCSPLOC]['PutOI']
#Convert to Words for print only
BNCSPCOI_Wd = format(BNCSPCOI/100000,'.2f')
BNCSPPOI_Wd = format(BNCSPPOI/100000,'.2f')

        
#Main Logic for Bank Nifty for print the OI and SP

print('#Highest Open Interest with STRIKE PRICE',file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))
print('#BankNifty have {} Lakh Call_OI & {} Lakh Put_OI for Current SP {}'.format(BNCSPCOI_Wd,BNCSPPOI_Wd,bnf),file=open("Option_data.txt", "a"))
print('1. Max highest {} Lakh Call_OI at SP {} R2 '.format(BNCH1OI_Wd,BNCH1OI_SP),file=open("Option_data.txt", "a"))
print('2. 2nd highest {} Lakh Call_OI at SP {} R1 '.format(BNCH2OI_Wd,BNCH2OI_SP),file=open("Option_data.txt", "a"))
print('3. Max highest {} Lakh Put_OI  at SP {} S2 '.format(BNPH1OI_Wd,BNPH1OI_SP),file=open("Option_data.txt", "a"))
print('4. 2nd highest {} Lakh Put_OI  at SP {} S1 '.format(BNPH2OI_Wd,BNPH2OI_SP),file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a")) 


##Price prediction 

#Main logic for direction of SP to neareset SP (Direction prediction)
TCOI_list = [BNCH1OI,BNCH2OI]
TPOI_list = [BNPH1OI,BNPH2OI]
R_SP = []


def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))] 
    
  
#Driver code 
#for Call_OI
if (closest(TCOI_list, BNCSPCOI)) == BNCH1OI:  #compare the 
    R_SP.append(BNCH1OI_SP)
elif (closest(TCOI_list, BNCSPCOI)) == BNCH2OI:
    R_SP.append(BNCH2OI_SP)

#for Put_OI    
if (closest(TPOI_list, BNCSPPOI)) == BNPH1OI:
    R_SP.append(BNPH1OI_SP)
elif (closest(TPOI_list, BNCSPPOI)) == BNPH2OI:
    R_SP.append(BNPH2OI_SP)

#for strick price     
print('#Probability prediction the price will move in direction of SP ',(closest(R_SP, BNp)),file=open("Option_data.txt", "a")) 

print('',file=open("Option_data.txt", "a"))

#Ideal Buy Range for CALL or Put
print('#Ideal Buy Range for Call & Put',file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))
BNCE= ((BNCH1OI_SP + BNCH2OI_SP)/2) #average of highest  Call_OI
BNPE= ((BNPH1OI_SP + BNPH2OI_SP)/2) #average of highest  Put_OI
print('1. Ideal Buy BankNifty {} CE'.format(BNCE-100),file=open("Option_data.txt", "a")) #Adjusting Ideal Buy lower to max OI
print('2. Ideal Buy BankNifty {} PE'.format(BNPE+100),file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))

print('BankNifty Run ok') #for run issue finding


#Risk and rewards
#Call
BNCEntry = (BNCE-100) #Call Spot SP
BNCSL = BNPH1OI_SP  #Support 2 CAll_SP derived from High Put_OI location
BNCTarget = BNCH2OI_SP #R1 as resistance
BNCRisk = (BNCEntry-BNCSL) ##Curent SP - Support 2 as stopLoss
BNCRewards = BNCTarget


if BNCRisk >0:
    BNCRR = BNCRewards / abs(BNCRisk)
else:
    BNCRR = 1.0
    
BNCRR = format(BNCRR,'.0f')

print('#For the Call If Entry is at {} then R:R is 1:{}'.format(BNCEntry,BNCRR),file=open("Option_data.txt", "a"))

#Put
BNPEntry = (BNPE+100) #Put Spot SP
BNPSL = BNCH2OI_SP  #R1 CAll_SP derived from High Put_OI location
BNPTarget = BNPH1OI_SP  #S1
BNPRisk = (BNCEntry-BNPSL) ##Curent SP - Support 2 as stopLoss
BNPRewards = BNPTarget

if BNPRisk >0:
    BNPRR = BNPRewards / abs(BNPRisk)
else:
    BNPRR = 1.0
    
BNPRR = format(BNPRR,'.0f')

print('#For the Put  If Entry is at {} then R:R is 1:{} '.format(BNPEntry,BNPRR),file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))


##Average trading price (Self dev formula)
##Need Back test
#avrage of 2 High OI Strick price LTP & Current Strick price LTP  and ~15%  range of tollarance 

print('#For BankNifty Total average Option price',file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))

#Call 
BNCLTPH1 = df_banknifty.iloc[BNCH1OI_loc]['CallLTP']
BNCLTPH2 = df_banknifty.iloc[BNCH2OI_loc]['CallLTP']

BNCSPLOC = 0
for BNCSPLOC in range(len(df_banknifty)):
    if (df_banknifty['Strike Price'][(BNCSPLOC)]) == BNp:
        BNCLTPSP = df_banknifty.iloc[BNCSPLOC]['CallLTP']
        

AvgBNCLTPH = ((BNCLTPH1+BNCLTPH2+BNCLTPSP )/3)
#AvgBNCLTPH_UR = AvgBNCLTPH*1.15
#AvgBNCLTPH_LR = (AvgBNCLTPH - (AvgBNCLTPH*0.15))

AvgBNCLTPH = format(((BNCLTPH1+BNCLTPH2+BNCLTPSP )/3),'.2f')

print('1. The Total avrage Call Option price is {} '.format(AvgBNCLTPH),file=open("Option_data.txt", "a"))

#Put
BNPLTPH1 = df_banknifty.iloc[BNPH1OI_loc]['PutLTP']
BNPLTPH2 = df_banknifty.iloc[BNPH2OI_loc]['PutLTP']


BNPSPLOC = 0
for BNPSPLOC in range(len(df_banknifty)):
    if (df_banknifty['Strike Price'][(BNPSPLOC)]) == BNp:
        BNPLTPSP = df_banknifty.iloc[BNPSPLOC]['PutLTP']
        
AvgBNPLTPH = (BNPLTPH1+BNPLTPH2+BNPLTPSP )/3
#AvgBNPLTPH_UR = (AvgBNPLTPH*1.15)
#AvgBNPLTPH_LR = (AvgBNPLTPH - (AvgBNPLTPH*0.15))

AvgBNPLTPH = format(((BNPLTPH1+BNPLTPH2+BNPLTPSP )/3),'.2f')

print('2. The Total avrage Put  Option price is {} '.format(AvgBNPLTPH),file=open("Option_data.txt", "a"))

print('',file=open("Option_data.txt", "a"))







######################################  NIFTY 50 ###########################################
print('',file=open("Option_data.txt", "a"))
print('########',file=open("Option_data.txt", "a"))
print('#For Nifty Option Data',file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))

##Data Slicing for Nifty 50
Dr_nifty50 = pd.read_excel('nifty.xlsx' , sheet_name='option-chain-equity-derivatives')
Dr_nifty501 = Dr_nifty50.iloc[:,[0,4,5,10,15,16,20]]
Dr_nifty501.columns = COLUMN_NAMES
#Dr_nifty502 = Dr_nifty501.dropna()
df_nifty50 = Dr_nifty501.replace(to_replace = ['- ','-'], value =0)


##Collect Higest and 2nd highest est Open intrest from call side
#Call values

NFCH1OI,NFCH2OI = df_nifty50['CallOI'].nlargest(2,keep='last')  #Returns a max and 2nd max values

#Convert to Words for print only
NFCH1OI_Wd = format(NFCH1OI/100000,'.2f')
NFCH2OI_Wd = format(NFCH2OI/100000,'.2f')

#Highest OI location

NFCH1OI_loc,NFCH2OI_loc = df_nifty50['CallOI'].nlargest(2,keep='last').index #Returns location of a max and 2nd max values

##Collect Higest and 2nd highest est Open intrest from Put side
#Put values

NFPH1OI,NFPH2OI = df_nifty50['PutOI'].nlargest(2,keep='last')  #Returns a max and 2nd max values
#Convert to Words for print only
NFPH1OI_Wd = format(NFPH1OI/100000,'.2f')
NFPH2OI_Wd = format(NFPH2OI/100000,'.2f')

#Highest OI location
NFPH1OI_loc,NFPH2OI_loc = df_nifty50['PutOI'].nlargest(2,keep='last').index #Returns location of a max and 2nd max values

##Calculate / data taken for the Strike price from Higest and 2nd highest Open intrest from call and Put side
#Call
NFCH1OI_SP = df_nifty50.iloc[NFCH1OI_loc]['Strike Price'] #Returns a Strick price 
NFCH2OI_SP = df_nifty50.iloc[NFCH2OI_loc]['Strike Price'] #Returns a Strick price 

#Put
NFPH1OI_SP = df_nifty50.iloc[NFPH1OI_loc]['Strike Price'] #Returns a Strick price 
NFPH2OI_SP = df_nifty50.iloc[NFPH2OI_loc]['Strike Price'] #Returns a Strick price 


##Main Logic for PCR Data Analysis

print('#Nifty PCR Data Analysis',file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))
#Calculate the highest  Put Call ratio (PCR)
NFHPCR = NFPH1OI/NFCH1OI
nfhpcr = format(NFHPCR,'.2f')
print('1. Nifty Higest Open Interest PCR ratio ',nfhpcr,file=open("Option_data.txt", "a"))

#Calculate the total Put Call ratio
NFCallOI_sum = df_nifty50['CallOI'].sum()  #Returns a sum of Call Open intrest values
NFPutOI_sum = df_nifty50['PutOI'].sum()  #Returns a sum of  Put Open intrest values
NFTPCR = NFPutOI_sum / NFCallOI_sum
nftpcr = format(NFTPCR,'.2f')
print('2. Nifty Total  Open Interest PCR ratio ',nftpcr,file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))


#Rising and Falling PCR data analysis. 

#Append the Highest PCR value in CSV file and write it to data frame
print(nfhpcr,file=open("NF_Option_data.csv", "a")) #Simple print fuction use for append value 
Dr_NFPCR_list = pd.read_csv('NF_Option_data.csv')
df_NFPCR_list = pd.DataFrame(data=Dr_NFPCR_list)

#find the persent change in NF HPCR
NFPCR_PC = (100 * ((df_NFPCR_list.iloc[-1] - df_NFPCR_list.iloc[-2]) / df_NFPCR_list.iloc[-2])) 

#Analysis

if  float(NFPCR_PC) > 0.0:
    print('#A rising put-call ratio, means more Puts are being bought versus Calls.',file=open("Option_data.txt", "a"))

print('',file=open("Option_data.txt", "a"))

if  float(NFPCR_PC) < 0.0:
    print('#A falling put-call ratio, means more calls are being bought versus puts.',file=open("Option_data.txt", "a"))

if  float(NFTPCR) < 0.5:
    print("#Over purchased Call Options",file=open("Option_data.txt", "a"))
if  float(NFTPCR) > 1.5:
    print("#Over purchased Put Options",file=open("Option_data.txt", "a"))

print('',file=open("Option_data.txt", "a"))


##Open Interest Analysis 

#Find the Call_OI & Put_OI for current NF50 Strick price 
NFCSPLOC = 0
for NFCSPLOC in range(len(df_nifty50)):
    if (df_nifty50['Strike Price'][(NFCSPLOC)]) == N50p:
        NFCSPCOI = df_nifty50.iloc[NFCSPLOC]['CallOI']
        NFCSPPOI = df_nifty50.iloc[NFCSPLOC]['PutOI']
#Convert to Words for print only
NFCSPCOI_Wd = format(NFCSPCOI/100000,'.2f')
NFCSPPOI_Wd = format(NFCSPPOI/100000,'.2f')



#Main Logic Nifty to print the open intrest and Strike Price
print('#Highest Open Interest with STRIKE PRICE',file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))
print('#Nifty 50 have {} Lakh Call_OI & {} Lakh Put_OI for Current SP {}'.format(NFCSPCOI_Wd,NFCSPPOI_Wd,n50f),file=open("Option_data.txt", "a"))

print('1. Max highest {} Lakh Call_OI at SP {} R2 '.format(NFCH1OI_Wd,NFCH1OI_SP),file=open("Option_data.txt", "a"))
print('2. 2nd highest {} Lakh Call_OI at SP {} R1 '.format(NFCH2OI_Wd,NFCH2OI_SP),file=open("Option_data.txt", "a"))
print('3. Max highest {} Lakh Put_OI  at SP {} S2 '.format(NFPH1OI_Wd,NFPH1OI_SP),file=open("Option_data.txt", "a"))
print('4. 2nd highest {} Lakh Put_OI  at SP {} S1 '.format(NFPH2OI_Wd,NFPH2OI_SP),file=open("Option_data.txt", "a"))

print('')
print('',file=open("Option_data.txt", "a"))

#Main logic for direction of SP to neareset SP (Direction prediction)
NTCOI_list = [NFCH1OI,NFCH2OI]
NTPOI_list = [NFPH1OI,NFPH2OI]
NR_SP = []


def closestn(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]
 
  
#Driver code 
#for Call_OI
if (closestn(NTCOI_list, NFCSPCOI)) == NFCH1OI:  #compare the OT
    NR_SP.append(NFCH1OI_SP)
elif (closestn(NTCOI_list, NFCSPCOI)) == NFCH2OI:
    NR_SP.append(NFCH2OI_SP)

#for Put_OI    
if (closestn(NTPOI_list, NFCSPPOI)) == NFPH1OI:
    NR_SP.append(NFPH1OI_SP)
elif (closestn(NTPOI_list, NFCSPPOI)) == NFPH2OI:
    NR_SP.append(NFPH2OI_SP)

#for strick price     
print('#Probability prediction the price will move in direction of SP ',(closestn(NR_SP, N50p)),file=open("Option_data.txt", "a")) 

print('',file=open("Option_data.txt", "a"))

##Price prediction 


#Ideal Buy Range for CALL or PUT
print('#Ideal Buy Range for CALL and PUT',file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))
NCE= ((NFCH1OI_SP + NFCH2OI_SP)/2) #average of highest  Call_OI
NPE= ((NFPH1OI_SP + NFPH2OI_SP)/2) #average of highest  Put_OI
print('1. Ideal Buy Nifty {} CE'.format(NCE-50),file=open("Option_data.txt", "a")) #Adjusting Ideal Buy lower to max OI
print('2. Ideal Buy Nifty {} PE'.format(NPE+50),file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))


#Risk and rewards
#Call
NFCEntry = (NCE-50) #Call Spot SP

NFCSL = NFPH1OI_SP  #Support 2 CAll_SP derived from High Put_OI location

NFCTarget = NFCH2OI_SP #R1 as resistance

NFCRisk = (NFCEntry-NFCSL) ##Curent SP - Support 2 as stopLoss

NFCRewards = NFCTarget

if NFCRisk >0:
    NFCRR = NFCRewards / abs(NFCRisk)
else:
    NFCRR = 1.0
    
NFCRR = format(NFCRR,'.0f')

print('#For the Call If Entry is at {} then R:R is 1:{}'.format(NFCEntry,NFCRR),file=open("Option_data.txt", "a"))

#Put
NFPEntry = (NPE+50) #Put Spot SP

NFPSL = NFCH2OI_SP  #R1 CAll_SP derived from High Put_OI location

NFPTarget = NFPH1OI_SP  #S1

NFPRisk = (NFCEntry-NFPSL) ##Curent SP - Support 2 as stopLoss

NFPRewards = NFPTarget

if NFPRisk >0:
    NFPRR = NFPRewards / abs(NFPRisk)
else:
    NFPRR = 1.0
    
NFPRR = format(NFPRR,'.0f')

print('#For the Put  If Entry is at {} then R:R is 1:{} '.format(NFPEntry,NFPRR),file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))







print('')
print('Nifty  50  Run ok')


##Average trading price 
#avrage of 2 High OI Strick price LTP & Current Strick price LTP  and ~15%  range of tollarance (Self dev formula)
##Need Back test
print('#For Nifty 50 Total average Option price',file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))

#Call highest OI price location and LTP
NFCLTPH1 = df_nifty50.iloc[NFCH1OI_loc]['CallLTP']
NFCLTPH2 = df_nifty50.iloc[NFCH2OI_loc]['CallLTP']

NFCSPLOC = 0
for NFCSPLOC in range(len(df_nifty50)):
    if (df_nifty50['Strike Price'][(NFCSPLOC)]) == N50p:
        NFCLTPSP = df_nifty50.iloc[NFCSPLOC]['CallLTP']
        

AvgNFCLTPH = ((NFCLTPH1+NFCLTPH2+NFCLTPSP )/3)
#AvgNFCLTPH_UR = AvgNFCLTPH*1.15
#AvgNFCLTPH_LR = (AvgNFCLTPH - (AvgNFCLTPH*0.15))
AvgNFCLTPH = format(((NFCLTPH1+NFCLTPH2+NFCLTPSP )/3),'.2f')
print('1. The Total avrage Call Option price is {} '.format(AvgNFCLTPH),file=open("Option_data.txt", "a"))

#Put highest open price location and LTP
NFPLTPH1 = df_nifty50.iloc[NFPH1OI_loc]['PutLTP']
NFPLTPH2 = df_nifty50.iloc[NFPH2OI_loc]['PutLTP']


NFPSPLOC = 0
for NFPSPLOC in range(len(df_nifty50)):
    if (df_nifty50['Strike Price'][(NFPSPLOC)]) == N50p:
        NFPLTPSP = df_nifty50.iloc[NFPSPLOC]['PutLTP']
        
AvgNFPLTPH = ((NFPLTPH1+NFPLTPH2+NFPLTPSP )/3)
#AvgNFPLTPH_UR = AvgNFPLTPH*1.15
#AvgNFPLTPH_LR = (AvgNFPLTPH - (AvgNFPLTPH*0.15))
AvgNFPLTPH = format(((NFPLTPH1+NFPLTPH2+NFPLTPSP )/3),'.2f')
print('2. The Total avrage Put  Option price is {} '.format(AvgNFPLTPH),file=open("Option_data.txt", "a"))
print('',file=open("Option_data.txt", "a"))

print('')
print('End of the BOT')


##############################################Stocks Options #########################################

"""
##Data slicing for FnO Stocks

I = 'SBIN'  ##Insert the name same as in file
Nisl = nse.get_quote(I)
Ins = Nisl['symbol']
Icn = Nisl['companyName']
Iop = Nisl['open']
Iltp = Nisl['lastPrice']
Ipc = Nisl['pChange']

Dr_stock = pd.read_excel ('Stock.xlsm' , sheet_name='Option Chain')

Dr_stock1 = Dr_stock.iloc[:,[0,4,5,10,15,16,20]]

Dr_stock1.columns = COLUMN_NAMES

Dr_stock2 = Dr_stock1.dropna()

df_stock = Dr_stock2.replace(to_replace = ['- ','-'], value =0)


"""