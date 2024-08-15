# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:45:06 2024

@author: Vivobook
"""
#Giải phương trình bậc nhất
a = float(input("Nhập vào số a:"))
b = float(input("Nhập vào số b:"))

if a==0:
    if b==0:
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else: 
     x = -(b/a)
     print("Phương trình có nghiệm duy nhất x:", x)     
            