# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 19:30:24 2021

@author: Yuan
"""

T = int(input("輸入巴斯卡三角形的層數:"))

t = [ [1] ]  #第一層，從1開始

for i in range(1,T):
    num = []
    for j in range(0,i+1):
        if j == 0 or j == i:
            num.append(1)
        else:
            num.append(t[i-1][j-1] + t[i-1][j])
    t.append(num)

for m in t:
    for n in m:
        print( n , end=" ")
    print()
