from pet import Pet,Dog
import pickle

d1=Dog("Mike",True)
d2=Dog("Tom",False)
d3=Dog("Fred",True)

d=[]
d.append(d1)
d.append(d2)
d.append(d3)

with open('animals2.pk','wb') as output:
	for t in d:
		pickle.dump(t,output,-1)
