# # -*- coding: utf-8 -*-
# """
# Created on Wed Jun 24 16:29:26 2020

# @author: Sangram Phadke
# """

# #Simple CALL & PUT suggestion based on NSE Index Direction notifier BOT


# Run time 9:10 , 9:20 : 10:00 , 11:00 , 12:00 , 13:00 , 14:00, 15:00, 15:35

# Out put is Text file name "NSEmarket.txt"

################################################# NSE DATA PULL start #################################################

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
print('',file=open("NSEmarket.txt", "a"))
starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull start time
print('Start time of BOT',starttime,file=open("NSEmarket.txt", "a"))

# Importing the NIFTY dataset from NSE live site / portel 

nse = Nse()  # NSE object creation

#print (nse)


#listallindex = nse.get_index_list()

#NIFTY indexs current values

nf_n50 = nse.get_index_quote("nifty 50") 
#print('NIFTY 50   index current value is {} and precent change is {} '.format(nf_n50['lastPrice'],nf_n50['pChange'])) 


nf_indiavix = nse.get_index_quote("INDIA VIX") 
#print('INDIA VIX  index current value is {} and precent change is {} '.format(nf_indiavix['lastPrice'],nf_indiavix['pChange'])) 

nf_200 = nse.get_index_quote("NIFTY 200") 
#print('NIFTY 200  index current value is {} and precent change is {} '.format(nf_200['lastPrice'],nf_200['pChange'])) 

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
#print('NIFTY IT   index current value is {} and precent change is {} '.format(nf_nint['lastPrice'],nf_nint['pChange'])) 

nf_fmcg = nse.get_index_quote("nifty fmcg") 
#print('NIFTY fmcg   index current value is {} and precent change is {} '.format(nf_fmcg['lastPrice'],nf_fmcg['pChange'])) 

nf_energy = nse.get_index_quote("nifty energy") 
#print('NIFTY Energy   index current value is {} and precent change is {} '.format(nf_energy['lastPrice'],nf_energy['pChange'])) 

nf_metal= nse.get_index_quote("nifty metal") 
#print('NIFTY metal index current value is {} and precent change is {} '.format(nf_metal['lastPrice'],nf_metal['pChange'])) 

nf_infra= nse.get_index_quote("nifty infra") 
#print('NIFTY Infra index current value is {} and precent change is {} '.format(nf_infra['lastPrice'],nf_infra['pChange'])) 


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
df_nislist.replace({None: 0.5}, inplace=True)


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

print("NIFTY 50 stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(n50grtz),len(n50negt),len(n50inzero)))


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
df_banklist.replace({None: 0.5}, inplace=True)


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
df_autolist.replace({None: 0.5}, inplace=True)

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
df_cementlist.replace({None: 0.5}, inplace=True)

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
df_nintlist.replace({None: 0.5}, inplace=True)

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
df_powerlist.replace({None: 0.5}, inplace=True)

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
df_pharmalist.replace({None: 0.5}, inplace=True)

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
df_niornlist.replace({None: 0.5}, inplace=True)

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
df_fmcglist.replace({None: 0.5}, inplace=True)

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
df_costlist.replace({None: 0.5}, inplace=True)

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

print('End of data pull from NSE')

#####################################  End of dat pull from NSE  ###############################

## End of data pull from NSE
        
endtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull end time


################################ Print statments #################################################
#Sectors
# print('')
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
# print('')


######################################  Main Logic ##########################################

#New logic ideas 
#print('NIFTY 50   index current value is {} and precent change is {} '.format(nf_n50['lastPrice'],nf_n50['pChange'])) 

#India volatity index
#print('INDIA VIX  index current value is {} and precent change is {} '.format(nf_indiavix['lastPrice'],nf_indiavix['pChange'])) 

#When the vix is go up probability of market direction is continty of same direction is high
#When the vix is down the probability of market direction is continty of same direction is low
# VIX is the persent nifty move in positive or negative  // range of trande

# dr_indiavix = pd.read_csv('INDIA_VIX.csv')
# df_indiavix = pd.DataFrame(data=dr_indiavix)
# indiavixdata = {'Date':01-01-2020,'Close':12,'PrevClose':12,'PChange':110}
# df_indiavix = df_indiavix.append(indiavixdata,ignore_index = True)

#For next month Aprox nifty movment in persent:
vixmpc = (float(nf_indiavix['lastPrice'])/3.465) 
nmp = nf_n50['lastPrice']+vixmpc
nmn = nf_n50['lastPrice']-vixmpc

### VIX   high > 15.811 < low VIX 
#Low VIX Logic
if float(nf_indiavix['lastPrice']) > (15.811-vixmpc) and float(nf_indiavix['lastPrice']) < 15.811:
    print("The VIX is Low ",nf_indiavix['lastPrice'],file=open("NSEmarket.txt", "a"))
    if float(nf_indiavix['pChange']) > 0.0 :
        print('Probability of NIFTY is going UP to ' ,nmp)
    elif float(nf_indiavix['pChange']) < 0.0 :
        print('Probability of NIFTY is going DOWN to ' ,nmn)
if float(nf_indiavix['lastPrice']) < (15.811-vixmpc):
    print("The VIX is very Low ",nf_indiavix['lastPrice'],file=open("NSEmarket.txt", "a"))
    if float(nf_indiavix['pChange']) > 0.0 :
        print('Probability of NIFTY is going UP to ' ,nmp)
    elif float(nf_indiavix['pChange']) < 0.0 :
        print('Probability of NIFTY is going DOWN to ' ,nmn)

#HIGH VIX Logic        
if float(nf_indiavix['lastPrice']) > (15.811+vixmpc):
    print("The VIX is Very high ",nf_indiavix['lastPrice'],file=open("NSEmarket.txt", "a"))
    if float(nf_indiavix['pChange']) < 0.0 :
        print('Probability of NIFTY is going UP to ' ,nmp,file=open("NSEmarket.txt", "a"))
    elif float(nf_indiavix['pChange']) > 0.0 :
        print('Probability of NIFTY is going DOWN to ' ,nmn,file=open("NSEmarket.txt", "a"))
if float(nf_indiavix['lastPrice']) < (15.811+vixmpc) and float(nf_indiavix['lastPrice']) > 15.811:
    print("The VIX is High ",nf_indiavix['lastPrice'],file=open("NSEmarket.txt", "a"))
    if float(nf_indiavix['pChange']) < 0.0 :
        print('Probability of NIFTY is going UP to ' ,nmp,file=open("NSEmarket.txt", "a"))
    elif float(nf_indiavix['pChange']) > 0.0 :
        print('Probability of NIFTY is going DOWN to ' ,nmn,file=open("NSEmarket.txt", "a"))

#PCR put call ratio 1.68 to 1.8

#highest Open intrest strike price in put and call when Nifty reach at the strike price sell...


#For next 7 day Aprox nifty movment in persent:
vixdpc = (float(nf_indiavix['lastPrice'])/7) 
ndp = nf_n50['lastPrice']+vixdpc
ndn = nf_n50['lastPrice']-vixdpc
print("At this time Aprox NIFTY High is {} and low is {} ".format(ndp,ndn),file=open("NSEmarket.txt", "a"))


# Advances Declines
##It containes the number of rising stocks, falling stocks and unchanged stocks in a given trading day, per index.

adv_dec = nse.get_advances_declines()
#pprint(adv_dec)

# To make simple list from dictionarys used in above    
adv_dec_list=[]

for index in range(len(adv_dec)):
    for key in adv_dec[index]:
        if key == 'indice':
            #retrive each value
            adv_decid = adv_dec[index]['indice']
            adv_decad = adv_dec[index]['advances']
            adv_decdc = adv_dec[index]['declines']
            adv_decun = adv_dec[index]['unchanged']
            #appended values
            adv_dec_list.append([adv_decid,adv_decad,adv_decdc,adv_decun])
            
    
df_adv_declist = pd.DataFrame(adv_dec_list,columns=['Index Name','Advances','Declines','Unchanged'])        
df_adv_declist = pd.DataFrame(df_adv_declist).set_index('Index Name')
df_adv_declist.replace({None: 0.5}, inplace=True)


adv_dec30 = []

for ind in range(len(df_adv_declist)):
    if (float(df_adv_declist.iloc[ind][1])>= ((df_adv_declist.iloc[ind][0]+df_adv_declist.iloc[ind][1]+df_adv_declist.iloc[ind][2])*0.25)):
        itgo = "Declines are 25% than total index stocks "
        adv_dec30.append([itgo,df_adv_declist.index[ind],df_adv_declist.iloc[ind][1]])
        
if len(adv_dec30) >= len(df_adv_declist)*0.50:
    print('The Declines are more than 50% at time {} market are down'.format(endtime),file=open("NSEmarket.txt", "a"))
elif (len(adv_dec30) >= len(df_adv_declist)*0.30) and (len(adv_dec30) < len(df_adv_declist)*0.50):
    print('The Declines are more than 30% at time {} market are down'.format(endtime),file=open("NSEmarket.txt", "a"))
else:
    print('Advance and Decline are Positive',file=open("NSEmarket.txt", "a"))
    

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
   
if ((len(autonegt) < 2 and len(banknegt) < 8 and len(cementnegt) < 1 and len(costnegt) < 1 and len(fmcgnegt) < 2 and len(niornnegt) < 2 and len(nintnegt) < 2 and len(pharmanegt) < 1 and len(powernegt) < 2)):
    print('The sectors are up at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
elif(len(autonegt) > 0 and len(banknegt) > 0 and len(cementnegt) > 0 and len(costnegt) > 0 and len(fmcgnegt) > 0 and len(niornnegt) > 0 and len(nintnegt) > 0 and len(pharmanegt) > 0 and len(powernegt) >0 ):
    print('All sectors are down by avrage {} percent'.format(((len(autonegt) + len(banknegt) + len(cementnegt) + len(costnegt) + len(fmcgnegt) + len(niornnegt) + len(nintnegt) + len(pharmanegt) + len(powernegt))/137)*100),file=open("NSEmarket.txt", "a"))
else:
    print('Read full details follows',file=open("NSEmarket.txt", "a"))


if len(autonegt) > 0 :
    # Auto
    print ('Auto sector is {} down'.format((len(autonegt)/15)*100),file=open("NSEmarket.txt", "a"))
else:
    print ('Auto sector is up',file=open("NSEmarket.txt", "a"))


if len(banknegt) > 0 :
    print ('Bank sector is {} down'.format((len(banknegt)/38)*100),file=open("NSEmarket.txt", "a"))
else:
    print ('Bank sector is up',file=open("NSEmarket.txt", "a"))


if len(nintnegt) > 0 :
    print ('IT sector is {} down'.format((len(nintnegt)/11)*100),file=open("NSEmarket.txt", "a"))
else:
    print ('IT sector is up',file=open("NSEmarket.txt", "a"))


if len(cementnegt) > 0 :
    # Cement
    print ('Cement sector is {} down'.format((len(cementnegt)/6)*100),file=open("NSEmarket.txt", "a"))
else:
    print ('Cement sector is up',file=open("NSEmarket.txt", "a"))


if len(costnegt) > 0 :
    # Construction
    print ('Construction sector is {} down'.format((len(costnegt)/12)*100),file=open("NSEmarket.txt", "a"))
else:
    print ('Construction sector is up',file=open("NSEmarket.txt", "a"))

if len(fmcgnegt) > 0 :
    # FMCG
    print ('FMCG sector is {} down'.format((len(fmcgnegt)/15)*100),file=open("NSEmarket.txt", "a"))
else:
    print ('FMCG sector is up',file=open("NSEmarket.txt", "a"))

if len(niornnegt) > 0 :
    # Iorn
    print ('Iorn sector is {} down'.format((len(niornnegt)/18)*100),file=open("NSEmarket.txt", "a"))
else:
    print ('Iorn sector is up',file=open("NSEmarket.txt", "a"))

 
if len(pharmanegt) > 0 :
    # Pharma 
    print ('Pharma sector is {} down'.format((len(pharmanegt)/10)*100),file=open("NSEmarket.txt", "a"))
else:
    print ('Pharma sector is up',file=open("NSEmarket.txt", "a"))
  

if len(powernegt) > 0:
    # Power
    print ('Power sector is {} down'.format((len(powernegt)/12)*100),file=open("NSEmarket.txt", "a"))
else:
    print ('Power sector is up',file=open("NSEmarket.txt", "a"))
    

###################### IT sector Options ################################# 


nint_len = len(nintgrtz)+len(nintnegt)+len(nintinzero)

#nint PUT BUY Logic 
if (float(nf_nint['pChange']) <= 0.01) and (float(nf_nint['pChange']) >= -0.75):
    if len(nintnegt) >= (nint_len*0.7) :
        #print('Total negative are more than 70%')
        print('For IT sector BUY PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        
    else:
        print('Do not BUY IT sector PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('High Risk For IT sector BUY Call at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    

#nint PUT SELL Logic
if float(nf_nint['pChange']) < -0.75:
    if (len(nintnegt) >= (nint_len*0.4)) and (len(nintnegt) <= (nint_len*0.7)) :
        #print('Total negative are more than 70%')
        print('For IT sector SELL PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Do not SELL IT sector PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))     
        print('Medium Risk For IT sector CALL',file=open("NSEmarket.txt", "a"))        
    
#nint CALL BUY Logic  ##working correctly 
        
if float(nf_nint['pChange']) >= 0.01 and float(nf_nint['pChange']) < 0.75:
    if len(nintnegt) <= (nint_len*0.3) :
        #print('Total negative are less than 20%')
        print('For IT sector BUY CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Do not BUY IT sector CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('High risk For IT sector BUY PUT',file=open("NSEmarket.txt", "a"))
              
#nint CALL SELL Logic

        
if float(nf_nint['pChange']) >= 0.75:
    if len(nintnegt) <= (nint_len*0.4) :
        #print('Total negative are less than 20%',file=open("NSEmarket.txt", "a"))
        print('For IT sector SELL CALL time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Do not SELL IT sector CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('Medium Risk For IT sector BUY PUT ',file=open("NSEmarket.txt", "a"))
    

   
###################### N50 Options #################################

"""
# NIFTY sector indexs persent chages 
nseindexs = float(nf_auto['pChange'])+(float(nf_psubank['pChange']) + float(nf_pvtbank['pChange'])+float(nf_finser['pChange']))+float(nf_infra['pChange'])+float(nf_fmcg['pChange'])+float(nf_metal['pChange'])+float(nf_nint['pChange'])+float(nf_pharma['pChange'])+float(nf_energy['pChange'])  

sub divided according to sector contrigution in NIFTY 50  : 0.12+0.2+0.14+0.08+0.12+0.12+0.08+0.14
  
nseindexs = (float(nf_auto['pChange'])*0.12)+(float(nf_psubank['pChange']) + float(nf_pvtbank['pChange'])+float(nf_finser['pChange']))*0.2+float(nf_infra['pChange'])*0.14+float(nf_fmcg['pChange'])*0.08+float(nf_metal['pChange'])*0.12+float(nf_nint['pChange'])*0.12+float(nf_pharma['pChange'])*0.08+float(nf_energy['pChange'])*0.14  

"""

nseindexs = (float(nf_auto['pChange'])*0.12)+(float(nf_psubank['pChange']) + float(nf_pvtbank['pChange'])+float(nf_finser['pChange']))*0.2+float(nf_infra['pChange'])*0.14+float(nf_fmcg['pChange'])*0.08+float(nf_metal['pChange'])*0.12+float(nf_nint['pChange'])*0.12+float(nf_pharma['pChange'])*0.08+float(nf_energy['pChange'])*0.14  

print ('NIFTY 50 index {} and NIFTY Sector index is {}'.format(nf_n50['pChange'],nseindexs),file=open("NSEmarket.txt", "a"))

n50_len = len(n50grtz)+len(n50negt)+len(n50inzero)

#n50 PUT BUY Logic 
if float(nf_n50['pChange']) <= 0.01 and float(nf_n50['pChange']) > -0.75:
    if len(n50negt) >= (n50_len*0.7) :
        #print('Total negative are more than 70%')
        n50PEITM = ndp
        n50PEATM = (nf_n50['lastPrice'])
        n50PEOTM = ndn
        print('For NIFTY 50 BUY PUT range are {} ATM {} ITM {} OTM at time {}'.format(n50PEATM,n50PEITM,n50PEOTM,endtime),file=open("NSEmarket.txt", "a"))
        
    else:
        print('Do not BUY NIFTY 50 PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('High Risk For NIFTY 50 BUY Call',file=open("NSEmarket.txt", "a"))
    

#n50 PUT SELL Logic
if float(nf_n50['pChange']) <= -0.75 and float(nseindexs) < 0.0:
    if (len(n50negt) >= (n50_len*0.4)) and (len(n50negt) <= (n50_len*0.7)) :
        #print('Total negative are more than 70%')
        n50PEITM = ndp
        n50PEATM = (nf_n50['lastPrice'])
        n50PEOTM = ndn
        print('For NIFTY 50 SELL PUT range are {} ATM {} ITM {} OTM at time {}'.format(n50PEATM,n50PEITM,n50PEOTM,endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Do not SELL NIFTY 50  PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))     
        print('Medium Risk For NIFTY BUY CALL',file=open("NSEmarket.txt", "a"))
        
    
#n50 CALL BUY Logic  ##working correctly 
        
if float(nf_n50['pChange']) >= 0.01 and float(nf_n50['pChange']) < 1 and float(nseindexs) > 0.0:
    if len(n50negt) <= (n50_len*0.30) :
        #print('Total negative are less than 30%')
        n50CEITM = (ndn) 
        n50CEATM = (nf_n50['lastPrice'])
        n50CEOTM = (ndp)
        print('For NIFTY 50 BUY CALL range are {} ATM {} ITM {} OTM at time {}'.format(n50CEATM,n50CEITM,n50CEOTM,endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Medium Risk to buy NIFTY 50  CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('High risk For NIFTY 50 BUY PUT',file=open("NSEmarket.txt", "a") )
              
#n50 CALL SELL Logic

        
if float(nf_n50['pChange']) >= 1:
    if len(n50negt) <= (n50_len*0.4) :
        #print('Total negative are less than 20%')
        n50CEITM = (ndn) 
        n50CEATM = (nf_n50['lastPrice'])
        n50CEOTM = (ndp)
        print('For NIFTY SELL CALL range are {} ATM {} ITM {} OTM at time {}'.format(n50CEATM,n50CEITM,n50CEOTM,endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Do not SELL NIFTY 50 CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('Medium Risk For NIFTY 50 BUY PUT ',file=open("NSEmarket.txt", "a"))
    

    
######################## NBANK Options ###################################

bank_len = (len(bankgrtz)+len(banknegt)+len(bankinzero))
bnseindexs = (float(nf_psubank['pChange']) * 0.25 + float(nf_pvtbank['pChange']) * 0.74 + float(nf_finser['pChange'])*0.01)

print ('BANK NIFTY index {} and BANKIFTY Sector index is {}'.format(nf_bank['pChange'],bnseindexs),file=open("NSEmarket.txt", "a"))

#For future prediction depend on NIFTY PSU Bank & PVT Bank Indexs    

if float(nf_psubank['pChange']) > 0.25 and float(nf_pvtbank['pChange']) > 0.75 and float(nf_finser['pChange']) > 0.0:
    print('Bank sector are in positive at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    if len(banknegt) > (bank_len*0.2):
        print('NSE Bank sector is going Down but trend is positive',file=open("NSEmarket.txt", "a"))
    else:
        print('Bank sector are in positive at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
elif float(nf_psubank['pChange']) < 0.25 and float(nf_pvtbank['pChange']) < 0.75 and float(nf_finser['pChange']) < 0.0:
    print('Bank sector are in negative at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    if (len(banknegt) > (bank_len*0.4)) and (len(banknegt) < (bank_len*0.70)):
        print('NSE Bank sector is going Down and trend is negative at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    if len(banknegt) > (bank_len*0.70):
        print('NSE Bank sector is going Down and trend is highly negative at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Bank sector are in positive and trend is negative at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
else:
    print('Bank sector is sideways at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))


#BANK PUT BUY Logic depend on NIFTY Bank Index
if (float(nf_bank['pChange']) > -1) and (float(nf_bank['pChange']) <= 0.01):
    if len(banknegt) >= (bank_len*0.55) :
        #print('Total negative are more than 55%')
        bankPEITM = (nf_bank['lastPrice']+500) 
        bankPEATM = (nf_bank['lastPrice'])
        bankPEOTM = (nf_bank['lastPrice']-500)
        print('For BANK NIFTY BUY PUT range are {} ATM {} ITM {} OTM at time {}'.format(bankPEATM,bankPEITM,bankPEOTM,endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Do not BUY BANKNIFTY PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('High Risk For BANK NIFTY BUY CALL',file=open("NSEmarket.txt", "a"))
        

#Bank PUT SELL Logic depend on NIFTY Bank Index
if float(nf_bank['pChange']) <= -1:
    if len(banknegt) >= (bank_len*0.4) :
        #print('Total negative are more than 70%')
        bankPEITM = (nf_bank['lastPrice']+100) 
        bankPEATM = (nf_bank['lastPrice'])
        bankPEOTM = (nf_bank['lastPrice']-100)
        print('For BANK NIFTY SELL PUT range are {} ATM {} ITM {} OTM at time {}'.format(bankPEATM,bankPEITM,bankPEOTM,endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Do not SELL BANKNIFTY  PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('Medium Risk For BANK NIFTY buy CALL',file=open("NSEmarket.txt", "a"))

#Bank CALL BUY Logic depend on NIFTY Bank Index
        
if (float(nf_bank['pChange']) >= 0.01) and (float(nf_bank['pChange']) < 1):
    if len(banknegt) <= (bank_len*0.3) :
        #print('Total negative are less than 20%')
        bankCEITM = (nf_bank['lastPrice']-100) 
        bankCEATM = (nf_bank['lastPrice'])
        bankCEOTM = (nf_bank['lastPrice']+100)
        print('For BANK NIFTY BUY CALL range are {} ATM {} ITM {} OTM at time {}'.format(bankCEATM,bankCEITM,bankCEOTM,endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Do not BUY BANKNIFTY CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('Medium Risk For BANK NIFTY BUY PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
#Bank CALL SELL Logic depend on NIFTY Bank Index
        
if float(nf_bank['pChange']) >= 1:
    if len(banknegt) <= (bank_len*0.5) :
        #print('Total negative are less than 40%')
        bankCEITM = (nf_bank['lastPrice']-50) 
        bankCEATM = (nf_bank['lastPrice'])
        bankCEOTM = (nf_bank['lastPrice']+50)
        print('For BANK NIFTY SELL CALL range are {} ATM {} ITM {} OTM at time {}'.format(bankCEATM,bankCEITM,bankCEOTM,endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Do not SELL BANKNIFTY CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('High Risk For BANK NIFTY BUY PUT',file=open("NSEmarket.txt", "a"))

################################### End of BOT ############################################
print('End Time of BOT',endtime,file=open("NSEmarket.txt", "a"))
print('End Time of BOT',endtime)
print('',file=open("NSEmarket.txt", "a"))
print('End of BOT')