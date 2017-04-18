#Обучение нейронной сети сокращению

from learn import learn

orig,chang,x,y=learn()
for i in range(len(orig)):
	inp=[]
	out=[]
	for j in orig[i]:
		for u in j.word:
			if u['speech']!='sign':
				inp.append(u['infinitive'])
	for j in chang[i]:
		for u in j.word:
			if u['speech']!='sign':
				out.append(u['infinitive'])
	# x - исходный текст
	# y - изменённый текст
	# inp - список слов исходного текста в инфинитиве
	# out - список слов изменённого текста в инфинитиве