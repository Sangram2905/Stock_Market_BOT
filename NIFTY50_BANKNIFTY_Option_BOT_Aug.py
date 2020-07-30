# # -*- coding: utf-8 -*-
# """
# Created on Wed Jun 24 16:29:26 2020

# @author: Sangram Phadke
# """

# #Simple CALL & PUT suggestion based on NSE Index Direction notifier BOT


# Run time 09:10 , 09:20 : 10:00 , 11:00 , 12:00 , 13:00 , 14:00, 15:00, 15:35

# Output is Text file name "NSEmarket.txt"

################################################# NSE DATA PULL start #################################################

# Importing the libraries
import numpy as np
import pandas as pd
from nsetools import Nse
import math
#from pprint import pprint # just for neatness of display
from datetime import datetime



print('############################################################################',file=open("NSEmarket.txt", "a"))
print('',file=open("NSEmarket.txt", "a"))
starttime = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #program data pull start time
pst = datetime.now().strftime("%H:%M")
day = datetime.now().strftime("%A")
daydate = datetime.now().strftime("%d")
print('AI Result Start Time',starttime,file=open("NSEmarket.txt", "a"))
print('Main Program')
print('Disclaimer: All posts are Technology demonstration its not an Financial advice.',file=open("NSEmarket.txt", "a"))
print('Read full Disclaimer at start of the Channel',file=open("NSEmarket.txt", "a"))
print('Overview of Todays Market at time: ',pst,file=open("NSEmarket.txt", "a"))
print('',file=open("NSEmarket.txt", "a"))
print('Start data pull from NSE server at time ',starttime)
      
print('',file=open("NSEmarket.txt", "a"))

   
# Importing the NIFTY dataset from NSE live site / portel 

nse = Nse()  # NSE object creation

#print (nse)

#listallindex = nse.get_index_list()
#lotsize = nse.get_fno_lot_sizes()

#riskmoney = float(input("Enter the Risk/Max Money for trade : "))
riskmoney =5000

# Following variables are use in Option range and risk money caluculations
crkr =0 
prkr = 0
cbrkr = 0
pbrkr = 0
rkr = 0
brkr = 0
bcorm = 0
bporm = 0 
nporm = 0
ncorm = 0

#NIFTY indexs current values


nf_indiavix = nse.get_index_quote("INDIA VIX") 
print('INDIA VIX  index current value is {} and percent change is {} '.format(nf_indiavix['lastPrice'],nf_indiavix['pChange'],'.2f')) 


nf_n50 = nse.get_index_quote("nifty 50") 
print('NIFTY 50   index current value is {} and percent change is {} '.format(nf_n50['lastPrice'],nf_n50['pChange'])) 


nf_nxt50 = nse.get_index_quote("NIFTY NEXT 50") 
print('NIFTY NEXT 50 index current value is {} and percent change is {} '.format(nf_nxt50['lastPrice'],nf_nxt50['pChange'],'.2f')) 

nf_bank = nse.get_index_quote("nifty bank") 
print('NIFTY BANK index current value is {} and percent change is {} '.format(nf_bank['lastPrice'],nf_bank['pChange'])) 

nf_psubank = nse.get_index_quote("nifty psu bank") 
#print('NIFTY PSU BANK index current value is {} and percent change is {} '.format(nf_psubank['lastPrice'],nf_psubank['pChange'])) 

nf_pvtbank = nse.get_index_quote("nifty pvt bank") 
#print('NIFTY PVT BANK index current value is {} and percent change is {} '.format(nf_pvtbank['lastPrice'],nf_pvtbank['pChange'])) 

nf_finser = nse.get_index_quote("nifty fin service") 
#print('NIFTY Financial service index current value is {} and percent change is {} '.format(nf_finser['lastPrice'],nf_finser['pChange'])) 

nf_auto = nse.get_index_quote("nifty auto") 
#print('NIFTY Auto index current value is {} and percent change is {} '.format(nf_auto['lastPrice'],nf_auto['pChange'])) 

nf_pharma = nse.get_index_quote("nifty pharma") 
#print('NIFTY Pharma index current value is {} and percent change is {} '.format(nf_pharma['lastPrice'],nf_pharma['pChange'])) 

nf_nint = nse.get_index_quote("nifty it") 
#print('NIFTY IT   index current value is {} and percent change is {} '.format(nf_nint['lastPrice'],nf_nint['pChange'])) 

nf_fmcg = nse.get_index_quote("nifty fmcg") 
#print('NIFTY fmcg   index current value is {} and percent change is {} '.format(nf_fmcg['lastPrice'],nf_fmcg['pChange'])) 

nf_energy = nse.get_index_quote("nifty energy") 
#print('NIFTY Energy   index current value is {} and percent change is {} '.format(nf_energy['lastPrice'],nf_energy['pChange'])) 

nf_metal= nse.get_index_quote("nifty metal") 
#print('NIFTY metal index current value is {} and percent change is {} '.format(nf_metal['lastPrice'],nf_metal['pChange'])) 

nf_infra= nse.get_index_quote("nifty infra") 
#print('NIFTY Infra index current value is {} and percent change is {} '.format(nf_infra['lastPrice'],nf_infra['pChange'])) 

nf_consum = nse.get_index_quote("NIFTY CONSUMPTION")
#print('NIFTY CONSUMPTION index current value is {} and percent change is {} '.format(nf_consum['lastPrice'],nf_consum['pChange'])) 

nf_cpse = nse.get_index_quote("nifty CPSE")
#print('NIFTY CPSE index current value is {} and percent change is {} '.format(nf_cpse['lastPrice'],nf_cpse['pChange'])) 

nf_commoditi = nse.get_index_quote("NIFTY COMMODITIES")
#print('NIFTY COMMODITIES index current value is {} and percent change is {} '.format(nf_commoditi['lastPrice'],nf_commoditi['pChange'])) 

nf_servsec = nse.get_index_quote("NIFTY SERV SECTOR")
#print('NIFTY SERVICE SECTOR index current value is {} and percent change is {} '.format(nf_servsec['lastPrice'],nf_servsec['pChange'])) 

nf_media = nse.get_index_quote("NIFTY MEDIA")
#print('NIFTY media SECTOR index current value is {} and percent change is {} '.format(nf_media['lastPrice'],nf_media['pChange'])) 

nf_midcap = nse.get_index_quote("NIFTY MIDCAP 100")
#print('NIFTY Midcap 100 index current value is {} and percent change is {} '.format(nf_midcap['lastPrice'],nf_midcap['pChange'])) 


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
    
df_nislist = pd.DataFrame(nislist,columns=['symbol','Company Name','Open price','LTP','percent change'] )        
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
    
df_banklist = pd.DataFrame(banklist,columns=['symbol','Company Name','Open price','LTP','percent change'] )        
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

print("NSE Bank stocks whre {} are greater than one, {} are negative , {} are in zeros".format(len(bankgrtz),len(banknegt),len(bankinzero)))



######### Advances Declines
##It containes the number of rising stocks, falling stocks and unchanged stocks in a given trading day, per index.

adv_dec = nse.get_advances_declines()

#pprint(adv_dec)


#####################################  End of dat pull from NSE  ###############################

## End of data pull from NSE
        
endtime = datetime.now().strftime("%H:%M") #program data pull end time
bot_endtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print('End of data pull from NSE at time ',endtime)

######################################  Main Logic ##########################################


###### Advances Declines
##It containes the number of rising stocks, falling stocks and unchanged stocks in a given trading day, per index.

#adv_dec = nse.get_advances_declines()

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

# Total 59 are max A_D added in below list if criteria match.
adv_dec30 = []
print('Advances Declines calculated for All NIFTY INDEX from NIFTY 50 to NIFT 200: ',file=open("NSEmarket.txt", "a"))

for ind in range(len(df_adv_declist)):
    if (float(df_adv_declist.iloc[ind][1])>= ((df_adv_declist.iloc[ind][0]+df_adv_declist.iloc[ind][2]))):
        adv_dec30.append([df_adv_declist.index[ind],df_adv_declist.iloc[ind][1]])
        
if len(adv_dec30) >= len(df_adv_declist)*0.30:
    print('All NIFTY INDEXs Declines are {} at time {}'.format(len(adv_dec30),endtime),file=open("NSEmarket.txt", "a"))
else:
    print('In Advance_Decline: Declines are {} and Positive at time {} '.format(len(adv_dec30),endtime),file=open("NSEmarket.txt", "a"))
    
print('',file=open("NSEmarket.txt", "a"))

## Sector %change

financial_service =(float(nf_psubank['pChange']) + float(nf_pvtbank['pChange'])+float(nf_finser['pChange']))/3
print ('Bank sector is at {} %'.format(format(financial_service,'.2f')),file=open("NSEmarket.txt", "a"))

info_tech = float(nf_nint['pChange'])
print ('IT sector is at {} %'.format(info_tech),file=open("NSEmarket.txt", "a"))

consumer_goods = ((float(nf_fmcg['pChange'])+float(nf_consum['pChange'])))/2
print ('FMCG sector is at {} %'.format(format(consumer_goods,'.2f')),file=open("NSEmarket.txt", "a"))


automobile = float(nf_auto['pChange'])
print ('Auto sector is at {} %'.format(automobile),file=open("NSEmarket.txt", "a"))


pharma = float(nf_pharma['pChange'])
print ('Pharma sector is at {} %'.format(pharma),file=open("NSEmarket.txt", "a"))


metals = float(nf_metal['pChange'])
print ('Metal sector is at {} %'.format(metals),file=open("NSEmarket.txt", "a"))

oil_gas = (float(nf_cpse['pChange']))
print ('Oil and Gas sector is at {} %'.format(oil_gas),file=open("NSEmarket.txt", "a"))
    
power = (float(nf_energy['pChange']))
print ('Power sector is at {} %'.format(power),file=open("NSEmarket.txt", "a"))
            
constuction = float(nf_infra['pChange'])
print ('Construction sector is at {} %'.format(constuction),file=open("NSEmarket.txt", "a"))

commoditi =  float(nf_commoditi['pChange'])
print ('Commodity sector is at {} %'.format(commoditi),file=open("NSEmarket.txt", "a"))
   
services_telecom = float(nf_servsec['pChange'])    
print ('Services sector is at {} %'.format(services_telecom),file=open("NSEmarket.txt", "a"))

media = float(nf_media['pChange'])
print ('Media sector is at {} %'.format(media),file=open("NSEmarket.txt", "a"))

print('',file=open("NSEmarket.txt", "a"))


if day == str('Thursday'):
    if int(daydate) < 24:
        print('Today is Weekly option expiry day : Carefully trade todays expiry day Call or Put options',file=open("NSEmarket.txt", "a"))
        print('The Call or Put options suggested for next week Date',file=open("NSEmarket.txt", "a"))
    if int(daydate) >=24:
        print('Today is Monthly option expiry day : Carefully trade todays expiry day Call or Put options',file=open("NSEmarket.txt", "a"))
    
## Options   

print('Todays options trades at time {} are as follows'.format(endtime),file=open("NSEmarket.txt", "a")) 
print('',file=open("NSEmarket.txt", "a"))  
   
###################### N50 Options #################################


print('For NIFTY 50 Options',file=open("NSEmarket.txt", "a"))

print('The NIFTY 50 weekly per lot ATM Option price calculated on Rs. 5000 margin Money \n',file=open("NSEmarket.txt", "a"))

print('You can increase or decrease per lot Option price & strick price depends on your daily margin Money & Risk',file=open("NSEmarket.txt", "a"))

print('',file=open("NSEmarket.txt", "a"))

#India volatity index
#print('INDIA VIX  index current value is {} and percent change is {} '.format(nf_indiavix['lastPrice'],nf_indiavix['pChange'])) 

#When the vix is go up probability of market direction is continty of same direction is high
#When the vix is % the probability of market direction is continty of same direction is low

# VIX is the persent NIFTY 50 move in positive or negative  // range of trande

# dr_indiavix = pd.read_csv('INDIA_VIX.csv')
# df_indiavix = pd.DataFrame(data=dr_indiavix)


print('NIFTY 50 index current value is {} and percent change is {} '.format(nf_n50['lastPrice'],nf_n50['pChange']),file=open("NSEmarket.txt", "a")) 
print('',file=open("NSEmarket.txt", "a"))    
print("NIFTY 50 stocks where {} are greater than one, {} are negative , {} are in zero percent change".format(len(n50grtz),len(n50negt),len(n50inzero)),file=open("NSEmarket.txt", "a"))
print('',file=open("NSEmarket.txt", "a"))
# NSE all sector indexs belong to NIFTY 50 with respected persent chages are  

financial_service_ni =(float(nf_psubank['pChange']) + float(nf_pvtbank['pChange'])+float(nf_finser['pChange']))*(34.48/100)
info_tech_ni = float(nf_nint['pChange'])*(14.17/100)
consumer_goods_ni = (float(nf_fmcg['pChange'])+float(nf_consum['pChange']))*(13.46/100)
automobile_ni = float(nf_auto['pChange'])*(5.52/100)
pharma_ni = float(nf_pharma['pChange'])*(3.03/100)
metals_ni = float(nf_metal['pChange'])*(2.48/100)
oil_gas_power_ni = (float(nf_energy['pChange'])+float(nf_cpse['pChange']))*(16.86/100)
constuction_ni = float(nf_infra['pChange'])*(2.66/100)
cement_ni =  float(nf_commoditi['pChange'])*(2.31/100)   
services_telecom_ni = float(nf_servsec['pChange'])*(4.13/100)    
media_ni = float(nf_media['pChange'])*(0.36/100)
fertilisers_ni = float(nf_midcap['pChange'])*(0.54/100)


nseindexsr = float(financial_service_ni+info_tech_ni+consumer_goods_ni+automobile_ni+pharma_ni+metals_ni+oil_gas_power_ni+constuction_ni+cement_ni+services_telecom_ni+media_ni+fertilisers_ni)

nseindexs = format(nseindexsr,'.2f')

print ('NIFTY 50 index at {} %Change and NIFTY 50 Sector index at {} %Change'.format(nf_n50['pChange'],nseindexs),file=open("NSEmarket.txt", "a"))

print('',file=open("NSEmarket.txt", "a"))    


#For next month Aprox NIFTY 50 movment in persent:
vixmpc = (float(nf_indiavix['lastPrice'])/3.465) 
nmp = nf_n50['lastPrice']+vixmpc
nmn = nf_n50['lastPrice']-vixmpc

if float(nf_indiavix['pChange']) < 0.0 :
    ndpr = nf_n50['lastPrice']-(float(nf_indiavix['lastPrice']) * float(nf_indiavix['pChange']))
else:
    ndpr = nf_n50['lastPrice']+(float(nf_indiavix['lastPrice']) * float(nf_indiavix['pChange']))


if float(nf_indiavix['pChange']) > 0.0 :
    ndnr = nf_n50['lastPrice']-(float(nf_indiavix['lastPrice']) * float(nf_indiavix['pChange']))
else:
    ndnr = nf_n50['lastPrice']+(float(nf_indiavix['lastPrice']) * float(nf_indiavix['pChange']))

ndpf = format(ndpr,'.2f')
ndnf = format(ndnr,'.2f')
ndp = int(50 * round(float(ndpf)/50))
ndn = int(50 * round(float(ndnf)/50))

## Retrive data from US VIX data from CSV file created from program US_market.py

dr_usvix = pd.read_csv('USVIX.csv')
df_usvix = pd.DataFrame(data=dr_usvix)

vixtime = datetime.now().strftime("%H") 
if int(vixtime) == 9:
    print("At this time Aprox NIFTY 50 Max High is {} and Max low is {} ".format(ndpf,ndnf),file=open("NSEmarket.txt", "a"))
    print('',file=open("NSEmarket.txt", "a"))    
    # Simple Stock Option suggestion BOT run
    import NSE_Stock_Option_suggestion_BOT
    #Volatility Index VIX (^VIX)
    usvixfr = df_usvix.iloc[-1][0]
    if abs(float(nf_indiavix['pChange'])) < abs(float(usvixfr)):
        if float(usvixfr) < 0.0 and float(nf_indiavix['pChange']) > 0.0:
            print('Probability of Market will change the direction from Negative to Positive ')#,file=open("NSEmarket.txt", "a"))
        elif float(usvixfr) > 0.0 and float(nf_indiavix['pChange']) > 0.0:
            print('Probability of Market will change the direction from Positive to Negative')#,file=open("NSEmarket.txt", "a"))
        elif float(nf_indiavix['pChange']) > 0.0 and float(nf_finser['pChange']) < 0.0:
            print('Probability of Market will Consolidated')#,file=open("NSEmarket.txt", "a"))


print('',file=open("NSEmarket.txt", "a"))    


### VIX   high > 15.811 < low VIX 
#print('INDIA VIX  index current value is {} Low and percent change is {} '.format(nf_indiavix['lastPrice'],nf_indiavix['pChange'],'.2f')) 

#Low VIX Logic
if float(nf_indiavix['lastPrice']) > (15.811-vixmpc) and float(nf_indiavix['lastPrice']) < 15.811:
    print("The VIX is {} Low and percent change is {} ".format(nf_indiavix['lastPrice'],nf_indiavix['pChange']),file=open("NSEmarket.txt", "a"))
    if float(nf_indiavix['pChange']) < 0.0 :
        print('Probability of NIFTY 50 is going UP to ' ,ndp,file=open("NSEmarket.txt", "a"))
    elif float(nf_indiavix['pChange']) > 0.0 :
        print('Probability of NIFTY 50 is going down to ' ,ndn,file=open("NSEmarket.txt", "a"))
if float(nf_indiavix['lastPrice']) < (15.811-vixmpc):
    print("The VIX is {} Very Low and percent change is {} ".format(nf_indiavix['lastPrice'],nf_indiavix['pChange']),file=open("NSEmarket.txt", "a"))
    if float(nf_indiavix['pChange']) < 0.0 :
        print('Probability of NIFTY 50 is going UP to ' ,ndp,file=open("NSEmarket.txt", "a"))
    elif float(nf_indiavix['pChange']) > 0.0 :
        print('Probability of NIFTY 50 is going down to ' ,ndn,file=open("NSEmarket.txt", "a"))


#HIGH VIX Logic        
if float(nf_indiavix['lastPrice']) > (15.811+vixmpc):
    print("The VIX is Very high  {}  and percent change is {} ".format(nf_indiavix['lastPrice'],nf_indiavix['pChange']),file=open("NSEmarket.txt", "a"))
    if float(nf_indiavix['pChange']) < 0.0 :
        print('Probability of NIFTY 50 is going UP to ' ,ndp,file=open("NSEmarket.txt", "a"))
    elif float(nf_indiavix['pChange']) > 0.0 :
        print('Probability of NIFTY 50 is going down to ' ,ndn,file=open("NSEmarket.txt", "a"))
if float(nf_indiavix['lastPrice']) < (15.811+vixmpc) and float(nf_indiavix['lastPrice']) > 15.811:
    print("The VIX is High  {} and percent change is {} ".format(nf_indiavix['lastPrice'],nf_indiavix['pChange']),file=open("NSEmarket.txt", "a"))
    if float(nf_indiavix['pChange']) < 0.0 :
        print('Probability of NIFTY 50 is going UP to ' ,ndp,file=open("NSEmarket.txt", "a"))
    elif float(nf_indiavix['pChange']) > 0.0 :
        print('Probability of NIFTY 50 is going down to ' ,ndn,file=open("NSEmarket.txt", "a"))

print('',file=open("NSEmarket.txt", "a"))


# nifty 50 stocks current position
n50_len = len(n50grtz)+len(n50negt)+len(n50inzero)

rkf = format((riskmoney/75),'.2f')
rkr = int(1 * round(float(rkf)/1))

#n50 PUT BUY Logic 
if float(nf_n50['pChange']) <= 0.01 and float(nf_n50['pChange']) > -0.95 and float(nf_indiavix['pChange']) > 0.0:
    nporm = 1 # Risk Money variable
    if len(n50negt) >= (n50_len*0.7) :
        if nporm > 0.0:
            prkr = rkr+(rkr*0.20)
            prkr = format(prkr,'.2f')
            print("For NIFTY 50 Buy PE for {} ATM at max {} Rs".format(nf_n50['lastPrice'],prkr),file=open("NSEmarket.txt", "a"))

        else:
            prkr = rkr-(rkr*0.40)
            prkr = format(prkr,'.2f')
            print("For NIFTY 50 Buy PE for {} ATM at max {} Rs".format(nf_n50['lastPrice'],prkr),file=open("NSEmarket.txt", "a"))
    else:
        #print('Medium Risk to BUY NIFTY 50 PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print("Medium Risk to BUY NIFTY 50 PE for {} ITM".format(ndn-100),file=open("NSEmarket.txt", "a"))
        print('High Risk For NIFTY 50 BUY Call',file=open("NSEmarket.txt", "a"))


# 1.5% Stratergy for finding range of ITM & OTM
ntwopr = nf_n50['lastPrice']*0.015
ntwop = int(10 * round(float(ntwopr)/10))

if nporm > 0.0:
    prkr = rkr+(rkr*0.20)
    prkr = format(prkr,'.2f')
else:
    prkr = rkr-(rkr*0.40)
    prkr = format(prkr,'.2f')

print("NIFTY 50 Buy PE for {} ATM at max {} Rs".format(nf_n50['lastPrice'],prkr))
print("NIFTY 50 Buy PE for {} ITM at max {} Rs".format(ndn-ntwop,prkr))
print("NIFTY 50 Buy PE for {} OTM at max {} Rs".format(ndp+ntwop,prkr))
print("")


  
#n50 PUT SELL Logic
if float(nf_n50['pChange']) <= -2 and float(nseindexs) < 0.0 and float(nf_indiavix['pChange']) > 0.0:
    if (len(n50negt) >= (n50_len*0.4)) and (len(n50negt) <= (n50_len*0.7)) :
        #print('Total negative are more than 70%')
        n50PEITM = ndp
        n50PEATM = (nf_n50['lastPrice'])
        n50PEOTM = ndn
        print('For (if previously Buy) NIFTY 50 SELL PUT range are {} ATM {} ITM {} OTM at time {}'.format(n50PEATM,n50PEITM,n50PEOTM,endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Medium Risk  to SELL (if previously Buy) NIFTY 50  PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))     
        print('Medium Risk For NIFTY 50 BUY CALL',file=open("NSEmarket.txt", "a"))
        
#n50 CALL BUY Logic  ##working correctly 

if float(nf_n50['pChange']) >= 0.1 and float(nf_n50['pChange']) < 1.00 and float(nseindexs) > 0.0 and float(nf_indiavix['pChange']) < 0.0:
    ncorm = -1 # Risk Money variable
    if float(len(n50negt)) <= (n50_len*0.30) :
        if ncorm < 0.0:
            crkr = rkr+(rkr*0.20)
            crkr = format(crkr,'.2f')
            print("For NIFTY 50 Buy CE for {} ATM at max {} Rs".format(nf_n50['lastPrice'],crkr),file=open("NSEmarket.txt", "a"))

        else:
            crkr = rkr-(rkr*0.40)
            crkr = format(crkr,'.2f')
            print("For NIFTY 50 Buy CE for {} ATM at max {} Rs".format(nf_n50['lastPrice'],crkr),file=open("NSEmarket.txt", "a"))
    else:
        #print('Medium Risk to buy NIFTY 50  CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print("Medium Risk to buy NIFTY 50 CE for {} ITM".format(ndp+100),file=open("NSEmarket.txt", "a"))
        print('High risk For NIFTY 50 BUY PUT',file=open("NSEmarket.txt", "a") )

if ncorm < 0.0:
    crkr = rkr+(rkr*0.20)
    crkr = format(crkr,'.2f')
else:
    crkr = rkr-(rkr*0.40)
    crkr = format(crkr,'.2f')
        
print("NIFTY 50 Buy CE for {} ATM at max {} Rs".format(nf_n50['lastPrice'],crkr))
print("NIFTY 50 Buy CE for {} ITM at max {} Rs".format(ndp+ntwop,crkr))
print("NIFTY 50 Buy CE for {} OTM at max {} Rs".format(ndn-ntwop,crkr))
print("")
print('',file=open("NSEmarket.txt", "a"))

#n50 CALL SELL Logic
  
if float(nf_n50['pChange']) >= 1.5 and float(nf_indiavix['pChange']) < 0.0:
    if len(n50negt) <= (n50_len*0.4) :
        #print('Total negative are less than 20%')
        n50CEITM = (ndn) 
        n50CEATM = (nf_n50['lastPrice'])
        n50CEOTM = (ndp)
        print('For (if previously Buy) NIFTY 50 SELL CALL range are {} ATM {} ITM {} OTM at time {}'.format(n50CEATM,n50CEITM,n50CEOTM,endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Medium Risk to NIFTY 50 50 CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('Medium Risk For NIFTY 50 BUY PUT ',file=open("NSEmarket.txt", "a"))



if float(nf_n50['pChange']) <= 0.01 and float(nf_n50['pChange']) > -0.95:print('Buy Put logic')
elif float(nf_n50['pChange']) <= -1.5 and float(nseindexs) < 0.0:print('Sell Put logic')
elif float(nf_n50['pChange']) >= 0.01 and float(nf_n50['pChange']) < 0.85 and float(nseindexs) > 0.0: print('Buy Call logic')
elif float(nf_n50['pChange']) >= 1.5:print('Sell Call logic')
else:
    print('Hold your existing NIFTY 50 CE or PE positions for next market move',file=open("NSEmarket.txt", "a"))
    print('Hold your existing NIFTY 50 CE or PE positions for next market move')


print('',file=open("NSEmarket.txt", "a"))    
    
######################## NBANK Options ###################################


print('For BANKNIFTY Options',file=open("NSEmarket.txt", "a"))

print('BANKNIFTY index current value is {} and percent change is {} '.format(nf_bank['lastPrice'],nf_bank['pChange']),file=open("NSEmarket.txt", "a"))
bank_len = (len(bankgrtz)+len(banknegt)+len(bankinzero))
bnseindexsr = (float(nf_psubank['pChange']) * 0.25 + float(nf_pvtbank['pChange']) * 0.74 + float(nf_finser['pChange'])*0.01)

bnseindexs = format(bnseindexsr,'.2f')

print('',file=open("NSEmarket.txt", "a"))  
print ('BANKNIFTY index at {} %Change and NSE BANK Sector index at {} %Change'.format(nf_bank['pChange'],bnseindexs),file=open("NSEmarket.txt", "a"))
print('',file=open("NSEmarket.txt", "a"))  
print('BankNIFTY index current value is {} and percent change is {} '.format(nf_bank['lastPrice'],nf_bank['pChange']),file=open("NSEmarket.txt", "a")) 



#For future prediction depend on NIFTY PSU Bank & PVT Bank Indexs    

if float(nf_psubank['pChange']) > 0.25 and float(nf_pvtbank['pChange']) > 0.75 and float(nf_finser['pChange']) > 0.0:
    #print('Bank sector are in positive at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    if len(banknegt) > (bank_len*0.2):
        print('NSE Bank sector is at going down but trend is positive',file=open("NSEmarket.txt", "a"))
    else:
        print('Bank sector are in positive at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
elif float(nf_psubank['pChange']) < 0.25 and float(nf_pvtbank['pChange']) < 0.75 and float(nf_finser['pChange']) < 0.0:
    print('Bank sector are in negative at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    if (len(banknegt) > (bank_len*0.4)) and (len(banknegt) < (bank_len*0.70)):
        print('NSE Bank sector is at going down and trend is negative at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    elif len(banknegt) > (bank_len*0.70):
        print('NSE Bank sector is at going down and trend is highly negative at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Bank sector are in positive and trend is negative at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
else:
    print('Bank sector is at sideways at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))



# For BankNifty Weekly Exp.
nf_bankr = int(50 * round(float(nf_bank['lastPrice']/50)))
brkf = format((riskmoney/20),'.2f')
brkr = int(1 * round(float(brkf)/1))
# 1.5% stratergy to calculate the ITM & OTM value
bnonepr = float(nf_bank['lastPrice'])*0.015
bnonep = int(10 * round(float(bnonepr)/10))

#BANK PUT BUY Logic depend on NIFTY Bank Index
if (float(nf_bank['pChange']) > -1) and (float(nf_bank['pChange']) <= 0.01):
    bporm = 1 # Risk Money variable
    if len(banknegt) >= (bank_len*0.55) :
        if bporm > 0.0:
            pbrkr = brkr+(brkr*0.20)
            pbrkr = format(pbrkr,'.2f')
            print("For BANKNIFTY Week buy  PE for  {} ATM at max {} Rs".format(nf_bankr,pbrkr),file=open("NSEmarket.txt", "a"))
        else:
            pbrkr = brkr-(brkr*0.40)
            pbrkr = format(pbrkr,'.2f')
            print("For BANKNIFTY Week buy  PE for  {} ATM at max {} Rs".format(nf_bankr,pbrkr),file=open("NSEmarket.txt", "a"))
    else:
        #print('Medium Risk to BUY BANKNIFTY PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print("Medium Risk to buy BANKNIFTY PE for {} ITM".format((nf_bankr-250)),file=open("NSEmarket.txt", "a"))
        print('High Risk For BANKNIFTY BUY CALL',file=open("NSEmarket.txt", "a"))


if bporm > 0.0:
    pbrkr = brkr+(brkr*0.20)
    pbrkr = format(pbrkr,'.2f')
else:
    pbrkr = brkr-(brkr*0.40)
    pbrkr = format(pbrkr,'.2f')
        
print("BANKNIFTY Week buy  PE for  {} ATM at max {} Rs".format(nf_bankr,pbrkr))
print("BANKNIFTY Week buy  PE for  {} ITM at max {} Rs".format((nf_bankr-bnonep),pbrkr))
print("BANKNIFTY Week buy  PE for  {} OTM at max {} Rs".format((nf_bankr+bnonep),pbrkr))
print("")
       
#Bank PUT SELL Logic depend on NIFTY Bank Index
if float(nf_bank['pChange']) <= -1.5:
    if len(banknegt) >= (bank_len*0.4) :
        #print('Total negative are more than 70%')
        bankPEITM = (nf_bank['lastPrice']+100) 
        bankPEATM = (nf_bank['lastPrice'])
        bankPEOTM = (nf_bank['lastPrice']-100)
        print('For (if previously Buy) BANKNIFTY SELL PUT range are {} ATM {} ITM {} OTM at time {}'.format(bankPEATM,bankPEITM,bankPEOTM,endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Medium Risk  to SELL (if previously Buy) BANKNIFTY PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('Medium Risk For BANKNIFTY buy CALL',file=open("NSEmarket.txt", "a"))


#Bank CALL BUY Logic depend on NIFTY Bank Index
        
if (float(nf_bank['pChange']) >= 0.1) and (float(nf_bank['pChange']) < 1):
    bcorm = -1 # Risk Money variable
    if len(banknegt) <= (bank_len*0.20) :
        #print('Total negative are less than 20%')
        if bcorm < 0.0:
            cbrkr = brkr+(brkr*0.20)
            cbrkr = format(cbrkr,'.2f')
            print("For BANKNIFTY Week buy  CE for  {} ATM at max {} Rs".format(nf_bankr,cbrkr),file=open("NSEmarket.txt", "a"))
        else:
            cbrkr = brkr-(brkr*0.40)
            cbrkr = format(cbrkr,'.2f')
            print("For BANKNIFTY Week buy  CE for  {} ATM at max {} Rs".format(nf_bankr,cbrkr),file=open("NSEmarket.txt", "a"))
    else:
        print('Medium Risk to Buy BANKNIFTY CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        #print('High Risk to Buy BANKNIFTY PUT at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))

if bcorm < 0.0:
    cbrkr = brkr+(brkr*0.20)
    cbrkr = format(cbrkr,'.2f')
else:
    cbrkr = brkr-(brkr*0.40)
    cbrkr = format(cbrkr,'.2f')
print("BANKNIFTY Week buy  CE for  {} ATM at max {} Rs".format(nf_bankr,cbrkr))
print("BANKNIFTY Week buy  CE for  {} ITM at max {} Rs".format((nf_bankr+bnonep),cbrkr))
print("BANKNIFTY Week buy  CE for  {} OTM at max {} Rs".format((nf_bankr-bnonep),cbrkr))
print("")

#Bank CALL SELL Logic depend on NIFTY Bank Index
        
if float(nf_bank['pChange']) >= 1.5:
    if len(banknegt) <= (bank_len*0.5) :
        #print('Total negative are less than 50%')
        bankCEITM = (nf_bank['lastPrice']-50) 
        bankCEATM = (nf_bank['lastPrice'])
        bankCEOTM = (nf_bank['lastPrice']+50)
        print('For (if previously Buy) BANKNIFTY SELL CALL range are {} ATM {} ITM {} OTM at time {}'.format(bankCEATM,bankCEITM,bankCEOTM,endtime),file=open("NSEmarket.txt", "a"))
    else:
        print('Medium Risk to SELL (if previously Buy) BANKNIFTY CALL at time {}'.format(endtime),file=open("NSEmarket.txt", "a"))
        print('High Risk For BANKNIFTY BUY PUT',file=open("NSEmarket.txt", "a"))


print('',file=open("NSEmarket.txt", "a"))

################################### End of BOT ############################################


#import Nifty_BankNifty_Option_data

print('End Time of BOT',bot_endtime,file=open("NSEmarket.txt", "a"))
print('',file=open("NSEmarket.txt", "a"))
print('End of BOT Read text file "NSEmarket" for results generated / saved at same folder as prrogram')


