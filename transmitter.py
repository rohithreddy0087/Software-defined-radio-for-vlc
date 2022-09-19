# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:39:22 2020

@author: sai narasimha
"""

import hamming_code as hmc
import pulse_shaping as plsh

d=0

#########################################################################
def error_correction(err,pulse):
    out = []
    if pulse == 'Manchester':
        out = plsh.MAnchester_encoding(err)
    elif pulse == 'Polar NRZ':
        out=plsh.polar_nrz(err)
    elif pulse == 'Polar RZ':
        out=plsh.polar_rz(err)
    elif pulse == 'Bipolar NRZ':
        out=plsh.bipolar_nrz(err)
    elif pulse == 'Bipolar RZ':
        out=plsh.bipolar_rz(err)
    return out

def transmit_data(data,error_corr,pulse):
    err=[]
    print(data)
    len_data=len(data)
#######################################################################    
    def ba1():
        for i in range(len(data)):
            for j in range(len(data[i])):
                err.append(hmc.hamming(ord(data[i][j])))
            err.append(hmc.hamming(ord("\n")))
            
    def ba2():
        for i in range(len(data)):
            for j in range(len(data[i])):
                err.append(bin(ord(data[i][j]))[2:].zfill(12))
            err.append(bin(ord("\n"))[2:].zfill(12))
            
    # Case statement for error correcting code
    error= { 
        'Hamming code': ba1,
        'No code': ba2
        }
    error.get(error_corr)()
    
    err=''.join(err)
    
    print(len(err))
    
    out = error_correction(err,pulse)
    print(len(out))
    print(out)
    
##########################################################################
    return out


def transmit_numbers(data,error_corr,pulse):
    err=[]
    length=len(data)
    
    def ba1():
        for i in range(len(data)):
            err.append(hmc.hamming(data[i]))
            
    def ba2():
        for i in range(len(data)):
            err.append(bin(data[i]))
            
    # Case statement for error correcting code
    error= { 
        'Hamming code': ba1,
        'No code': ba2
        }
    error.get(error_corr)()
    
    err=''.join(err)
    out = error_correction(err,pulse)
    print(out)
    return out
    
    
"""
data = ['bala narasimha ', 'mvs', 'Rohit reddy ', 'rachala ']
hamm=transmit_data(data,'No code','Polar NRZ')
print(hamm)
"""