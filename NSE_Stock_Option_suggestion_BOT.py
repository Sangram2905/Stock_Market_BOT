# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:53:55 2020

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
​s
Time Value=Option Price−Intrinsic Value
	
"""
# Importing the libraries
import numpy as np
import pandas as pd
import datetime
from nsetools import Nse
import math
import os
import sys
from pprint import pprint # just for neatness of display
from datetime import datetime
print('####################################################################',file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
print('')#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull start time




print('Start data pull for Stock Options from NSE server at time ',starttime,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))

# Importing the NIFTY dataset from NSE live site / portel 
nse = Nse()  # NSE object creation

day = datetime.now().strftime("%A")
daydate = datetime.now().strftime("%d")


if day == str('Thursday'):
    if int(daydate) >=24:
        print('Today is Monthly option expiry day : Carefully trade todays expiry day Call or Put options')#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
        
    
####https://www.nseindia.com/json/option-chain/option-chain.json


#print (nse)

#Creating data frame for Option lotsize and there Rs. 1000 to Rs. 5000 price

 
dr_lotsize = pd.read_csv('FnO_lotsizelist.csv',index_col = 'symbols')
df_lotsize = pd.DataFrame(data=dr_lotsize)


dr_lotmoney = pd.read_csv('FnO_lotsizelist_fund_sector_filter.csv',index_col = 'symbols')
df_lotmoney = pd.DataFrame(data=dr_lotmoney)

# all FnO stock EQ list and day high and low

#fnogsw = nse.get_fno_sec_stock()

#Extract Data from lists pull from NSE

"""
## For Lot size data
#fnolotsize = nse.get_fno_lot_sizes()
#df_fnolotsizelist = pd.DataFrame(fnolotsize.items(),columns=['symbols','lotSize']).set_index('symbols')
#df_fnolotsizelist.to_csv('FnO_lotsizelist.csv')
#df_fnolotsizelist.replace({None: 0.5}, inplace=True)

"""

# NSE FNO data

# Simple list for FnO Todays Top gainers 

fnogainers = nse.get_top_fno_gainers()

fnogainerslist=[]

for index in range(len(fnogainers)):
    for key in fnogainers[index]:
        if key == 'symbol':
            #retrive each value
            fnogainersns = fnogainers[index]['symbol']
            fnogainersltp = fnogainers[index]['ltp']
            fnogainerspc = fnogainers[index]['netPrice']
            #appended values
            fnogainerslist.append([fnogainersns,fnogainersltp,fnogainerspc])
    
df_fnogainerslist = pd.DataFrame(fnogainerslist,columns=['symbol','LTP','percent change'] )        
df_fnogainerslist = pd.DataFrame(df_fnogainerslist).set_index('symbol')
#df_fnogainerslist.replace({None: 0.5}, inplace=True)
df_fnogainerslist.sort_values("percent change", axis = 0, ascending = False,inplace = True, na_position ='last')
df_fnogainerslist_sort = df_fnogainerslist.iloc[0:7]
df_fnogainerslist_sort.sort_values("symbol", axis = 0, ascending = True,inplace = True, na_position ='last')

#print("Todays Top 3 FnO gainers Stock details  \n",df_fnogainerslist_sort)#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
#print("df_fnogainerslist created")

## Comaring to the Dataframe of lotsize with fno & equity Todays Top gainers & losers and function intersect retrive the list as follows

##FnO Todays Top 5 Gainers

fnogainers_inx = np.intersect1d(df_fnogainerslist_sort.index,df_lotsize.index)
#print (fnogainers_inx)
df_fnogainers_inx = df_lotsize.loc[fnogainers_inx]
df_fnogainers_inx.sort_values("symbols", axis = 0, ascending = True,inplace = True, na_position ='last')

#print("Todays Top 3 FnO gainers Lot size \n",df_fnogainers_inx[0:])#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
#print('')

df_fnogainers_join = pd.concat([df_fnogainers_inx,df_fnogainerslist_sort], axis=1, join='inner')
#print("Todays Top 3 FnO gainers with Lot size \n",df_fnogainers_join[0:])#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))


# NSE Equity data
# Simple list for Equity Todays Top gainers

eqgainers = nse.get_top_gainers()

eqgainerslist=[]

for index in range(len(eqgainers)):
    for key in eqgainers[index]:
        if key == 'symbol':
            #retrive each value
            eqgainersns = eqgainers[index]['symbol']
            eqgainersltp = eqgainers[index]['ltp']
            eqgainerspc = eqgainers[index]['netPrice']
            #appended values
            eqgainerslist.append([eqgainersns,eqgainersltp,eqgainerspc])
    
df_eqgainerslist = pd.DataFrame(eqgainerslist,columns=['symbol','LTP','percent change'] )        
df_eqgainerslist = pd.DataFrame(df_eqgainerslist).set_index('symbol')
df_eqgainerslist.sort_values("percent change", axis = 0, ascending = False,inplace = True, na_position ='last')
df_eqgainerslist_sort = df_eqgainerslist[0:]
df_eqgainerslist_sort.sort_values("symbol", axis = 0, ascending = True,inplace = True, na_position ='last')

#df_eqgainerslist.replace({None: 0.5}, inplace=True)
#print("Todays Top Equity gainer \n", df_eqgainerslist_sort[0:])#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
#print("df_eqgainerslist created")


## Compare the FnO Todays Top gainers with equity gainers

fno_eq_gainers = np.intersect1d(df_fnogainerslist_sort.index,df_eqgainerslist_sort.index)
#print (fno_eq_gainers)
df_eq_fno_gainers = df_eqgainerslist_sort.loc[fno_eq_gainers]
df_eq_fno_gainers.sort_values("symbol", axis = 0, ascending = True,inplace = True, na_position ='last')

#if len(df_eq_fno_gainers)>0:
#    print("Todays Top Equity compare to FnO gainers stock details \n",df_eq_fno_gainers[0:])#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))

eqfnogainers_inx = np.intersect1d(df_eq_fno_gainers.index,df_lotsize.index)
#print (fnogainers_inx)
df_lotsize_eqfnogainers_inx = df_lotsize.loc[eqfnogainers_inx]

#if len(df_lotsize_eqfnogainers_inx)>0:
#    print("Todays Top Equity compare to FnO gainers with Lot size \n",df_lotsize_eqfnogainers_inx[0:])#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
#print('')


if len(df_lotsize_eqfnogainers_inx)>0:
    df_eqfnogainers_join = pd.concat([df_lotsize_eqfnogainers_inx,df_eqgainerslist_sort], axis=1, join='inner')
    #print("Todays Top Equity Compareto FnO gainers with Lot size \n",df_eqfnogainers_join[0:])#)#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))


##################################### Losers ##################################

# Simple list for FnO Todays Top losers  
fnolosers = nse.get_top_fno_losers()

fnoloserslist=[]

for index in range(len(fnolosers)):
    for key in fnolosers[index]:
        if key == 'symbol':
            #retrive each value
            fnolosersns = fnolosers[index]['symbol']
            fnolosersltp = fnolosers[index]['ltp']
            fnoloserspc = fnolosers[index]['netPrice']
            #appended values
            fnoloserslist.append([fnolosersns,fnolosersltp,fnoloserspc])
    
df_fnoloserslist = pd.DataFrame(fnoloserslist,columns=['symbol','LTP','percent change'] )        
df_fnoloserslist = pd.DataFrame(df_fnoloserslist).set_index('symbol')
#df_fnoloserslist.replace({None: 0.5}, inplace=True)
df_fnoloserslist.sort_values("percent change", axis = 0, ascending = False,inplace = True, na_position ='last')
df_fnoloserslist_sort = df_fnoloserslist[0:7]
df_fnoloserslist_sort.sort_values("symbol", axis = 0, ascending = True,inplace = True, na_position ='last')

#print("Todays Top 3 FnO Losers Stock details \n",df_fnoloserslist_sort)#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
#print("df_fnoloserslist created")


##FnO Todays Top 5 Losers

fnolosers_inx = np.intersect1d(df_fnoloserslist_sort.index,df_lotsize.index)
#print (fnolosers_inx)
#df_fnolosers_inx = df_fnoloserslist.loc[fnolosers_inx] 

df_lotsize_fnolosers_inx = df_lotsize.loc[fnolosers_inx]
df_lotsize_fnolosers_inx.sort_values("symbols", axis = 0, ascending = True,inplace = True, na_position ='last')

#print("Todays Top 3 FnO Losers Lot size \n",df_lotsize_fnolosers_inx[0:])#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
#print('')


df_fnolosers_join = pd.concat([df_lotsize_fnolosers_inx,df_fnoloserslist_sort], axis=1, join='inner')
#print("Todays Top 3 FnO Losers with Lot size \n",df_fnolosers_join[0:])#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))



### Simple list for equity Todays Top losers

eqlosers = nse.get_top_losers()
 
eqloserslist=[]

for index in range(len(eqlosers)):
    for key in eqlosers[index]:
        if key == 'symbol':
            #retrive each value
            eqlosersns = eqlosers[index]['symbol']
            eqlosersltp = eqlosers[index]['ltp']
            eqloserspc = eqlosers[index]['netPrice']
            #appended values
            eqloserslist.append([eqlosersns,eqlosersltp,eqloserspc])
    
df_eqloserslist = pd.DataFrame(eqloserslist,columns=['symbol','LTP','percent change'] )        
df_eqloserslist = pd.DataFrame(df_eqloserslist).set_index('symbol')
#df_eqgainerslist.replace({None: 0.5}, inplace=True)
df_eqloserslist.sort_values("percent change", axis = 0, ascending = False,inplace = True, na_position ='last')
df_eqloserslist_sort = df_eqloserslist[0:]
df_eqloserslist_sort.sort_values("symbol", axis = 0, ascending = True,inplace = True, na_position ='last')
#print("Todays Top Equity losers \n", df_eqloserslist_sort[0:])#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
#print("df_eqloserslist created")
#print('')

## Compare the FnO Todays Top Losers with equity Losers

fno_eq_losers = np.intersect1d(df_fnoloserslist.index,df_eqloserslist.index)
#print (fno_eq_losers)
df_eq_fno_losers = df_eqloserslist.loc[fno_eq_losers]
df_eq_fno_losers.sort_values("symbol", axis = 0, ascending = True,inplace = True, na_position ='last')

#if len(df_eq_fno_losers) >0:
 #   print("Todays Top Equity compare to FnO losers \n",df_eq_fno_losers[0:])#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))

eqfnolosers_inx = np.intersect1d(df_eq_fno_losers.index,df_lotsize.index)
#print (fnolosers_inx)
df_lotsize_eqfnolosers_inx = df_lotsize.loc[eqfnolosers_inx]
df_lotsize_eqfnolosers_inx.sort_values("symbols", axis = 0, ascending = True,inplace = True, na_position ='last')
#if len(df_lotsize_eqfnolosers_inx) >0:
 #   print("Todays Top Equity compare to FnO losers with Lot size \n",df_lotsize_eqfnolosers_inx[0:])#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
#print('')



if len(df_lotsize_eqfnolosers_inx)>0:
    df_eqfnolosers_join = pd.concat([df_lotsize_eqfnolosers_inx,df_eqloserslist_sort], axis=1, join='inner')
    #print("Todays Top equity compare to FnO losers with Lot size \n",df_eqfnolosers_join[0:])#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))





####################################### Main Logic ########################################


print("")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
       
# nf_n50 = nse.get_index_quote("nifty 50") 
# print('NIFTY 50 index current value is {} and percent change is {} '.format(nf_n50['lastPrice'],nf_n50['pChange']))#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a")) 
# print("")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))

# nf_indiavix = nse.get_index_quote("INDIA VIX") 
# print('INDIA VIX  index current value is {} and percent change is {} '.format(nf_indiavix['lastPrice'],nf_indiavix['pChange'])) 


# nf_nxt50 = nse.get_index_quote("NIFTY NEXT 50") 
# print('NIFTY Next 50  index current value is {} and percent change is {} '.format(nf_nxt50['lastPrice'],nf_nxt50['pChange'],'.2f')) 


"""
    
#Reseting the counters
fl = 0
fg = 0
eg = 0

if float(nf_n50['pChange']) >= 0.05:
    print("Todays BUY CALLs from FnO Top Gainer Stock list")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
    print("")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
    for fg in range(len (df_fnogainers_join)):
        print("{} lotsize {} & above strike_price {}".format(df_fnogainers_join.index[fg],df_fnogainers_join.iloc[fg][0],df_fnogainers_join.iloc[fg][1]))#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
    print("")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
    if len(df_lotsize_eqfnogainers_inx)>0:
        print("Todays BUY CALLs from Equity Top Gainer Stock list")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
        print("")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
        for eg in range(len(df_lotsize_eqfnogainers_inx)):
            print("{} lotsize {} & above strike_price {}".format(df_eqfnogainers_join.index[eg],df_eqfnogainers_join.iloc[eg][0],df_eqfnogainers_join.iloc[eg][1]))#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
    print("")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
    print("Todays BUY PUTs from FnO Top Loser Stock list")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
    print("")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
    for fl in range(len(df_fnolosers_join)):
        print("{} lotsize {} & below strike_price {}".format(df_fnolosers_join.index[fl],df_fnolosers_join.iloc[fl][0],df_fnolosers_join.iloc[fl][1]))#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
    print("")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))    
    

#Reseting the counters
fl = 0
el = 0
fg = 0    
if float(nf_n50['pChange']) <= -0.05:
    print("Todays BUY PUTs  from FnO Top Loser Stock list")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
    print("")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
    for fl in range(len(df_fnolosers_join)):
        print("{} lotsize {} & below strike_price {}".format(df_fnolosers_join.index[fl],df_fnolosers_join.iloc[fl][0],df_fnolosers_join.iloc[fl][1]))#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
    print("")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))    
    if len(df_lotsize_eqfnolosers_inx)>0:
        print("Todays BUY PUT from Equity Top Loser Stock list")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
        print("")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
        for el in range(len(df_lotsize_eqfnolosers_inx)):
            print("{} lotsize {} & below strike_price {}".format(df_eqfnolosers_join.index[el],df_eqfnolosers_join.iloc[el][0],df_eqfnolosers_join.iloc[el][1]))#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
    print("")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
    print("Todays BUY CALLs from FnO Top Gainer Stock list")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
    print("")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
    for fg in range(len (df_fnogainers_join)):
        print("{} lotsize {} & above strike_price {}".format(df_fnogainers_join.index[fg],df_fnogainers_join.iloc[fg][0],df_fnogainers_join.iloc[fg][1]))#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
   

"""

# For risk money 
#rm = float(input('Enteryour Risk money'))
#rmd = rm/3

rmd = 2000
if rmd >=2000:
    rmc = 2

print('')
df=0
fl=0
for df in range(len(df_lotmoney)):
    if (df_lotmoney.index[df] in df_fnolosers_join.index[0:]):
        for fl in range(len(df_fnolosers_join)):
            if (df_lotmoney.index[df] == df_fnolosers_join.index[fl]):
                print("PE {} below_SP {} at price {}".format(df_lotmoney.index[df],format(((df_fnolosers_join.iloc[fl][1])-((df_fnolosers_join.iloc[fl][1])*0.1)),'.2f'),df_lotmoney.iloc[df][rmc]),file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))

print('')
df=0
fg=0                
for df in range(len(df_lotmoney)):
    if (df_lotmoney.index[df] in df_fnogainers_join.index[0:]):
        for fg in range(len (df_fnogainers_join)):
            if (df_lotmoney.index[df] == df_fnogainers_join.index[fg]):
                print("CE {} above_SP {} at price {}".format(df_lotmoney.index[df],format(((df_fnogainers_join.iloc[fg][1])*1.1),'.2f'),df_lotmoney.iloc[df][rmc]),file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
                
                
               


# ## Event of FnO companys 
# ### Update the BSE file on month to month

# print('List of FnO company have upcoming Event: Expected Earning Release in next 7 days')#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))                
# print("")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
# dr_event = pd.read_csv('BSE Result for jul to aug 2020.csv',index_col='symbol')
# df_event = pd.DataFrame(data = dr_event)
# df_lotmoney = pd.DataFrame(data=dr_lotmoney)

# print('')
# de=0   
# fe=0             
# for de in range(len(df_event)):
#     for fe in range(len (df_lotmoney)):
#         if (df_lotmoney.index[fe] == df_event.index[de]):
#             if ((int(df_event.iloc[de][1][0:2])) >= int(daydate)) and ((int(df_event.iloc[de][1][0:2])) <= int(daydate)+7):
#                 print('For {} release on {} \n'.format(df_event.index[de],df_event.iloc[de][1]))#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))
               
        
endtime = datetime.now().strftime("%H:%M") #program data pull end time
bot_endtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("")#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))

print('End of data pull from NSE at time ',endtime)#,file=open("NSE_FnO_Todays_ Top_G_L.txt", "a"))

print('End of BOT Read text file "NSE_FnO_Todays_ Top_G_L.txt" for results generated / saved at same folder as prrogram')






"""
Main logic.

Strategy 1

1] get the data feom server of option with respect to current month & current strike_price for booth CE & PE
2] compare to the above tables and get the appropeate in  symbol for day trade for buget     
3] roundup the current symbol ltp for camparing 2nd point
4] search the symbol and option price of strike_price in df_lotsizeeq if found then return the result
    

#Buying strategy

1] first check nifty futures if first 10 min candels is green / bullish the go to buy
2] then go and check the Todays Top gainers
3] buy 2 Todays Top gainers stocks call @9:25 
    3.1] select call above 2% of current stock price as strike_price 
4] buy 1 Todays Top losers stock PUT @9:45
    4.1] select put below 2% of current stock price as strike_price 
5] Open intrest ratio sellers and buyers
6] for sell the sellers must be 2 times then buyers 
7] for buy the buyers must be 2 times then  sellers
8] if the 6 or 7 condition are not achived then go for 2nd Todays Top gainer or 3rd 4th so on..
9] if the sellers & buyers are equal then exit the position

    
#sellinging strategy

1] first check nifty futures if first 10 min candels is red the go to sell
2] then go and check the Todays Top losers
3] buy 2 Todays Top losers stocks put @9:25 
    3.1] select put below 2% of current stock price as strike_price 
4] buy 1 Todays Top gainers stock CALL @9:45
    4.1] select call above 2% of current stock price as strike_price 
5] Open intrest ratio sellers abd buyers    
6] for sell the sellers must be 2 times then buyers 
7] for buy the buyers must be 2 times then  sellers
8] if the 6 or 7 condition are not achived then go for 2nd Todays Top gainer or 3rd 4th so on..
9] if the sellers & buyers are equal then exit the position


#STodays Toploss & taget
STodays Toploss 30% - 40% of your entry
Target 100%

Trails sTodays Toploss once your tradde goes profit side of 30% then trail your SL @ cost & hold max till 2pm or 3pm
    
"""
"""
Strategy 2

1] gauge market direction
2] find killer setup
3] enter weekly option on wedensday
4] pick otm
5] scale out slowly
    
"""



