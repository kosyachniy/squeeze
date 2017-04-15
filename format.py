#Перевод текстов в формат CSV

from parse import parse
import csv

def text(x):
	y=[]
	for i in parse(x):
		for j in i.word:
			if j['speech']!='sign':
				y.append(j['infinitive'])
	return y

io=open('input.txt','r')
oo=open('output.txt','r')

with open('input.csv', 'w') as csvfile:
	writer=csv.writer(csvfile, quotechar=' ', quoting=csv.QUOTE_MINIMAL)
	for i in io:
		inp=text(i.strip())
		writer.writerow(inp)
with open('output.csv', 'w') as csvfile:
	writer=csv.writer(csvfile, quotechar=' ', quoting=csv.QUOTE_MINIMAL)
	for i in oo:
		out=text(i.strip())
		writer.writerow(out)

io.close()
oo.close()