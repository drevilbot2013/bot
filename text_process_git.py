# -*- coding: utf-8 -*-
"""
Created on Fri May  4 22:00:59 2018

@author: me
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from bs4 import BeautifulSoup
import requests
import pandas
import re

#get script1
url="http://www.dailyscript.com/scripts/Austin_Powers_IMM.html"
response = requests.get(url)
html = response.text

#scrape
soup = BeautifulSoup(html, "html.parser")
script=soup.find('pre').get_text()

#clean
regex = re.compile("\((.*?)\)")
result = re.sub(regex,'', script)
drevil_test=result.split("\r\n\r\n")
newlist=[]
for x in drevil_test:
    x=re.sub('\s+', ' ', x)
    x=x.replace("\r\n","")
    x=x.replace("&emdash","")
    x=x.split(" ")
    newlist.append(x[1:])

#get script2
url2="http://www.dailyscript.com/scripts/Austin_Powers_TPWSM.html"
response2 = requests.get(url2)
html2 = response2.text
#scrape
soup2 = BeautifulSoup(html2, "html.parser")
script2=soup2.find('pre').get_text()

#clean
result2 = re.sub(regex,'', script2)
drevil_test2=result2.split("\r\n\r\n")
newlist2=[]
for x in drevil_test2:
    x=re.sub('\s+', ' ', x)
    x=x.replace("\r\n","")
    x=x.replace("&emdash","")
    x=x.split(" ")
    x=x[1:]
    newlist2.append(x)

#combine both datasets to create one for clustering
combined=newlist+newlist2
drevil=[]
before1=[]
before2=[]
after1=[]
after2=[]
alltext=[]
length=len(combined)
count2=0
#structure into columns based on text around drevil dialogue
while count2<length:
    if len(combined[count2])>2:
        if combined[count2][0]=='DR.' and combined[count2][1]=='EVIL':
            #combine text surrounding dr evil lines
            alltext.append(combined[count2]+combined[count2-1]+combined[count2-2]+combined[count2+1]+combined[count2+2])
            #dr evil lines
            drevil.append(combined[count2])
            #not used
            before1.append(combined[count2-1])
            before2.append(combined[count2-2])
            after1.append(combined[count2+1])
            after2.append(combined[count2+2])
    count2+=1

count3=0
sentences=[]
while count3<len(alltext):
    sentences.append(' '.join(alltext[count3]))
    count3+=1

#export dataframe as input for dialogue
DF = pandas.DataFrame({'drevil': drevil,'context':sentences})
DF.to_pickle("FILE PATH")


















