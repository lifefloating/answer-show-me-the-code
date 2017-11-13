#!/usr/bin/env python3.6
# encoding:utf-8
# author: yqq


import random, string

def rand_str(num, length=7):
    with open('Activation_code.txt', 'w+') as f:
        for i in range(num):
            chars = string.ascii_letters + string.digits
            s = [random.choice(chars) for i in range(length)]
            f.write(''.join(s) + '\n')
    f.close()

if __name__ == '__main__':
    rand_str(200)
