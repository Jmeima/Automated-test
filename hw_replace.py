#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import os,commands,shlex
import time 


#every app's HW
lines_1 = open('/home/jueimei/desktop/permission_script/total_app_list_1245.csv').read()
lines_1 = lines_1.strip()
# N1 support HW
lines_2 = open('/home/jueimei/n1.txt').readlines()


f=open('temp.txt','w')
for line in lines_2:
    line = line.strip()
    lines_1 = lines_1.replace(line, "")
    print line

f.write(lines_1)
f.close()
