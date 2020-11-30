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


"""
#Importing the libraries
import numpy as np
import pandas as pd
import math
from datetime import datetime
from nsetools import Nse
import matplotlib.pyplot as plt

   
#Importing the NIFTY dataset from NSE live site / portel 

nse = Nse()  #NSE object creation


print('############################################################################',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
Starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull start time
Pst = datetime.now().strftime("%H:%M")
Day = datetime.now().strftime("%A")
Daydate = datetime.now().strftime("%d")
pdate = datetime.now().strftime("%d-%m-%Y")
print('AI for Weekly Option data Start Time',Starttime,file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
#Capital letter words / variable which are not appre in data variable box to reduce the display data frames and clean program view


# # uncomment this to Test data  / no internet program
# N50 = 11089
# BN = 21000
 

#uncomment this to Test data  / no internet program

Nf_n50 = nse.get_index_quote("nifty 50")
# nf_n50_val = nse.get_index_quote("nifty 50") 
print('NIFTY 50   index current value is {} and percent change is {} '.format(Nf_n50['lastPrice'],Nf_n50['pChange']))#,file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('NIFTY 50   index current value is {} and percent change is {} '.format(Nf_n50['lastPrice'],Nf_n50['pChange']),file=open("NIFTY_BankNifty_OI_data.txt", "a")) 
# print('')
N50 = Nf_n50['lastPrice']

Bf_bank = nse.get_index_quote("nifty bank")
print('NIFTY BANK index current value is {} and percent change is {} '.format(Bf_bank['lastPrice'],Bf_bank['pChange']),file=open("NIFTY_BankNifty_OI_data.txt", "a")) 
print('NIFTY BANK index current value is {} and percent change is {} '.format(Bf_bank['lastPrice'],Bf_bank['pChange'])) 
# print('')
BN = Bf_bank['lastPrice']


#Converting the LTP in term of SP

N50p = int(50 * round(float(N50)/50)) # To convert the LTP to SP in multipal of 50
n50f = format(N50p,'.2f')
BNp = int(100 * round(float(BN)/100)) # To convert the LTP to SP in multipal of 100
bnf = format(BNp,'.2f')


#Importing the Weekly Option dataset from Files stored in same folder
##Run the specific files on 9:45  12 and 1:30 each day and save on exit 

COLUMN_NAMES=['CallOI','Call_OI_Change','CallLTP','Strike Price','PutLTP','Put_OI_Change','PutOI']
COLUMN_NAMES_Rev=['CallOI','Call_OI_Change','CallLTP','CallPremium','Strike Price','PutPremium','PutLTP','Put_OI_Change','PutOI']

# Option data below is combine // added 2 expires data  
## For avrage out use Divde by 2 for LTP  / for OI its correct to take as it is. 

####################################### Bank Nifty ##########################################
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('#Analysis for BankNifty Option Data',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))


##Data from CSV File
#Data Slicing for BankNifty
"""
Automate this process
"""
#dr_banknifty = pd.read_excel('banknifty.xlsx',sheet_name = 'option-chain-equity-derivatives')

Dr_banknifty1 = pd.read_csv('banknifty1.csv')
Dr_banknifty2 = pd.read_csv('banknifty2.csv')

#after  Remove the unwanted columns manulay on CSV file. 

# replace the string text
# replace the '-' value to zero & ccoma content number to float number 
Dr_banknifty3 = Dr_banknifty1.replace(to_replace = ['- ','-'], value =0)
Dr_banknifty3 = Dr_banknifty3.replace('\,','', regex=True)
Dr_banknifty4 = Dr_banknifty2.replace(to_replace = ['- ','-'], value =0)
Dr_banknifty4 = Dr_banknifty4.replace('\,','', regex=True)


#take required coulmns from above file
dr_banknifty5 = Dr_banknifty3.iloc[:,[0,1,4,10,16,19,20]]
dr_banknifty6 = Dr_banknifty4.iloc[:,[0,1,4,10,16,19,20]]


# set column name as per our choice
dr_banknifty5.columns = COLUMN_NAMES
dr_banknifty6.columns = COLUMN_NAMES

Df_banknifty1  = []  # reSet the dataframe
#Combine dataframes 
Df_banknifty1 = pd.concat((dr_banknifty5,dr_banknifty6)) 
Df_banknifty1 = Df_banknifty1.astype(float) # converting in to float

#Df_banknifty1 = Df_banknifty1.reset_index(drop = True) # Use if needed
#Df_banknifty1 = Df_banknifty1.replace(np.nan,0) # Use if needed

df_banknifty = pd.pivot_table(data=Df_banknifty1,index=['Strike Price'],aggfunc='sum') # Pivot table for adding the columns values
df_banknifty = df_banknifty.reset_index()  # Adding the automated index numbers                             

df_banknifty = df_banknifty.reindex(columns=COLUMN_NAMES)      # rearranging the values as per columans names                          
# df_banknifty.to_csv('df_banknifty_file.csv') # Use if needed

#Collect Higest and 2nd high Open intrest from call side

"""
Exact value functions
#BNCH1OI = df_banknifty['CallOI'].max() #Returns a max value
#BNCH1OI_loc = df_banknifty['CallOI'].idxmax() #Returns a index location max value
"""
#Call values
BNCH1OI,BNCH2OI = df_banknifty['CallOI'].nlargest(2,keep='last')  #Returns a max and 2nd max values OI

#BNCH1OIC,BNCH2OIC = df_banknifty['Call_OI_Change'].nlargest(2,keep='last')  #Returns a max and 2nd max values of Change in OI

BNCH1OIC = df_banknifty['Call_OI_Change'].nlargest(1,keep='last')  #Returns a max values of Change in OI
BNCH2OIC = df_banknifty['Call_OI_Change'].nsmallest(1,keep='last')  #Returns a min values of Change in OI


#Convert to Words for print only
BNCH1OI_Wd = format(BNCH1OI/10000,'.2f')
BNCH2OI_Wd = format(BNCH2OI/10000,'.2f')

BNCH1OIC_Wd = format(float(BNCH1OIC)/10000,'.2f')
BNCH2OIC_Wd = format(float(BNCH2OIC)/10000,'.2f')

#Returns location of a max and 2nd max values
BNCH1OI_loc,BNCH2OI_loc = df_banknifty['CallOI'].nlargest(2,keep='last').index 
BNCH1OIC_loc,BNCH2OIC_loc = df_banknifty['Call_OI_Change'].nlargest(2,keep='last').index 

#Collect Higest and 2nd high est Open intrest from Put side
#Put values

BNPH1OI,BNPH2OI = df_banknifty['PutOI'].nlargest(2,keep='last')  #Returns a max and 2nd max values of OI
#BNPH1OIC,BNPH2OIC = df_banknifty['Put_OI_Change'].nlargest(2,keep='last')  #Returns a max and 2nd max values of change in OI

BNPH1OIC = df_banknifty['Put_OI_Change'].nlargest(1,keep='last')  #Returns a max and 2nd max values of change in OI
BNPH2OIC = df_banknifty['Put_OI_Change'].nsmallest(1,keep='last')  #Returns a max and 2nd max values of change in OI

#Convert to Words for print only
BNPH1OI_Wd = format(BNPH1OI/10000,'.2f')
BNPH2OI_Wd = format(BNPH2OI/10000,'.2f')

BNPH1OIC_Wd = format(float(BNPH1OIC)/10000,'.2f')
BNPH2OIC_Wd = format(float(BNPH2OIC)/10000,'.2f')


#Returns location of a max and 2nd max values
BNPH1OI_loc,BNPH2OI_loc = df_banknifty['PutOI'].nlargest(2,keep='last').index 
BNPH1OIC_loc,BNPH2OIC_loc = df_banknifty['Put_OI_Change'].nlargest(2,keep='last').index 


##Calculate / data of Stick price taken from Higest and 2nd high Open intrest & change in OI from call and Put side

#Call
BNCH1OI_SP = df_banknifty.iloc[BNCH1OI_loc]['Strike Price'] #Returns a Strick price
BNCH2OI_SP = df_banknifty.iloc[BNCH2OI_loc]['Strike Price'] #Returns a Strick price
BNCH1OIC_SP = df_banknifty.iloc[BNCH1OIC_loc]['Strike Price'] #Returns a Strick price  Change OI
BNCH2OIC_SP = df_banknifty.iloc[BNCH2OIC_loc]['Strike Price'] #Returns a Strick price Change OI

#Put
BNPH1OI_SP = df_banknifty.iloc[BNPH1OI_loc]['Strike Price'] #Returns a Strick price
BNPH2OI_SP = df_banknifty.iloc[BNPH2OI_loc]['Strike Price'] #Returns a Strick price 
BNPH1OIC_SP = df_banknifty.iloc[BNPH1OIC_loc]['Strike Price'] #Returns a Strick price Change OI
BNPH2OIC_SP = df_banknifty.iloc[BNPH2OIC_loc]['Strike Price'] #Returns a Strick price Change OI

"""
#Direct calculation
# BNC_Pre = (BNCH1OI_LTP/BNCSPCLTP)/2
# BNC_Pre_Wd = format(BNC_Pre,'.2f')
# BNP_Pre = (BNPH1OI_LTP/BNCSPPLTP)/2
# BNP_Pre_Wd = format(BNP_Pre,'.2f')
"""

##PCR Analysis
print('#BankNifty PCR Data Analysis',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
#Calculate the high  Put Call ratio (PCR)
BNHPCR = BNPH1OI/BNCH1OI
HighOI_BN1 = BNPH1OI + BNCH1OI
HighOI_BN = format(HighOI_BN1/10000,'.2f')
bnhpcr = format(BNHPCR,'.2f')

print('1. BankNifty Higest Open Interest is {} & PCR ratio {}'.format(HighOI_BN,bnhpcr),file=open("NIFTY_BankNifty_OI_data.txt", "a"))

##Calculate the total Put Call ratio
BNCallOI_sum = df_banknifty['CallOI'].sum()  #Returns a sum of Call Open intrest values
BNPutOI_sum = df_banknifty['PutOI'].sum()  #Returns a sum of  Put Open intrest values
BNTPCR = BNPutOI_sum / BNCallOI_sum
bntpcr = format(BNTPCR,'.2f')
TotalOI_BN1 = BNPutOI_sum + BNCallOI_sum
TotalOI_BN = format(TotalOI_BN1/10000,'.2f')
print('2. BankNifty Total  Open Interest is {} Lakh & PCR ratio {} '.format(TotalOI_BN,bntpcr),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))

##Calculate the total Put Call ratio of Change in OI
BNCallOI_Change_sum = df_banknifty['Call_OI_Change'].sum()  #Returns a sum of Call Open intrest values
BNPutOI_Change_sum = df_banknifty['Put_OI_Change'].sum()  #Returns a sum of  Put Open intrest values
BNTPCR_Change = BNPutOI_Change_sum / BNCallOI_Change_sum
bntpcr_Change = format(BNTPCR_Change,'.2f')
TotalOI_BN1_Change = BNPutOI_Change_sum + BNCallOI_Change_sum
TotalOI_BN_Change = format(TotalOI_BN1_Change/10000,'.2f')
print('3. BankNifty Total Change in Open Interest is {} Lakh & PCR ratio {} '.format(TotalOI_BN_Change,bntpcr_Change),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))




"""
# #Append the high PCR value in CSV file and write it to PCR data frame
# print(bnhpcr,file=open("BN_Option_data.csv", "a")) #Simple append function using print
# Dr_BNPCR_list = pd.read_csv('BN_Option_data.csv')
# df_BNPCR_list = pd.DataFrame(data=Dr_BNPCR_list)
# #find the persent change in BN HPCR
# BNPCR_PC = (100 * ((df_BNPCR_list.iloc[-1] - df_BNPCR_list.iloc[-2]) / df_BNPCR_list.iloc[-2])) 
# if  float(BNPCR_PC) > 0.0:
#     print('#A rising put-call ratio, means more Puts are being bought versus Calls.',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
# print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
# if  float(BNPCR_PC) < 0.0:
#     print('#A falling put-call ratio, means more calls are being bought versus puts.',file=open("NIFTY_BankNifty_OI_data.txt", "a"))

"""

if  float(BNTPCR) < 0.5:
    print("#BN: Over purchased Call Options",file=open("NIFTY_BankNifty_OI_data.txt", "a"))
if  float(BNTPCR) > 1.5:
    print("#BN: Over purchased Put Options",file=open("NIFTY_BankNifty_OI_data.txt", "a"))

print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('')


if  float(BNTPCR) > 1 :
    print('The Resistance Base on PCR is: ',BNCH1OI_SP,file=open("NIFTY_BankNifty_OI_data.txt", "a"))
    #SP of the High OI in calls # It act as a resistance
    
if  float(BNTPCR) < 1 :
    print('The Support Base on PCR is: ',BNPH1OI_SP,file=open("NIFTY_BankNifty_OI_data.txt", "a"))
    #SP of the High OI in put  # it act as a support
    

print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))

##Open Interest Analysis

#Find the Call_OI & Put_OI for current BN Strick price 
BNCSPLOC = 0

def BNcurrentvalue(Cname):
    CurrentLOC = 0
    for CurrentLOC in range(len(df_banknifty)):
        if (df_banknifty['Strike Price'][(CurrentLOC)]) == BNp:
            CurrentValue = df_banknifty.iloc[CurrentLOC][Cname]
            
    return CurrentValue

for BNCSPLOC in range(len(df_banknifty)):
    if (df_banknifty['Strike Price'][(BNCSPLOC)]) == BNp:
        BNSPLOC = BNCSPLOC


BNCSPCOI = BNcurrentvalue('CallOI')
BNCSPPOI = BNcurrentvalue('PutOI')
BNCSPCLTP = BNcurrentvalue('CallLTP')
BNCSPPLTP = BNcurrentvalue('PutLTP')
        
#Convert to Words for print only
BNCSPCOI_Wd = format(BNCSPCOI/10000,'.2f')
BNCSPPOI_Wd = format(BNCSPPOI/10000,'.2f')


##Premium  calculation: SP LTP / Current SpotPrice LTP
df_banknifty['CallPremium'] = (df_banknifty.CallLTP/BNCSPCLTP)
df_banknifty['PutPremium'] = (df_banknifty.PutLTP/BNCSPPLTP)

# rearranging the values as per columans names
df_banknifty = df_banknifty.reindex(columns=COLUMN_NAMES_Rev)      

# Values of Premium 

BNCH1OI_Pr = df_banknifty.iloc[BNCH1OI_loc]['CallPremium'] #Returns a CallPremium  
BNCH2OI_Pr = df_banknifty.iloc[BNCH2OI_loc]['CallPremium'] #Returns a CallPremium
BNCH1OI_COIn = df_banknifty.iloc[BNCH1OI_loc]['Call_OI_Change'] #Returns a CallPremium  
BNCH2OI_COIn = df_banknifty.iloc[BNCH2OI_loc]['Call_OI_Change'] #Returns a CallPremium
#Convert to Words for print only
BNCH1OI_COI = format(BNCH1OI_COIn/10000,'.2f')
BNCH2OI_COI = format(BNCH2OI_COIn/10000,'.2f')



BNCH1OIC_Pr = df_banknifty.iloc[BNCH1OIC_loc]['CallPremium'] #Returns a CallPremium  Change OI
BNCH2OIC_Pr = df_banknifty.iloc[BNCH2OIC_loc]['CallPremium'] #Returns a CallPremium Change OI
BNPH1OI_Pr = df_banknifty.iloc[BNPH1OI_loc]['PutPremium'] #Returns a PutPremium
BNPH2OI_Pr = df_banknifty.iloc[BNPH2OI_loc]['PutPremium'] #Returns a PutPremium
BNPH1OI_COIn = df_banknifty.iloc[BNPH1OI_loc]['Put_OI_Change'] #Returns a PutPremium
BNPH2OI_COIn = df_banknifty.iloc[BNPH2OI_loc]['Put_OI_Change'] #Returns a PutPremium
#Convert to Words for print only
BNPH1OI_COI = format(BNPH1OI_COIn/10000,'.2f')
BNPH2OI_COI = format(BNPH2OI_COIn/10000,'.2f')

BNPH1OIC_Pr = df_banknifty.iloc[BNPH1OIC_loc]['PutPremium'] #Returns a PutPremium Change OI
BNPH2OIC_Pr = df_banknifty.iloc[BNPH2OIC_loc]['PutPremium'] #Returns a PutPremium Change OI 


       
#Main Logic for Bank Nifty for print the OI and SP

print('#high Open Interest with STRIKE PRICE',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('#BankNifty have {} Lakh Call_OI & {} Lakh Put_OI for Current SP {}'.format(BNCSPCOI_Wd,BNCSPPOI_Wd,bnf),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('1. Max high {} Lakh Call_OI & {} ChangeOI at SP {} with Premium {}% OIR2'.format(BNCH1OI_Wd,BNCH1OI_COI,BNCH1OI_SP,format(BNCH1OI_Pr,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('2. 2nd high {} Lakh Call_OI & {} ChangeOI at SP {} with Premium {}% OIR1'.format(BNCH2OI_Wd,BNCH2OI_COI,BNCH2OI_SP,format(BNCH2OI_Pr,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('3. Max high {} Lakh Put_OI  & {} ChangeOI at SP {} with Premium {}% OIS2'.format(BNPH1OI_Wd,BNPH1OI_COI,BNPH1OI_SP,format(BNPH1OI_Pr,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('4. 2nd high {} Lakh Put_OI  & {} ChangeOI at SP {} with Premium {}% OIS1'.format(BNPH2OI_Wd,BNPH2OI_COI,BNPH2OI_SP,format(BNPH2OI_Pr,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))

print('',file=open("NIFTY_BankNifty_OI_data.txt", "a")) 

print('#Change in Open Interest Added & Left ',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('1. {}  Lakh Call_OI_Change added at  SP {} with Premium {}%'.format(BNCH1OIC_Wd,BNCH1OIC_SP,format(BNCH1OIC_Pr,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('2. {} Lakh Call_OI_Change  left  at SP {} with Premium {}%'.format(BNCH2OIC_Wd,BNCH2OIC_SP,format(BNCH2OIC_Pr,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('3. {}  Lakh Put_OI_Change  added at  SP {} with Premium {}%'.format(BNPH1OIC_Wd,BNPH1OIC_SP,format(BNPH1OIC_Pr,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('4. {} Lakh Put_OI_Change   left  at SP {} with Premium {}%'.format(BNPH2OIC_Wd,BNPH2OIC_SP,format(BNPH2OIC_Pr,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a")) 



##Price prediction 

#Main logic for direction of SP to neareset SP (Direction prediction)
TCOI_list = [BNCH1OI,BNCH2OI]
TPOI_list = [BNPH1OI,BNPH2OI]
R_SP = []

def closest(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))] 
    
#Driver code 
#for Call_OI
if (closest(TCOI_list, BNCSPCOI)) == BNCH1OI:  #compare the closest OI 
    R_SP.append(BNCH1OI_SP)
elif (closest(TCOI_list, BNCSPCOI)) == BNCH2OI:
    R_SP.append(BNCH2OI_SP)

#for Put_OI    
if (closest(TPOI_list, BNCSPPOI)) == BNPH1OI: #compare the closest OI 
    R_SP.append(BNPH1OI_SP)
elif (closest(TPOI_list, BNCSPPOI)) == BNPH2OI:
    R_SP.append(BNPH2OI_SP)

#for strick price
## Probability prediction     
print('#Probability base on OI Diffrance : The price will move in direction of SP ',(closest(R_SP, BNp)),file=open("NIFTY_BankNifty_OI_data.txt", "a"))  #compare the closest SP 

print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))

# #Find the Call_OI & Put_OI for current BN Strick price  
DBNp= (closest(R_SP, BNp))

def DBNcurrentvalue(Cname):
    CurrentLOC = 0
    for CurrentLOC in range(len(df_banknifty)):
        if (df_banknifty['Strike Price'][(CurrentLOC)]) == DBNp:
            DCurrentValue = df_banknifty.iloc[CurrentLOC][Cname]
    return DCurrentValue

DBNCSPCOI = DBNcurrentvalue('CallOI')
DBNCSPPOI = DBNcurrentvalue('PutOI')
DBNCSPCCOI = DBNcurrentvalue('Call_OI_Change')
DBNCSPPCOI = DBNcurrentvalue('Put_OI_Change')
                
#Convert to Words for print only
DBNCSPCOI_Wd = format(DBNCSPCOI/10000,'.2f')
DBNCSPPOI_Wd = format(DBNCSPPOI/10000,'.2f')
DBNCSPCCOI_Wd = format(DBNCSPCCOI/10000,'.2f')
DBNCSPPCOI_Wd = format(DBNCSPPCOI/10000,'.2f')

print('{} Lakh Call_OI \n{} Lakh Put_OI \n{} Lakh Call_OI_Change \n{} Lakh Put_OI_Change \n'.format(DBNCSPCOI_Wd,DBNCSPPOI_Wd,DBNCSPCCOI_Wd,DBNCSPPCOI_Wd),file=open("NIFTY_BankNifty_OI_data.txt", "a"))


print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
##Average trading price (Self dev formula)
##Need Back test
#avrage of 2 High OI Strick price LTP & Current Strick price LTP  and ~15%  range of tollarance 

print('#BankNifty Total average Option price',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
#To find range Range
#Stradel price logic

# #LTP + (ATM_SP CE price + ATM_SP PE price) 
# #LTP - (ATM_SP CE price + ATM_SP PE price)
# # devided by 2 as concated 2 OI data
# SR1 = BN + float((BNCSPCLTP+BNCSPPLTP)/2)
# SS1 = BN - float((BNCSPCLTP+BNCSPPLTP)/2)


#Call 
BNCLTPH1 = df_banknifty.iloc[BNCH1OI_loc]['CallLTP']
BNCLTPH2 = df_banknifty.iloc[BNCH2OI_loc]['CallLTP']
BNCLTPSP = BNcurrentvalue('CallLTP')
        
# devided by 2 as concated 2 OI data
AvgBNCLTPH1 = (((BNCLTPH1+BNCLTPH2+BNCLTPSP )/3)/2)
#AvgBNCLTPH_UR = AvgBNCLTPH*1.15
#AvgBNCLTPH_LR = (AvgBNCLTPH - (AvgBNCLTPH*0.15))

AvgBNCLTPH = format(AvgBNCLTPH1,'.2f')

print('1.0 The Total avrage of High OI Call Option price is {} '.format(AvgBNCLTPH),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('1.1 Total avrage Call Option price Premium is {} '.format(format(df_banknifty['CallPremium'].mean(),'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('1.2 The Total avrage Call Option price is {} '.format(format(df_banknifty['CallLTP'].mean(),'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))


#Put
BNPLTPH1 = df_banknifty.iloc[BNPH1OI_loc]['PutLTP']
BNPLTPH2 = df_banknifty.iloc[BNPH2OI_loc]['PutLTP']
BNPLTPSP = BNcurrentvalue('PutLTP')
        
AvgBNPLTPH1 = (((BNPLTPH1+BNPLTPH2+BNPLTPSP )/3)/2)
#AvgBNPLTPH_UR = (AvgBNPLTPH*1.15)
#AvgBNPLTPH_LR = (AvgBNPLTPH - (AvgBNPLTPH*0.15))

AvgBNPLTPH = format(AvgBNPLTPH1,'.2f')

print('2.0 The Total avrage of High OI Put  Option price is {} '.format(AvgBNPLTPH),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('2.1 Total avrage Put Option price Premium is {} '.format(format(df_banknifty['PutPremium'].mean(),'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('2.2 The Total avrage Put Option price is {} '.format(format(df_banknifty['PutLTP'].mean(),'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))

print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))

# Avrage price stat 
SR1 = BN + AvgBNCLTPH1
SS1 = BN - AvgBNPLTPH1

SR11 = int(100 * round(float(SR1)/100)) # To convert the LTP to SP in multipal of 100
SS11 = int(100 * round(float(SS1)/100)) # To convert the LTP to SP in multipal of 100
print('**',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('BankNifty todays range is {} R1 & {} S1'.format(format(SR1,'.2f'),format(SS1,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('**',file=open("NIFTY_BankNifty_OI_data.txt", "a"))



#Append the Range in CSV file and write it to data frame with Simple print fuction use for append value 
print('BankNifty_OID,{},{},{},{},{},{}'.format(pdate,format(SS1,'.2f'),BNp,format(SR1,'.2f'),0,0),file=open("BN_Support_Resistance_data.csv", "a")) #Simple print fuction use for append value 


"""
#the Ideal Buy BankNifty CE or PE 
What is the current LTP and if the ideal ce or pe touch support then what is the LTP and if it touch resistance then what will be the LTP

# Current Ideal Buy BankNifty {} CE'.format(BNCE), Ideal Buy BankNifty {} PE'.format(BNPE)

if BNCE at SS1 or at SR1:
    then BNCE(CallLTP) =   

"""
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
#Ideal Buy Range for CALL or Put
print('#Ideal Buy Range for Call & Put',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))

# 0.5% stratergy to calculate the ITM & OTM value
BNpr = float(BNp)*0.0025
BN1d5 = int(100 * round(float(BNpr)/100))

BNCE= (BNp + BN1d5) 
BNPE= (BNp - BN1d5) 
print('1. Ideal Buy BankNifty {} CE'.format(BNCE),file=open("NIFTY_BankNifty_OI_data.txt", "a")) #Adjusting Ideal Buy lower to max OI
print('2. Ideal Buy BankNifty {} PE'.format(BNPE),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))

print('BankNifty Run ok') #for run issue finding


#Risk and rewards
#Call
BNCEntry = (SS11) #Call Spot SP
BNCSL = BNPH1OI_SP  #Support 2 CAll_SP derived from High Put_OI location
BNCTarget = BNCH1OI_SP #R1 as resistance
BNCRisk = (BNCEntry-BNCSL) ##Curent SP - Support 2 as stopLoss
BNCRewards = BNCTarget

#RR Cal
BNCRRn = BNCRewards / abs(BNCRisk)
BNCRR = format(BNCRRn,'.0f')

def BNcurrentvalue(Cname,SCSP):
    BNCurrentLOC = 0
    for BNCurrentLOC in range(len(df_banknifty)):
        if (df_banknifty['Strike Price'][(BNCurrentLOC)]) == SCSP:
            BNCurrentValue = df_banknifty.iloc[BNCurrentLOC][Cname]
    return BNCurrentValue

BNCELTPn = BNcurrentvalue('CallLTP',BNCE)
BNCELTP = BNCELTPn/2
ABNCELTPn = (BNCELTP+(BNCELTP*BNCRRn)/100)
ABNCELTP = format(ABNCELTPn,'.2f')
print('#{} SP {} Call AvgLTP {} If Entry is at {} then R:R is 1:{} & LTP will be {}'.format("BankNifty",BNCE,BNCELTP,BNCEntry,BNCRR,ABNCELTP),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
#print('',file=open("Stock_EQ_OI_data.txt", "a"))

#Put
BNPEntry = (SR11) #Put Spot SP
BNPSL = BNCH1OI_SP  #R1 CAll_SP derived from High Put_OI location
BNPTarget = BNPH1OI_SP  #S1
BNPRisk = (BNCEntry-BNPSL) ##Curent SP - Support 2 as stopLoss
BNPRewards = BNPTarget

## RR Cal
BNPRRn = BNPRewards / abs(BNPRisk)
BNPRR = format(BNPRRn,'.0f')

BNPELTPn = BNcurrentvalue('PutLTP',BNPE)
BNPELTP = BNPELTPn/2

ABNPELTPn = (BNPELTP+(BNPELTP*BNPRRn)/100)
ABNPELTP = format(ABNPELTPn,'.2f')
print('#{} SP {} Put AvgLTP {} If Entry is at {} then R:R is 1:{} & LTP will be {}'.format("BankNifty",BNPE,BNPELTP,BNPEntry,BNPRR,ABNPELTP),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
#print('',file=open("Stock_EQ_OI_data.txt", "a"))

#print('#the Put  If Entry is at {} then R:R is 1:{} '.format(BNPEntry,BNPRR),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))




##### Call OI & Call_OI_Change cross over Plot

#COLUMN_NAMES=['CallOI','Call_OI_Change','CallLTP','Strike Price','PutLTP','Put_OI_Change','PutOI']

# Taking -10 index valus of dataframe to +10 values from Current SP
BNSPN=(BNSPLOC-10)
BNSPP=(BNSPLOC+10)
df_bankniftyOI = df_banknifty.iloc[BNSPN:BNSPP,:]
               
# df_bankniftyOI.plot(x='Strike Price',y=['CallOI','Call_OI_Change'])
# df_bankniftyOI.plot(x='Strike Price',y=['PutOI','Put_OI_Change'])
# df_bankniftyOI.plot(x='Strike Price',y=['CallOI','PutOI'])
# df_bankniftyOI.plot(x='Strike Price',y=['Call_OI_Change','Put_OI_Change'])

#print('Bank Nifty Open Intrest Graph')

# BNLTP_PLOT = df_bankniftyOI.plot(x='Strike Price',y=['CallPremium','PutPremium'])
# BNOI_PLOT = df_bankniftyOI.plot(x='Strike Price',y=['CallOI','Call_OI_Change'])
# BNOI_PLOT = df_bankniftyOI.plot(x='Strike Price',y=['PutOI','Put_OI_Change'])
# plt.show()

#df_bankniftyOI['Strike Price'].plot.kde()


#######################################  NIFTY 50 ##################################################################
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('########',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('#Analysis for Nifty50 Option Data',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))

##Data Slicing for Nifty 50
#Dr_nifty50 = pd.read_excel('nifty.xlsx' , sheet_name='option-chain-equity-derivatives')

# Take 2 data CSV files for current week and next from NSE site 
Dr_nifty501 = pd.read_csv('nifty1.csv')
Dr_nifty502 = pd.read_csv('nifty2.csv')

#after  Remove the unwanted columns manulay on CSV file. 

# replace the string text
# replace the '-' value to zero & ccoma content number to float number 
Dr_nifty503 = Dr_nifty501.replace(to_replace = ['- ','-'], value =0)
Dr_nifty503= Dr_nifty503.replace('\,','', regex=True)
Dr_nifty504 = Dr_nifty502.replace(to_replace = ['- ','-'], value =0)
Dr_nifty504= Dr_nifty504.replace('\,','', regex=True)


#take required coulmns from above file
dr_nifty505 = Dr_nifty503.iloc[:,[0,1,4,10,16,19,20]]
dr_nifty506 = Dr_nifty504.iloc[:,[0,1,4,10,16,19,20]]


# set column name as per our choice
dr_nifty505.columns = COLUMN_NAMES
dr_nifty506.columns = COLUMN_NAMES

Df_nifty501  = []  # reSet the dataframe
#Combine dataframes 
Df_nifty501 = pd.concat((dr_nifty505,dr_nifty506)) 
Df_nifty501 = Df_nifty501.astype(float) # converting in to float

#Df_nifty501 = Df_nifty501.reset_index(drop = True) # Use if needed
#Df_nifty501 = Df_nifty501.replace(np.nan,0) # Use if needed

df_nifty50 = pd.pivot_table(data=Df_nifty501,index=['Strike Price'],aggfunc='sum') # Pivot table for adding the columns values
df_nifty50 = df_nifty50.reset_index()  # Adding the index numbers                             

df_nifty50 = df_nifty50.reindex(columns=COLUMN_NAMES)      # rearranging the values as per columans names                          
# df_nifty50.to_csv('df_nifty50_file.csv') # Use if needed

#Collect Higest and 2nd high Open intrest from call side

#Call values

NFCH1OI,NFCH2OI = df_nifty50['CallOI'].nlargest(2,keep='last')  #Returns a max and 2nd max values of OI
#NFCH1OIC,NFCH2OIC = df_nifty50['Call_OI_Change'].nlargest(2,keep='last')  #Returns a max and 2nd max values of Change in OI

NFCH1OIC = df_nifty50['Call_OI_Change'].nlargest(1,keep='last')  #Returns a max values of Change in OI
NFCH2OIC = df_nifty50['Call_OI_Change'].nsmallest(1,keep='last')  #Returns a min values of Change in OI


#Convert to Words for print only
NFCH1OI_Wd = format(NFCH1OI/10000,'.2f')
NFCH2OI_Wd = format(NFCH2OI/10000,'.2f')

NFCH1OIC_Wd = format(float(NFCH1OIC)/10000,'.2f')
NFCH2OIC_Wd = format(float(NFCH2OIC)/10000,'.2f')


#high OI location

NFCH1OI_loc,NFCH2OI_loc = df_nifty50['CallOI'].nlargest(2,keep='last').index #Returns location of a max and 2nd max values of OI
NFCH1OIC_loc,NFCH2OIC_loc = df_nifty50['Call_OI_Change'].nlargest(2,keep='last').index #Returns location of a max and 2nd max values of change in OI

##Collect Higest and 2nd high est Open intrest from Put side
#Put values

NFPH1OI,NFPH2OI = df_nifty50['PutOI'].nlargest(2,keep='last')  #Returns a max and 2nd max values
#NFPH1OIC,NFPH2OIC = df_nifty50['Put_OI_Change'].nlargest(2,keep='last')  #Returns a max and 2nd max values
NFPH1OIC = df_nifty50['Put_OI_Change'].nlargest(1,keep='last')  #Returns a max values
NFPH2OIC = df_nifty50['Put_OI_Change'].nsmallest(1,keep='last')  #Returns a min values


#Convert to Words for print only
NFPH1OI_Wd = format(NFPH1OI/10000,'.2f')
NFPH2OI_Wd = format(NFPH2OI/10000,'.2f')
NFPH1OIC_Wd = format(float(NFPH1OIC)/10000,'.2f')
NFPH2OIC_Wd = format(float(NFPH2OIC)/10000,'.2f')


#high OI location
NFPH1OI_loc,NFPH2OI_loc = df_nifty50['PutOI'].nlargest(2,keep='last').index #Returns location of a max and 2nd max values
NFPH1OIC_loc,NFPH2OIC_loc = df_nifty50['Put_OI_Change'].nlargest(2,keep='last').index #Returns location of a max and 2nd max values


##Calculate / data taken for the Strike price from Higest and 2nd high Open intrest from call and Put side
#Call
NFCH1OI_SP = df_nifty50.iloc[NFCH1OI_loc]['Strike Price'] #Returns a Strick price 
NFCH2OI_SP = df_nifty50.iloc[NFCH2OI_loc]['Strike Price'] #Returns a Strick price 
NFCH1OIC_SP = df_nifty50.iloc[NFCH1OIC_loc]['Strike Price'] #Returns a Strick price Change OI
NFCH2OIC_SP = df_nifty50.iloc[NFCH2OIC_loc]['Strike Price'] #Returns a Strick price Change OI


#Put
NFPH1OI_SP = df_nifty50.iloc[NFPH1OI_loc]['Strike Price'] #Returns a Strick price 
NFPH2OI_SP = df_nifty50.iloc[NFPH2OI_loc]['Strike Price'] #Returns a Strick price 
NFPH1OIC_SP = df_nifty50.iloc[NFPH1OIC_loc]['Strike Price'] #Returns a Strick price Change OI
NFPH2OIC_SP = df_nifty50.iloc[NFPH2OIC_loc]['Strike Price'] #Returns a Strick price Change OI


## Main Logic for PCR Data Analysis

print('#Nifty PCR Data Analysis',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
#Calculate the high  Put Call ratio (PCR)
NFHPCR = NFPH1OI/NFCH1OI
nfhpcr = format(NFHPCR,'.2f')
print('1. Nifty Higest Open Interest PCR ratio ',nfhpcr,file=open("NIFTY_BankNifty_OI_data.txt", "a"))

#Calculate the total Put Call ratio
NFCallOI_sum = df_nifty50['CallOI'].sum()  #Returns a sum of Call Open intrest values
NFPutOI_sum = df_nifty50['PutOI'].sum()  #Returns a sum of  Put Open intrest values
NFTPCR = NFPutOI_sum / NFCallOI_sum
TotalOI_NF1 = NFPutOI_sum + NFCallOI_sum
TotalOI_NF = format(TotalOI_NF1/10000,'.2f')
nftpcr = format(NFTPCR,'.2f')
print('2. Nifty Total  Open Interest is {} Lakh & PCR ratio {}'.format(TotalOI_NF,nftpcr),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))


#Calculate the total Put Call ratio of Change in OI
NFCallOI_sum_Change = df_nifty50['Call_OI_Change'].sum()  #Returns a sum of Call Open intrest values
NFPutOI_sum_Change = df_nifty50['Put_OI_Change'].sum()  #Returns a sum of  Put Open intrest values
NFTPCR_Change = NFPutOI_sum_Change / NFCallOI_sum_Change
TotalOI_NF1_Change = NFPutOI_sum_Change + NFCallOI_sum_Change
TotalOI_NF_Change = format(TotalOI_NF1_Change/10000,'.2f')
nftpcr_Change = format(NFTPCR_Change,'.2f')
print('3. Nifty Total Change in Open Interest is {} Lakh & PCR ratio {}'.format(TotalOI_NF_Change,nftpcr_Change),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))


#Rising and Falling PCR data analysis. 

# #Append the high PCR value in CSV file and write it to data frame
# print(nfhpcr,file=open("NF_Option_data.csv", "a")) #Simple print fuction use for append value 
# Dr_NFPCR_list = pd.read_csv('NF_Option_data.csv')
# df_NFPCR_list = pd.DataFrame(data=Dr_NFPCR_list)

# #find the persent change in NF HPCR
# NFPCR_PC = (100 * ((df_NFPCR_list.iloc[-1] - df_NFPCR_list.iloc[-2]) / df_NFPCR_list.iloc[-2])) 

#Analysis

if  float(NFTPCR) < 0.5:
    print("#Over purchased Call Options",file=open("NIFTY_BankNifty_OI_data.txt", "a"))
    print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
if  float(NFTPCR) > 1.5:
    print("#Over purchased Put Options",file=open("NIFTY_BankNifty_OI_data.txt", "a"))
    print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))

if  float(NFTPCR) > 1 :
    print('The Resistance Base on PCR is: ',NFCH1OI_SP,file=open("NIFTY_BankNifty_OI_data.txt", "a"))
    #SP of the High OI in calls # It act as a resistance
    
if  float(NFTPCR) < 1 :
    print('The Support Base on PCR is: ',NFPH1OI_SP,file=open("NIFTY_BankNifty_OI_data.txt", "a"))
    #SP of the High OI in put  # it act as a support
    

print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))


##Open Interest Analysis 

#Find the Call_OI & Put_OI for current NF50 Strick price 
# Caclucating the Location of SP in index

def NFcurrentvalue(NFCname):
    NFCurrentLOC = 0
    for NFCurrentLOC in range(len(df_nifty50)):
        if (df_nifty50['Strike Price'][(NFCurrentLOC)]) == N50p:
            NFCurrentValue = df_nifty50.iloc[NFCurrentLOC][NFCname]
            NFSPLOC  = NFCurrentLOC
    return NFCurrentValue


NFCSPCOI = NFcurrentvalue('CallOI')
NFCSPPOI = NFcurrentvalue('PutOI')
NFCSPCLTP = NFcurrentvalue('CallLTP')
NFCSPPLTP = NFcurrentvalue('PutLTP')

#Convert to Words for print only
NFCSPCOI_Wd = format(NFCSPCOI/10000,'.2f')
NFCSPPOI_Wd = format(NFCSPPOI/10000,'.2f')


##Premium  calculation: SP LTP / Current SP LTP
df_nifty50['CallPremium'] = (df_nifty50.CallLTP/NFCSPCLTP)
df_nifty50['PutPremium'] = (df_nifty50.PutLTP/NFCSPPLTP)

# rearranging the values as per columans names
df_nifty50 = df_nifty50.reindex(columns=COLUMN_NAMES_Rev)      

# Values of Premium 

NFCH1OI_Pr = df_nifty50.iloc[NFCH1OI_loc]['CallPremium'] #Returns a CallPremium  
NFCH2OI_Pr = df_nifty50.iloc[NFCH2OI_loc]['CallPremium'] #Returns a CallPremium
NFCH1OI_COIn = df_nifty50.iloc[NFCH1OI_loc]['Call_OI_Change'] #Returns a Chnage OI  
NFCH2OI_COIn = df_nifty50.iloc[NFCH2OI_loc]['Call_OI_Change'] #Returns a Chnage OI
#Convert to Words for print only
NFCH1OI_COI = format(NFCH1OI_COIn/10000,'.2f')
NFCH2OI_COI = format(NFCH2OI_COIn/10000,'.2f')
NFCH1OIC_Pr = df_nifty50.iloc[NFCH1OIC_loc]['CallPremium'] #Returns a CallPremium Change OI
NFCH2OIC_Pr = df_nifty50.iloc[NFCH2OIC_loc]['CallPremium'] #Returns a CallPremium Change OI
NFPH1OI_Pr = df_nifty50.iloc[NFPH1OI_loc]['PutPremium'] #Returns a PutPremium
NFPH2OI_Pr = df_nifty50.iloc[NFPH2OI_loc]['PutPremium'] #Returns a PutPremium 
NFPH1OI_COIn = df_nifty50.iloc[NFPH1OI_loc]['Put_OI_Change'] #Returns a PutPremium
NFPH2OI_COIn = df_nifty50.iloc[NFPH2OI_loc]['Put_OI_Change'] #Returns a PutPremium 
#Convert to Words for print only
NFPH1OI_COI = format(NFPH1OI_COIn/10000,'.2f')
NFPH2OI_COI = format(NFPH2OI_COIn/10000,'.2f')
NFPH1OIC_Pr = df_nifty50.iloc[NFPH1OIC_loc]['PutPremium'] #Returns a PutPremium Change OI
NFPH2OIC_Pr = df_nifty50.iloc[NFPH2OIC_loc]['PutPremium'] #Returns a PutPremium Change OI


#Main Logic Nifty to print the open intrest and Strike Price
print('#high Open Interest with STRIKE PRICE',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('#Nifty 50 have {} Lakh Call_OI & {} Lakh Put_OI for Current SP {}'.format(NFCSPCOI_Wd,NFCSPPOI_Wd,n50f),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('1. Max high {} Lakh Call_OI & {} Change OI at SP {} OIR2 with Premium {}%'.format(NFCH1OI_Wd,NFCH1OI_COI,NFCH1OI_SP,format(NFCH1OI_Pr,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('2. 2nd high {} Lakh Call_OI & {} Change OI at SP {} OIR1 with Premium {}%'.format(NFCH2OI_Wd,NFCH2OI_COI,NFCH2OI_SP,format(NFCH2OI_Pr,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('3. Max high {} Lakh Put_OI  & {} Change OI at SP {} OIS2 with Premium {}%'.format(NFPH1OI_Wd,NFPH1OI_COI,NFPH1OI_SP,format(NFPH1OI_Pr,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('4. 2nd high {} Lakh Put_OI  & {} Change OI at SP {} OIS1 with Premium {}%'.format(NFPH2OI_Wd,NFPH2OI_COI,NFPH2OI_SP,format(NFPH2OI_Pr,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('')
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))


print('#Change in Open Interest Added & Left ',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('1. {}  Lakh Call_OI_Change added at  SP {} with Premium {}%'.format(NFCH1OIC_Wd,NFCH1OIC_SP,format(NFCH1OIC_Pr,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('2. {} Lakh Call_OI_Change  left  at  SP {} with Premium {}%'.format(NFCH2OIC_Wd,NFCH2OIC_SP,format(NFCH2OIC_Pr,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('3. {}  Lakh Put_OI_Change  added at  SP {} with Premium {}%'.format(NFPH1OIC_Wd,NFPH1OIC_SP,format(NFPH1OIC_Pr,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('4. {} Lakh Put_OI_Change   left  at  SP {} with Premium {}%'.format(NFPH2OIC_Wd,NFPH2OIC_SP,format(NFPH2OIC_Pr,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))

print('')
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))



#Main logic for direction of SP to neareset SP (Direction prediction)
NTCOI_list = [NFCH1OI,NFCH2OI]
NTPOI_list = [NFPH1OI,NFPH2OI]
NR_SP = []


def closestn(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]
 
  
#Driver code 
#for Call_OI
if (closestn(NTCOI_list, NFCH1OI)) == NFCH1OI:  #compare the closest OI 
    NR_SP.append(NFCH1OI_SP)
elif (closestn(NTCOI_list, NFCSPCOI)) == NFCH2OI:  
    NR_SP.append(NFCH2OI_SP)

#for Put_OI    
if (closestn(NTPOI_list, NFCSPPOI)) == NFPH1OI: #compare the closest OI
    NR_SP.append(NFPH1OI_SP)
elif (closestn(NTPOI_list, NFCSPPOI)) == NFPH2OI:
    NR_SP.append(NFPH2OI_SP)


if (NR_SP[0] - N50p) == (N50p - NR_SP[1]) :
    print('#Probability base on OI Diffrance : The price will Consolidated near SP',(closestn(NR_SP, N50p)),file=open("NIFTY_BankNifty_OI_data.txt", "a"))  #compare the closest SP 
else:#for strick price     
    print('#Probability base on OI Diffrance : The price will move in direction of SP ',(closestn(NR_SP, N50p)),file=open("NIFTY_BankNifty_OI_data.txt", "a"))  #compare the closest SP 

    

print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))

#Find the Call_OI & Put_OI for Probability base direction of NF50 Strick price 
DN50p = (closestn(NR_SP, N50p))

def DNFcurrentvalue(DNFCname):
    DNFCurrentLOC = 0
    for DNFCurrentLOC in range(len(df_nifty50)):
        if (df_nifty50['Strike Price'][(DNFCurrentLOC)]) == DN50p:
            DNFCurrentValue = df_nifty50.iloc[DNFCurrentLOC][DNFCname]
    return DNFCurrentValue


DNFCSPCOI = DNFcurrentvalue('CallOI')
DNFCSPPOI = DNFcurrentvalue('PutOI')
DNFCSPPCOI = DNFcurrentvalue('Call_OI_Change')
DNFPSPPCOI = DNFcurrentvalue('Put_OI_Change')

#Convert to Words for print only
DNFCSPCOI_Wd = format(DNFCSPCOI/10000,'.2f')
DNFCSPPOI_Wd = format(DNFCSPPOI/10000,'.2f')
DNFCSPPCOI_Wd = format(DNFCSPPCOI/10000,'.2f')
DNFPSPPCOI_Wd = format(DNFPSPPCOI/10000,'.2f')


print('{} Lakh Call_OI \n{} Lakh Put_OI \n{} Lakh Call_OI_Change \n{} Lakh Put_OI_Change \n'.format(DNFCSPCOI_Wd,DNFCSPPOI_Wd,DNFCSPPCOI_Wd,DNFPSPPCOI_Wd ),file=open("NIFTY_BankNifty_OI_data.txt", "a")) #"NIFTY_BankNifty_OI_data.txt" file

print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))

##Average trading price 
#avrage of 2 High OI Strick price LTP & Current Strick price LTP  and ~15%  range of tollarance (Self dev formula)
##Need Back test
print('#Nifty 50 Total average Option price',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))

#Call high OI price location and LTP
NFCLTPH1 = df_nifty50.iloc[NFCH1OI_loc]['CallLTP']
NFCLTPH2 = df_nifty50.iloc[NFCH2OI_loc]['CallLTP']

NFCLTPSP = NFcurrentvalue('CallLTP')
        
# devided by 2 as concated 2 OI data
AvgNFCLTPH1 = (((NFCLTPH1+NFCLTPH2+NFCLTPSP )/3)/2)
#AvgNFCLTPH_UR = AvgNFCLTPH*1.15
#AvgNFCLTPH_LR = (AvgNFCLTPH - (AvgNFCLTPH*0.15))
AvgNFCLTPH = format(AvgNFCLTPH1,'.2f')
print('1. The Total avrage of High OI  Call Option price is {} '.format(AvgNFCLTPH),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('1.1 Total avrage Call Option price Premium is {} '.format(format(df_nifty50['CallPremium'].mean(),'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('1.2 The Total avrage Call Option price is {} '.format(format(df_nifty50['CallLTP'].mean(),'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))

print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
#Put high open price location and LTP
NFPLTPH1 = df_nifty50.iloc[NFPH1OI_loc]['PutLTP']
NFPLTPH2 = df_nifty50.iloc[NFPH2OI_loc]['PutLTP']
NFPLTPSP = NFcurrentvalue('PutLTP')
        
AvgNFPLTPH1 = (((NFPLTPH1+NFPLTPH2+NFPLTPSP )/3)/2)
#AvgNFPLTPH_UR = AvgNFPLTPH*1.15
#AvgNFPLTPH_LR = (AvgNFPLTPH - (AvgNFPLTPH*0.15))
AvgNFPLTPH = format(AvgNFPLTPH1,'.2f')
print('2. The Total avrage of High OI Put  Option price is {} '.format(AvgNFPLTPH),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('2.1 Total avrage Put Option price Premium is {} '.format(format(df_nifty50['PutPremium'].mean(),'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('2.2 The Total avrage Put Option price is {} '.format(format(df_nifty50['PutLTP'].mean(),'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))

print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))

#To find range Range
#Stradel price

#LTP + (ATM_SP CE price + ATM_SP PE price) 
#LTP - (ATM_SP CE price + ATM_SP PE price)
# devided by 2 as concated 2 OI data
# NFSR1 = N50 + float((NFCSPCLTP+NFCSPPLTP)/2)
# NFSS1 = N50 - float((NFCSPCLTP+NFCSPPLTP)/2)
#print('Stradel price: ',float((NFCSPCLTP+NFCSPPLTP)/2))#,file=open("NIFTY_BankNifty_OI_data.txt", "a"))

# Avg price stat
NFSR1 = N50 + AvgNFCLTPH1
NFSS1 = N50 - AvgNFPLTPH1
NFSR11 = int(50 * round(float(NFSR1)/50))
NFSS11 = int(50 * round(float(NFSS1)/50))

print('For Nifty50 todays range is {} R1 & {} S1'.format(format(NFSR1,'.2f'),format(NFSS1,'.2f')),file=open("NIFTY_BankNifty_OI_data.txt", "a"))


#Append the Range in CSV file and write it to data frame
print('Nifty_OID,{},{},{},{},{},{}'.format(pdate,format(NFSS1,'.2f'),N50p,format(NFSR1,'.2f'),0,0),file=open("NF_Support_Resistance_data.csv", "a")) #Simple print fuction use for append value 
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))


##Price prediction 

#Ideal Buy Range for CALL or PUT
print('#Ideal Buy Range for CALL and PUT',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))

# 0.5% stratergy to calculate the ITM value
NFpr = float(N50p)*0.005
NF1d5 = int(50 * round(float(NFpr)/50))

NCE= (N50p+NF1d5)
NPE= (N50p-NF1d5)

## P&L = SP - SpotP - SpotLTP
## Break Even BE = SP - (Premium+Brokrage)

print('1. Ideal Buy Nifty {} CE'.format(NCE),file=open("NIFTY_BankNifty_OI_data.txt", "a")) #Adjusting Ideal Buy lower to max OI

print('2. Ideal Buy Nifty {} PE'.format(NPE),file=open("NIFTY_BankNifty_OI_data.txt", "a"))

print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))


#Risk and rewards
#Call
NFCEntry = NFSS11 #Call Spot SP
NFCSL = NFPH1OI_SP  #Support 1 CAll_SP derived from High Put_OI location
NFCTarget = NFCH1OI_SP #R1 as resistance
NFCRisk = (NFCEntry-NFCSL) ##Curent SP - Support 2 as stopLoss
NFCRewards = NFCTarget

NFCRRn = NFCRewards / abs(NFCRisk)
NFCRR = format(NFCRRn,'.0f')

def NFcurrentvalue(Cname,SCSP):
    NFCurrentLOC = 0
    for NFCurrentLOC in range(len(df_nifty50)):
        if (df_nifty50['Strike Price'][(NFCurrentLOC)]) == SCSP:
            NFCurrentValue = df_nifty50.iloc[NFCurrentLOC][Cname]
    return NFCurrentValue

NFCELTPn = NFcurrentvalue('CallLTP',NCE)
NFCELTP = NFCELTPn/2

ANFCELTPn = (NFCELTP+(NFCELTP*NFCRRn)/100)
ANFCELTP = format(ANFCELTPn,'.2f')
print('#{} SP {} Call AvgLTP {} If Entry is at {} then R:R is 1:{} & LTP will be {}'.format("Nifty50",NCE,NFCELTP,NFCEntry,NFCRR,ANFCELTP),file=open("NIFTY_BankNifty_OI_data.txt", "a"))

#print('#the Call If Entry is at {} then R:R is 1:{}'.format(NFCEntry,NFCRR),file=open("NIFTY_BankNifty_OI_data.txt", "a"))

#Put
NFPEntry = (NFSR11) #Put Spot SP
NFPSL = NFCH1OI_SP  #R1 CAll_SP derived from High Put_OI location
NFPTarget = NFPH1OI_SP  #S1
NFPRisk = (NFCEntry-NFPSL) ##Curent SP - Support 2 as stopLoss
NFPRewards = NFPTarget
NFPRRn = NFPRewards / abs(NFPRisk)
NFPRR = format(NFPRRn,'.0f')
NFPELTPn = NFcurrentvalue('PutLTP',NPE)
NFPELTP = NFPELTPn/2
ANFPELTPn = (NFPELTP+(NFPELTP*NFPRRn)/100)
ANFPELTP = format(ANFPELTPn,'.2f')
print('#{} SP {} Put  AvgLTP {} If Entry is at {} then R:R is 1:{} & LTP will be {}'.format("Nifty50",NPE,NFPELTP,NFPEntry,NFPRR,ANFPELTP),file=open("NIFTY_BankNifty_OI_data.txt", "a"))

#print('#For the Put  If Entry is at {} then R:R is 1:{} '.format(NFPEntry,NFPRR),file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('',file=open("NIFTY_BankNifty_OI_data.txt", "a"))
print('')
print('Nifty  50  Run ok')


# Call OI & Call_OI_Change cross over Plot

# Taking -10 index valus of dataframe to +10 values from Current SP

NFSPLOC = 0
for NFCSPLOC in range(len(df_nifty50)):
    if (df_nifty50['Strike Price'][(NFCSPLOC)]) == N50p:
        NFSPLOC = NFCSPLOC

NFSPN=(NFSPLOC-10)
NFSPP=(NFSPLOC+10)

df_niftyOI = df_nifty50.iloc[NFSPN:NFSPP,:]


# print('Nifty 50 Open Intrest Graph')
# NFLTP_PLOT = df_niftyOI.plot(x='Strike Price',y=['CallLTP','PutLTP'])
# NFOI_PLOT = df_niftyOI.plot(x='Strike Price',y=['CallOI','Call_OI_Change'])
# NFOI_PLOT = df_niftyOI.plot(x='Strike Price',y=['PutOI','Put_OI_Change'])
# plt.show()

print('')
print('End of the BOT')
print('End of the BOT',file=open("NIFTY_BankNifty_OI_data.txt", "a"))


# Seller Ststes:



############################################## End Program #########################################

"""

back test:
Price action: 
how many high touch R line
Volume factor
recent touch
how many low touch S line

"""

