# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 22:59:51 2021

@author: furka
"""

#Birinci soru
try:
    deger=int(input("Bir sayı giriniz: "))
    for i in range(1,11):
        print(deger*i)
except:
    print("İnteher bir değer girin")
#--------------------------------------

#ikinci soru
try:
    sayi= int(input("Bir sayı giriniz: "))
    basamakSayi=str(sayi)
    j=0

    while j<len(basamakSayi):
        sayi=sayi/10
        j=j+1

    if j==len(basamakSayi):
        print("Doğru bulundu: basamak sayısı: ",j)
except:
    print("İnteher bir değer girin")
#------------------------------------------------------
#Üçüncü Soru
sayısalDeğerler = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for z in range(1,len(sayısalDeğerler)):
    if sayısalDeğerler[z] % 5==0:
        if sayısalDeğerler[z] <=150:
            print("For bölündü: ",sayısalDeğerler[z])

count=0
while count<len(sayısalDeğerler):
     if sayısalDeğerler[count] % 5==0:
        if sayısalDeğerler[count] <=150:
            print("While bölündü: ",sayısalDeğerler[count])
            
     count=count+1
#-----------------------------------------------------------
#dördüncü soru
try:
    birinci=int(input("Birinci sayıyı girin: "))
    ikinci=int(input("İkinci sayıyı girin: "))
    ucuncu=int(input("Üçüncü sayıyı girin: "))

    tut=birinci

    if birinci!=ikinci:
        if ikinci>birinci:
            birinci=ikinci  
            ikinci=tut

    for x in range(ikinci,birinci):
        if x % ucuncu==0:
            print("Bölünen değerler: ",x)
        else:
            print("Birinci ve ikinci sayı birbirine eşittir")
except:
    print("İnteher bir değer girin")
#----------------------------------------------------------
#beşinci soru

azalanDeger=100
for q in range(1,azalanDeger):
    azalanDeger=azalanDeger-1
    print(q," -- ",azalanDeger)
#-------------------------------------------



    
    




            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    
