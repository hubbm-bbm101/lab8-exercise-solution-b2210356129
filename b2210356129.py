import os, sys

file = open(sys.argv[1],"r",encoding="utf-8")
uninfo = dict()
for a in file:
    name = a.split(":")[0]
    uninfo[name] = [(a.split(":")[1])]

inp = sys.argv[2].split(",")

for b in inp:
    try:
        if uninfo[b][0].endswith("\n") == True:
            uninfo[b][0] = uninfo[b][0][:-1]
        print("Name: %s, University = %s"%(b,uninfo[b][0]))
    except KeyError:
        print("No record of '%s' found"%b)

