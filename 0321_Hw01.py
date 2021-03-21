# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 11:21:19 2021

@author: user
"""

"""
3/21 作業1
由系統亂數產生1~49之間六個不重複的整數，
請遞增排序印出
"""
import random

number = []
while True:
    num = random.randint(1, 49)
    if number.count(num) == 0: 
        number.append(num)
    if len(number) == 6:
        break;
number.sort()
print(number)