# Squeeze
Запускать squeeze.py

Модули
-----
### Действующие

Номер модуля | Название файла | Описание
---|---|---
1 | parse.py | Разбор текста на слова и знаки, установка связи и подчинений, устанавливается роль каждого слова.
3 | excess.py | Замена фразеологизмов, повторений.
4 | attachment.py | Удаление и обобщение конкретики, уточнений, пояснений. Объединение предложений по смыслу.
5 | additionally.py | Удаление примечаний, дополнений, отсылок.

### Перспектива

Номер модуля | Название файла | Описание
---|---|---
2 | style.py | Определения стиля текста, настроения, главной темы, тип, уровень цензуры.
6 | literacy.py | Проверка грамотности и логичности. Изменение логических связей между словами.
7 |  | Дополнение информацией из других источников.

Формат данных
-----
### После обработки parse

mas - список экземпляров класса - текст (список предложений)

mas[i].number - номер предложения

mas[i].count - количество слов без знаков

mas[i].word - список экзампляров класса - предложение (список слов)

mas[i].word[j]['original'] - оригинальное слово / знак

mas[i].word[j]['change'] - на что заменим

mas[i].word[j]['speech'] - часть речи

mas[i].word[j]['sentence'] - член предложения

mas[i].word[j]['case'] - падеж

mas[i].word[j]['number'] - число

mas[i].word[j]['gender'] - род

mas[i].word[j]['numsp'] - номер предложения в тексте

### Части речи

Граммема | Значение | Примеры
---------|----------|--------
noun | имя существительное | хомяк
adjf | имя прилагательное (полное) | хороший
adjs | имя прилагательное (краткое) | хорош
comp | компаратив | лучше, получше, выше
verb | глагол (личная форма) | говорю, говорит, говорил
infn | глагол (инфинитив) | говорить, сказать
prtf | причастие (полное) | прочитавший, прочитанная
prts | причастие (краткое) | прочитана
grnd | деепричастие | прочитав, рассказывая
numr | числительное | три, пятьдесят
advb | наречие | круто
npro | местоимение-существительное | он
pred | предикатив | некогда
prep | предлог | в
conj | союз | и
prcl | частица | бы, же, лишь
intj | междометие | ой
sign | знаки препинания | , . ! ?! … : ;
numb | числа | 0 1 1F

### Члены предложений

Граммема | Значение
---------|---------
subject | Подлежащее
predicate | Сказуемое

### Падежи

Граммема | Значение | Пояснение | Примеры
---------|----------|-----------|--------
nomn | Именительный | Кто? Что? | хомяк ест
gent | Родительный | Кого? Чего? | у нас нет хомяка
datv | Дательный | Кому? Чему? | сказать хомяку спасибо
accs | Винительный | Кого? Что? | хомяк читает книгу
ablt | Творительный | Кем? Чем? | зерно съедено хомяком
loct | Предложный | О ком? О чём? и т.п. | хомяка несут в корзинке
voct | Звательный | Его формы используются при обращении к человеку. | Саш, пойдем в кино.
gen2 | Второй родительный (Частичный) |  | ложка сахару (gent - производство сахара); стакан яду (gent - нет яда)
acc2 | Второй винительный |  | записался в солдаты
loc2 | Второй предложный (Местный) |  | я у него в долгу (loct - напоминать о долге); висит в шкафу (loct - монолог о шкафе); весь в снегу (loct - писать о снеге)

Настройка
-----

pip3 install pymorphy2

pip3 install -U pymorphy2-dicts-ru

#pip install -U pymorphy2-dicts-uk

#>>>morph=pymorphy2.MorphAnalyzer(lang='uk')
