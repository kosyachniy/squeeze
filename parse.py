#Разбивает на слова и символы, строит логические связи и подчинение, определяет роль каждого слова

import re
signs=('.','!','?')
def parse(text):
	text=re.sub(r'([.,!?])',r' \1 ',text).split()
	class sentence:
		word=[]
		number=1
	num=0
	mas=[sentence()]
	for i in range(len(text)):
		mas[num].word.append({'orig':text[i],'sentence':num+1})
		if (text[i] in signs) and (i!=len(text)-1):
			num+=1
			mas.append(sentence())
			mas[num].word=[]
			mas[num].number=num+1
	return mas

#!? ?! !" ?"
