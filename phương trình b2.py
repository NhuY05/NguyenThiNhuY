# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:07:39 2024

@author: Vivobook
"""

#Giải phương trình bậc 2
import math
a=float(input("Nhập vào giá trị a:"))
b=float(input("Nhập vào giá trị b:"))
c=float(input("Nhập vào giá trị c:"))
delta=float()
delta= (b**2)-(4*a*c)
if a== 0:
    print("Phương trình k phải pt bậc 2")
elif delta>0:
    x1 = -b+math.sqrt(delta)/(2*a)
    x2 = -b-math.sqrt(delta)/(2*a)
    print("Phương trình có 2 nghiệm phân biệt:")
    print("x1:", x1)
    print("x2:",x2)
elif delta==0:
    print("Phương trình có nghiệm kép x1=x2=",-b/2*a)
elif delta <0:
    print("Phương trình vô nghiệm: ")
    

