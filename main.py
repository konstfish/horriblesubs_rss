#!/usr/bin/python

import feedparser
import time
from subprocess import check_output
import sys
import os

animlst =  ['Sword Art Online - Alicization', 'Zombieland Saga', 'Tensei Shitara Slime Datta Ken', 'SSSS.Gridman']

feed_name = 'HorribleSubs'
url = 'http://www.horriblesubs.info/rss.php?res=1080'

d = feedparser.parse(url)

animels = os.listdir("/stor/plex/anime/")

numlist = ["0","1","2","3","4","5","6","7","8","9"]

i = 0
while i != len(d['entries']):
    for j in range(len(animlst)):
        if((d['entries'][i]['title'].find(animlst[j])) != -1):

            strnew = ""
            a = 15
            while(d['entries'][i]['title'][a] not in numlist):
                strnew += d['entries'][i]['title'][a]
                a += 1

            strnew = strnew[:-3]

            strnew = strnew.replace(" ", "_")

            try:
                animfold = os.listdir("/stor/plex/anime/" + strnew + "/")
            except:
                os.system("mkdir /stor/plex/anime/" + strnew + "/")

            animfold = os.listdir("/stor/plex/anime/" + strnew + "/")

            if(d['entries'][i]['title'] not in animfold):
                print(d['entries'][i]['title'])
                os.system("/home/fish/horriblesubs/./totransm.sh " + d.entries[i]['link'])
                print("Added to Transmission Q")
    i+=1;
