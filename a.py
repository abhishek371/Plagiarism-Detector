from collections import deque
import math
from bloom_filter import *
def roll_hash(prev,next, present_hashes):
	next_hash = present_hashes
	for idx, base in enumerate(bases):
		next_hash[idx] -= prev
		next_hash[idx] /= base
		next_hash[idx] += next * math.pow(base, 2)
	return next_hash
if __name__ == '__main__':
	w="Hi i am abhishek kamal, an apple a day keeps a doctor away"
	patterns=['HI I AM', 'I AM ABHISHEK', 'AM ABHISHEK KAMAL', 'ABHISHEK KAMAL AN', 'KAMAL AN APPLE', 'AN APPLE A', 'APPLE A DAY', 'A DAY KEEPS', 'DAY KEEPS A', 'KEEPS A DOCTOR']
	patt_code=[15, 8, 12, 55, 33, 13, 45, 0, 27, 51, 0, 69]
	bases = (113, 117, 119, 123, 129, 131, 137)
	filter = ff_bloom_filter(10000007)
	window=deque()
	#print(window)
	indices=[0]*7
	a=patt_code[0]
	b=patt_code[1]
	c=patt_code[2]
	for i,base in enumerate(bases):
		#hash values calculation using each 7 prime number and storing in the indices array
		indices[i]=a+b*base+c*math.pow(base,2)
	filter.set_bit(1, indices)
	window.extend([a, b, c])
	#print(window)
	for code in patt_code[3:]:
		x = window.popleft()
		window.append(code)
		indices=roll_hash(x,code,indices)
	filter.set_bit(1, indices)


#What we are doing is after getting the ascii value of words and storing it in patt_code. and we are applying rolling hash function of 
