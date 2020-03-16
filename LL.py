import re

#Reading Input File
fp=open("Input.txt","r")
r=fp.readlines()

#Variable declarations
Variable=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','T','S','U','V','W','X','Y','Z']
i=0
l=0
j=0
k=0
m=0
n=0


print ("\n***************************THE PROVIDED GRAMMAR IS ::**************************\n")
Grammar=[]
for line in r:
	Grammar.append(line.split())
length= len(Grammar)-1
for i in range (0,length):
	print ('\t\t\t\t',Grammar[i][0])

print ("\n************************THE PROVIDED INPUT STRING IS ::************************\n")
print ('\t\t\t\t',Grammar[length][0])

p=[]
for i in range (0,length):
	p.append(Grammar[i][0].split("->"))

GS=[]
for i in range (0,length):
	GS.append(re.split(r'[|]',p[i][1]))

#-------------------------------------Finding out the Position of a Variable--------------------------------------#
def Position(Var,p=[]):
	for i in range (0,len(p)):
		if p[i][0]==Var:
			return i;
	return -1;

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FIRST OF VARIABLES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
First=[[] for i in range(length)]
	
def CopyFirst(Pos,i,Source=[],Dest=[]):
	for l in range (0,len(Source[Pos])):
		if Source[Pos][l] not in Dest[i] and  Source[Pos][l]!='^':
			Dest[i].append(Source[Pos][l])
			
                       #--------Appending the Terminals to First of Varibales---------#
for i in range (0,length):
	for j in range (0,len(GS[i])):
		if GS[i][j][0] not in Variable and GS[i][j][0] not in First[i]:
			First[i].append(GS[i][j][0])
		
		
						#--------Appending the First of Variables to the First of Varibles-------#
	
def InitFirst():
	for i in range (0,length):
		for j in range (0,len(GS[i])):
			if GS[i][j][0] in Variable and GS[i][j][0]!=p[i][0]:
				k=Position(GS[i][j][0],p)
				CopyFirst(k,i,First,First)
				for m in range(1,len(GS[i][j])):
					if '^' in First[k]:
						if GS[i][j][m] not in Variable and GS[i][j][m] not in First[i]:
							First[i].append(GS[i][j][m])
							break
						else:
							k=Position(GS[i][j][m],p)
							CopyFirst(k,i,First,First)
					else:
						break
				if '^' in First[k] and '^' not in First[i]:
					First[i].append('^')
					
i=0
UpdatedFirst=[[] for i in range(length)]
def ComputeFirst():
	count=0
	InitFirst()
	for i in range (0,length):
		if len(UpdatedFirst[i])==len(First[i]):
			count+=1
	if count!=length:
		for i in range (0,length):
			UpdatedFirst[i]=list(First[i])
		ComputeFirst()
	else:
		return;
				
ComputeFirst()				
				
						#------------Printing the First of Varibles-----------------#
print ("\n**************************FIRST OF VARIABLES ARE ::****************************\n")					
for i in range (0,length):
	print ('\t\t\t   ',p[i][0],' = ',UpdatedFirst[i])
	


	
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~FOLLOW OF VARIABLES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
Follow=[[] for i in range(length)]
Follow[0].append('$')
							#-------------------------------------------------#
def CopyFollow(Pos,i,j,List=[]):
	if Pos==len(List)-1:
		CopyFirst(j,i,Follow,Follow)
	elif List[Pos+1] not in Variable:
		if List[Pos+1] not in Follow[i]:
			Follow[i].append(List[Pos+1])
	elif List[Pos+1]!=p[i][0]:
		m=Position(List[Pos+1],p)
		CopyFirst(m,i,First,Follow)
		if '^' in First[m]:
			CopyFollow(Pos+1,i,j,List)
		else:
			return;
	else:
		return;
					
							#-----------------------------------------------------------#
def	InitFollow():
	for i in range (0,length):
		for j in range (0,length):
			for k in range (0,len(GS[j])):
				l=Position(p[i][0],GS[j][k])
				if l!=-1:
					CopyFollow(l,i,j,GS[j][k])


							#-----------------------------------------------------------#
UpdatedFollow=[[] for i in range(length)]							
def ComputeFollow():
		count=0
		InitFollow()
		for i in range (0,length):
			if len(UpdatedFollow[i])==len(Follow[i]):
				count+=1
		if count!=length:
			for i in range (0,length):
				UpdatedFollow[i]=list(Follow[i])
			ComputeFollow()
		else:
			return;
			
							#------------------------------------------------------------#
ComputeFollow()
for i in range (0,length):
	if ('^' in UpdatedFollow[i]):
		UpdatedFollow[i].remove('^')
	
							#------------Printing the Follow of Varibales------------------#
print ("\n*************************FOLLOW OF VARIABLES ARE ::****************************\n")	
for i in range (0,length):
	print ('\t\t\t   ',p[i][0],' = ',UpdatedFollow[i])
						


							#------------First of Production rules-----------------------#
Prod=[]
for i in range (0,length):
	for j in range (0,len(GS[i])):
		Prod.append(GS[i][j])
FirstP=[[] for i in range(len(Prod))]
for i in range(0,len(Prod)):
		if Prod[i][0] not in Variable:
			FirstP[i].append(Prod[i][0])
		else:
			k=Position(Prod[i][0],p)
			CopyFirst(k,i,First,FirstP)
			for m in range(1,len(Prod[i])):
				if '^' in First[k]:
					if Prod[i][m] not in Variable:
						FirstP[i].append(Prod[i][m])
						break
					else:
						k=Position(Prod[i][m],p)
						CopyFirst(k,i,First,FirstP)
			
			if '^' in First[k] and '^' not in FirstP[i]:
				FirstP[i].append('^')


print ("\n**************************FIRST OF PRODUCTIONS ARE ::***************************\n")			
for i in range (0,len(Prod)):
	print ('\t\t\t   ',Prod[i],' = ',FirstP[i])



							#--------------Terminals-------------------#
i=0
j=0
k=0				
Terminal=[]
for i in range(0,len(Prod)):
	for j in range(0,len(Prod[i])):
		if Prod[i][j] not in Variable and Prod[i][j] not in Terminal and Prod[i][j]!='^':
			Terminal.append(Prod[i][j])
			
Terminal.append('$')

#------------------------------PARSING TABLE GENERATION------------------------------------#
Table=[[0]*(len(Terminal)) for x in range(len(p))] 
for i in range (0,len(p)):
	for j in range (n,n+len(GS[i])):
		for k in range(0,len(FirstP[j])):
			if FirstP[j][k]=='^':
				for l in range(0,len(Follow[i])):
					m=Position(Follow[i][l],Terminal)
					if(Table[i][m]==0):
						Table[i][m]=Prod[j]
					else:
						print ("\n\n\nOOPS:	GRAMMAR IS NOT LL(1)")
						print ("\n\t(Double ENTRY IN TABLE AT",p[i][0],',',Terminal[m],':',Table[i][m],'AND',Prod[j],")\n\n\n")
						exit(1)
			else:
				m=Position(FirstP[j][k],Terminal)
				if m!=-1:
					if(Table[i][m]==0):
						Table[i][m]=Prod[j]
					else:
						print ("\n\n\nOOPS:	GRAMMAR IS NOT LL(1)")
						print ("\n\t(Double ENTRY IN TABLE AT",p[i][0],',',Terminal[m],':',Table[i][m],'AND',Prod[j],")\n\n\n")
						exit(1)
	n=j+1
print ("\n**************************PARSING TABLE IS ::***********************************\n")
print ('\t\t',)
for i in range (0,len(Terminal)):
	print (Terminal[i],'\t\t',)
print ('\n')
for i in range (0,len(p)):
	print (p[i][0],'\t\t' ,)
	for j in range (0,len(Terminal)):
		print (Table[i][j] ,'\t\t',)
	print ("\n",)
	
	
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~PARSING OF THE INPUT STRING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
         
print ("\n\n*********************PARSING OF THE INPUT STRING********************************")
print ("\nSTACK\t\t\tINPUT\t\t\t\tACTION\n\n")
row=0
column=0
i=0
s=Stack()
s.push('$')
s.push(p[0][0])
while i<len(Grammar[length][0]):
	for j in range(0,s.size()):
		print (s.items[j],)
	print ("\t\t\t",)
	for j in range(i,len(Grammar[length][0])):
		print (Grammar[length][0][j],)
	print ("\t\t\t",)
	if s.peek() not in Variable and s.peek()!='$' and s.peek()==Grammar[length][0][i]:
		s.pop()
		print ("SHIFT")
		i=i+1
	elif s.peek()=='$':
		if Grammar[length][0][i]=='$' and i==len(Grammar[length][0])-1:
			print ("ACCEPTED")
			break;
		else:
			print ("\n\n**************************REJECTED*************************************\n\n")
			exit(0)
	else:
		row=Position(s.peek(),p)
		column=Position(Grammar[length][0][i],Terminal)
		if Table[row][column]==0:
			print ("\n\n**************************REJECTED**************************************\n\n")
			exit(0)
		s.pop()
		if Table[row][column]!='^':
			for j in range ((len(Table[row][column]))-1,-1,-1):
				s.push(Table[row][column][j])
		print ("REDUCE",'(',p[row][0],'->',Table[row][column],')')
		

print ("\n\n************************STRING IS ACCEPTED**************************************")		
print ("\n\n~~~~~~~~~~~~~~~~~~~~~~~~END OF THE PROGRAM~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

