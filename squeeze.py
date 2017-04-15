from parse import parse
#from style import style
#from excess import excess
#from attachment import attachment
#from additionally import additionally
from literacy import literacy

opensigns='(<\[\{'+'«'

def assembly(mas):
	text=''
	t=False
	for i in mas:
		for j in i.word:
			if (j['change'] in opensigns) and t:
				text+=' '
				t=False
			elif (j['speech']!='sign') and t:
				text+=' '
			elif (j['change']!=''):
				t=True
			text+=j['change']
	return text

mas=parse(input())
#type=style(mas)
#mas=excess(mas)
#mas=attachment(mas)
#mas=additionally(mas)
mas=literacy(mas)

print('\n')
for i in mas:
	print(i.number,end=' ')
	for j in i.word:
		print(j['original'],'(',j['speech'],'-',j['sentence'],')',end=' ')
	print('\n')
print('\n')
print(assembly(mas))