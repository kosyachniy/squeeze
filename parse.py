#Разбивает на слова и символы, строит логические связи и подчинение, определяет роль каждого слова

#from pymongo import MongoClient
from pymorphy2 import MorphAnalyzer
import subprocess
import re
import os
allsigns=(',.!?\'":;()/&')

def parse(str):
#Разбиение на слова и объединение знаков
	str=re.sub(r'([.,!?"/():;&\'])',r' \1 ',str).split()
	class word:
		cont=''
		speech=''
		sentence=''
		case=''
		number=''
		gender=''
	text=[]
	for i in range(len(str)):
		text.append(word())
		text[i].cont=str[i]
		if text[i].cont in allsigns:
			text[i].speech='signs'
	i=0
	while i<=len(text)-2:
		if (text[i].cont in allsigns) and (text[i+1].cont in allsigns):
			text[i].cont+=text[i+1].cont
			del text[i+1]
			if (i<=len(text)-2) and (text[i+1].cont in allsigns):
				text[i].cont+=text[i+1].cont
				del text[i+1]
		i+=1

#Определение граммем (части речи, падежа, рода, числа, ...)

#	client=MongoClient()
#	db=client['k']
#	cursor=db.user.find()
#	for doc in cursor:
#		print(doc)

	morph=MorphAnalyzer()
	for i in text:
		if i.speech!='signs':
			p=(morph.parse(i.cont)[0]).tag
			print(p)
			i.speech=p.POS
			i.gender=p.gender
			i.case=p.case
			i.number=p.number
#			cmd='echo "'+i.cont+'" | '+os.getcwd()+'/mystem -i'
#			PIPE=subprocess.PIPE
#			p=subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
#			stderr=subprocess.STDOUT, close_fds=True, cwd='/home/')
#			print(bytes(p.stdout.read()).decode('utf8'))

#Разбиение на предложения
	class sentence:
		def __init__(self):
			self.word=[]
			self.count=0
		number=1
	num=0
	mas=[sentence()]
	for i in range(len(text)):
		if text[i].speech in ('PRED', 'NPRO', 'CONJ', 'PRCL', 'ADJF', 'NUMR', 'ADJS', 'NOUN', 'VERB', 'INTJ', 'PRTS', 'ADVB', 'PRTF', 'INFN', 'PREP', 'GRND', 'COMP'):
			mas[num].count+=1
		mas[num].word.append({'original':text[i].cont,'change':text[i].cont,'numsp':num+1,'speech':text[i].speech,'sentence':text[i].sentence,'case':text[i].case,'number':text[i].number,'gender':text[i].gender})
		if any(c in ('.!?') for c in text[i].cont) and (i!=len(text)-1):
			num+=1
			mas.append(sentence())
			mas[num].number=num+1

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
	#Если предложение из одного слова???
	for i in mas:
		if i.count==1:
			for j in i.word:
				if j['speech'] in ('VERB','INFN'):
					j['sentence']='predicate'

	return mas
