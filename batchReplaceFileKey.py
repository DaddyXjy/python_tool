#!/usr/bin/python
# -*- coding: UTF-8 -*- 

#Date: 2019/01/30
#Author: dylan
#Desc: 批量替换文件关键字

from optparse import OptionParser  
import os

def replaceKey(filename , originalKey , destKey):
    with open(filename , 'r') as f:
        data = f.read().replace(originalKey , destKey)
    with open(filename , 'w') as o:
        if data :
            o.write(data)
if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option('-f' , '--filename' , dest = "filename")
    parser.add_option('-o' , '--originalKey' , dest = "originalKey")
    parser.add_option('-d' , '--destKey' , dest = "destKey")
    (option , args) = parser.parse_args()

    originalKey = option.originalKey
    destKey = option.destKey
    filename = option.filename
    
    replaceKey(filename , originalKey , destKey)

