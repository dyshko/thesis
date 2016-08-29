#this program calculates the groups Mon(C) and Iso(C)
#and outputs their sizes. The input code is represented
#by the set of columns and a multiplicity function:
#a vector that says how many columns of the corresponding
#type belong to the code.
#Since the considered codes have small cardinality
#and are over the binary alphabet {0,1}, it is 
#implemented the brute-force algorithm

import itertools

#returns the Hamming distance between two codewords
def hamming_distance(cw1, cw2, mlt):
    return sum([mlt[i] for i in range(len(mlt)) if \
	cw1[i]!=cw2[i]])

#check if there is a Hamming isometry between two codes
#(second distance distribution is precalculated)
def isometry(code_new, code_dist, mlt):
    m = len(code_new) 	#the number of rows
    for i in range(m):
        for j in range(i+1, m):
            if hamming_distance\
            (code_new[i], code_new[j], mlt)!=code_dist[i][j]:
                return False
    return True

#action of permutation
def act_perm(code, p):
    m = len(code)
    res = []
    for i in range(m):
        res.append(code[p[i]])
    return res

#code to string
def code_to_str(code, mlt):
    m = len(code) 	#the number of rows
    columns = [list(x) for x in zip(*code)]
    for col in columns:
        if col[0]==1:
            for i in range(m):
                col[i]^=1
    columns, new_mlt = zip(*sorted(zip(columns, mlt)))
    return "".join([str(col) \
    for col in columns])+str(new_mlt)

#main
def sizes_of_groups(code, mlt):
	MON = []
	ISO = []
	N = len(code[0]) #size of the support
	m = len(code) 	#the number of rows

	code_dist = [[0]*m for i in range(m)]
	for i in range(m):
		code_dist[i][i] = 0
		for j in range(i+1,m):
			code_dist[i][j] =\
	code_dist[i][j] = hamming_distance(code[i], code[j], mlt)

	code_str = code_to_str(code, mlt)
	
	for p in itertools.permutations(list(range(m))):
		code_new = act_perm(code, p)
		if isometry(code_new, code_dist, mlt):
			ISO+=[p]
			if code_to_str(code_new, mlt)\
			==code_str:
				MON+=[p]
	print("#Mon(C) = "+str(len(MON))+ "\t #Iso(C)="\
	+str(len(ISO)))

########## INPUTS #####################

C1 = [
[1,0,0,0,0,1,1,1,1,0,0,0,0,0,0],
[0,1,0,0,0,1,0,0,0,1,1,1,0,0,0],
[0,0,1,0,0,0,1,0,0,1,0,0,1,1,0],
[0,0,0,1,0,0,0,1,0,0,1,0,1,0,1],
[0,0,0,0,1,0,0,0,1,0,0,1,0,1,1]
    ]

mlt11 =[0,1,2,3,4,6,5,4,3,4,3,2,2,1,0]

##############

C2 = [
[1,0,0,0,1,1,1],
[0,1,0,0,1,0,0],
[0,0,1,0,0,1,0],
[0,0,0,1,0,0,1]
    ]

mlt21 =[1,2,3,4,0,0,0]

mlt22 =[1,1,2,3,0,0,0]

mlt23 =[1,1,1,2,0,0,0]

mlt24 =[1,1,2,2,0,0,0]

mlt25 =[0,0,0,0,2,1,0]

mlt26 =[0,0,0,0,1,1,0]

mlt27 =[1,1,1,1,0,0,0]

#############

C3 = [
[0,0,0,0],
[1,1,0,0],
[1,0,1,0],
[1,0,0,1],
[0,1,1,0]
    ]

mlt31 = [1,1,1,1]

########## OUTPUT #####################

print("Code 1:")
sizes_of_groups(C1, mlt11)
print("Code 2:")
sizes_of_groups(C2, mlt21)
print("Code 3:")
sizes_of_groups(C2, mlt22)
print("Code 4:")
sizes_of_groups(C2, mlt23)
print("Code 5:")
sizes_of_groups(C2, mlt24)
print("Code 6:")
sizes_of_groups(C2, mlt25)
print("Code 7:")
sizes_of_groups(C2, mlt26)
print("Code 8:")
sizes_of_groups(C2, mlt27)
print("Code 9:")
sizes_of_groups(C3, mlt31)

"""
Code 1:
#Mon(C) = 1	 #Iso(C)=120
Code 2:
#Mon(C) = 1	 #Iso(C)=1
Code 3:
#Mon(C) = 2	 #Iso(C)=2
Code 4:
#Mon(C) = 6	 #Iso(C)=6
Code 5:
#Mon(C) = 4	 #Iso(C)=4
Code 6:
#Mon(C) = 4	 #Iso(C)=4
Code 7:
#Mon(C) = 8	 #Iso(C)=8
Code 8:
#Mon(C) = 24	 #Iso(C)=24
Code 9:
#Mon(C) = 6	 #Iso(C)=12
"""
