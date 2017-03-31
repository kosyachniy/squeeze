#Разбивает на слова и символы, строит логические связи и подчинение, определяет роль каждого слова

import re
signs=('.','!','?')
def parse(text):
	text=re.sub(r'([.,!?])',r' \1 ',text).split()
	class sentence:
		word=[]
		number=0
	num=0
	mas=[sentence()]
	mas[0].number=1
	for i in text:
		mas[num].word.append({'orig':i,'number':num+1})
		if i in signs:
			num+=1
			sent2=sentence()
			mas.append(sentence())
			mas[num].number=num+1
	return mas

#!? ?! !" ?"
