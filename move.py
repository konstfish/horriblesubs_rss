#!/usr/bin/python

import os, sys

torrentfolder = "/stor/torrents"
dest = "/stor/plex/anime"

torrentls = os.listdir(torrentfolder)

print(torrentls)

i = 0
while i < len(torrentls):
    if(".part" in torrentls[i]):
        torrentls.remove(torrentls[i])
    if("[HorribleSubs]" not in torrentls[i]):
        torrentls.remove(torrentls[i])
    i += 1

print(torrentls)

numlist = ["0","1","2","3","4","5","6","7","8","9"]
animefolders = []
unixname = []

i = 0
while i < len(torrentls):
    fold_n = ""
    unix_n = ""
    a = 15
    while(torrentls[i][a] not in numlist):
        fold_n += torrentls[i][a]
        unix_n += torrentls[i][a]
        a += 1

    fold_n = fold_n[:-3]
    unix_n = unix_n[:-3]

    fold_n = fold_n.replace(" ", "_")
    unix_n = unix_n.replace(" ", "\\ ")

    animefolders.append(fold_n)
    unixname.append(unix_n)

    i += 1

print(animefolders)
print(unixname)

i = 0
while i < len(unixname):
    # if you want some sort if ifttt notification every time something is added
    # uncomment this line and add your maker link
    #command = "curl -X POST -H \"Content-Type: application/json\" -d \'{\"value1\":\"" + torrentls[i] + "\"}\' https://maker.ifttt.com/trigger/horriblesubs/with/key/xxx"
    os.system(command)
    os.system("mv " + torrentfolder + "*" + str(unixname[i]) + "*.mkv " + dest + str(animefolders[i]))
    i += 1
