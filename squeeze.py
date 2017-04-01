from parse import parse
from style import style
from excess import excess
from attachment import attachment
from additionally import additionally
from literacy import literacy

mas=parse(input())
#type=style(mas)
mas=literacy(additionally(attachment(excess(mas))))
#<Превращаем массив в текст> mas->text
for i in mas:
	print(i.number,end=' ')
	for j in i.word:
		print(j['change'],'(',j['speech'],')',end=' ')
	print()
