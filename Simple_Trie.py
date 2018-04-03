class Node:
	def __init__(self,value):
		self.value=value
		self.children=[None for _ in range(26)]
		self.isEnd=False

class Simple_Trie:
	def __init__(self):
		self.root=Node(None)

	def insert_word(self,wrd):
		temp=self.root
		self.l=len(wrd)
		for curr_letter in wrd.lower():
			v=ord(curr_letter)-ord('a')
			if temp.children[v] is None:
				temp.children[v]=Node(curr_letter)
				if curr_letter==wrd[self.l-1]:
					temp.isEnd=True
			temp=temp.children[v]

	def isPresent(self,word):
		temp=self.root
		for curr_letter in word.lower():
			v=ord(curr_letter)-ord('a')
			if temp.children[v] is None:
				return False
			else:
				temp=temp.children[v]
		return True


def main():
	S=Simple_Trie()
	S.insert_word('hello')
	S.insert_word('Abhishek')
	'''print("Enter the words to put in trie :(0 to stop)")
	while True:
		n=input()
		if n==0:
			break
		S.insert_word(n)'''
	search_wrd=input("Enter the word u want to search :")
	k=S.isPresent(search_wrd)
	if k is True:
		print("True")
	else:
		print("False")

if __name__ == '__main__':
	main()