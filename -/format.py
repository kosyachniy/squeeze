#Перевод текстов в формат CSV

from parse import parse
import csv

def learn():
	f=open('db','r')
	orig=[]
	chang=[]
	inp=[]
	out=[]
	t=True
	for i in f:
		if f:
			inp.append(i[:-2])
			orig.append(parse(i))
			f=False
		else:
			out.append(i[:-2])
			chang.append(parse(i))
			f=True
	return orig, chang, inp, out

io=open('input.txt','r')
oo=open('output.txt','r')
#ic=open('input.csv','w')
#oc=open('output.csv','w')
#orig=[]
#chang=[]
#t=True
#for i in io:
#	ic.strip()

with open('input.csv', 'w') as csvfile:
	writer=csv.writer(csvfile, quotechar=' ', quoting=csv.QUOTE_MINIMAL)
	for i in io:
		for j in parse(i.strip()):
			writer.writerow(j)
with open('output.csv', 'w') as csvfile:
	writer=csv.writer(csvfile, quotechar=' ', quoting=csv.QUOTE_MINIMAL)
	for i in oo:
		writer.writerow(i.strip())

io.close()
oo.close()
#ic.close()
#oc.close()