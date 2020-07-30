# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:53:55 2020

@author: Sangram Phadke

Call Option Intrinsic Value=USC−CS
where:
    
USC=Underlying Stock’s Current Price
CS=Call Strike Price

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
print('####################################################################')#,file=open("NSEFnO_Todays TopGL.txt", "a"))
print('')#,file=open("NSEFnO_Todays TopGL.txt", "a"))
starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull start time
print('Start data pull from NSE server at time ',starttime)#,file=open("NSEFnO_Todays TopGL.txt", "a"))

# Importing the NIFTY dataset from NSE live site / portel 
nse = Nse()  # NSE object creation
#print (nse)
day = datetime.now().strftime("%A")
daydate = datetime.now().strftime("%d")


if day == str('Thursday'):
    if int(daydate) >=24:
        print('Today is Monthly option expiry day : Carefully trade todays expiry day Call or Put options')#,file=open("NSEFnO_Todays TopGL.txt", "a"))
 



#Creating data frame for Option lotsize and there Rs. 1000 to Rs. 5000 price

 
dr_lotsize = pd.read_csv('FnO_lotsizelist.csv',index_col = 'symbols')
df_lotsize = pd.DataFrame(data=dr_lotsize)


dr_lotmoney = pd.read_csv('FnO_lotsizelist_fund.csv',index_col = 'symbols')
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



####################################### Main Logic ########################################


#Buying strategy
print("")#,file=open("NSEFnO_Todays TopGL.txt", "a"))
       
## Event of FnO companys 
### Update the BSE file on month to month

print('List of FnO company have upcoming Event: Expected Earning Release in next 7 days')#,file=open("NSEFnO_Todays TopGL.txt", "a"))                
print("")#,file=open("NSEFnO_Todays TopGL.txt", "a"))
dr_event = pd.read_csv('BSE Result for jul to aug 2020.csv',index_col='symbol')
df_event = pd.DataFrame(data = dr_event)
df_lotmoney = pd.DataFrame(data=dr_lotmoney)

print('')
de=0   
fe=0
symbolist  = []             
for de in range(len(df_event)):
    for fe in range(len (df_lotmoney)):
        if (df_lotmoney.index[fe] == df_event.index[de]):
            #if ((int(df_event.iloc[de][1][0:2])) >= int(daydate)) and ((int(df_event.iloc[de][1][0:2])) <= int(daydate)+5):
                #print('')
                #print('For {} release on {} \n'.format(df_event.index[de],df_event.iloc[de][1]))#,file=open("NSEFnO_Todays TopGL.txt", "a"))
            if ((int(df_event.iloc[de][1][0:2])) >= int(daydate)+5) and ((int(df_event.iloc[de][1][0:2])) <= int(daydate)+10):
                symbolist.append([df_event.index[de],df_lotmoney.iloc[fe][0]])
                #print(df_event.index[de],',',df_lotmoney.iloc[fe][0])#,file=open("FnOresultsToday.csv", "a")) 

df_fnosymbols = pd.DataFrame(data=symbolist)
df_fnosymbol = df_fnosymbols.set_index(0)

##Retrive NSE live data for each stock as above data frame

fnosymbol = []
for i,r in df_fnosymbol.iterrows():
    #print(i)
    fnosymboll = nse.get_quote(i)
    fnosymbol.append(fnosymboll) 

# To make simple list from dictionarys used in above    
fnosymbollist=[]

for index in range(len(fnosymbol)):
    for key in fnosymbol[index]:
        if key == 'symbol':
            #retrive each value
            fnosymbolns = fnosymbol[index]['symbol']
            fnosymbolcn = fnosymbol[index]['companyName']
            fnosymbolltp = fnosymbol[index]['lastPrice']
            fnosymbolCE = (fnosymbol[index]['lastPrice'])*1.095
            fnosymbolPE = ((fnosymbol[index]['lastPrice'])-((fnosymbol[index]['lastPrice'])*0.095))
            #appended values
            fnosymbollist.append([fnosymbolns,fnosymbolcn,fnosymbolPE,fnosymbolltp,fnosymbolCE])
    
df_fnosymbollist = pd.DataFrame(fnosymbollist,columns=['symbol','Company Name','PE','LTP','CE'] )        
df_fnosymbollist = pd.DataFrame(df_fnosymbollist).set_index('symbol')
#df_fnosymbollist.replace({None: 0.5}, inplace=True)
            
#print(df_fnosymbollist,file=open("FnOresultsToday.txt", "a")) 

## End of data pull from NSE


        
endtime = datetime.now().strftime("%H:%M") #program data pull end time
bot_endtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("")#,file=open("NSEFnO_Todays TopGL.txt", "a"))

print('End of data pull from NSE at time ',endtime)#,file=open("NSEFnO_Todays TopGL.txt", "a"))

print('End of BOT Read text file "NSEFnO_Todays TopGL.txt" for results generated / saved at same folder as prrogram')





