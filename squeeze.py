from parse import parse
from style import style
from excess import excess
from attachment import attachment
from additionally import additionally
from literacy import literacy

mas=parse(input())
#type=style(mas)
mas=literacy(additionally(attachment(excess(mas))))

print()
for i in mas:
	print(i.number,end=' ')
	for j in i.word:
		print(j['change'],'(',j['speech'],'-',j['sentence'],')',end=' ')
	print()
print()
text=''
t=False
for i in mas:
	for j in i.word:
		if (j['change'] in '([{<') and t:
			text+=' '
			t=False
		elif (j['speech']!='sign') and t:
			text+=' '
		else:
			t=True
		text+=j['change']
print(text)