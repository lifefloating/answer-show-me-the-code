#!/usr/bin/env python3.5
# encoding:utf-8
# author:yqq


import collections

wordcount = collections.Counter()
with open("english.txt") as file:
    for line in file:
        wordcount.update(line.split())

for k,v in wordcount.items():
    print(k,v)
