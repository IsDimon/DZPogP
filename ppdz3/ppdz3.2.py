# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
#  Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.


text = """Познавательный интерес к египетским древностям фиксируется ещё со времён античного мира.
Первое описание древнеегипетских памятников, нравов и обычаев было представлено в середине V века до н. э.
Геродотом в его «Истории». Египетский жрец Манефон два века спустя представил на греческом языке систематизированное изложение египетской истории.
После римского завоевания Египта отмечается устойчивый интерес к его искусству и религии;
один из трактатов о египетском письме авторства Гораполлона дошёл до наших дней. 
Во время арабского завоевания некоторые мусульманские географы и историки (Ибн Вахшия)
разрабатывали вопросы коптского языка и египетских древностей. В эпоху ренессансного гуманизма
Египет стал восприниматься как прародина герметизма и всех мировых культур. В XVII веке Афанасий Кирхер
опубликовал первые словари и грамматики коптского языка и предпринял неудачную попытку дешифровки иероглифики,
продолженную учёными XVIII—XIX веков, в том числе Георгом Соэгой и Давидом Окербладом.
Египетский поход Наполеона породил первую волну египтомании; 
научное изучение языка и культуры Египта стимулировалось открытием Розеттского камня.
Деятельность политических деятелей и авантюристов 1810-х годов, наподобие Генри Солта и Джованни Бельцони,
привела к созданию первых коллекций египетского искусства и основанию первых «египетских» музеев.
Из профессиональных учёных ближе всех к дешифровке египетской письменности подошли француз Сильвестр де Саси и англичанин Томас Юнг.
Датой создания «Старой школы» научной египтологии считается 27 сентября 1822 года,
когда Жан Шампольон объявил о фонетической дешифровке иероглифики.
Именно Шампольон представил первые словарь и грамматику египетской иероглифики.
Для него в 1831 году была открыта первая в мире кафедра египтологии в Коллеж де Франс. """
words = []
word = ""
for ch in text.lower():
    if ch.isalpha():
        word += ch
    else:
        if word:
            words.append(word)
        word = ""
else:
    words.append(word)  

word_count = sorted([(words.count(word), word) for word in set(words)], reverse=True)

for i in range(10):
    print(f'{i+1}. {word_count[i][1]: <11} - {word_count[i][0]}')