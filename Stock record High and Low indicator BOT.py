# -*- coding: utf-8 -*-

"""
#Stock record High and Low indicator BOT

Created on Thu Jun 18 15:39:12 2020

@author: Sangram Phadke

#Stock record High and Low indicator BOT

#BOT take 20 yaers of NIFTY 50 Stocks 

ADANIPORTS,ASIANPAINT,AXISBANK,BAJAJ-AUTO,BAJAJFINSV,BAJAUTOFIN,BAJFINANCE,BHARTIARTL,BPCL,BRITANNIA
CIPLA,COALINDIA,DRREDDY,EICHERMOT,GAIL,GRASIM,HCLTECH,HDFC,HDFCBANK,HEROMOTOCO,HINDALCO,HINDUNILVR,ICICIBANK
INDUSINDBK,INFRATEL,INFY,IOC,ITC,JSWSTEEL,KOTAKBANK,LT,M&M,MARUTI,NESTLEIND,NTPC,ONGC,POWERGRID,RELIANCE,SBIN
SHREECEM,SUNPHARMA,TATAMOTORS,TATASTEEL,TCS,TECHM,TITAN,ULTRACEMCO,UPL,VEDL,WIPRO,ZEEL

Starting from 2000 to 2020
## Stock split is not considerd price pu as it is...!!!

"""
# 1st Objective to indicate the High & Low of Current / End of day stock price to 5 yaers Avg. High or Low price.

# 2nd Objective to indicate the High & Low of Current / End of day stock price to current year High or Low price.

# 3rd Objective to indicate the High & Low of Current / End of day stock price to current 6 Month High or Low price.

# 4th Objective to indicate the High & Low of Current / End of day stock price to "financial crisis" year High or Low price.




# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from nsetools import Nse


# 1st Objective to indicate the High & Low of Current / End of day stock price to 5 yaers Avg. High or Low price.

# Importing the NIFTY dataset from PC file
df_ahal = pd.read_csv('NIFTY_AH_AL.csv',index_col = 'Symbol')
dtfrm = pd.DataFrame(data=df_ahal)
#dataset = pd.read_csv('NIFTY50_all_with_new_tickers.csv')
#H_table = pd.pivot_table(dataset, values=['High'], index=['Date'],columns=['Symbol'], aggfunc={'High': np.mean})
#L_table = pd.pivot_table(dataset, values=['Low'], index=['Date'],columns=['Symbol'], aggfunc={'Low': np.mean})
#dfahal_ex = pd.read_excel('NIFTY_AH_AL.xlsx', sheet_name= 'NIFTY_AH_AL')

# Importing the NIFTY dataset from NSE live site / portel 
nse = Nse()
#print (nse)

fifty = []
for i,r in df_ahal.iterrows():
    q = nse.get_quote(i)
    fifty.append(q) 
    #print(q)



# if the index is not the symbol and one of the row is 'Symbol'
# for i in df_ahal['Symbol']:
#     q = nse.get_quote(i)
#     fifty.append(q) 
#     #print(q)

    
#list of symbol and day low treded value 
dayLow_fifty = []
symbol_fifty = []
for index in range(len(fifty)):
    for key in fifty[index]:
        if key == 'dayLow':
            a = fifty[index]['symbol']
            b = fifty[index]['dayLow']
            dayLow_fifty.append(b) 
            symbol_fifty.append(a)
            
            
dtfrm['TodaysLow'] = dayLow_fifty

##Logic      
##For Todays DayLow is less than previous 5 years avrage low then it will print the Symbol and Todays Low price.
            
for ind in range(len(dtfrm)):
    if ((dtfrm.iloc[ind][0:-1]>=dtfrm.iloc[ind][-1]).all()):
        print(dtfrm.index[ind],dtfrm.iloc[ind][-1])
         
        
        


    
    


    
    










