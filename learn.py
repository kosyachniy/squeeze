from parse import parse

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