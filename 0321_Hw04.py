# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:04:24 2021

@author: user
"""

"""
挑戰題:巴斯卡三角形
"""

#公式: n! / (m!*(n-m)!)
for i in range(0,6):
    for j in range(0,i+1):
        
        n = 1
        for a in range(1,i+1):
            n *= a
        
        m = 1
        for a in range(1,j+1):
            m *= a   
        
        nm = 1
        for a in range(1,i-j+1):
            nm *= a    
            
        num = int(n/(m*nm))
        print( num , end= " ")      
    print()
    
