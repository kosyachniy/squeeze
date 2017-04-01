from parse import parse
from style import style
from excess import excess
from attachment import attachment
from additionally import additionally
from literacy import literacy

list=parse(input())
#type=style(mas)
list=literacy(additionally(attachment(excess(list))))
#<Превращаем массив в текст> mas->text
for i in list:
	print(i.number,end=' ')
	for j in i.word:
		print(j['change'],'(',j['speech'],')',end=' ')
	print()
