#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CHECKING FOR FIRST CONDITION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#lists=[]
#temp=[]
'''k=0
j=0
i=0
while (i<len(Prod)):
	for j in range(i,len(GS[k])+i):
		lists.append(FirstP[j])
	if(len(lists)>1):
		temp=list(set.intersection(*map(set, lists)))
		if(len(temp)>0):
			print "\n\n\nOOPS:	GRAMMAR IS NOT LL(1)\n\n\n"
			exit(1)
	del lists[:]
	i=j+1
	k=k+1 
	
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CHECKING FOR SECOND CONDITION~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
k=0
j=0
i=0
while (i<len(Prod)):
	for j in range(i,len(GS[k])+i):
		lists.insert(0,FirstP[j])
	count=0
	i=j+1
	for j in range(0,len(lists)):
		print lists[j]
		if('^' in lists[j]):
			lists.pop(j)
			count=count+1
	if(count>1):
		print "\n\n\nOOPS:	GRAMMAR IS NOT LL(1) (LEFT RECURSION PROBLEM)\n\n\n"
		exit(1)
	elif(count>0):
				
		for j in range(0,len(lists)):
			if(list(set(lists[j]) & set(Follow[k]))):
				print "\n\n\nOOPS:	GRAMMAR IS NOT LL(1) (LEFT RECURSION PROBLEM)\n\n\n"
				exit(1)
	#print j
	#i=j+1
	k=k+1'''
	
	
	


S->Aa|b
A->Ac|Sd|e
ea$

E->E+E|E-E|E*E|E/E|id
i+i*i$

E->T+E|T
T->i*T|i|(E)
X->+E|^
Y->*T|^
i+i*i$

S->Ab|^
A->c
D->Sc|d
ia,a,a


E->TX 
X->+E|^
T->(E)|iY
Y->*T|^
i*i$

E->TA
A->+TA|^
T->FB
B->*FB|^
F->(E)|i
i+i*i$

S->aAB|AB|^
A->aAb|^
B->bBc|AS
aab$
