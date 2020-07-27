# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 08:00:12 2020

@author: Sangram Phadke
"""

# ######################## Creating U.S index ########################################

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
import yfinance as yf
import math
from datetime import datetime
print('###############################################################################',file=open("USmarket.txt", "a"))
starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull start time
pst = datetime.now().strftime("%H:%M")
day = datetime.now().strftime("%A")
daydate = datetime.now().strftime("%d")
if day == str('Monday'):
    print('US Markets On Friday: ',file=open("USmarket.txt", "a"))

    


print('Start time of BOT',starttime,file=open("USmarket.txt", "a"))

print('Start data pull from Yahoo server at time ',starttime)

#United states index
sp500 = yf.Ticker("^GSPC")
nf_sp500 = sp500.info
nf_sp500pcr = float(((((nf_sp500['dayLow']+nf_sp500['dayHigh'])/2)-nf_sp500['previousClose'])/nf_sp500['previousClose'])*100)
nf_sp500pc = format(nf_sp500pcr,'.2f')
print('US S&P 500 index is {} and percent change is {}'.format(nf_sp500['dayLow'],nf_sp500pc))

dow = yf.Ticker("^DJI")
nf_dow = dow.info
nf_dowpcrr = float((((nf_dow['dayLow']+nf_dow['dayHigh'])/2-nf_dow['previousClose'])/nf_dow['previousClose'])*100)
nf_dowpc = format(nf_dowpcrr,'.2f')
#print('US DOW index is {} and percent change is {}'.format(nf_dow['dayLow'],nf_dowpc))

nasd = yf.Ticker("^IXIC")
nf_nasd = nasd.info
nf_nasdpcr = float((((nf_nasd['dayLow']+nf_nasd['dayHigh'])/2-nf_nasd['previousClose'])/nf_nasd['previousClose'])*100)
nf_nasdpc = format(nf_nasdpcr,'.2f')
#print('US Nasdaq Composite index is {} and percent change is {}'.format(nf_nasd['dayLow'],nf_nasdpc))


#United states Sectors


#Dow Jones U.S. Bank Index
dowbank = yf.Ticker("^DJUSBK")
nf_dowbank = dowbank.info
nf_dowbankpcr = float((((nf_dowbank['dayLow']+nf_dowbank['dayHigh'])/2-nf_dowbank['previousClose'])/nf_dowbank['previousClose'])*100)
nf_dowbankpc = format(nf_dowbankpcr,'.2f')
#print('US Bank sector index is {} and percent change is {}'.format(nf_dowbank['dayLow'],nf_dowbankpc))


#Dow Jones U.S. IT Index
dowit = yf.Ticker("^DJUSTC")
nf_dowit = dowit.info
nf_dowitpcr = float((((nf_dowit['dayLow']+nf_dowit['dayHigh'])/2-nf_dowit['previousClose'])/nf_dowit['previousClose'])*100)
nf_dowitpc = format(nf_dowitpcr,'.2f')
#print('US IT sector index is {} and percent change is {}'.format(nf_dowit['dayLow'],nf_dowitpc))

#Dow Jones U.S. Pharma Index
dowph = yf.Ticker("^DJUSPR")
nf_dowph = dowph.info
nf_dowphpcr = float((((nf_dowph['dayLow']+nf_dowph['dayHigh'])/2-nf_dowph['previousClose'])/nf_dowph['previousClose'])*100)
nf_dowphpc = format(nf_dowphpcr,'.2f')
#print('US Pharma sector index is {} and percent change is {}'.format(nf_dowph['dayLow'],nf_dowphpc))

#Dow Jones U.S. Phara & bio Index
dowpb = yf.Ticker("^DJUSPN")
nf_dowpb = dowpb.info
nf_dowpbpcr = float((((nf_dowpb['dayLow']+nf_dowpb['dayHigh'])/2-nf_dowpb['previousClose'])/nf_dowpb['previousClose'])*100)
nf_dowpbpc = format(nf_dowpbpcr,'.2f')
#print('US Pharma & Biotech sector index is {} and percent change is {}'.format(nf_dowpb['dayLow'],nf_dowpbpc))

#Dow Jones U.S. Automobiles Inde (^DJUSAU)
dowau = yf.Ticker("^DJUSAU")
nf_dowau = dowpb.info
nf_dowauar = float((((nf_dowau['dayLow']+nf_dowau['dayHigh'])/2-nf_dowau['previousClose'])/nf_dowau['previousClose'])*100)
nf_dowaua = format(nf_dowauar,'.2f')
#print('US Auto sector index is {} and percent change is {}'.format(nf_dowau['dayLow'],nf_dowaua))

#Dow Jones U.S. Oil & Gas Index (^DJUSEN)
dowen = yf.Ticker("^DJUSEN")
nf_dowen = dowen.info
nf_dowener = float((((nf_dowen['dayLow']+nf_dowen['dayHigh'])/2-nf_dowen['previousClose'])/nf_dowen['previousClose'])*100)
nf_dowene = format(nf_dowener,'.2f')
#print('US Oil& Gas sector index is {} and percent change is {}'.format(nf_dowen['dayLow'],nf_dowene))

#(^DJUSCN)Dow Jones US Construction & Materials Index
dowcn = yf.Ticker("^DJUSCN")
nf_dowcn = dowcn.info
nf_dowcncr = float((((nf_dowcn['dayLow']+nf_dowcn['dayHigh'])/2-nf_dowcn['previousClose'])/nf_dowcn['previousClose'])*100)
nf_dowcnc = format(nf_dowcncr,'.2f')

#print('US Construction sector index is {} and percent change is {}'.format(nf_dowcn['dayLow'],nf_dowcnc))

#Dow Jones US Food & Beverages Index
dowfm = yf.Ticker("^DJUSFB")
nf_dowfm = dowfm.info
nf_dowfmfr = float((((nf_dowfm['dayLow']+nf_dowfm['dayHigh'])/2-nf_dowfm['previousClose'])/nf_dowfm['previousClose'])*100)
nf_dowfmf = format(nf_dowfmfr,'.2f')
#print('US FMCG sector index is {} and percent change is {}'.format(nf_dowfm['dayLow'],nf_dowfmf))

# Volatility Index VIX (^VIX)
usvix = yf.Ticker("^VIX")
nf_usvix = usvix.info
nf_usvixfr = float((((nf_usvix['dayLow']+nf_usvix['dayHigh'])/2-nf_usvix['previousClose'])/nf_usvix['previousClose'])*100)
nf_usvixf = format(nf_usvixfr,'.2f')

# apend values in csv file 

print(nf_usvixfr,file=open("USVIX.csv", "a"))


#print('US VIX index is {} and percent change is {}'.format(nf_usvix['dayLow'],nf_usvixf))




#United states futures

nqf = yf.Ticker("NQ=F")
nf_nqf = nqf.info
nf_nqfpcr = float((((nf_nqf['dayLow']+nf_nqf['dayHigh'])/2-nf_nqf['previousClose'])/nf_nqf['previousClose'])*100)
nf_nqfpc = format(nf_nqfpcr,'.2f')
#print('US NQ FUTURE index is {} and percent change is {}'.format(nf_nqf['dayLow'],nf_nqfpc))


spf = yf.Ticker("ES=F")
nf_spf = spf.info
nf_spfpcr = float((((nf_spf['dayLow']+nf_spf['dayHigh'])/2-nf_spf['previousClose'])/nf_spf['previousClose'])*100)
nf_spfpc = format(nf_spfpcr,'.2f')
#print('US S&P FUTURE index is {} and percent change is {}'.format(nf_spf['dayLow'],nf_spfpc))


dowf = yf.Ticker("YM=F")
nf_dowf = dowf.info
nf_dowfpcr = float((((nf_dowf['dayLow']+nf_dowf['dayHigh'])/2-nf_dowf['previousClose'])/nf_dowf['previousClose'])*100)
nf_dowfpc = format(nf_dowfpcr,'.2f')
#print('US DOW FUTURE index is {} and percent change is {}'.format(nf_dowf['dayLow'],nf_dowfpc))


################################### US analysis ###########################################

# Index

print('',file=open("USmarket.txt", "a"))
print('US Nasdaq Composite index is {} and percent change is {}'.format(nf_nasd['dayLow'],nf_nasdpc),file=open("USmarket.txt", "a"))
print('US DOW index is {} and percent change is {}'.format(nf_dow['dayLow'],nf_dowpc),file=open("USmarket.txt", "a"))
print('US S&P 500 index is {} and percent change is {}'.format(nf_sp500['dayLow'],nf_sp500pc),file=open("USmarket.txt", "a"))
print('',file=open("USmarket.txt", "a"))

# Sectors

print('US Pharma & Biotech sector index is {} and percent change is {}'.format(nf_dowpb['dayLow'],nf_dowpbpc),file=open("USmarket.txt", "a"))
print('US Pharma sector index is {} and percent change is {}'.format(nf_dowph['dayLow'],nf_dowphpc),file=open("USmarket.txt", "a"))
print('US IT sector index is {} and percent change is {}'.format(nf_dowit['dayLow'],nf_dowitpc),file=open("USmarket.txt", "a"))
print('US Bank sector index is {} and percent change is {}'.format(nf_dowbank['dayLow'],nf_dowbankpc),file=open("USmarket.txt", "a"))
print('US Auto sector index is {} and percent change is {}'.format(nf_dowau['dayLow'],nf_dowaua),file=open("USmarket.txt", "a"))
print('US Oil& Gas sector index is {} and percent change is {}'.format(nf_dowen['dayLow'],nf_dowene),file=open("USmarket.txt", "a"))
print('US Construction sector index is {} and percent change is {}'.format(nf_dowcn['dayLow'],nf_dowcnc),file=open("USmarket.txt", "a"))
print('US FMCG sector index is {} and percent change is {}'.format(nf_dowfm['dayLow'],nf_dowfmf),file=open("USmarket.txt", "a"))

print('',file=open("USmarket.txt", "a"))

# Futures

print('US DOW FUTURE index is {} and percent change is {}'.format(nf_dowf['dayLow'],nf_dowfpc),file=open("USmarket.txt", "a"))
print('US S&P FUTURE index is {} and percent change is {}'.format(nf_spf['dayLow'],nf_spfpc),file=open("USmarket.txt", "a"))
print('US NQ FUTURE index is {} and percent change is {}'.format(nf_nqf['dayLow'],nf_nqfpc),file=open("USmarket.txt", "a"))
print('',file=open("USmarket.txt", "a"))

uspcr = (nf_nasdpcr+nf_dowpcrr+nf_sp500pcr+nf_dowpbpcr+nf_dowphpcr+nf_dowitpcr+nf_dowbankpcr+nf_dowfpcr+nf_spfpcr+nf_nqfpcr)

uspcrr = uspcr/10
uspc = format(uspcrr,'.2f')

print('Total Persent Change in all US Index,sector & future is {}'.format(uspcr))
print('Average Percent Change in all US Index and sector & future is {}'.format(uspc),file=open("USmarket.txt", "a"))

print('',file=open("USmarket.txt", "a"))

print('US VIX index is {} and percent change is {}'.format(nf_usvix['dayLow'],nf_usvixf),file=open("USmarket.txt", "a"))

print('',file=open("USmarket.txt", "a"))


################################### End of BOT ############################################
        
endtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull end time
print('End Time of BOT',endtime,file=open("USmarket.txt", "a"))
print('',file=open("USmarket.txt", "a"))
print('End of BOT')

###########################################################################################

"""
Future imlimentation 

# #Creating data frame for Yahoo Finance index stocks

# dr_yus = pd.read_csv('USIndexYsymbols.csv',index_col = 'ysymbols')
# df_yus = pd.DataFrame(data=dr_yus)

# df_yusc = df_yus[0:2]

# yusindex = []
# for i,r in df_yusc.iterrows():
#     yus =  yf.Ticker(i)
#     yusi = yus.info
#     yusindex.append(yusi) 

# # To make simple list from dictionarys used in above    
# nislist=[]

# for index in range(len(nis)):
#     for key in nis[index]:
#         if key == 'symbol':
#             #retrive each value
#             ins = nis[index]['symbol']
#             icn = nis[index]['companyName']
#             iop = nis[index]['open']
#             iltp = nis[index]['lastPrice']
#             ipc = nis[index]['pChange']
            
#             #appended values
#             nislist.append([ins,icn,iop,iltp,ipc])
    
# df_nislist = pd.DataFrame(nislist,columns=['symbol','Company Name','Open price','LTP','precent change'] )        
# df_nislist = pd.DataFrame(df_nislist).set_index('symbol')
# df_nislist.replace({None: 0.5}, inplace=True)

"""
