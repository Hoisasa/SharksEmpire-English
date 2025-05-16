import time

from tinydb import TinyDB, Query, where

tb = TinyDB("db.json")
query = Query()
c = 0


def add_word(name, transl, weight, transcr, s_group, group, pos):
	global c
	doc = {"Name": name, "translation": transl, "weight": weight, "transcription": transcr, "Sub group": s_group,
		   "Group": group, "Part of speech": pos}
	if tb.search((where("Name") == name) & (where("Sub group") == s_group)):
		c += 1
		print(f"{c}", end=' ')
	
	else:
		tb.insert(doc)


print(tb.all())

start_time = time.time()

# VERBS

add_word("be ill", "начало", 1.0, '', "Болеть • Be ill", "Бытовые Глаголы • Verbs of Everyday Life", "verb")
add_word("be sick", "начало", 1.0, '', "Болеть • Be ill", "Бытовые Глаголы • Verbs of Everyday Life", "verb")
add_word("ache", "начало", 1.0, '', "Болеть • Be ill", "Бытовые Глаголы • Verbs of Everyday Life", "verb")
add_word("catch a cold", "начало", 1.0, '', "Болеть • Be ill", "Бытовые Глаголы • Verbs of Everyday Life", "verb")
add_word("cough", "начало", 1.0, '', "Болеть • Be ill", "Бытовые Глаголы • Verbs of Everyday Life", "verb")
add_word("sneeze", "начало", 1.0, '', "Болеть • Be ill", "Бытовые Глаголы • Verbs of Everyday Life", "verb")
add_word("recover", "начало", 1.0, '', "Болеть • Be ill", "Бытовые Глаголы • Verbs of Everyday Life", "verb")
add_word("treat", "начало", 1.0, '', "Болеть • Be ill", "Бытовые Глаголы • Verbs of Everyday Life", "verb")
add_word("cure", "начало", 1.0, '', "Болеть • Be ill", "Бытовые Глаголы • Verbs of Everyday Life", "verb")
add_word("heal", "начало", 1.0, '', "Болеть • Be ill", "Бытовые Глаголы • Verbs of Everyday Life", "verb")
add_word("die", "начало", 1.0, '', "Болеть • Be ill", "Бытовые Глаголы • Verbs of Everyday Life", "verb")
add_word("bury", "начало", 1.0, '', "Болеть • Be ill", "Бытовые Глаголы • Verbs of Everyday Life", "verb")


add_word("bury", "начало", 1.0, '', "Хорошее Отношение • Good Attitude", "Глаголы Чувства • Verbs of Feeling", "verb")
add_word("bury", "начало", 1.0, '', "Плохое Отношение • Bad Attitude", "Глаголы Чувства • Verbs of Feeling", "verb")
add_word("bury", "начало", 1.0, '', "Горе / Радость • Grief / Joy", "Глаголы Чувства • Verbs of Feeling", "verb")
add_word("bury", "начало", 1.0, '', "Гордость / Скромность • Pride / Modesty", "Глаголы Чувства • Verbs of Feeling", "verb")
add_word("bury", "начало", 1.0, '', "Уверенность / Сомнение • Confidence / Doubt", "Глаголы Чувства • Verbs of Feeling", "verb")
add_word("bury", "начало", 1.0, '', "Старание / Лень • Diligence / Laziness", "Глаголы Чувства • Verbs of Feeling", "verb")
add_word("bury", "начало", 1.0, '', "Оттенки Эмоций • Shades of Emotions", "Глаголы Чувства • Verbs of Feeling", "verb")
add_word("bury", "начало", 1.0, '', "Восприятие Мира • Perception of the World", "Глаголы Восприятия и Мышления • Verbs of Perception and Thinking", "verb")
add_word("bury", "начало", 1.0, '', "Обучение • Instruction", "Глаголы Восприятия и Мышления • Verbs of Perception and Thinking", "verb")
add_word("bury", "начало", 1.0, '', "Учебные операции • Learning Operation", "Глаголы Восприятия и Мышления • Verbs of Perception and Thinking", "verb")
add_word("bury", "начало", 1.0, '', "Логические операции • Logical operations", "Глаголы Восприятия и Мышления • Verbs of Perception and Thinking", "verb")
add_word("bury", "начало", 1.0, '', "Работать / Делать • Work / Do", "Рабочие операции • Working operations", "verb")
add_word("bury", "начало", 1.0, '', "Готовить / Проверять • Prepare / Control", "Рабочие операции • Working operations", "verb")
add_word("bury", "начало", 1.0, '', "Ручные операции • Manual operations", "Рабочие операции • Working operations", "verb")
add_word("bury", "начало", 1.0, '', "Соединять / Закреплять • Connect / Fix", "Рабочие операции • Working operations", "verb")
add_word("bury", "начало", 1.0, '', "Закрывать / Открывать • Close / Open", "Рабочие операции • Working operations", "verb")
add_word("bury", "начало", 1.0, '', "Разрушать / Делить на части • Destroy / Divide into parts", "Рабочие операции • Working operations", "verb")
add_word("bury", "начало", 1.0, '', "Операции с Водой • Operations with Water", "Рабочие операции • Working operations", "verb")
add_word("bury", "начало", 1.0, '', "Говорить • Speak", "Глаголы Общения • Verbs of Communication", "verb")
add_word("bury", "начало", 1.0, '', "Обращаться • Adress", "Глаголы Общения • Verbs of Communication", "verb")
add_word("bury", "начало", 1.0, '', "Отвечать • Answer", "Глаголы Общения • Verbs of Communication", "verb")
add_word("bury", "начало", 1.0, '', "Брать • Take", "Глаголы Общения • Verbs of Communication", "verb")
add_word("bury", "начало", 1.0, '', "Давать • Give", "Глаголы Общения • Verbs of Communication", "verb")
add_word("bury", "начало", 1.0, '', "Визит / Этикет • Visit / Etiquette", "Глаголы Общения • Verbs of Communication", "verb")
add_word("bury", "начало", 1.0, '', "Нарушение Этикета / Наказание • Breach of Etiquette / Punishment", "Глаголы Общения • Verbs of Communication", "verb")
add_word("bury", "начало", 1.0, '', "Нападать • Attack", "Глаголы Борьбы • Verbs of Fighting", "verb")
add_word("bury", "начало", 1.0, '', "Защищиаться • Defend Oneself", "Глаголы Борьбы • Verbs of Fighting", "verb")
add_word("bury", "начало", 1.0, '', "Военные операции • Field Operations", "Глаголы Борьбы • Verbs of Fighting", "verb")
add_word("bury", "начало", 1.0, '', "Действия с Оружием • Actions with Weapons", "Глаголы Борьбы • Verbs of Fighting", "verb")

# NOUNS

add_word("bell", "начало", 1.0, '', "Начало • Begining", "Мир • World", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Погода • Weather", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Геометрия • Geometry", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Время • Time", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Вещество / Материал • Substance / Material", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Растения • Plants", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Животные • Animals", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Человек • Human", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Жилье • Dwelling", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Одежда • Clothes", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Питание • Nourishment", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Чувство / Характер • Feeling / Character", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Мышление • Thinking", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Образование • Education", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Культура • Culture", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Работа • Work", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Связь / Траснпорт • Communication / Transport", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Город • City", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Общение • Communication", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Государство • State", "noun")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Медицина • Medicine", "noun")

# ADJECTIVES

add_word("bell", "начало", 1.0, '', "Начало • Begining", "Органы чувтсв • Organs of senses", "adjective")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Время • Time", "adjective")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Способности человека • Faculties, abilities", "adjective")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Эмоция • Emotions", "adjective")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Мораль / Поведение • Moral / Behaviour", "adjective")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Абстрактные прилагательные • Abstract Adjectives", "adjective")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Состояние / Статус • Condition / Status", "adjective")

# ADVERBS

add_word("bell", "начало", 1.0, '', "Начало • Begining", "Вопросительные Наречия • Interrogative Adverbs", "adverb")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Наречия Места • Adverbs of Place", "adverb")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Наречия Времени • Adverbs of Time ", "adverb")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Наречия Меры, Степени и Количетсва • Adverbs of Degree, Measure and Quantity", "adverb")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Наречия Образа действий • Adverbs of Manner", "adverb")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Наречия относящиеся к Предложениям • Adverbs Relating to the Whole Sentence", "adverb")
add_word("bell", "начало", 1.0, '', "Начало • Begining", "Наречия соединения Предложений • Conjunctive Adverbs", "adverb")

# PRONOUNS

add_word("bell", "начало", 1.0, '', "Начало • Begining", "Местоимения  • Pronouns", "pronouns")

# PREPOSITIONS

add_word("bell", "начало", 1.0, '', "Начало • Begining", "Предлоги  • Prepositions", "prepositions")

# NUMERALS

add_word("bell", "начало", 1.0, '', "Начало • Begining", "Числительные • Numerals", "pronouns")


end_time = time.time()
elapsed_time = end_time - start_time
print(f"\nTime spent: {elapsed_time:.6f} seconds")
