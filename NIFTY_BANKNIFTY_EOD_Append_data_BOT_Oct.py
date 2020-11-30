# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:03:00 2020

@author: Sangram Phadke
"""

#Importing the libraries

import numpy as np
import pandas as pd
from datetime import date
from nsepy import get_history
from datetime import datetime

Starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull start time


ddn = datetime.now().strftime("%d")
dmn = datetime.now().strftime("%m")
dyn = datetime.now().strftime("%Y")

dd = int(ddn)
dm = int(dmn)
dy = int(dyn)


indexvix = get_history(symbol="INDIAVIX",
            start=date(dy,dm-1,1),
            end=date(dy,dm,dd),
            index=True)


nifty_50 = get_history(symbol="NIFTY 50",
                            start=date(dy,dm-1,1),
                            end=date(dy,dm,dd),
                            index=True)

banknifty = get_history(symbol="NIFTY BANK",
                            start=date(dy,dm-1,1),
                            end=date(dy,dm,dd),
                            index=True)


# Date	Day	Open	High	Low	Close	Yclose	up	down	side	VIXOpen	VIXHigh	VIXLow	VIXClose	VIXPclose

#columns to be updated 

nfov = nifty_50.iloc[-1][0]
nfhv = nifty_50.iloc[-1][1]
nflv = nifty_50.iloc[-1][2]
nfcv = nifty_50.iloc[-1][3]

nfycv = nifty_50.iloc[-2][3]

if nfcv > nfycv*1.015:
    nfup = 1
    nfdown = 0
    nfside = 0
elif nfcv < (nfycv-(nfycv*0.015)):
    nfup = 0
    nfdown = 1
    nfside = 0
elif nfcv < nfycv*1.015 and nfcv > (nfycv-(nfycv*0.015)):
    nfup = 0
    nfdown = 0
    nfside = 1
    
    
nfovix = indexvix.iloc[-1][0]
nfhvix = indexvix.iloc[-1][1]
nflvix = indexvix.iloc[-1][2]
nfcvix = indexvix.iloc[-1][3]
nfycvix = indexvix.iloc[-1][4]

pdate = (nifty_50.index[-1]).strftime("%d-%m-%Y")
day = (nifty_50.index[-1]).strftime("%A")
print(('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(pdate,day,nfov,nfhv,nflv,nfcv,nfycv,nfup,nfdown,nfside,nfovix,nfhvix,nflvix,nfcvix,nfycvix)),file=open('NIFTY_50_Data_Jan2000To2020.csv', "a"))

bnov = banknifty.iloc[-1][0]
bnhv = banknifty.iloc[-1][1]
bnlv = banknifty.iloc[-1][2]
bncv = banknifty.iloc[-1][3]
bnycv = banknifty.iloc[-2][3]

if bncv > bnycv*1.015:
    bnup = 1
    bndown = 0
    bnside = 0
elif bncv < (bnycv-(bnycv*1.015)):
    bnup = 0
    bndown = 1
    bnside = 0
elif bncv < bnycv*1.015 and bncv > (bnycv-(bnycv*1.015)):
    bnup = 0
    bndown = 0
    bnside = 1


pdate = (banknifty.index[-1]).strftime("%d-%m-%Y")
day = (banknifty.index[-1]).strftime("%A")
print(('{},{},{},{},{},{},{},{},{},{}'.format(pdate,day,bnov,bnhv,bnlv,bncv,bnycv,bnup,bndown,bnside)),file=open('BANKNIFTY_Data_Jan2000To2020.csv', "a"))
