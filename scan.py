#This files basically check the input phrase with pattern. Same process it takes first group word is a phrases and when a phrase is ready, it calculate its hash 
#hash value and then it corresponding to that hash value checks in bloom filter ,if already present then is add in 2nd bloomfilter.

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
	input='An apple is a sweet, edible fruit produced by an apple tree.An apple a day keeps a doctor away. Apple trees are cultivated worldwide as a fruit tree.'
	hold,word,appended,shift_no=0,'',True,0
	window=deque()
	input_code=[]
	bases = (113, 117, 119, 123, 129, 131, 137)
	indices=[0]*7
	prev=''
	first,pair=True,[]
	input.upper()
	for idx,c in enumerate(input):
		if 'A'<=c<='Z':
			if first:
				pair.append(idx)
				first=False
			appended=False
			hold=hold+ord(c)-65
			word=word+c
		else:
			if appended is False:
				input_code.append(hold)
				pair.append(idx)
				window.append([word,pair])
				if len(input_code)==3:
					if shift_no==0:
						a, b, c = input_code[0],input_code[1],input_code[2]
						for idx, base in enumerate(self.bases):
							indices[idx] = a + b * base + c * math.pow(base, 2)
					else:
						indices = self.roll_hash(prev, hold, indices)

					if filter.look_up(1, indices):
						filter.set_bit(2, indices)
						input_phrases.append(window[0][0]+' '+window[1][0]+' '+window[2][0])
						input_phrases_idx.append([window[0][1][0],window[2][1][1]])
					prev = self.input_code.popleft()
					window.popleft()
					shift_no += 1
				hold, word, appended,first,pair = 0, '', True,True,[]