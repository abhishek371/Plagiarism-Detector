def RabinKarp(txt,pat):
	p=0
	n=len(txt)
	m=len(pat)
	d=256
	h=1
	q=11
	hash_pat=0
	hash_txt=0
	#1.finding the value of h = d^m-1
	for i in range(0,m):
		h=(h*d)%q

	#2.finding the hash value of pattern and hash value of first shift window in text
	for i in range(0,m-1):
		hash_pat=(d*hash_pat+ord(pat[i]))%q
		hash_txt=(d*hash_txt+ord(txt[i]))%q

	#3.Sliding of character to find the match
	for s in range(0,n-m+1):
		if hash_txt==hash_pat:
			#check each character
			for i in range(m):
				if txt[s+i]!=pat[i]:
					break
			if i==m-1:
				print("Pattern found at position %s"%(s))
				p=p+1
		else:
			'''
			slide the window
			finding the new hash value
			s=trailing letter index
			s+m=leading letter or incoming letter index'''
			if s<n-m:
				hash_txt=(d*(hash_txt-ord(txt[s])*h)+ord(txt[s+m]))%q
				#if new hash value is less than 0, then it has to be made positive
				if hash_txt<0:
					t=t+q
	return p

def Plag_Test(p,n):
	Plag_percentage=(p/n)*100
	print("Plag percentage : %s"%(Plag_percentage))




def main():
	text=input("Enter the Text :")
	pattern=input("Enter the pattern to be search :")
	p=RabinKarp(text,pattern)
	Plag_Test(p,len(text))
	

if __name__ == '__main__':
	main()