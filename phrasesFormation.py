from collections import deque
#patterns-making collection of three words
#pattcode-containg ascii value of all the words
#this code is making phrases containing 3 words and storing it in list called pattern
#and storing total ascii value of a word is list named pattcode
if __name__ == '__main__':
	patterns=[]
	pattcode=[]
	w="Hi i1 am abhishek kamal, an apple a day keeps a doctor away"
	line=w.upper()
	hold, word, appended = 0, '', True
	window = deque()
	for c in line:
		if 'A' <= c <= 'Z':
			appended = False
			hold = hold + ord(c) - 65
			word = word + c
		else:
			if appended is False:
				pattcode.append(hold)
				window.append(word)
				if len(window) == 3:
					patterns.append(' '.join(list(window)))
					window.popleft()
				hold, word, appended = 0, '', True

	print(window)
	print(patterns)
	print(pattcode)