#Разбивает на слова и символы, строит логические связи и подчинение, определяет роль каждого слова

from pymystem3 import Mystem
import subprocess
import re
import os
signs=('.','!','?')
allsigns=(',','.','!','?','\'','"',':',';','(',')','/','&')

def parse(str):
	str=re.sub(r'([.,!?"/():;&\'])',r' \1 ',str).split()
	class word:
		cont=''
		speech=''
		sentence=''
	text=[]
	for i in range(len(str)):
		text.append(word())
		text[i].cont=str[i]
		if text[i] in allsigns:
			text[i].speech='signs'
	i=0
	while i<=len(text)-2:
		if (text[i].cont in allsigns) and (text[i+1].cont in allsigns):
			text[i].cont+=text[i+1].cont
			del text[i+1]
			if text[i+1].cont in allsigns:
				text[i].cont+=text[i+1].cont
				del text[i+1]
		i+=1
	for i in text:
		if i.speech!='signs':
			cmd = 'echo "'+i.cont+'" | '+os.getcwd()+'/mystem -i'
			PIPE = subprocess.PIPE
			p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
			stderr=subprocess.STDOUT, close_fds=True, cwd='/home/')
			print(bytes(p.stdout.read()).decode('utf8'))

	class sentence:
		word=[]
		number=1
	num=0
	mas=[sentence()]
	for i in range(len(text)):
		mas[num].word.append({'original':text[i].cont,'change':text[i].cont,'number':num+1,'speech':'','sentence':''})
		if (text[i] in signs) and (i!=len(text)-1):
			num+=1
			mas.append(sentence())
			mas[num].word=[]
			mas[num].number=num+1
	return mas

#mas[i].word[j]['...']
#original - Начальное слово
#change - Замена
#number - Номер предложения
#speech - Часть речи
#sentence - Часть предложения
#!? ?! !" ?"
