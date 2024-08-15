# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:11:46 2024

@author: Vivobook
"""
tongtien = 0
sokm=int(input("Nhập số km:"))
#1km đầu
if sokm == 1:
   tongtien = sokm * 20000
 #2-3   
elif 1 < sokm <= 3:
   tongtien = sokm * 13000
#4-8
elif 4 <= sokm <= 8:
   tongtien = ( 3 * 13000 ) + (sokm - 3 ) * 12000
#>9
else:
   tongtien = (3 * 13000) + (sokm - 3) * 12000 + (sokm - 8) * 10000 
if tongtien > 100000:
   tongtien =  ((3 * 13000) + (sokm - 3) * 12000 + (sokm - 8) * 10000) * 0.92
print("Tổng tiền phải trả: ", int(tongtien), "VNĐ")