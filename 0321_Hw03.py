# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:19:51 2021

@author: user
"""

"""
3/21 作業2
由使用者輸入獲利金額
1. 含10萬以內，獎金10%
2. 10~20萬(低於10萬獎金10%，剩餘的獎金7%)
3. 20~40萬(低於10萬獎金10%,10萬7%，剩餘的獎金3%)
"""

money = int(input("請輸入獲利金額:"))

if money <= 100000:
    bonus = money * 0.1
elif money <= 200000: 
    bonus = 100000 * 0.1 + (money-100000)*0.07
else:
    bonus = 100000 * 0.1 + 100000 * 0.07 +(money-200000)*0.03
print(bonus)
        
