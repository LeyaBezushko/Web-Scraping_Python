#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import libraries 


from bs4 import BeautifulSoup
import requests
import time
import datetime

import smtplib

import re


# In[2]:


# Connect to Website and pull in data

URL = 'https://xn--80aa6aoj2a.com.ua/torgovelne-obladnannya/termoprinteri/printeri-etiketok/termoprinter-dlja-druku-etiketok-6973'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(),"html.parser")

print(soup2)


# In[3]:


#Parsing of title

title = soup1.find(class_="col-12 sc-page-title pb-3").get_text(strip=True)

print(title)


# In[7]:


#Parsing of price

price = soup1.find(class_="sc-module-price fw-800 dark-text mt-1 fsz-20").get_text(strip=True)

print(price)



# In[8]:


# Clean up the data a little bit

price = price.replace(" ", "")
title = title.strip()

print(title)
print(price)


# In[9]:


#Removing non numeric values

price = "3799грн"
price_digits_only = re.sub(r'\D', '', price)
print(price_digits_only)


# In[10]:


# Create a Timestamp for an output to track when data was collected

import datetime

today = datetime.date.today()

print(today)


# In[83]:


# Create CSV and write headers and data into the file

import csv 

header = ['Title', 'Price', 'Date']
data = [title, price,today]

type(data) #checking if format is list or  dictionaries

#сreating and editing file via atrybut "w", file is becoming totally blank and new rows apppear

with open('SpalachWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


    


# In[86]:


import pandas as pd 

df = pd.read_csv(r'C:\Users\Pawlo\SpalachWebScraperDataset.csv')

print(df)


# In[85]:


#here the data is added in addition to the existing file, through the transition 'a+', additional information is added to the existing file

with open('SpalachWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)


# In[114]:


#Creating function for the furure updating information

def check_price():
    
    URL = 'https://xn--80aa6aoj2a.com.ua/torgovelne-obladnannya/termoprinteri/printeri-etiketok/termoprinter-dlja-druku-etiketok-6973'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(),"html.parser")
    
    title = soup1.find(class_="col-12 sc-page-title pb-3").get_text(strip=True)
    
    price = soup1.find(class_="sc-module-price fw-800 dark-text mt-1 fsz-20").get_text(strip=True)
    
    price = price.replace(" ", "")
    price = "3799 грн"
    price_digits_only = re.sub(r'\D', '', price)
    
    title = title.strip()
    
    
    
    
    import datetime

    today = datetime.date.today()
    
    import csv 
    
    header = ['Title', 'Price', 'Date']
    
    data = [title, price,today]
    
    with open('SpalachWebScraperDataset.csv', 'w', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
    if (price >200):
        send_mail()



# In[98]:


#This while(True) loop, along with the check_price() function and time.sleep(5), will infinitely call the check_price() function every 5 seconds. This is how it works:


while(True):
    check_price()
    time.sleep(5)


# In[100]:


import pandas as pd 

df = pd.read_csv(r'C:\Users\Pawlo\SpalachWebScraperDataset.csv')

print(df)


# In[108]:


# If uou want to try sending yourself an email (just for fun) when a price hits below a certain level you can try it
# out with this script

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('pawlo0677@gmail.com','qwASDzxcv12')
    
    subject = "The Shirt you want is below $15! Now is your chance to buy!"
    body = "Alex, This is the moment we have been waiting for. Now is your chance to pick up the shirt of your dreams. Don't mess it up! Link here: https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data+analyst+tshirt&qid=1626655184&sr=8-3"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'pawlo0677@gmail.com',
        msg
     
    )


# In[115]:


print(price)


# In[ ]:




