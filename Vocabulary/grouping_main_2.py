import time

from Tools.scripts.texi2html import MAGIC
from tinydb import TinyDB, Query, where

tb = TinyDB("db.json")
query = Query()
c = 0


def add_word(name, transl, s_group, group, pos):
	global c
	doc = {"Name": name, "translation": transl, "weight": 1.0, "transcription": '', "Sub group": s_group,
		   "Group": group, "Part of speech": pos}
	if tb.search((where("Name") == name) & (where("Sub group") == s_group)):
		c += 1
		print(f"{c}", end=' ')
	
	else:
		tb.insert(doc)


print(tb.all())

start_time = time.time()

# VERBS
POS = "verb"
MAIN_GROUP = "Бытовые Глаголы • Verbs of Everyday Life"
SUB_GROUP = "Болеть • Feel sick"

add_word("be ill", "начало", SUB_GROUP, MAIN_GROUP, POS)
add_word("ache", "начало",SUB_GROUP, MAIN_GROUP, POS)
add_word("catch a cold", "начало",SUB_GROUP, MAIN_GROUP, POS)
add_word("cough", "начало",SUB_GROUP, MAIN_GROUP, POS)
add_word("sneeze", "начало",SUB_GROUP, MAIN_GROUP, POS)
add_word("recover", "начало",SUB_GROUP, MAIN_GROUP, POS)
add_word("treat", "начало",SUB_GROUP, MAIN_GROUP, POS)
add_word("cure", "начало",SUB_GROUP, MAIN_GROUP, POS)
add_word("heal", "начало",SUB_GROUP, MAIN_GROUP, POS)
add_word("die", "начало",SUB_GROUP, MAIN_GROUP, POS)
add_word("bury", "начало",SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Глаголы Чувства • Verbs of Feeling"

love; fall in love; like; prefer; respect; praise; admire; adore
SUB_GROUP = "Хорошее Отношение • Good Attitude"

hate; dislike; accuse; envy; disregard
SUB_GROUP = "Плохое Отношение • Bad Attitude"

suffer; bear; stand; give up; complain; cry; laugh; smile; enjoy; comfort; calm down; endure; surrender
SUB_GROUP = "Горе / Радость • Grief / Joy"

be proud; be shy; brag; be modest
SUB_GROUP = "Гордость / Скромность • Pride / Modesty"

hope ; believe; rely ; be sure; doubt; hesitate ; suspect
SUB_GROUP = "Уверенность / Сомнение • Confidence / Doubt"

care; try to do one's best; be lazy; neglect; be tired; get tired;
SUB_GROUP = "Старание / Лень • Diligence / Laziness"

excite; move; frighten; fear; scare; surprise; astonish; amaze; hurt; offend; be angry
SUB_GROUP = "Оттенки Эмоций • Subtle Emotions"

MAIN_GROUP = "Глаголы Восприятия и Мышления • Verbs of Perception and Thinking"

feel; see; hear; watch; observe; look; distinguish; listen; recognize
SUB_GROUP = "Восприятие Мира • Perception of the World"

learn; study; memorize; learn by heart; understand; teach; train; explain; know;
remember; bear in mind; mean; forget; make a mistake; err; examine; correct
SUB_GROUP = "Обучение • Learning"

read; write; count; add; subtract; multiply; divide; calculate; express; describe; relate; translate
SUB_GROUP = "Учебные операции • Study Processes"

think; change one's mind; take into account; compare; analyse; process data; conclude;'
research; consider; suppose; expect; discover; find out; experiment;
prove; convince; decide; invent; develop; make up one's mind
SUB_GROUP = "Логические операции • Logical operations"

MAIN_GROUP = "Рабочие операции • Work Tasks"

SUB_GROUP = "Работать / Делать • Work / Do"
SUB_GROUP = "Готовить / Проверять • Prepare / Check"
SUB_GROUP = "Соединять / Закреплять • Connect / Fix"
SUB_GROUP = "Закрывать / Открывать • Close / Open"
SUB_GROUP = "Разрушать / Делить на части • Destroy / Divide into parts"
SUB_GROUP = "Операции с Водой • Water-related Actions"

MAIN_GROUP = "Глаголы Общения • Verbs of Communication"

SUB_GROUP = "Говорить • Speak"
SUB_GROUP = "Обращаться • Address"
SUB_GROUP = "Отвечать • Answer"
SUB_GROUP = "Брать • Take"
SUB_GROUP = "Давать • Give"
SUB_GROUP = "Визит / Этикет • Visit / Etiquette"
SUB_GROUP = "Нарушение Этикета / Наказание • Breach of Etiquette / Punishment"

MAIN_GROUP = "Глаголы Борьбы • Verbs of Fighting"

SUB_GROUP = "Нападать • Attack"
SUB_GROUP = "Защищаться • Defend Oneself"
SUB_GROUP = "Военные операции • Field Operations"
SUB_GROUP = "Действия с Оружием • Actions with Weapons"

# NOUNS
POS = "nouns"

MAIN_GROUP = "Мир • World"

SUB_GROUP = "Небо • Sky"
SUB_GROUP = "Земля • Earth"
SUB_GROUP = "Вода • Water"
SUB_GROUP = "Позиция • Position"
SUB_GROUP = "Зона • Zone"

MAIN_GROUP = "Погода • Weather"

SUB_GROUP = "Сезон • Season"
SUB_GROUP = "Метеорология • Meteorology"
SUB_GROUP = "Осадки • Precipitation"
SUB_GROUP = "Стихийные Бедствия • Natural Disasters"

MAIN_GROUP = "Геометрия • Geometry"

SUB_GROUP = "Размер • Size"
SUB_GROUP = "Форма • Shape"
SUB_GROUP = "Фигуры на плоскости • Plane Figures"
SUB_GROUP = "Линии • Lines"
SUB_GROUP = "Структура • Structure"

MAIN_GROUP = "Время • Time"

SUB_GROUP = "Единицы времени • Time Units"
SUB_GROUP = "Месяцы • Months"
SUB_GROUP = "Дни Недели • Days of The Week"
SUB_GROUP = "Временные Этапы • Time Periods"
SUB_GROUP = "Стадии дня • Parts of Day"
SUB_GROUP = "Рабочее время • Working Time"
SUB_GROUP = "Праздник / Свободное Время • Holiday / Free Time"

MAIN_GROUP = "Вещество / Материал • Substance / Material"

SUB_GROUP = "Физическое Состояние • Physical State"
SUB_GROUP = "Металлы • Metals"
SUB_GROUP = "Строительные Материалы • Construction Materials"
SUB_GROUP = "Сырье • Raw Materials"
SUB_GROUP = "Ткани • Textiles"
SUB_GROUP = "Отходы • Waste"

MAIN_GROUP = "Растения • Plants"

SUB_GROUP = "Овощи • Vegetables"
SUB_GROUP = "Фрукты / Ягоды • Fruits / Berries"
SUB_GROUP = "Зерновые • Grains"
SUB_GROUP = "Деревья • Trees"
SUB_GROUP = "Части дерева • Parts of a Tree"
SUB_GROUP = "Цветы • Flowers"

MAIN_GROUP = "Животные • Animals"

SUB_GROUP = "Дикие Животные • Wild Animals"
SUB_GROUP = "Домашние Животные • Domestic Animals"
SUB_GROUP = "Птицы • Birds"
SUB_GROUP = "Рыба • Fish"
SUB_GROUP = "Насекомые • Insects"
SUB_GROUP = "Остальные Классы • Other Groups"

MAIN_GROUP = "Человек • Human"

SUB_GROUP = "Общие Сведения • General Information"
SUB_GROUP = "Анатомия • Anatomy"
SUB_GROUP = "Отношения между Людьми • Human Relationships"

MAIN_GROUP = "Жилье • Dwelling"

SUB_GROUP = "Дом • House"
SUB_GROUP = "Устройство Дома • House Layout"
SUB_GROUP = "Комнаты • Rooms"
SUB_GROUP = "Мебель • Furniture"
SUB_GROUP = "Кровать • Bed"
SUB_GROUP = "Сосуды / Емкости • Vessels / Containers"
SUB_GROUP = "Бытовые приборы • Household Appliances"

MAIN_GROUP = "Одежда • Clothes"

SUB_GROUP = "Верхняя Одежда • Outer Clothing"
SUB_GROUP = "Одежда / Белье • Clothes / Underwear"
SUB_GROUP = "Обувь • Footwear"
SUB_GROUP = "Головные уборы • Headgear"
SUB_GROUP = "Аксессуары • Accessories"

MAIN_GROUP = "Питание • Nourishment"

SUB_GROUP = "Прием Пищи • Eating"
SUB_GROUP = "Блюда • Dishes"
SUB_GROUP = "Приправы • Condiments"
SUB_GROUP = "Напитки • Drinks and Beverages"
SUB_GROUP = "Сладости • Sweets"
SUB_GROUP = "Пищевые Продукты • Foodstuffs"
SUB_GROUP = "Хлеб • Bread"
SUB_GROUP = "Кухонные Принадлежности • Kitchen Utensils"

MAIN_GROUP = "Чувства / Характер • Feeling / Character"

SUB_GROUP = "Позитивные Эмоции • Positive Emotions"
SUB_GROUP = "Негативные Эмоции • Negative Emotions"
SUB_GROUP = "Терпение / Слабость • Patience / Weakness"
SUB_GROUP = "Любовь / Ненависть • Love / Hatred"
SUB_GROUP = "Гордость / Скромность • Pride / Modesty"
SUB_GROUP = "Старание / Лень • Diligence / Laziness"

MAIN_GROUP = "Мышление • Thinking"

SUB_GROUP = "Сознание • Consciousness"
SUB_GROUP = "Познание • Cognition"
SUB_GROUP = "Категории Мышления • Thinking Categories"
SUB_GROUP = "Исследование • Research"
SUB_GROUP = "Анализ • Analysis"
SUB_GROUP = "Результат • Result"
SUB_GROUP = "Сообщение • Report"
SUB_GROUP = "Критика • Criticism"

MAIN_GROUP = "Образование • Education"

SUB_GROUP = "Учебные Заведения • Educational Institutions"
SUB_GROUP = "Учебные Предметы • Subjects"
SUB_GROUP = "Учеба • Studies"
SUB_GROUP = "Экзамен / Оценки • Exams / Grades"
SUB_GROUP = "Лингвистика • Linguistics"

MAIN_GROUP = "Культура • Culture"

SUB_GROUP = "Кино • Cinema"
SUB_GROUP = "Театр • Theatre"
SUB_GROUP = "Музыка • Music"
SUB_GROUP = "Литература • Literature"
SUB_GROUP = "Спорт • Sport"

MAIN_GROUP = "Работа • Work"

SUB_GROUP = "Труд / Занятость • Labour / Employment"
SUB_GROUP = "Сферы • Fields"
SUB_GROUP = "Предприятие • Enterprise"
SUB_GROUP = "Професcия • Profession"
SUB_GROUP = "Инструменты / Оборудование • Tools / Equipment"

MAIN_GROUP = "Связь / Транспорт • Communication / Transport"

SUB_GROUP = "Телефон / Почта • Phone / Post"
SUB_GROUP = "Железная Дорога • Railway"
SUB_GROUP = "Воздушный Транспорт • Air Transport"
SUB_GROUP = "Автомобильный Транспорт • Motor Transport"

MAIN_GROUP = "Город • City"

SUB_GROUP = "Улицы • Streets"
SUB_GROUP = "Транспорт • Transport"
SUB_GROUP = "Культурные Учреждения • Social and Cultural institutions"
SUB_GROUP = "Торговля / Услуги • Trade / Services"

MAIN_GROUP = "Общение • Communication"

SUB_GROUP = "Информация • Information"
SUB_GROUP = "Общение / Высказывание • Communication / Expression"
SUB_GROUP = "Визит • Visit"
SUB_GROUP = "Этикет • Etiquette"

MAIN_GROUP = "Государство • State"

SUB_GROUP = "Государство • State"
SUB_GROUP = "Народ • People"
SUB_GROUP = "Социальный Статус • Social Status"
SUB_GROUP = "Закон / Право • Law"
SUB_GROUP = "Политика • Politics"
SUB_GROUP = "Экономика • Economy"
SUB_GROUP = "Внешняя Политика • Foreign Policy"

MAIN_GROUP = "Медицина • Medicine"

SUB_GROUP = "Здоровье / болезнь • Health / Illness"
SUB_GROUP = "Наружные повреждения • Injuries"
SUB_GROUP = "Инфекции • Infections"
SUB_GROUP = "Остальные Заболевания • Other Diseases"
SUB_GROUP = "Симптомы • Symptoms"
SUB_GROUP = "Лечение • Treatment"
SUB_GROUP = "Больница • Hospital"


# ADJECTIVES
POS = "adjectives"

MAIN_GROUP = "Органы чувств • Organs of senses"

SUB_GROUP = "Глаза • Eye"
SUB_GROUP = "Кожа • Skin"
SUB_GROUP = "Язык • Tongue"
SUB_GROUP = "Ухо • Ear"
SUB_GROUP = "Нос • Nose"

MAIN_GROUP = "Время • Time"

SUB_GROUP = "Основные Свойства • Main Properties"
SUB_GROUP = "Стадии • Stages"
SUB_GROUP = "Продолжительность / Частота • Duration / Frequency"

MAIN_GROUP = "Способности человека • Human abilities"

SUB_GROUP = "Способность • Ability"
SUB_GROUP = "Отсутствие Способности • Lack of Ability"
SUB_GROUP = "Старание / Внимание • Diligence / Attention"
SUB_GROUP = "Навык / Опыт • Skill / Experience"

MAIN_GROUP = "Эмоция • Emotions"

SUB_GROUP = "Характер • Character"
SUB_GROUP = "Настроение • Mood"
SUB_GROUP = "Эмоциональная Оценка • Emotional Evaluation"
SUB_GROUP = "Оттенки Эмоции • Shades of Emotion"

MAIN_GROUP = "Мораль / Поведение • Moral / Behaviour"

SUB_GROUP = "Основные Свойства • Main Properties"
SUB_GROUP = "Отношение к Окружающим • Attitude towards Others"
SUB_GROUP = "Качества в Общении • Communication Qualities"
SUB_GROUP = "Качества в Поведении • Qualities in Behavior"

MAIN_GROUP = "Абстрактные прилагательные • Abstract Adjectives"

SUB_GROUP = "Классификация • Classification"
SUB_GROUP = "Качество • Quality"
SUB_GROUP = "Количество • Quantity"
SUB_GROUP = "Категория • Category"
SUB_GROUP = "Соответствие • Accordance"
SUB_GROUP = "Преимущество • Advantage"

MAIN_GROUP = "Состояние / Статус • Condition / Status"

SUB_GROUP = "Физическое Состояние • Physical Condition"
SUB_GROUP = "Финансовое Положение • Financial Status"
SUB_GROUP = "Семейное Положение • Family Status"
SUB_GROUP = "Состояние • Condition"


# ADVERBS
POS = "adverbs"

MAIN_GROUP = "Наречия Без группы • Ungrouped Adverbs"

SUB_GROUP = "Вопросительные Наречия • Interrogative Adverbs"
SUB_GROUP = "Наречия Образа действий • Adverbs of Manner"
SUB_GROUP = "Наречия относящиеся к Предложениям • Sentence Adverbs"
SUB_GROUP = "Наречия соединения Предложений • Conjunctive Adverbs"

MAIN_GROUP = "Наречия Места • Adverbs of Place"

SUB_GROUP = "Наречия со значением Места • Adverbs of meaning Place"
SUB_GROUP = "Собственно Наречия Места • Adverbs of Place itself"
SUB_GROUP = "Наречия Направления • Adverbs of Direction"

MAIN_GROUP = "Наречия Времени • Adverbs of Time "

SUB_GROUP = "Последовательность • Sequence"
SUB_GROUP = "Частота • Frequency"
SUB_GROUP = "Вчера / Сегодня / Завтра • Yesterday / Today / Tomorrow"
SUB_GROUP = "Все Еще / Уже • Still / Already"

MAIN_GROUP = "Наречия Меры, Степени и Количества • Adverbs of Degree, Measure and Quantity"

SUB_GROUP = "Большая Степень • High Degree"
SUB_GROUP = "Средняя Степень • Medium Degree"
SUB_GROUP = "Небольшая Степень • Low Degree"





# PRONOUNS
POS = "pronouns"
MAIN_GROUP = "Местоимения  • Pronouns"

SUB_GROUP = "Личные Местоимения • Personal Pronouns"
SUB_GROUP = "Указательные Местоимения • Demonstrative Pronouns"
SUB_GROUP = "Вопросительные Местоимения • Interrogative Pronouns"
SUB_GROUP = "Неопределенные Местоимения • Indefinite Pronouns"
SUB_GROUP = "Определенные Местоимения • Definite Pronouns"
SUB_GROUP = "Отрицательные Местоимения • Negative Pronouns"



# PREPOSITIONS
POS = "prepositions"
MAIN_GROUP = "Предлоги  • Prepositions"

SUB_GROUP = "Предлоги Места • Prepositions of place"
SUB_GROUP = "Предлоги Направления • Prepositions of Direction"
SUB_GROUP = "Предлоги Времени • Prepositions of Time"
SUB_GROUP = "Смешанная Группа • Mixed Group"


# NUMERALS
POS = "numerals"
MAIN_GROUP = "Числительные • Numerals"

SUB_GROUP = "Количественные Числительные • Cardinal Numerals"
SUB_GROUP = "Порядковые Числительные • Ordinal Numerals"
SUB_GROUP = "Дроби • Fractions"



end_time = time.time()
elapsed_time = end_time - start_time
print(f"\nTime spent: {elapsed_time:.6f} seconds")
