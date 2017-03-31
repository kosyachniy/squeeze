#Разбивает на слова и символы, строит логические связи и подчинение, определяет роль каждого слова

import re
signs=('.','!','?')
def parse(text):
	text=re.sub(r'([.,!?])',r' \1 ',text).split()
	class sentence:
		word=[]
	mas=[sentence()]
	num=0
	for i in text:
		mas[num].word.append({'orig':i,'number':num})
		if i in signs:
			num+=1
			mas.append(sentence())
	return mas

#!? ?! !" ?"
