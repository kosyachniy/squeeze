#Проверяет грамотность, логичность, связанность -> корректирует

#priority=['-',':','?','!','.',','] Для замены, если стоят подряд
norepeat=',«»'
casesigns='.!?«'
closesigns=')>\]\}'

def literacy(text):
#Убираем повторяющиеся знаки
	deep=0
	for i in text:
		t=False
		f=True
		for j in range(len(i.word)):
			word=i.word[j]['change']
			if word in norepeat:
				if t:
					word=''
				else:
					t=True
			else:
				t=False

#Заглавные буквы, регистр
			if f and word:
				word=word[0].upper()+word[1:]
				f=False
			if any(c in casesigns for c in word):
				f=True

#Проверка глубины предложений
			if i.word[j]['deep']<=0:
				if i.word[j-1]['change'] in closesigns:
					i.word[j-1]['change']=''
					deep+=1
			i.word[j]['deep']+=deep #Чтобы компенсировать удалённый знак
			i.word[j]['change']=word
		last=i.word[len(i.word)-1]
		if (last['deep']==1) and (last['change'] in closesigns):
			last['change']=''

	return text
