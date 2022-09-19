# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 00:09:33 2020

@author: sai narasimha
"""

def MAnchester_encoding(data):
    man_encoded = str()
    #print(data)
    for i in range (len(data)):
        if data[i] == '1':
            man_encoded=man_encoded+'1'
            man_encoded=man_encoded+'0'
        elif data[i] == '0':
            man_encoded=man_encoded+'0'
            man_encoded=man_encoded+'1'
    return man_encoded
                
def polar_nrz(data):

    return data
    

def polar_rz(data):
    prz=str()
    for i in range (len(data)):
        if data[i] == '1':
            prz=prz+'1'
            prz=prz+'0'
        elif data[i] == '0':
            prz=prz+'0'
            prz=prz+'0'
    return prz

def bipolar_nrz(data):
    ind = -1
    bipnrz = str()
    for i in range (len(data)):
        if data[i] == '1' and ind == -1:
            bipnrz=bipnrz+'1'
            ind = 1
        elif data[i] == '1' and ind == 1:
            bipnrz=bipnrz+'-1'
            ind = -1
        elif data[i] == '0':
            bipnrz=bipnrz+'0'
    return bipnrz

def bipolar_rz(data):
    ind = -1
    biprz = str()
    for i in range (len(data)):
        if data[i] == '1' and ind == -1:
            biprz=biprz+'1'
            biprz=biprz+'0'
            ind = 1
        elif data[i] == '1' and ind == 1:
            biprz=biprz+'-1'
            biprz=biprz+'0'
            ind = -1
        elif data[i] == '0':
            biprz=biprz+'0'
            biprz=biprz+'0'
    return biprz




    

    