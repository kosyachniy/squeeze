#Разбивает на слова и символы, строит логические связи и подчинение, определяет роль каждого слова

#from pymongo import MongoClient
from pymorphy2 import MorphAnalyzer
import re
import os
signs=',.!?\'":;/&'
m=MorphAnalyzer()

def morph(text):
#	MongoDB
	p=(m.parse(text)[0]).tag
	return p.POS, p.gender, p.case, p.number

def parse(str):
#Разбиение текста на слова
	str=re.sub(r'(['+signs+'()<>\[\]])',r' \1 ',str).split()
	class word:
		def __init__(self,cont='',speech='',case='',number='',gender=''):
			self.cont=cont
			self.speech=speech
			self.sentence=''
			self.case=case
			self.number=number
			self.gender=gender
	text=[]
	t=False
	for i in range(len(str)):
#Объединение знаков
		if str[i] in signs:
			if t:
				text[len(text)-1].cont+=str[i]
			else:
				text.append(word(str[i],'signs'))
				t=True
		else:
#Определение граммем (части речи, падежа, рода, числа, ...)
			text.append(word(str[i],(x for x in morph(str[i]))))
			t=False
			
#			print(p)
#import subprocess
#			cmd='echo "'+i.cont+'" | '+os.getcwd()+'/mystem -i'
#			PIPE=subprocess.PIPE
#			p=subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
#			stderr=subprocess.STDOUT, close_fds=True, cwd='/home/')
#			print(bytes(p.stdout.read()).decode('utf8'))

#Объединение слов в предложения
	class sentence:
		def __init__(self,number=1):
			self.word=[]
			self.count=0
			self.number=number
	num=0
	mas=[sentence()]
	for i in range(len(text)):
		if text[i].speech in ('PRED', 'NPRO', 'CONJ', 'PRCL', 'ADJF', 'NUMR', 'ADJS', 'NOUN', 'VERB', 'INTJ', 'PRTS', 'ADVB', 'PRTF', 'INFN', 'PREP', 'GRND', 'COMP'):
			mas[num].count+=1
		mas[num].word.append({'original':text[i].cont,'change':text[i].cont,'numsp':num+1,'speech':text[i].speech,'sentence':text[i].sentence,'case':text[i].case,'number':text[i].number,'gender':text[i].gender})
		if any(c in ('.!?') for c in text[i].cont) and (i!=len(text)-1):
			num+=1
			mas.append(sentence(num+1))

#Определение членов предложения (ЗАМЕНИТЬ НЕЙРОНКОЙ)
	t=False
	for i in mas:
		for j in i.word:
			if (j['case']=='nomn'): # or (j['speech']=='INFN')
				j['sentence']='subject'
				t=True
	if t:
		for i in mas:
			for j in i.word:
				if j['speech'] in ('VERB','INFN'):
					j['sentence']='predicate'
#	Если предложение из одного слова???
	for i in mas:
		if i.count==1:
			for j in i.word:
				if j['speech'] in ('VERB','INFN'):
					j['sentence']='predicate'

	return mas
