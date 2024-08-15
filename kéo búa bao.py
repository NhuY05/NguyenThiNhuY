# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:54:31 2024

@author: Vivobook
"""
import random

Chọn = ("Kéo","Búa","Bao")

Người_chơi_chọn = input("Chọn Kéo, Búa hoặc Bao:")
Máy_chọn = random.choice(Chọn)

print("Máy chọn:",(Máy_chọn))

if Người_chơi_chọn == Máy_chọn:
     print("Hòa")
elif Người_chơi_chọn == "Kéo" and Máy_chọn == "Bao" or\
     Người_chơi_chọn == "Búa" and Máy_chọn == "Kéo" or\
     Người_chơi_chọn == "Bao" and Máy_chọn == "Búa":
     print("Bạn thắng")
else:
     print("Bạn thua")