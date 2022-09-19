#Import all the files here

import random
import string

def get_random_string(length):
	# Funtion genrate randon string of specified length.  
	letters = string.ascii_lowercase
	result_str = ''.join(random.choice(letters) for i in range(length))
	print("Random string of length", length, "is:", result_str)

def gen_samples():              
	#Write your function here
	#Don't forget to add indentation
	
	rand_str = get_random_string(10)
	
	res = ''.join(format(ord(i), 'b') for i in rand_str) # String -> Binary
	
	return res

