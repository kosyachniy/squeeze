# Squeeze
Запускать squeeze.py

Модули
-----
### Действующие

1 | parse.py | Разбор текста на слова и знаки, установка связи и подчинений, устанавливается роль каждого слова;

2 | style.py | Определения стиля текста, настроения, главной темы, тип, уровень цензуры;

3 | excess.py | Замена фразеологизмов, повторений;

4 | attachment.py | Удаление и обобщение конкретики, уточнений, пояснений. Объединение предложений по смыслу;

5 | additionally.py | Удаление примечаний, дополнений, отсылок;

### Перспектива

6 | literacy.py | Проверка грамотности и логичности. Изменение логических связей между словами;

7 |  | Дополнение информацией из других источников.

Формат данных
-----
### После обработки parse

list - массив экземпляров класса - текст (массив предложений)

list[i].number - номер предложения

list[i].word - массив экзампляров класса - предложение (массив слов)

list[i].word[j]['original'] - оригинальное слово / знак

list[i].word[j]['change'] - на что заменим

list[i].word[j]['speech'] - часть речи

list[i].word[j]['sentence'] - член предложения

list[i].word[j]['number'] - номер предложения в тексте

### Части речи

Граммема | Значение | Примеры
---------|----------|--------
NOUN | имя существительное | хомяк
ADJF | имя прилагательное (полное) | хороший
ADJS | имя прилагательное (краткое) | хорош
COMP | компаратив | лучше, получше, выше
VERB | глагол (личная форма) | говорю, говорит, говорил
INFN | глагол (инфинитив) | говорить, сказать
PRTF | причастие (полное) | прочитавший, прочитанная
PRTS | причастие (краткое) | прочитана
GRND | деепричастие | прочитав, рассказывая
NUMR | числительное | три, пятьдесят
ADVB | наречие | круто
NPRO | местоимение-существительное | он
PRED | предикатив | некогда
PREP | предлог | в
CONJ | союз | и
PRCL | частица | бы, же, лишь
INTJ | междометие | ой
signs | знаки препинания | , . ! ?! … : ;

### Члены предложений

Настройка
-----

pip3 install pymorphy2

pip3 install -U pymorphy2-dicts-ru

#pip install -U pymorphy2-dicts-uk

#>>>morph=pymorphy2.MorphAnalyzer(lang='uk')
