#!/usr/bin/env python 3.6
# encoding:utf-8
# author: yqq

"""讲0001生成的激活码保存到mysql"""

import pymysql

list_id = []
with open('Activation_code.txt','r') as file:
    files = file.readlines()
    for content in files:
        list_id.append(str(content).replace('\n',''))
try:
    conn = pymysql.connect(host='127.0.0.1',user='root',passwd='root',db='mysql')
    cur = conn.cursor()
except BaseException as e:
    print(e)
else:
    cur.execute('CREATE DATABASE IF NOT EXISTS test0002')
    cur.execute('USE test0002')
    cur.execute('CREATE TABLE IF NOT EXISTS CODE002(id INT,uuid VARCHAR(50))')
    for i in range(len(list_id)):
        cur.execute('INSERT INTO CODE002 VALUES (%s,%s)',(i,list_id[i]))
    conn.commit()
    cur.close()
    conn.close()











