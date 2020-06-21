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

Ideal Run time is before market open!!!! 
"""


# 1st Objective to indicate the High & Low of Current / End of day stock price to 5 yaers Avg. High or Low price.

# 2nd Objective to indicate the High & Low of Current / End of day stock price to current year High or Low price.

# 3rd Objective to indicate the High & Low of Current / End of day stock price to 52 week High or Low price.

# 4th Objective to indicate the High & Low of Current / End of day stock price to "financial crisis" year High or Low price.

# 5th Objective to take daily list of top losing and gaining stocks for the last trading session.

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from nsetools import Nse

# Importing the NIFTY dataset from NSE live site / portel 
nse = Nse() # NSE object creation
#print (nse)

# 1st Objective to indicate the High & Low of Current / End of day stock price to 5 yaers Avg. High or Low price.

# Importing the NIFTY avrage low dataset from PC file
df_al = pd.read_csv('NIFTY_2015to2019_AL.csv',index_col = 'Symbol')
dt_al = pd.DataFrame(data=df_al)


#dataset = pd.read_csv('NIFTY50_all_with_new_tickers.csv')
#H_table = pd.pivot_table(dataset, values=['High'], index=['Date'],columns=['Symbol'], aggfunc={'High': np.mean})
#L_table = pd.pivot_table(dataset, values=['Low'], index=['Date'],columns=['Symbol'], aggfunc={'Low': np.mean})
#dfahal_ex = pd.read_excel('NIFTY_AH_AL.xlsx', sheet_name= 'NIFTY_AH_AL')



fifty = []
for i,r in df_al.iterrows():
    q = nse.get_quote(i)
    fifty.append(q) 
    #print(q)# Importing the NIFTY dataset from NSE live site / portel 
    
#list of NSE Live data symbol and day High & low treded value 
dayLow_fifty = []
dayHigh_fifty = []
symbol_fifty = []
shl_52=[]
h_52=[]
l_52=[]
for index in range(len(fifty)):
    for key in fifty[index]:
        if key == 'symbol':
            #retrive each value
            a = fifty[index]['symbol']
            b = fifty[index]['dayLow']
            c = fifty[index]['dayHigh']
            d = fifty[index]['high52']
            e = fifty[index]['low52']
            #appended values
            symbol_fifty.append(a)
            dayLow_fifty.append(b)
            dayHigh_fifty.append(c)
            h_52.append(d)
            l_52.append(e)
            shl_52.append([a,d,e])
            

# added todays low value in data frame
dt_al['TodaysLow'] = dayLow_fifty

##Logic      
##For Todays DayLow is less than previous 5 years avrage low then it will print the Symbol and Todays Low price.
            
for ind in range(len(dt_al)):
    if ((dt_al.iloc[ind][0:-1]>=dt_al.iloc[ind][-1]).all()):
        print("The Todays DayLow is less than previous 5 years avrage low "+dt_al.index[ind],dt_al.iloc[ind][-1])
        
##For Todays DayHigh is greter than previous 5 years avrage low then it will print the Symbol and Todays Low price.
                
# Importing the NIFTY avrage High dataset from PC file

df_ah = pd.read_csv('NIFTY_2015to2019_AH.csv',index_col = 'Symbol')
dt_ah = pd.DataFrame(data=df_ah)
    
# added todays High value in data frame from list of symbol and day low treded value 
dt_ah['TodaysHigh'] = dayHigh_fifty

          
for ind in range(len(dt_ah)):
    if ((dt_ah.iloc[ind][0:-1]<=dt_ah.iloc[ind][-1]).all()):
        print("The Todays DayHigh is greter than previous 5 years avrage High "+dt_ah.index[ind],dt_ah.iloc[ind][-1])


# 2nd Objective to indicate the High & Low of Current / End of day stock price to current year High or Low price.
# Importing the NIFTY current year dataset from PC file
df_cy = pd.read_csv('NIFTY_2020.csv',index_col = 'Symbol')
dt_cy = pd.DataFrame(data=df_cy)
    

# added todays low & High value in data frame
dt_cy['TodaysLow'] = dayLow_fifty
dt_cy['TodaysHigh'] = dayHigh_fifty

##Logic      
##For Todays DayLow is less than current years avrage low then it will print the Symbol and Todays Low price.
            
for ind in range(len(dt_cy)):
    if ((dt_cy.iloc[ind][1:-2:2]>=dt_cy.iloc[ind][-2]).all()):
        print("The Todays DayLow is less than current years avrage low "+dt_cy.index[ind],dt_cy.iloc[ind][-1])

    
        
##For Todays DayHigh is greter than current years avrage low then it will print the Symbol and Todays Low price.
          
for ind in range(len(dt_cy)):
    if ((dt_cy.iloc[ind][0:-1:2]<=dt_cy.iloc[ind][-1]).all()):
        print("The Todays DayHigh is greter than current years avrage High "+dt_cy.index[ind],dt_cy.iloc[ind][-1])
        


# 3rd Objective to indicate the High & Low of Current / End of day stock price to 52 week High or Low price.
#Creating data frame for 52 week high low

dt_shl_52 = pd.DataFrame(data=shl_52,columns=['Symbols','High_52w','Low_52w'])

dt_shl_52 = dt_shl_52.set_index('Symbols')
    
#print('List of current year 52 week high low: '+dt_shl_52)    

# added todays low & High value in data frame
dt_shl_52['TodaysHigh'] = dayHigh_fifty
dt_shl_52['TodaysLow'] = dayLow_fifty

##Logic      
##For Todays stock price is less or greter than current 52 week then it will print the Symbol and Todays Low price.
            
for ind in range(len(dt_shl_52)):
    if ((dt_shl_52.iloc[ind][1:-2:2]>=dt_shl_52.iloc[ind][-1]).all()):
        print("The Todays DayLow is less than current 52 week low "+dt_cy.index[ind],dt_cy.iloc[ind][-1])

for ind in range(len(dt_shl_52)):
    if ((dt_shl_52.iloc[ind][0:-2:2]<=dt_shl_52.iloc[ind][-2]).all()):
        print("The Todays DayHigh is greter than current 52 week High "+dt_cy.index[ind],dt_cy.iloc[ind][-1])



# 4th Objective to indicate the High & Low of Current / End of day stock price to "financial crisis" year High or Low price.
# Importing the NIFTY financial crisis 2008 2009 2010 2020 dataset from PC file
df_fc = pd.read_csv('NIFTY_FC.csv',index_col = 'Symbol')
dt_fc = pd.DataFrame(data=df_fc)

# added todays low & High value in data frame
dt_fc['TodaysHigh'] = dayHigh_fifty
dt_fc['TodaysLow'] = dayLow_fifty



##Logic      
##For Todays DayLow is less than financial crisis year low then it will print the Symbol and Todays Low price.
            
for ind in range(len(dt_fc)):
    if ((dt_fc.iloc[ind][1:-2:2]>=dt_fc.iloc[ind][-1]).all()):
        print("The Todays DayLow is less than financial crisis year low "+dt_cy.index[ind],dt_cy.iloc[ind][-1])

for ind in range(len(dt_fc)):
    if ((dt_fc.iloc[ind][0:-2:2]<=dt_fc.iloc[ind][-2]).all()):
        print("The Todays DayHigh is greter than financial crisis year High "+dt_cy.index[ind],dt_cy.iloc[ind][-1])




# 5th Objective to take daily list of top losing and gaining stocks for the last trading session.

top_gainers = nse.get_top_gainers()
top_losers = nse.get_top_losers()

#Creating data frame for top_gainers & top_losers

df_tg = pd.DataFrame(top_gainers).set_index('symbol')
df_tl = pd.DataFrame(top_losers).set_index('symbol')

##Lretrive nse live data for each stock as above data frames top_gainers & top_losers

tg = []
for i,r in df_tg.iterrows():
    tgl = nse.get_quote(i)
    tg.append(tgl) 
  
tl = []
for i,r in df_tl.iterrows():
    tll = nse.get_quote(i)
    tl.append(tll) 

# To make simple list from dictionarys used in above    
top_g=[]

for index in range(len(tg)):
    for key in tg[index]:
        if key == 'symbol':
            #retrive each value
            gs = tg[index]['symbol']
            gdl = tg[index]['dayLow']
            gdh = tg[index]['dayHigh']
            gh52 = tg[index]['high52']
            gl52 = tg[index]['low52']
            #appended values
            top_g.append([gs,gdl,gdh,gh52,gl52])

top_l=[]

for index in range(len(tl)):
    for key in tl[index]:
        if key == 'symbol':
            #retrive each value
            ls = tl[index]['symbol']
            ldl = tl[index]['dayLow']
            ldh = tl[index]['dayHigh']
            lh52 = tl[index]['high52']
            ll52 = tl[index]['low52']
            #appended values
            top_l.append([ls,ldl,ldh,lh52,ll52])

            
df_top_gn = pd.DataFrame(top_g,columns=['symbol','dayLow','dayHigh','high52','low52'] )        
df_top_gn = pd.DataFrame(df_top_gn).set_index('symbol')

            
df_top_ln = pd.DataFrame(top_l,columns=['symbol','dayLow','dayHigh','high52','low52'] )        
df_top_ln = pd.DataFrame(df_top_ln).set_index('symbol')

            
for ind in range(len(df_top_ln)):
    if ((df_top_ln.iloc[ind][3]>=df_top_ln.iloc[ind][0]).all()):
        print("The Todays top_losers DayLow is less than 52 week low "+df_top_ln.index[ind],df_top_ln.iloc[ind][0])

for ind in range(len(df_top_gn)):
    if ((df_top_gn.iloc[ind][2]<=df_top_gn.iloc[ind][1]).all()):
        print("The Todays top_gainers DayHigh is greter than 52 week High "+df_top_gn.index[ind],df_top_gn.iloc[ind][1])




















