# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 12:47:35 2017

@author: mikkopos
"""

list_a = [10,2,3,4,5,6]
list_b = [8,9,8,7,6,5]

# val = arvo 
#range on index.luku 0-4
# len = numeroiden maara 
# range luvut nollasta niin suureksi kuin len on
for val in range(len(list_a)):
    #print (val)
    item_a = list_a[val]
   # print (item_a)
    item_b = list_b[val]
    
    #print (item_b)
   # print (item_a, item_b)
    
   # toinen vaihtoehto on kayttaa .index(value) komentoa
   
for value in list_a:
    #check the index number
    idx = list_a.index(value)
    item_b = list_b[idx]
    print(value, item_b)
    
    #print (idx) 
   