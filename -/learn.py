from parse import parse

opensigns='(<\[\{'+'«'

def assembly(mas):
	text=''
	t=False
	for i in mas:
		for j in i.word:
			if (j['infinitive'] in opensigns) and t:
				text+=' '
				t=False
			elif (j['speech']!='sign') and t:
				text+=' '
			else:
				t=True
			text+=j['infinitive']
	return text

def learn():
	f=open('db','r')
	orig=[]
	chang=[]
	t=True
	for i in f:
		if f:
			orig.append(parse(i))
			f=False
		else:
			chang.append(parse(i))
			f=True
	return orig, chang

a,b=learn()
for i in a:
	print(assembly(i))
print('-----')
for i in b:
	print(assembly(i))
