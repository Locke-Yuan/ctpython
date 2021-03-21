# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 15:44:09 2021

@author: user
"""

"""
3/21 作業2
1.由系統產生7個整數數字(亂數1-100)要遞增排序印出來，ex:[10,7,6,100,90,5,17]
2.由使用者輸入一個值，去找尋串列中的值，用2分法顯示找尋過程

"""

import random

number = []
while True:
    number.append(random.randint(1, 100))
    if len(number) == 7:
        break;
number.sort()
print(number)

num = int(input("輸入搜尋數字:"))

freq = 0     #搜尋次數
position = 0    #資料位置

while True:
    a = len(number)//2
    if num == number[a]:
        if a == 0:
            position += 1
        else:
            position += a+1
        position -= 1
        print('找到了! 在串列%d的位置'%position)
        break
    elif num < number[a]:
        del number[a:]
    else:
        del number[:a+1]        
        position += a+1
        
    freq +=1
    print("第%d次沒找到，剩下:"%freq, number)


