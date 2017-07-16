'''
This file is used to de-serlize data
'''

from pet import Pet,Dog
import pickle


data=[]
with open('animals2.pk','rb') as input:
	for t in range(3):
		data.append(pickle.load(input))

for t in data:
	print t
