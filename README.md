# Squeeze
Запускать squeeze.py

Модули
-----
### Модули обработки текста

Номер модуля | Название файла | Описание
---|---|---
1 | parse.py | Разбор текста на слова и знаки, установка связи и подчинений, устанавливается роль каждого слова.
3 | treatment.py | Обработка текста нейронными сетями: сокращение, обобщение. 
4 | literacy.py | Проверка грамотности и логичности. Изменение логических связей между словами. Восстановление форм слов.

### Перспектива

Номер модуля | Название файла | Описание
---|---|---
2 | style.py | Определения стиля текста, настроения, главной темы, тип, уровень цензуры.
5 |  | Дополнение информацией из других источников.
 | excess.py | Замена фразеологизмов, повторений.
 |  | Удаление и обобщение конкретики, уточнений, пояснений. Объединение предложений по смыслу.
 |  | Удаление примечаний, дополнений, отсылок.

### Модули машинного обучения

Номер модуля | Название файла | Описание
---|---|---
1 | format.py | Преобразование текстов в форматированный вид для машинного обучения.
2 | training.py | Обучение нейронной сети на базе текстов.

Формат данных
-----
### Данные для обучения
 | Исходные данные | Обработанные данные
---|---|---
Входные данные | input.txt | input.csv
Выходные данные | output.txt | output.csv

### После обработки parse

mas - список экземпляров класса - текст (список предложений)

mas[i].number - номер предложения

mas[i].count - количество слов без знаков

mas[i].word - список экзампляров класса - предложение (список слов)

mas[i].word[j]['original'] - оригинальное слово / знак

mas[i].word[j]['change'] - на что заменим

mas[i].word[j][‘infinitive’] - инфинитив

mas[i].word[j]['speech'] - часть речи

mas[i].word[j]['sentence'] - член предложения

mas[i].word[j]['case'] - падеж

mas[i].word[j]['number'] - число

mas[i].word[j]['gender'] - род

mas[i].word[j]['language'] - язык оригинала

mas[i].word[j]['numsp'] - номер предложения в тексте

mas[i].word[j]['deep'] - смысловая глубина предложения (уровень уточнения)

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

[Полный список (OpenCorpora)](http://opencorpora.org/dict.php?act=gram)

### Язык

Граммема | Значение
---------|---------
ru | Русский
en | English

[Полный список (639-1 коды)](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)

Не исправлено
-----
1. Определение членов предложения: дополнение, ...
2. Определение частей речи в нужной форме слова
3. Ассоциировать корпус со своей базой данных для смысловой глубины
4. Слишком долгое определение языка
5. Установление соответствий между открывающими и закрывающими знаками
6. Распознание названий, имён, фамилий для заглавных букв
7. Знак тире (–) не объединяется