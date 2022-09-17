# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 12:28:49 2020

@author: Dell
"""

import random
numbers =0


howMany = int(input('How many numbers would you like to generate?: '))

infile = open ('rand_write.txt', 'w')

for n in range(1,howMany):
    number=random.randint(1,60)
    infile.write(str(n)+','+str(number)+ '\n')
infile.close()