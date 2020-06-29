# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 16:29:26 2020

@author: Sangram Phadke
"""
#Simple CALL & PUT suggetion based on NSE Index Direction notifier BOT

######################## Creating U.S index ########################################

import yfinance as yf

#United states index
sp500 = yf.Ticker("^GSPC")
nf_sp500 = sp500.info
nf_sp500pc = float(((nf_sp500['dayLow']-nf_sp500['previousClose'])/nf_sp500['previousClose'])*100)
#print('US S&P 500 index is {} and persent change is {}'.format(nf_sp500['dayLow'],nf_sp500pc))

dow = yf.Ticker("^DJI")
nf_dow = dow.info
nf_dowpc = float(((nf_dow['dayLow']-nf_dow['previousClose'])/nf_dow['previousClose'])*100)
#print('US DOW index is {} and persent change is {}'.format(nf_dow['dayLow'],nf_dowpc))


nasd = yf.Ticker("^IXIC")
nf_nasd = nasd.info
nf_nasdpc = float(((nf_nasd['dayLow']-nf_nasd['previousClose'])/nf_nasd['previousClose'])*100)
#print('US Nasdaq Composite index is {} and persent change is {}'.format(nf_nasd['dayLow'],nf_nasdpc))


#United states Sectors


#Dow Jones U.S. Bank Index
dowbank = yf.Ticker("^DJUSBK")
nf_dowbank = dowbank.info
nf_dowbankpc = float(((nf_dowbank['dayLow']-nf_dowbank['previousClose'])/nf_dowbank['previousClose'])*100)
#print('US Bank sector index is {} and persent change is {}'.format(nf_dowbank['dayLow'],nf_dowbankpc))




#Dow Jones U.S. IT Index
dowit = yf.Ticker("^DJUSTC")
nf_dowit = dowit.info
nf_dowitpc = float(((nf_dowit['dayLow']-nf_dowit['previousClose'])/nf_dowit['previousClose'])*100)
#print('US IT sector index is {} and persent change is {}'.format(nf_dowit['dayLow'],nf_dowitpc))




#Dow Jones U.S. Pharma Index
dowph = yf.Ticker("^DJUSPR")
nf_dowph = dowph.info
nf_dowphpc = float(((nf_dowph['dayLow']-nf_dowph['previousClose'])/nf_dowph['previousClose'])*100)
#print('US Pharma sector index is {} and persent change is {}'.format(nf_dowph['dayLow'],nf_dowphpc))



#Dow Jones U.S. Phara & bio Index
dowpb = yf.Ticker("^DJUSPN")
nf_dowpb = dowpb.info
nf_dowpbpc = float(((nf_dowpb['dayLow']-nf_dowpb['previousClose'])/nf_dowpb['previousClose'])*100)
#print('US Pharma & Biotech sector index is {} and persent change is {}'.format(nf_dowpb['dayLow'],nf_dowpbpc))




#United states futures

nqf = yf.Ticker("NQ=F")
nf_nqf = nqf.info
nf_nqfpc = float(((nf_nqf['dayLow']-nf_nqf['previousClose'])/nf_nqf['previousClose'])*100)
#print('US NQ FUTURE index is {} and persent change is {}'.format(nf_nqf['dayLow'],nf_nqfpc))


spf = yf.Ticker("ES=F")
nf_spf = spf.info
nf_spfpc = float(((nf_spf['dayLow']-nf_spf['previousClose'])/nf_spf['previousClose'])*100)
#print('US S&P FUTURE index is {} and persent change is {}'.format(nf_spf['dayLow'],nf_spfpc))


dowf = yf.Ticker("YM=F")
nf_dowf = dowf.info
nf_dowfpc = float(((nf_dowf['dayLow']-nf_dowf['previousClose'])/nf_dowf['previousClose'])*100)
#print('US DOW FUTURE index is {} and persent change is {}'.format(nf_dowf['dayLow'],nf_dowfpc))



################################################# NSE DATA PULL start #################################################

# Objective to indicate the trend direction


# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
from nsetools import Nse
import math
import os
import sys

from datetime import datetime
starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull start time

# Importing the NIFTY dataset from NSE live site / portel 
nse = Nse() 
# NSE object creation
#print (nse)
#il = nse.get_index_list()

#NIFTY indexs current values

nf_n50 = nse.get_index_quote("nifty 50") 
#print('NIFTY 50   index current value is {} and precent change is {} '.format(n50_index['lastPrice'],n50_index['pChange'])) 


n50_200 = nse.get_index_quote("NIFTY 200") 
#print('NIFTY 200  index current value is {} and precent change is {} '.format(n50_200['lastPrice'],n50_200['pChange'])) 


nf_bank = nse.get_index_quote("nifty bank") 
#print('NIFTY BANK index current value is {} and precent change is {} '.format(nf_bank['lastPrice'],nf_bank['pChange'])) 

nf_psubank = nse.get_index_quote("nifty psu bank") 
#print('NIFTY PSU BANK index current value is {} and precent change is {} '.format(nf_psubank['lastPrice'],nf_psubank['pChange'])) 

nf_pvtbank = nse.get_index_quote("nifty pvt bank") 
#print('NIFTY PVT BANK index current value is {} and precent change is {} '.format(nf_pvtbank['lastPrice'],nf_pvtbank['pChange'])) 

nf_finser = nse.get_index_quote("nifty fin service") 
#print('NIFTY Financial service index current value is {} and precent change is {} '.format(nf_finser['lastPrice'],nf_finser['pChange'])) 

nf_auto = nse.get_index_quote("nifty auto") 
#print('NIFTY Auto index current value is {} and precent change is {} '.format(nf_auto['lastPrice'],nf_auto['pChange'])) 


nf_pharma = nse.get_index_quote("nifty pharma") 
#print('NIFTY Pharma index current value is {} and precent change is {} '.format(nf_pharma['lastPrice'],nf_pharma['pChange'])) 


nf_nint = nse.get_index_quote("nifty it") 
#print('NIFTY IT   index current value is {} and precent change is {} '.format(n50_nit['lastPrice'],n50_nit['pChange'])) 



#Creating data frame for NSE index stocks

dr_nis = pd.read_csv('NSEallsymbol.csv',index_col = 'Symbol')
df_nis = pd.DataFrame(data=dr_nis)


##################      N50   ###########################

df_n50 = df_nis[0:50]

##Retrive NSE live data for each stock as above data frame

nis = []
for i,r in df_n50.iterrows():
    nisl = nse.get_quote(i)
    nis.append(nisl) 

# To make simple list from dictionarys used in above    
nislist=[]

for index in range(len(nis)):
    for key in nis[index]:
        if key == 'symbol':
            #retrive each value
            ins = nis[index]['symbol']
            icn = nis[index]['companyName']
            iop = nis[index]['open']
            iltp = nis[index]['lastPrice']
            ipc = nis[index]['pChange']
            
            #appended values
            nislist.append([ins,icn,iop,iltp,ipc])
    
df_nislist = pd.DataFrame(nislist,columns=['symbol','Company Name','Open price','LTP','precent change'] )        
df_nislist = pd.DataFrame(df_nislist).set_index('symbol')


# N50 shares from NSE

n50grtz = []
n50inzero = []
n50negt = []
for ind in range(len(df_nislist)):
    if (float(df_nislist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        n50grtz.append([itgo,df_nislist.index[ind],df_nislist.iloc[ind][3]])
        
    if (float(df_nislist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        n50negt.append([itlz,df_nislist.index[ind],df_nislist.iloc[ind][3]])
        
    if ((float(df_nislist.iloc[ind][3]) <= 0.99) and (float(df_nislist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        n50inzero.append([itgz,df_nislist.index[ind],df_nislist.iloc[ind][3]])

#print("NIFTY 50 stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(n50grtz),len(n50negt),len(n50inzero)))


########################## NBANK ##########################################

df_bank = df_nis[65:104]

##Retrive NSE live data for each stock as above data frame

bank = []
for i,r in df_bank.iterrows():
    bankl = nse.get_quote(i)
    bank.append(bankl) 

# To make simple list from dictionarys used in above    
banklist=[]

for index in range(len(bank)):
    for key in bank[index]:
        if key == 'symbol':
            #retrive each value
            bankns = bank[index]['symbol']
            bankcn = bank[index]['companyName']
            bankop = bank[index]['open']
            bankltp = bank[index]['lastPrice']
            bankpc = bank[index]['pChange']
            #appended values
            banklist.append([bankns,bankcn,bankop,bankltp,bankpc])
    
df_banklist = pd.DataFrame(banklist,columns=['symbol','Company Name','Open price','LTP','precent change'] )        
df_banklist = pd.DataFrame(df_banklist).set_index('symbol')


# Nbank shares from NSE

bankgrtz = []
bankinzero = []
banknegt = []
for ind in range(len(df_banklist)):
    if (float(df_banklist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        bankgrtz.append([itgo,df_banklist.index[ind],df_banklist.iloc[ind][3]])
        
    if (float(df_banklist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        banknegt.append([itlz,df_banklist.index[ind],df_banklist.iloc[ind][3]])
        
    if ((float(df_banklist.iloc[ind][3]) <= 0.99) and (float(df_banklist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        bankinzero.append([itgz,df_banklist.index[ind],df_banklist.iloc[ind][3]])

#print("NSE Bank stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(bankgrtz),len(banknegt),len(bankinzero)))



########################## NAUTO #################################

df_auto = df_nis[50:65]

##Retrive NSE live data for each stock as above data frame

auto = []
for i,r in df_auto.iterrows():
    autol = nse.get_quote(i)
    auto.append(autol) 

# To make simple list from dictionarys used in above    
autolist=[]

for index in range(len(auto)):
    for key in auto[index]:
        if key == 'symbol':
            #retrive each value
            autons = auto[index]['symbol']
            autocn = auto[index]['companyName']
            autoop = auto[index]['open']
            autoltp = auto[index]['lastPrice']
            autopc = auto[index]['pChange']
            
            #appended values
            autolist.append([autons,autocn,autoop,autoltp,autopc])
    
df_autolist = pd.DataFrame(autolist,columns=['symbol','Company Name','Open price','LTP','precent change'] )        
df_autolist = pd.DataFrame(df_autolist).set_index('symbol')


# NAUTO shares from NSE

autogrtz = []
autoinzero = []
autonegt = []
for ind in range(len(df_autolist)):
    if (float(df_autolist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        autogrtz.append([itgo,df_autolist.index[ind],df_autolist.iloc[ind][3]])
        
    if (float(df_autolist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        autonegt.append([itlz,df_autolist.index[ind],df_autolist.iloc[ind][3]])
        
    if ((float(df_autolist.iloc[ind][3]) <= 0.99) and (float(df_autolist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        autoinzero.append([itgz,df_autolist.index[ind],df_autolist.iloc[ind][3]])

#print("NSE AUTO stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(autogrtz),len(autonegt),len(autoinzero)))


#############################  NCement ########################################
df_cement = df_nis[104:110]

##Retrive NSE live data for each stock as above data frame

cement = []
for i,r in df_cement.iterrows():
    cementl = nse.get_quote(i)
    cement.append(cementl) 

# To make simple list from dictionarys used in above    
cementlist=[]

for index in range(len(cement)):
    for key in cement[index]:
        if key == 'symbol':
            #retrive each value
            cementns = cement[index]['symbol']
            cementcn = cement[index]['companyName']
            cementop = cement[index]['open']
            cementltp = cement[index]['lastPrice']
            cementpc = cement[index]['pChange']
            #appended values
            cementlist.append([cementns,cementcn,cementop,cementltp,cementpc])
    
df_cementlist = pd.DataFrame(cementlist,columns=['symbol','Company Name','Open price','LTP','precent change'] )        
df_cementlist = pd.DataFrame(df_cementlist).set_index('symbol')


# Ncement shares from NSE

cementgrtz = []
cementinzero = []
cementnegt = []
for ind in range(len(df_cementlist)):
    if (float(df_cementlist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        cementgrtz.append([itgo,df_cementlist.index[ind],df_cementlist.iloc[ind][3]])
        
    if (float(df_cementlist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        cementnegt.append([itlz,df_cementlist.index[ind],df_cementlist.iloc[ind][3]])
        
    if ((float(df_cementlist.iloc[ind][3]) <= 0.99) and (float(df_cementlist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        cementinzero.append([itgz,df_cementlist.index[ind],df_cementlist.iloc[ind][3]])

#print("NSE cement stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(cementgrtz),len(cementnegt),len(cementinzero)))


############################  NIT  ##################################

df_nint = df_nis[110:121]

##Retrive NSE live data for each stock as above data frame

nint = []
for i,r in df_nint.iterrows():
    nintl = nse.get_quote(i)
    nint.append(nintl) 

# To make simple list from dictionarys used in above    
nintlist=[]

for index in range(len(nint)):
    for key in nint[index]:
        if key == 'symbol':
            #retrive each value
            nintns = nint[index]['symbol']
            nintcn = nint[index]['companyName']
            nintop = nint[index]['open']
            nintltp = nint[index]['lastPrice']
            nintpc = nint[index]['pChange']
            #appended values
            nintlist.append([nintns,nintcn,nintop,nintltp,nintpc])
    
df_nintlist = pd.DataFrame(nintlist,columns=['symbol','Company Name','Open price','LTP','precent change'] )        
df_nintlist = pd.DataFrame(df_nintlist).set_index('symbol')


# Nnint shares from NSE

nintgrtz = []
nintinzero = []
nintnegt = []
for ind in range(len(df_nintlist)):
    if (float(df_nintlist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        nintgrtz.append([itgo,df_nintlist.index[ind],df_nintlist.iloc[ind][3]])
        
    if (float(df_nintlist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        nintnegt.append([itlz,df_nintlist.index[ind],df_nintlist.iloc[ind][3]])
        
    if ((float(df_nintlist.iloc[ind][3]) <= 0.99) and (float(df_nintlist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        nintinzero.append([itgz,df_nintlist.index[ind],df_nintlist.iloc[ind][3]])

#print("NSE IT stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(nintgrtz),len(nintnegt),len(nintinzero)))

############################  NPOWER  #########################################

df_power = df_nis[121:133]

##Retrive NSE live data for each stock as above data frame

power = []
for i,r in df_power.iterrows():
    powerl = nse.get_quote(i)
    power.append(powerl) 

# To make simple list from dictionarys used in above    
powerlist=[]

for index in range(len(power)):
    for key in power[index]:
        if key == 'symbol':
            #retrive each value
            powerns = power[index]['symbol']
            powercn = power[index]['companyName']
            powerop = power[index]['open']
            powerltp = power[index]['lastPrice']
            powerpc = power[index]['pChange']
            #appended values
            powerlist.append([powerns,powercn,powerop,powerltp,powerpc])
    
df_powerlist = pd.DataFrame(powerlist,columns=['symbol','Company Name','Open price','LTP','precent change'] )        
df_powerlist = pd.DataFrame(df_powerlist).set_index('symbol')


# Npower shares from NSE

powergrtz = []
powerinzero = []
powernegt = []
for ind in range(len(df_powerlist)):
    if (float(df_powerlist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        powergrtz.append([itgo,df_powerlist.index[ind],df_powerlist.iloc[ind][3]])
        
    if (float(df_powerlist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        powernegt.append([itlz,df_powerlist.index[ind],df_powerlist.iloc[ind][3]])
        
    if ((float(df_powerlist.iloc[ind][3]) <= 0.99) and (float(df_powerlist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        powerinzero.append([itgz,df_powerlist.index[ind],df_powerlist.iloc[ind][3]])

#print("NSE Power stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(powergrtz),len(powernegt),len(powerinzero)))


#############################  Npharma ###########################################

df_pharma = df_nis[133:143]

##Retrive NSE live data for each stock as above data frame

pharma = []
for i,r in df_pharma.iterrows():
    pharmal = nse.get_quote(i)
    pharma.append(pharmal) 

# To make simple list from dictionarys used in above    
pharmalist=[]

for index in range(len(pharma)):
    for key in pharma[index]:
        if key == 'symbol':
            #retrive each value
            pharmans = pharma[index]['symbol']
            pharmacn = pharma[index]['companyName']
            pharmaop = pharma[index]['open']
            pharmaltp = pharma[index]['lastPrice']
            pharmapc = pharma[index]['pChange']
            #appended values
            pharmalist.append([pharmans,pharmacn,pharmaop,pharmaltp,pharmapc])
    
df_pharmalist = pd.DataFrame(pharmalist,columns=['symbol','Company Name','Open price','LTP','precent change'] )        
df_pharmalist = pd.DataFrame(df_pharmalist).set_index('symbol')


# Npharma shares from NSE

pharmagrtz = []
pharmainzero = []
pharmanegt = []
for ind in range(len(df_pharmalist)):
    if (float(df_pharmalist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        pharmagrtz.append([itgo,df_pharmalist.index[ind],df_pharmalist.iloc[ind][3]])
        
    if (float(df_pharmalist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        pharmanegt.append([itlz,df_pharmalist.index[ind],df_pharmalist.iloc[ind][3]])
        
    if ((float(df_pharmalist.iloc[ind][3]) <= 0.99) and (float(df_pharmalist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        pharmainzero.append([itgz,df_pharmalist.index[ind],df_pharmalist.iloc[ind][3]])

#print("NSE Pharma stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(pharmagrtz),len(pharmanegt),len(pharmainzero)))



#######################  Niorn ####################################

df_niorn = df_nis[143:161]

##Retrive NSE live data for each stock as above data frame

niorn = []
for i,r in df_niorn.iterrows():
    niornl = nse.get_quote(i)
    niorn.append(niornl) 

# To make simple list from dictionarys used in above    
niornlist=[]

for index in range(len(niorn)):
    for key in niorn[index]:
        if key == 'symbol':
            #retrive each value
            niornns = niorn[index]['symbol']
            niorncn = niorn[index]['companyName']
            niornop = niorn[index]['open']
            niornltp = niorn[index]['lastPrice']
            niornpc = niorn[index]['pChange']
            #appended values
            niornlist.append([niornns,niorncn,niornop,niornltp,niornpc])
    
df_niornlist = pd.DataFrame(niornlist,columns=['symbol','Company Name','Open price','LTP','precent change'] )        
df_niornlist = pd.DataFrame(df_niornlist).set_index('symbol')


# Nniorn shares from NSE

niorngrtz = []
niorninzero = []
niornnegt = []
for ind in range(len(df_niornlist)):
    if (float(df_niornlist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        niorngrtz.append([itgo,df_niornlist.index[ind],df_niornlist.iloc[ind][3]])
        
    if (float(df_niornlist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        niornnegt.append([itlz,df_niornlist.index[ind],df_niornlist.iloc[ind][3]])
        
    if ((float(df_niornlist.iloc[ind][3]) <= 0.99) and (float(df_niornlist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        niorninzero.append([itgz,df_niornlist.index[ind],df_niornlist.iloc[ind][3]])

#print("NSE Iorn stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(niorngrtz),len(niornnegt),len(niorninzero)))






#############################  NFMCG ###########################################

df_fmcg = df_nis[161:176]

##Retrive NSE live data for each stock as above data frame

fmcg = []
for i,r in df_fmcg.iterrows():
    fmcgl = nse.get_quote(i)
    fmcg.append(fmcgl) 

# To make simple list from dictionarys used in above    
fmcglist=[]

for index in range(len(fmcg)):
    for key in fmcg[index]:
        if key == 'symbol':
            #retrive each value
            fmcgns = fmcg[index]['symbol']
            fmcgcn = fmcg[index]['companyName']
            fmcgop = fmcg[index]['open']
            fmcgltp = fmcg[index]['lastPrice']
            fmcgpc = fmcg[index]['pChange']
            #appended values
            fmcglist.append([fmcgns,fmcgcn,fmcgop,fmcgltp,fmcgpc])
    
df_fmcglist = pd.DataFrame(fmcglist,columns=['symbol','Company Name','Open price','LTP','precent change'] )        
df_fmcglist = pd.DataFrame(df_fmcglist).set_index('symbol')


# Nfmcg shares from NSE

fmcggrtz = []
fmcginzero = []
fmcgnegt = []
for ind in range(len(df_fmcglist)):
    if (float(df_fmcglist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        fmcggrtz.append([itgo,df_fmcglist.index[ind],df_fmcglist.iloc[ind][3]])
        
    if (float(df_fmcglist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        fmcgnegt.append([itlz,df_fmcglist.index[ind],df_fmcglist.iloc[ind][3]])
        
    if ((float(df_fmcglist.iloc[ind][3]) <= 0.99) and (float(df_fmcglist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        fmcginzero.append([itgz,df_fmcglist.index[ind],df_fmcglist.iloc[ind][3]])

#print("NSE FMCG stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(fmcggrtz),len(fmcgnegt),len(fmcginzero)))






#############################  Nconstruction  ##########################################

df_cost = df_nis[176:188]

##Retrive NSE live data for each stock as above data frame

cost = []
for i,r in df_cost.iterrows():
    costl = nse.get_quote(i)
    cost.append(costl) 

# To make simple list from dictionarys used in above    
costlist=[]

for index in range(len(cost)):
    for key in cost[index]:
        if key == 'symbol':
            #retrive each value
            costns = cost[index]['symbol']
            costcn = cost[index]['companyName']
            costop = cost[index]['open']
            costltp = cost[index]['lastPrice']
            costpc = cost[index]['pChange']
            #appended values
            costlist.append([costns,costcn,costop,costltp,costpc])
    
df_costlist = pd.DataFrame(costlist,columns=['symbol','Company Name','Open price','LTP','precent change'] )        
df_costlist = pd.DataFrame(df_costlist).set_index('symbol')


# Ncost shares from NSE

costgrtz = []
costinzero = []
costnegt = []
for ind in range(len(df_costlist)):
    if (float(df_costlist.iloc[ind][3])>=1.0):
        itgo = "Price change is greater than one  "
        costgrtz.append([itgo,df_costlist.index[ind],df_costlist.iloc[ind][3]])
        
    if (float(df_costlist.iloc[ind][3]) <= 0.01):
        itlz = "Price change is Negative  "
        costnegt.append([itlz,df_costlist.index[ind],df_costlist.iloc[ind][3]])
        
    if ((float(df_costlist.iloc[ind][3]) <= 0.99) and (float(df_costlist.iloc[ind][3]) > 0.0)):
        itgz = "Price change are in zeros 0 "
        costinzero.append([itgz,df_costlist.index[ind],df_costlist.iloc[ind][3]])

#print("NSE cost stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(costgrtz),len(costnegt),len(costinzero)))



#####################################  End of dat pull from NSE  ###############################

## End of data pull from NSE
        
endtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull end time


################################ Print statments #################################################
# #Sectors
# print("NIFTY 50    stocks where {} are greater than one {} are negative {} are in zeros".format(len(n50grtz),len(n50negt),len(n50inzero)))
# print("NSE AUTO    stocks where {} are greater than one {} are negative {} are in zeros".format(len(autogrtz),len(autonegt),len(autoinzero)))
# print("NSE Bank    stocks where {} are greater than one {} are negative {} are in zeros".format(len(bankgrtz),len(banknegt),len(bankinzero)))
# print("NSE cement  stocks where {} are greater than one {} are negative {} are in zeros".format(len(cementgrtz),len(cementnegt),len(cementinzero)))
# print("NSE IT      stocks where {} are greater than one {} are negative {} are in zeros".format(len(nintgrtz),len(nintnegt),len(nintinzero)))
# print("NSE Power   stocks where {} are greater than one {} are negative {} are in zeros".format(len(powergrtz),len(powernegt),len(powerinzero)))
# print("NSE Pharma  stocks where {} are greater than one {} are negative {} are in zeros".format(len(pharmagrtz),len(pharmanegt),len(pharmainzero)))
# print("NSE Iorn    stocks where {} are greater than one {} are negative {} are in zeros".format(len(niorngrtz),len(niornnegt),len(niorninzero)))
# print("NSE FMCG    stocks where {} are greater than one {} are negative {} are in zeros".format(len(fmcggrtz),len(fmcgnegt),len(fmcginzero)))
# print("NSE Costconstruction stk {} are greater than one {} are negative {} are in zeros".format(len(costgrtz),len(costnegt),len(costinzero)))



##Index

# print('NIFTY 50   index current value is {} and precent change is {} '.format(nf_n50['lastPrice'],nf_n50['pChange'])) 

# print('NIFTY BANK index current value is {} and precent change is {} '.format(nf_bank['lastPrice'],nf_bank['pChange'])) 
# print('NIFTY PSU BANK index currentvalue {} and precent change is {} '.format(nf_psubank['lastPrice'],nf_psubank['pChange'])) 
# print('NIFTY PVT BANK index currentvalue {} and precent change is {} '.format(nf_pvtbank['lastPrice'],nf_pvtbank['pChange'])) 
# print('NIFTY Financial service idx value {} and precent change is {} '.format(nf_finser['lastPrice'],nf_finser['pChange'])) 

# print('NIFTY Auto index current value is {} and precent change is {} '.format(nf_auto['lastPrice'],nf_auto['pChange'])) 
# print('NIFTY Pharma idx current value is {} and precent change is {} '.format(nf_pharma['lastPrice'],nf_pharma['pChange'])) 
# print('NIFTY IT   index current value is {} and precent change is {} '.format(nf_nint['lastPrice'],nf_nint['pChange'])) 
# print('NIFTY 200  index current value is {} and precent change is {} '.format(n50_200['lastPrice'],n50_200['pChange'])) 


################################### US analysis ###########################################

## Index

# print('US Nasdaq Composite index is {} and persent change is {}'.format(nf_nasd['dayLow'],nf_nasdpc))
# print('US DOW index is {} and persent change is {}'.format(nf_dow['dayLow'],nf_dowpc))
# print('US S&P 500 index is {} and persent change is {}'.format(nf_sp500['dayLow'],nf_sp500pc))

## Sectors

# print('US Pharma & Biotech sector index is {} and persent change is {}'.format(nf_dowpb['dayLow'],nf_dowpbpc))
# print('US Pharma sector index is {} and persent change is {}'.format(nf_dowph['dayLow'],nf_dowphpc))
# print('US IT sector index is {} and persent change is {}'.format(nf_dowit['dayLow'],nf_dowitpc))
# print('US Bank sector index is {} and persent change is {}'.format(nf_dowbank['dayLow'],nf_dowbankpc))

## Futures

# print('US DOW FUTURE index is {} and persent change is {}'.format(nf_dowf['dayLow'],nf_dowfpc))
# print('US S&P FUTURE index is {} and persent change is {}'.format(nf_spf['dayLow'],nf_spfpc))
# print('US NQ FUTURE index is {} and persent change is {}'.format(nf_nqf['dayLow'],nf_nqfpc))


######################################  Main Logic ##########################################

#################################### sectors percentage #####################################

# Sectors	Count	% in N50   innumber
# NAUTO	    15	     0.12	   1.8   2
# NBANK	    38	     0.2	   7.6   8
# NCement	6	     0.04	   0.24  1
# Nconstruction	12	 0.1	   1.2   1
# NFMCG	    15	     0.08	   1.2   1
# Niorn	    18	     0.12	   2.16  2
# NIT	    11	     0.12      1.32  2
# Npharma	10	     0.08      0.8   1
# Npower	12	     0.14	   1.68  2
   

if (len(autonegt) < 2 and len(banknegt) < 8 and len(cementnegt) < 1 and len(costnegt) < 1 and len(fmcgnegt) < 2 and len(niornnegt) < 2 and len(nintnegt) < 2 and len(pharmanegt) < 1 and len(powernegt) < 2):
    print('the sectors are up, NIFTY 50 is up')
else:
    print('One or more sectors are down, NIFTY 50 is down')
    if (len(autonegt) > 0 and len(banknegt) > 0 and len(cementnegt) > 0 and len(costnegt) > 0 and len(fmcgnegt) > 0 and len(niornnegt) > 0 and len(nintnegt) > 0 and len(pharmanegt) > 0 and len(powernegt) >0 ):
        print('All sectors are down by avrage {} percent'.format(((len(autonegt) + len(banknegt) + len(cementnegt) + len(costnegt) + len(fmcgnegt) + len(niornnegt) + len(nintnegt) + len(pharmanegt) + len(powernegt))/137)*100))

if len(autonegt) > 0 :
    # Auto
    print ('Auto sector is {} down'.format((len(autonegt)/15)*100))
else:
    print ('Auto sector is up')


if float(nf_dowbankpc)<0.0:
    if len(banknegt) > 0 :
        print ('Bank sector is {} down'.format((len(banknegt)/38)*100))
        print('US Bank sector index is {} and persent change is {}'.format(nf_dowbank['dayLow'],nf_dowbankpc))
else:
    print ('Bank sector is up')


if nf_dowitpc < 0.0:
    if len(nintnegt) > 0 :
        print ('IT sector is {} down'.format((len(nintnegt)/11)*100))
        print('US IT sector index is {} and persent change is {}'.format(nf_dowit['dayLow'],nf_dowitpc))
else:
    print ('IT sector is up')


if len(cementnegt) > 0 :
    # Cement
    print ('Cement sector is {} down'.format((len(cementnegt)/6)*100))
else:
    print ('Cement sector is up')


if len(costnegt) > 0 :
    # Construction
    print ('Construction sector is {} down'.format((len(costnegt)/12)*100))
else:
    print ('Construction sector is up')

if len(fmcgnegt) > 0 :
    # FMCG
    print ('FMCG sector is {} down'.format((len(fmcgnegt)/15)*100))
else:
    print ('FMCG sector is up')

if len(niornnegt) > 0 :
    # Iorn
    print ('Iorn sector is {} down'.format((len(niornnegt)/18)*100))
else:
    print ('Iorn sector is up')

 
if len(pharmanegt) > 0 :
    # Pharma 
    print ('Pharma sector is {} down'.format((len(pharmanegt)/10)*100))
    print('US Pharma & Biotech sector index is {} and persent change is {}'.format(nf_dowpb['dayLow'],nf_dowpbpc))
    print('US Pharma sector index is {} and persent change is {}'.format(nf_dowph['dayLow'],nf_dowphpc))
else:
    print ('Pharma sector is up')
  

if len(powernegt) > 0:
    # Power
    print ('Power sector is {} down'.format((len(powernegt)/12)*100))
else:
    print ('Power sector is up')
    

###################### IT sector Options ################################# 


nint_len = len(nintgrtz)+len(nintnegt)+len(nintinzero)

#nint PUT BUY Logic 
if (float(nf_nint['pChange']) <= 0.01) and (float(nf_nint['pChange']) >= -0.75):
    if len(nintnegt) >= (nint_len*0.7) :
        #print('Total negative are more than 70%')
        print('For IT sector BUY PUT at time {}'.format(endtime))
        
    else:
        print('Do not BUY IT sector PUT at time {}'.format(endtime))
        print('High Risk For IT sector BUY Call at time {}'.format(endtime))
    

#nint PUT SELL Logic
if float(nf_nint['pChange']) <= -0.75:
    if (len(nintnegt) >= (nint_len*0.4)) and (len(nintnegt) <= (nint_len*0.7)) :
        #print('Total negative are more than 70%')
        print('For IT sector SELL PUT at time {}'.format(endtime))
    else:
        print('Do not SELL IT sector PUT at time {}'.format(endtime))     
        print('Medium Risk For IT sector CALL')        
    
#nint CALL BUY Logic  ##working correctly 
        
if float(nf_nint['pChange']) >= 0.20:
    if len(nintnegt) <= (nint_len*0.2) :
        #print('Total negative are less than 20%')
        print('For IT sector BUY CALL at time {}'.format(endtime))
    else:
        print('Do not BUY IT sector CALL at time {}'.format(endtime))
        print('High risk For IT sector BUY PUT' )
              
#nint CALL SELL Logic

        
if float(nf_nint['pChange']) >= 0.75:
    if len(nintnegt) <= (nint_len*0.4) :
        #print('Total negative are less than 20%')
        print('For IT sector SELL CALL time {}'.format(endtime))
    else:
        print('Do not SELL IT sector CALL at time {}'.format(endtime))
        print('Medium Risk For IT sector BUY PUT ')
    

   
###################### N50 Options #################################

n50_len = len(n50grtz)+len(n50negt)+len(n50inzero)

#n50 PUT BUY Logic 
if float(nf_n50['pChange']) <= 0.01 and float(nf_n50['pChange']) > -0.75:
    if len(n50negt) >= (n50_len*0.7) :
        #print('Total negative are more than 70%')
        n50PEITM = (nf_n50['lastPrice']+200) 
        n50PEATM = (nf_n50['lastPrice'])
        n50PEOTM = (nf_n50['lastPrice']-200)
        print('For NIFTY 50 BUY PUT range are {} ATM {} ITM {} OTM at time {}'.format(n50PEATM,n50PEITM,n50PEOTM,endtime))
        
    else:
        print('Do not BUY NIFTY 50 PUT at time {}'.format(endtime))
        print('High Risk For NIFTY 50 BUY Call')
    

#n50 PUT SELL Logic
if float(nf_n50['pChange']) <= -0.75:
    if (len(n50negt) >= (n50_len*0.4)) and (len(n50negt) <= (n50_len*0.7)) :
        #print('Total negative are more than 70%')
        n50PEITM = (nf_n50['lastPrice']+200) 
        n50PEATM = (nf_n50['lastPrice'])
        n50PEOTM = (nf_n50['lastPrice']-200)
        print('For NIFTY 50 SELL PUT range are {} ATM {} ITM {} OTM at time {}'.format(n50PEATM,n50PEITM,n50PEOTM,endtime))
    else:
        print('Do not SELL NIFTY 50  PUT at time {}'.format(endtime))     
        print('Medium Risk For NIFTY BUY CALL')
        
    
#n50 CALL BUY Logic  ##working correctly 
        
if float(nf_n50['pChange']) >= 0.2:
    if len(n50negt) <= (n50_len*0.2) :
        #print('Total negative are less than 20%')
        n50CEITM = (nf_n50['lastPrice']-200) 
        n50CEATM = (nf_n50['lastPrice'])
        n50CEOTM = (nf_n50['lastPrice']+200)
        print('For NIFTY 50 BUY CALL range are {} ATM {} ITM {} OTM at time {}'.format(n50CEATM,n50CEITM,n50CEOTM,endtime))
    else:
        print('Do not BUY NIFTY 50  CALL at time {}'.format(endtime))
        print('High risk For NIFTY 50 BUY PUT' )
              
#n50 CALL SELL Logic

        
if float(nf_n50['pChange']) >= 1:
    if len(n50negt) <= (n50_len*0.4) :
        #print('Total negative are less than 20%')
        n50CEITM = (nf_n50['lastPrice']-200) 
        n50CEATM = (nf_n50['lastPrice'])
        n50CEOTM = (nf_n50['lastPrice']+200)
        print('For NIFTY SELL CALL range are {} ATM {} ITM {} OTM at time {}'.format(n50CEATM,n50CEITM,n50CEOTM,endtime))
    else:
        print('Do not SELL NIFTY 50 CALL at time {}'.format(endtime))
        print('Medium Risk For NIFTY 50 BUY PUT ')
    

    
######################## NBANK Options ###################################

bank_len = (len(bankgrtz)+len(banknegt)+len(bankinzero))

#For future prediction depend on NIFTY PSU Bank & PVT Bank Indexs    

if float(nf_psubank['pChange']) > 0.25 and float(nf_pvtbank['pChange']) > 0.75 and float(nf_finser['pChange']) > 0.0:
    print('Bank sector are in positive at time {}'.format(endtime))
    if len(banknegt) > (bank_len*0.2):
        print('NSE Bank sector is going Down but trend is positive')
    else:
        print('Bank sector are in positive at time {}'.format(endtime))
elif float(nf_psubank['pChange']) < 0.25 and float(nf_pvtbank['pChange']) < 0.75 and float(nf_finser['pChange']) < 0.0:
    print('Bank sector are in negative at time {}'.format(endtime))
    if (len(banknegt) > (bank_len*0.4)) and (len(banknegt) < (bank_len*0.70)):
        print('NSE Bank sector is going Down and trend is negative at time {}'.format(endtime))
    if len(banknegt) > (bank_len*0.70):
        print('NSE Bank sector is going Down and trend is highly negative at time {}'.format(endtime))
    else:
        print('Bank sector are in positive and trend is negative at time {}'.format(endtime))
else:
    print('Bank sector is sideways at time {}'.format(endtime))


#BANK PUT BUY Logic depend on NIFTY Bank Index
if (float(nf_bank['pChange']) > -1) and (float(nf_bank['pChange']) <= 0.01):
    if len(banknegt) >= (bank_len*0.7) :
        #print('Total negative are more than 70%')
        bankPEITM = (nf_bank['lastPrice']+500) 
        bankPEATM = (nf_bank['lastPrice'])
        bankPEOTM = (nf_bank['lastPrice']-500)
        print('For BANK NIFTY BUY PUT range are {} ATM {} ITM {} OTM at time {}'.format(bankPEATM,bankPEITM,bankPEOTM,endtime))
    else:
        print('Do not BUY BANKNIFTY PUT at time {}'.format(endtime))
        print('High Risk For BANK NIFTY BUY CALL ')
        

#Bank PUT SELL Logic depend on NIFTY Bank Index
if float(nf_bank['pChange']) <= -1:
    if len(banknegt) >= (bank_len*0.4) :
        #print('Total negative are more than 70%')
        bankPEITM = (nf_bank['lastPrice']+100) 
        bankPEATM = (nf_bank['lastPrice'])
        bankPEOTM = (nf_bank['lastPrice']-100)
        print('For BANK NIFTY SELL PUT range are {} ATM {} ITM {} OTM at time {}'.format(bankPEATM,bankPEITM,bankPEOTM,endtime))
    else:
        print('Do not SELL BANKNIFTY  PUT at time {}'.format(endtime))
        print('Medium Risk For BANK NIFTY buy CALL')

#Bank CALL BUY Logic depend on NIFTY Bank Index
        
if (float(nf_bank['pChange']) >= 0.1) and (float(nf_bank['pChange']) < 1):
    if len(banknegt) <= (bank_len*0.2) :
        #print('Total negative are less than 20%')
        bankCEITM = (nf_bank['lastPrice']-100) 
        bankCEATM = (nf_bank['lastPrice'])
        bankCEOTM = (nf_bank['lastPrice']+100)
        print('For BANK NIFTY BUY CALL range are {} ATM {} ITM {} OTM at time {}'.format(bankCEATM,bankCEITM,bankCEOTM,endtime))
    else:
        print('Do not BUY BANKNIFTY CALL at time {}'.format(endtime))
        print('Medium Risk For BANK NIFTY BUY PUT')

#Bank CALL SELL Logic depend on NIFTY Bank Index
        
if float(nf_bank['pChange']) >= 1:
    if len(banknegt) <= (bank_len*0.4) :
        #print('Total negative are less than 40%')
        bankCEITM = (nf_bank['lastPrice']-50) 
        bankCEATM = (nf_bank['lastPrice'])
        bankCEOTM = (nf_bank['lastPrice']+50)
        print('For BANK NIFTY SELL CALL range are {} ATM {} ITM {} OTM at time {}'.format(bankCEATM,bankCEITM,bankCEOTM,endtime))
    else:
        print('Do not SELL BANKNIFTY CALL at time {}'.format(endtime))
        print('High Risk For BANK NIFTY BUY PUT')

################################### End of BOT ############################################
print('')
print('')
print('End of BOT')