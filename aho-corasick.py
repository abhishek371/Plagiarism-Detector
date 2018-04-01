maxs=500

maxc=26

out=[0]*maxs

f=[-1]*maxs

g=[]

for i in range(maxs):

    g.append([])

    for j in range(maxc):

        g[i].append(-1)

def buildMatchingMachine(arr,k):

    states=1

    for i in range(k):

        word=arr[i]

        currentState=0

        for j in range(len(word)):

            ch=ord(word[j])-ord('a')

            if(g[currentState][ch]==-1):

                g[currentState][ch]=states;

                states+=1

            currentState=g[currentState][ch]

        out[currentState] |= (1<<i)

 

    for ch in range(maxc):

        if (g[0][ch]==-1):

            g[0][ch]=0

    q=[]

    for ch in range(maxc):

        if g[0][ch]!=0:

            f[g[0][ch]]=0

            q.append(g[0][ch])

    while(len(q)):

        state=q.pop(0)

        for ch in range(maxc):

            if(g[state][ch]!=-1):

               failure=f[state]

               while(g[failure][ch]==-1):

                   failure=f[failure]

               failure=g[failure][ch]

               f[g[state][ch]]=failure

               out[g[state][ch]] |= out[failure]

               q.append(g[state][ch])

    return states

def findNextState(currentState,nextInput):

    answer=currentState

    ch=ord(nextInput)-ord('a')

    while(g[answer][ch]==-1):

        answer=f[answer]

    return g[answer][ch]

def searchWords(arr,k,text):

    buildMatchingMachine(arr,k)

    currentState=0

    for i in range(len(text)):

        currentState=findNextState(currentState,text[i])

        if(out[currentState]==0):

            continue

        for j in range(k):

            if (out[currentState] & (1<<j) ):

               print(" WORD " + arr[j] +" "+ str(i-len(arr[j])+1) +" to " + str(i) )

arr=["he","she","hers","his"]

text="ahishers"

k=4

searchWords(arr,k,text)