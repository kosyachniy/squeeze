#Ищет отсылки, примечания, дополнения -> удаляет

def additionally(text):
	for i in text:
		for j in i.word:
			if int(j['deep'])>=2:
				j['change']=''
	return text
