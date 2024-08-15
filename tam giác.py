# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:44:18 2024

@author: Vivobook
"""

a=int(input("Nhập cạnh a:"))
b=int(input("Nhập cạnh b:"))
c=int(input("Nhập cạnh c:"))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
        print("Đây là tam giác đều")
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Đây là tam giác vuông")
    elif a==b or a==c or b==c:
        print("Đây là tam giác cân")
    else:
        print("Đây là tam giác thường")
else:
    print("Đây không phải là tam giác")