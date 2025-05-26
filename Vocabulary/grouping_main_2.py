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

add_word("be ill", "болеть (болезнь)", SUB_GROUP, MAIN_GROUP, POS)
add_word("ache", "болеть (боль)",SUB_GROUP, MAIN_GROUP, POS)
add_word("catch a cold", "простудиться",SUB_GROUP, MAIN_GROUP, POS)
add_word("cough", "кашлять",SUB_GROUP, MAIN_GROUP, POS)
add_word("sneeze", "чихать",SUB_GROUP, MAIN_GROUP, POS)
add_word("recover", "выздоравливать",SUB_GROUP, MAIN_GROUP, POS)
add_word("treat", "лечить",SUB_GROUP, MAIN_GROUP, POS)
add_word("cure", "излечивать",SUB_GROUP, MAIN_GROUP, POS)
add_word("heal", "заживлять",SUB_GROUP, MAIN_GROUP, POS)
add_word("die", "умирать",SUB_GROUP, MAIN_GROUP, POS)
add_word("bury", "хоронить",SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Глаголы Чувства • Verbs of Feeling"

love; fall in love; like; prefer; respect; praise; admire; adore
SUB_GROUP = "Хорошее Отношение • Good Attitude"

add_word("love", "любить", SUB_GROUP, MAIN_GROUP, POS)
add_word("fall in love", "влюбляться", SUB_GROUP, MAIN_GROUP, POS)
add_word("like", "нравиться", SUB_GROUP, MAIN_GROUP, POS)
add_word("prefer", "предпочитать", SUB_GROUP, MAIN_GROUP, POS)
add_word("respect", "уважать", SUB_GROUP, MAIN_GROUP, POS)
add_word("praise", "хвалить", SUB_GROUP, MAIN_GROUP, POS)
add_word("admire", "восхищаться", SUB_GROUP, MAIN_GROUP, POS)
add_word("adore", "обожать", SUB_GROUP, MAIN_GROUP, POS)

hate; dislike; accuse; envy; disregard
SUB_GROUP = "Плохое Отношение • Bad Attitude"

add_word("hate", "ненавидеть", SUB_GROUP, MAIN_GROUP, POS)
add_word("dislike", "не нравиться", SUB_GROUP, MAIN_GROUP, POS)
add_word("accuse", "обвинять", SUB_GROUP, MAIN_GROUP, POS)
add_word("envy", "завидовать", SUB_GROUP, MAIN_GROUP, POS)
add_word("disregard", "игнорировать", SUB_GROUP, MAIN_GROUP, POS)


suffer; bear; stand; give up; complain; cry; laugh; smile; enjoy; comfort; calm down; endure; surrender
SUB_GROUP = "Горе / Радость • Grief / Joy"
add_word("suffer", "страдать", SUB_GROUP, MAIN_GROUP, POS)
add_word("bear", "выносить", SUB_GROUP, MAIN_GROUP, POS)
add_word("stand", "терпеть", SUB_GROUP, MAIN_GROUP, POS)
add_word("give up", "сдаваться", SUB_GROUP, MAIN_GROUP, POS)
add_word("complain", "жаловаться", SUB_GROUP, MAIN_GROUP, POS)
add_word("cry", "плакать", SUB_GROUP, MAIN_GROUP, POS)
add_word("laugh", "смеяться", SUB_GROUP, MAIN_GROUP, POS)
add_word("smile", "улыбаться", SUB_GROUP, MAIN_GROUP, POS)
add_word("enjoy", "наслаждаться", SUB_GROUP, MAIN_GROUP, POS)
add_word("comfort", "утешать", SUB_GROUP, MAIN_GROUP, POS)
add_word("calm down", "успокаиваться", SUB_GROUP, MAIN_GROUP, POS)
add_word("endure", "выдерживать", SUB_GROUP, MAIN_GROUP, POS)
add_word("surrender", "капитулировать", SUB_GROUP, MAIN_GROUP, POS)

be proud; be shy; brag; be modest
SUB_GROUP = "Гордость / Скромность • Pride / Modesty"
add_word("be proud", "гордиться", SUB_GROUP, MAIN_GROUP, POS)
add_word("be shy", "быть застенчивым", SUB_GROUP, MAIN_GROUP, POS)
add_word("brag", "хвастаться", SUB_GROUP, MAIN_GROUP, POS)
add_word("be modest", "быть скромным", SUB_GROUP, MAIN_GROUP, POS)


hope ; believe; rely ; be sure; doubt; hesitate ; suspect
SUB_GROUP = "Уверенность / Сомнение • Confidence / Doubt"
add_word("hope", "надеяться", SUB_GROUP, MAIN_GROUP, POS)
add_word("believe", "верить", SUB_GROUP, MAIN_GROUP, POS)
add_word("rely", "полагаться", SUB_GROUP, MAIN_GROUP, POS)
add_word("be sure", "быть уверенным", SUB_GROUP, MAIN_GROUP, POS)
add_word("doubt", "сомневаться", SUB_GROUP, MAIN_GROUP, POS)
add_word("hesitate", "колебаться", SUB_GROUP, MAIN_GROUP, POS)
add_word("suspect", "подозревать", SUB_GROUP, MAIN_GROUP, POS)



care; try to do one's best; be lazy; neglect; be tired; get tired;
SUB_GROUP = "Старание / Лень • Diligence / Laziness"
add_word("care", "заботиться", SUB_GROUP, MAIN_GROUP, POS)
add_word("try to do one's best", "стараться изо всех сил", SUB_GROUP, MAIN_GROUP, POS)
add_word("be lazy", "лениться", SUB_GROUP, MAIN_GROUP, POS)
add_word("neglect", "пренебрегать", SUB_GROUP, MAIN_GROUP, POS)
add_word("be tired", "быть уставшим", SUB_GROUP, MAIN_GROUP, POS)
add_word("get tired", "уставать", SUB_GROUP, MAIN_GROUP, POS)



excite; move; frighten; fear; scare; surprise; astonish; amaze; hurt; offend; be angry
SUB_GROUP = "Оттенки Эмоций • Subtle Emotions"
add_word("excite", "возбуждать", SUB_GROUP, MAIN_GROUP, POS)
add_word("move", "трогать", SUB_GROUP, MAIN_GROUP, POS)
add_word("frighten", "пугать", SUB_GROUP, MAIN_GROUP, POS)
add_word("fear", "бояться", SUB_GROUP, MAIN_GROUP, POS)
add_word("scare", "испугать", SUB_GROUP, MAIN_GROUP, POS)
add_word("surprise", "удивлять", SUB_GROUP, MAIN_GROUP, POS)
add_word("astonish", "поражать", SUB_GROUP, MAIN_GROUP, POS)
add_word("amaze", "изумлять", SUB_GROUP, MAIN_GROUP, POS)
add_word("hurt", "обижать", SUB_GROUP, MAIN_GROUP, POS)
add_word("offend", "оскорблять", SUB_GROUP, MAIN_GROUP, POS)
add_word("be angry", "сердиться", SUB_GROUP, MAIN_GROUP, POS)


MAIN_GROUP = "Глаголы Восприятия и Мышления • Verbs of Perception and Thinking"

feel; see; hear; watch; observe; look; distinguish; listen; recognize
SUB_GROUP = "Восприятие Мира • Perception of the World"
add_word("feel", "чувствовать", SUB_GROUP, MAIN_GROUP, POS)
add_word("see", "видеть", SUB_GROUP, MAIN_GROUP, POS)
add_word("hear", "слышать", SUB_GROUP, MAIN_GROUP, POS)
add_word("watch", "смотреть", SUB_GROUP, MAIN_GROUP, POS)
add_word("observe", "наблюдать", SUB_GROUP, MAIN_GROUP, POS)
add_word("look", "глядеть", SUB_GROUP, MAIN_GROUP, POS)
add_word("distinguish", "различать", SUB_GROUP, MAIN_GROUP, POS)
add_word("listen", "слушать", SUB_GROUP, MAIN_GROUP, POS)
add_word("recognize", "узнавать", SUB_GROUP, MAIN_GROUP, POS)

learn; study; memorize; learn by heart; understand; teach; train; explain; know;
remember; bear in mind; mean; forget; make a mistake; err; examine; correct
SUB_GROUP = "Обучение • Learning"
add_word("learn", "учить(ся)", SUB_GROUP, MAIN_GROUP, POS)
add_word("study", "изучать", SUB_GROUP, MAIN_GROUP, POS)
add_word("memorize", "запоминать", SUB_GROUP, MAIN_GROUP, POS)
add_word("learn by heart", "зазубривать", SUB_GROUP, MAIN_GROUP, POS)
add_word("understand", "понимать", SUB_GROUP, MAIN_GROUP, POS)
add_word("teach", "обучать", SUB_GROUP, MAIN_GROUP, POS)
add_word("train", "тренировать", SUB_GROUP, MAIN_GROUP, POS)
add_word("explain", "объяснять", SUB_GROUP, MAIN_GROUP, POS)
add_word("know", "знать", SUB_GROUP, MAIN_GROUP, POS)
add_word("remember", "помнить", SUB_GROUP, MAIN_GROUP, POS)
add_word("bear in mind", "иметь в виду", SUB_GROUP, MAIN_GROUP, POS)
add_word("mean", "значить", SUB_GROUP, MAIN_GROUP, POS)
add_word("forget", "забывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("make a mistake", "ошибаться", SUB_GROUP, MAIN_GROUP, POS)
add_word("err", "допускать ошибку", SUB_GROUP, MAIN_GROUP, POS)
add_word("examine", "исследовать", SUB_GROUP, MAIN_GROUP, POS)
add_word("correct", "исправлять", SUB_GROUP, MAIN_GROUP, POS)


read; write; count; add; subtract; multiply; divide; calculate; express; describe; relate; translate
SUB_GROUP = "Учебные операции • Study Processes"
add_word("read", "читать", SUB_GROUP, MAIN_GROUP, POS)
add_word("write", "писать", SUB_GROUP, MAIN_GROUP, POS)
add_word("count", "считать", SUB_GROUP, MAIN_GROUP, POS)
add_word("add", "складывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("subtract", "вычитать", SUB_GROUP, MAIN_GROUP, POS)
add_word("multiply", "умножать", SUB_GROUP, MAIN_GROUP, POS)
add_word("divide", "делить", SUB_GROUP, MAIN_GROUP, POS)
add_word("calculate", "вычислять", SUB_GROUP, MAIN_GROUP, POS)
add_word("express", "выражать", SUB_GROUP, MAIN_GROUP, POS)
add_word("describe", "описывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("relate", "соотносить", SUB_GROUP, MAIN_GROUP, POS)
add_word("translate", "переводить", SUB_GROUP, MAIN_GROUP, POS)


think; change one's mind; take into account; compare; analyse; process data; conclude;'
research; consider; suppose; expect; discover; find out; experiment;
prove; convince; decide; invent; develop; make up one's mind
SUB_GROUP = "Логические операции • Logical operations"
add_word("think", "думать", SUB_GROUP, MAIN_GROUP, POS)
add_word("change one's mind", "передумать", SUB_GROUP, MAIN_GROUP, POS)
add_word("take into account", "принимать во внимание", SUB_GROUP, MAIN_GROUP, POS)
add_word("compare", "сравнивать", SUB_GROUP, MAIN_GROUP, POS)
add_word("analyse", "анализировать", SUB_GROUP, MAIN_GROUP, POS)
add_word("process data", "обрабатывать данные", SUB_GROUP, MAIN_GROUP, POS)
add_word("conclude", "делать вывод", SUB_GROUP, MAIN_GROUP, POS)
add_word("research", "исследовать", SUB_GROUP, MAIN_GROUP, POS)
add_word("consider", "рассматривать", SUB_GROUP, MAIN_GROUP, POS)
add_word("suppose", "предполагать", SUB_GROUP, MAIN_GROUP, POS)
add_word("expect", "ожидать", SUB_GROUP, MAIN_GROUP, POS)
add_word("discover", "обнаруживать", SUB_GROUP, MAIN_GROUP, POS)
add_word("find out", "узнавать", SUB_GROUP, MAIN_GROUP, POS)
add_word("experiment", "экспериментировать", SUB_GROUP, MAIN_GROUP, POS)
add_word("prove", "доказывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("convince", "убеждать", SUB_GROUP, MAIN_GROUP, POS)
add_word("decide", "решать", SUB_GROUP, MAIN_GROUP, POS)
add_word("invent", "изобретать", SUB_GROUP, MAIN_GROUP, POS)
add_word("develop", "развивать", SUB_GROUP, MAIN_GROUP, POS)
add_word("make up one's mind", "принимать решение", SUB_GROUP, MAIN_GROUP, POS)


MAIN_GROUP = "Рабочие операции • Work Tasks"


work; do; carry out; perform; fulfill; conduct; make; manufacture; produce
SUB_GROUP = "Работать / Делать • Work / Do"
add_word("work", "работать", SUB_GROUP, MAIN_GROUP, POS)
add_word("do", "делать", SUB_GROUP, MAIN_GROUP, POS)
add_word("carry out", "выполнять", SUB_GROUP, MAIN_GROUP, POS)
add_word("perform", "исполнять", SUB_GROUP, MAIN_GROUP, POS)
add_word("fulfill", "исполнять", SUB_GROUP, MAIN_GROUP, POS)
add_word("conduct", "проводить", SUB_GROUP, MAIN_GROUP, POS)
add_word("make", "делать", SUB_GROUP, MAIN_GROUP, POS)
add_word("manufacture", "производить", SUB_GROUP, MAIN_GROUP, POS)
add_word("produce", "производить", SUB_GROUP, MAIN_GROUP, POS)


prepare; repair; fit; adjust; control; test; verify; replace; substitute;
assemble; disassemble; use; apply; act; function
SUB_GROUP = "Готовить / Проверять • Prepare / Check"
add_word("prepare", "готовить", SUB_GROUP, MAIN_GROUP, POS)
add_word("repair", "ремонтировать", SUB_GROUP, MAIN_GROUP, POS)
add_word("fit", "подгонять", SUB_GROUP, MAIN_GROUP, POS)
add_word("adjust", "регулировать", SUB_GROUP, MAIN_GROUP, POS)
add_word("control", "контролировать", SUB_GROUP, MAIN_GROUP, POS)
add_word("test", "тестировать", SUB_GROUP, MAIN_GROUP, POS)
add_word("verify", "проверять", SUB_GROUP, MAIN_GROUP, POS)
add_word("replace", "заменять", SUB_GROUP, MAIN_GROUP, POS)
add_word("substitute", "замещать", SUB_GROUP, MAIN_GROUP, POS)
add_word("assemble", "собирать", SUB_GROUP, MAIN_GROUP, POS)
add_word("disassemble", "разбирать", SUB_GROUP, MAIN_GROUP, POS)
add_word("use", "использовать", SUB_GROUP, MAIN_GROUP, POS)
add_word("apply", "применять", SUB_GROUP, MAIN_GROUP, POS)
add_word("act", "действовать", SUB_GROUP, MAIN_GROUP, POS)
add_word("function", "функционировать", SUB_GROUP, MAIN_GROUP, POS)


take; catch; keep; hold; touch; throw; drop; let fall; scatter; pick up; pull; push
SUB_GROUP = "Ручные операции • Manual Operations"
add_word("take", "брать", SUB_GROUP, MAIN_GROUP, POS)
add_word("catch", "ловить", SUB_GROUP, MAIN_GROUP, POS)
add_word("keep", "держать", SUB_GROUP, MAIN_GROUP, POS)
add_word("hold", "удерживать", SUB_GROUP, MAIN_GROUP, POS)
add_word("touch", "касаться", SUB_GROUP, MAIN_GROUP, POS)
add_word("throw", "бросать", SUB_GROUP, MAIN_GROUP, POS)
add_word("drop", "ронять", SUB_GROUP, MAIN_GROUP, POS)
add_word("let fall", "давать упасть", SUB_GROUP, MAIN_GROUP, POS)
add_word("scatter", "рассыпать", SUB_GROUP, MAIN_GROUP, POS)
add_word("pick up", "поднимать", SUB_GROUP, MAIN_GROUP, POS)
add_word("pull", "тянуть", SUB_GROUP, MAIN_GROUP, POS)
add_word("push", "толкать", SUB_GROUP, MAIN_GROUP, POS)

attach; connect; fix; tie; bind; screw; stick; weld; nail; undo; unfasten
SUB_GROUP = "Соединять / Закреплять • Connect / Fix"
add_word("attach", "прикреплять", SUB_GROUP, MAIN_GROUP, POS)
add_word("connect", "соединять", SUB_GROUP, MAIN_GROUP, POS)
add_word("fix", "закреплять", SUB_GROUP, MAIN_GROUP, POS)
add_word("tie", "завязывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("bind", "связывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("screw", "закручивать", SUB_GROUP, MAIN_GROUP, POS)
add_word("stick", "приклеивать", SUB_GROUP, MAIN_GROUP, POS)
add_word("weld", "сваривать", SUB_GROUP, MAIN_GROUP, POS)
add_word("nail", "прибивать гвоздями", SUB_GROUP, MAIN_GROUP, POS)
add_word("undo", "развязывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("unfasten", "отстёгивать", SUB_GROUP, MAIN_GROUP, POS)

shut; close; cover; lock; wrap; open; hide; put away; search; find;
SUB_GROUP = "Закрывать / Открывать • Close / Open"
add_word("shut", "закрывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("close", "закрывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("cover", "накрывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("lock", "запирать", SUB_GROUP, MAIN_GROUP, POS)
add_word("wrap", "заворачивать", SUB_GROUP, MAIN_GROUP, POS)
add_word("open", "открывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("hide", "прятать", SUB_GROUP, MAIN_GROUP, POS)
add_word("put away", "убирать", SUB_GROUP, MAIN_GROUP, POS)
add_word("search", "искать", SUB_GROUP, MAIN_GROUP, POS)
add_word("find", "находить", SUB_GROUP, MAIN_GROUP, POS)

break; destroy; demolish; cut; saw; split; grind; tear; scrape; scratch; rub
SUB_GROUP = "Разрушать / Делить на части • Destroy / Divide into parts"
add_word("break", "ломать", SUB_GROUP, MAIN_GROUP, POS)
add_word("destroy", "разрушать", SUB_GROUP, MAIN_GROUP, POS)
add_word("demolish", "сносить", SUB_GROUP, MAIN_GROUP, POS)
add_word("cut", "резать", SUB_GROUP, MAIN_GROUP, POS)
add_word("saw", "пилить", SUB_GROUP, MAIN_GROUP, POS)
add_word("split", "раскалывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("grind", "точить", SUB_GROUP, MAIN_GROUP, POS)
add_word("tear", "рвать", SUB_GROUP, MAIN_GROUP, POS)
add_word("scrape", "скоблить", SUB_GROUP, MAIN_GROUP, POS)
add_word("scratch", "царапать", SUB_GROUP, MAIN_GROUP, POS)
add_word("rub", "тереть", SUB_GROUP, MAIN_GROUP, POS)

pour; spill; water; moisten; wash; dry; dissolve; dilute; mix; filter
SUB_GROUP = "Операции с Водой • Water-related Actions"
add_word("pour", "лить", SUB_GROUP, MAIN_GROUP, POS)
add_word("spill", "проливать", SUB_GROUP, MAIN_GROUP, POS)
add_word("water", "поливать", SUB_GROUP, MAIN_GROUP, POS)
add_word("moisten", "увлажнять", SUB_GROUP, MAIN_GROUP, POS)
add_word("wash", "мыть", SUB_GROUP, MAIN_GROUP, POS)
add_word("dry", "сушить", SUB_GROUP, MAIN_GROUP, POS)
add_word("dissolve", "растворять", SUB_GROUP, MAIN_GROUP, POS)
add_word("dilute", "разбавлять", SUB_GROUP, MAIN_GROUP, POS)
add_word("mix", "смешивать", SUB_GROUP, MAIN_GROUP, POS)
add_word("filter", "фильтровать", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Глаголы Общения • Verbs of Communication"

speak; talk; say; tell; pronounce; whisper; cry; be silent
SUB_GROUP = "Говорить • Speak"
add_word("speak", "говорить", SUB_GROUP, MAIN_GROUP, POS)
add_word("talk", "разговаривать", SUB_GROUP, MAIN_GROUP, POS)
add_word("say", "сказать", SUB_GROUP, MAIN_GROUP, POS)
add_word("tell", "рассказывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("pronounce", "произносить", SUB_GROUP, MAIN_GROUP, POS)
add_word("whisper", "шептать", SUB_GROUP, MAIN_GROUP, POS)
add_word("cry", "кричать", SUB_GROUP, MAIN_GROUP, POS)
add_word("be silent", "молчать", SUB_GROUP, MAIN_GROUP, POS)

address; have a conversation; inform; state; withhold; announce; ask; request; beg; demand; order
SUB_GROUP = "Обращаться • Address"
add_word("address", "обращаться", SUB_GROUP, MAIN_GROUP, POS)
add_word("have a conversation", "вести разговор", SUB_GROUP, MAIN_GROUP, POS)
add_word("inform", "информировать", SUB_GROUP, MAIN_GROUP, POS)
add_word("state", "заявлять", SUB_GROUP, MAIN_GROUP, POS)
add_word("withhold", "удерживать", SUB_GROUP, MAIN_GROUP, POS)
add_word("announce", "объявлять", SUB_GROUP, MAIN_GROUP, POS)
add_word("ask", "спрашивать", SUB_GROUP, MAIN_GROUP, POS)
add_word("request", "просить", SUB_GROUP, MAIN_GROUP, POS)
add_word("beg", "умолять", SUB_GROUP, MAIN_GROUP, POS)
add_word("demand", "требовать", SUB_GROUP, MAIN_GROUP, POS)
add_word("order", "приказывать", SUB_GROUP, MAIN_GROUP, POS)

answer; reply; explain; show; advise; suggest; propose; warn; order; help; assist; contribute
SUB_GROUP = "Отвечать • Answer"
add_word("answer", "отвечать", SUB_GROUP, MAIN_GROUP, POS)
add_word("reply", "отвечать", SUB_GROUP, MAIN_GROUP, POS)
add_word("explain", "объяснять", SUB_GROUP, MAIN_GROUP, POS)
add_word("show", "показывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("advise", "советовать", SUB_GROUP, MAIN_GROUP, POS)
add_word("suggest", "предлагать", SUB_GROUP, MAIN_GROUP, POS)
add_word("propose", "предлагать", SUB_GROUP, MAIN_GROUP, POS)
add_word("warn", "предупреждать", SUB_GROUP, MAIN_GROUP, POS)
add_word("order", "приказывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("help", "помогать", SUB_GROUP, MAIN_GROUP, POS)
add_word("assist", "ассистировать", SUB_GROUP, MAIN_GROUP, POS)
add_word("contribute", "способствовать", SUB_GROUP, MAIN_GROUP, POS)

accept; take; get; receive; borrow; hire; rent; buy
SUB_GROUP = "Брать • Take"
add_word("accept", "принимать", SUB_GROUP, MAIN_GROUP, POS)
add_word("take", "брать", SUB_GROUP, MAIN_GROUP, POS)
add_word("get", "получать", SUB_GROUP, MAIN_GROUP, POS)
add_word("receive", "получать", SUB_GROUP, MAIN_GROUP, POS)
add_word("borrow", "занимать", SUB_GROUP, MAIN_GROUP, POS)
add_word("hire", "нанимать", SUB_GROUP, MAIN_GROUP, POS)
add_word("rent", "арендовать", SUB_GROUP, MAIN_GROUP, POS)
add_word("buy", "покупать", SUB_GROUP, MAIN_GROUP, POS)

offer; suggest; give; provide; supply; present; sell; lend; bribe
SUB_GROUP = "Давать • Give"
add_word("offer", "предлагать", SUB_GROUP, MAIN_GROUP, POS)
add_word("suggest", "предлагать", SUB_GROUP, MAIN_GROUP, POS)
add_word("give", "давать", SUB_GROUP, MAIN_GROUP, POS)
add_word("provide", "обеспечивать", SUB_GROUP, MAIN_GROUP, POS)
add_word("supply", "поставлять", SUB_GROUP, MAIN_GROUP, POS)
add_word("present", "дарить", SUB_GROUP, MAIN_GROUP, POS)
add_word("sell", "продавать", SUB_GROUP, MAIN_GROUP, POS)
add_word("lend", "одалживать", SUB_GROUP, MAIN_GROUP, POS)
add_word("bribe", "давать взятку", SUB_GROUP, MAIN_GROUP, POS)

invite; call; wait; welcome; shake hands; visit; introduce; present to; greet;
apologize; excuse; forgive; congratulate; say good bye; thank; leave; get acquainted
SUB_GROUP = "Визит / Этикет • Visit / Etiquette"
add_word("invite", "приглашать", SUB_GROUP, MAIN_GROUP, POS)
add_word("call", "звонить", SUB_GROUP, MAIN_GROUP, POS)
add_word("wait", "ждать", SUB_GROUP, MAIN_GROUP, POS)
add_word("welcome", "приветствовать", SUB_GROUP, MAIN_GROUP, POS)
add_word("shake hands", "пожимать руки", SUB_GROUP, MAIN_GROUP, POS)
add_word("visit", "посещать", SUB_GROUP, MAIN_GROUP, POS)
add_word("introduce", "представлять", SUB_GROUP, MAIN_GROUP, POS)
add_word("present to", "представлять", SUB_GROUP, MAIN_GROUP, POS)
add_word("greet", "приветствовать", SUB_GROUP, MAIN_GROUP, POS)
add_word("apologize", "извиняться", SUB_GROUP, MAIN_GROUP, POS)
add_word("excuse", "прощать", SUB_GROUP, MAIN_GROUP, POS)
add_word("forgive", "прощать", SUB_GROUP, MAIN_GROUP, POS)
add_word("congratulate", "поздравлять", SUB_GROUP, MAIN_GROUP, POS)
add_word("say good bye", "прощаться", SUB_GROUP, MAIN_GROUP, POS)
add_word("thank", "благодарить", SUB_GROUP, MAIN_GROUP, POS)
add_word("leave", "уходить", SUB_GROUP, MAIN_GROUP, POS)
add_word("get acquainted", "знакомиться", SUB_GROUP, MAIN_GROUP, POS)

disturb; bother; offend; hurt; steal; lie; judge; investigate; sentence; convict;
punish; imprison; give evidence
SUB_GROUP = "Нарушение Этикета / Наказание • Breach of Etiquette / Punishment"
add_word("disturb", "беспокоить", SUB_GROUP, MAIN_GROUP, POS)
add_word("bother", "мучить", SUB_GROUP, MAIN_GROUP, POS)
add_word("offend", "обижать", SUB_GROUP, MAIN_GROUP, POS)
add_word("hurt", "причинять боль", SUB_GROUP, MAIN_GROUP, POS)
add_word("steal", "красть", SUB_GROUP, MAIN_GROUP, POS)
add_word("lie", "лгать", SUB_GROUP, MAIN_GROUP, POS)
add_word("judge", "судить", SUB_GROUP, MAIN_GROUP, POS)
add_word("investigate", "расследовать", SUB_GROUP, MAIN_GROUP, POS)
add_word("sentence", "выносить приговор", SUB_GROUP, MAIN_GROUP, POS)
add_word("convict", "признавать виновным", SUB_GROUP, MAIN_GROUP, POS)
add_word("punish", "наказывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("imprison", "заключать в тюрьму", SUB_GROUP, MAIN_GROUP, POS)
add_word("give evidence", "давать показания", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Глаголы Борьбы • Verbs of Fighting"

threaten; arm oneself; disarm; attack; invade
SUB_GROUP = "Нападать • Attack"
add_word("threaten", "угрожать", SUB_GROUP, MAIN_GROUP, POS)
add_word("arm oneself", "вооружаться", SUB_GROUP, MAIN_GROUP, POS)
add_word("disarm", "разоружать", SUB_GROUP, MAIN_GROUP, POS)
add_word("attack", "атаковать", SUB_GROUP, MAIN_GROUP, POS)
add_word("invade", "вторгаться", SUB_GROUP, MAIN_GROUP, POS)

struggle; fight; resist; defend; save; rescue; drive out
SUB_GROUP = "Защищаться • Defend Oneself"
add_word("struggle", "бороться", SUB_GROUP, MAIN_GROUP, POS)
add_word("fight", "сражаться", SUB_GROUP, MAIN_GROUP, POS)
add_word("resist", "сопротивляться", SUB_GROUP, MAIN_GROUP, POS)
add_word("defend", "защищать", SUB_GROUP, MAIN_GROUP, POS)
add_word("save", "спасать", SUB_GROUP, MAIN_GROUP, POS)
add_word("rescue", "спасать", SUB_GROUP, MAIN_GROUP, POS)
add_word("drive out", "выгонять", SUB_GROUP, MAIN_GROUP, POS)

win; lose; conquer; occupy; defeat; overcome; surrender; submit; yield
SUB_GROUP = "Военные операции • Field Operations"
add_word("win", "побеждать", SUB_GROUP, MAIN_GROUP, POS)
add_word("lose", "проигрывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("conquer", "завоёвывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("occupy", "оккупировать", SUB_GROUP, MAIN_GROUP, POS)
add_word("defeat", "побеждать", SUB_GROUP, MAIN_GROUP, POS)
add_word("overcome", "преодолевать", SUB_GROUP, MAIN_GROUP, POS)
add_word("surrender", "сдаваться", SUB_GROUP, MAIN_GROUP, POS)
add_word("submit", "подчиняться", SUB_GROUP, MAIN_GROUP, POS)
add_word("yield", "уступать", SUB_GROUP, MAIN_GROUP, POS)

shoot; aim; point; hit; miss; wound; kill; burst; explode; blow up; bomb; fire
SUB_GROUP = "Действия с Оружием • Actions with Weapons"
add_word("shoot", "стрелять", SUB_GROUP, MAIN_GROUP, POS)
add_word("aim", "целиться", SUB_GROUP, MAIN_GROUP, POS)
add_word("point", "наводить", SUB_GROUP, MAIN_GROUP, POS)
add_word("hit", "попадать", SUB_GROUP, MAIN_GROUP, POS)
add_word("miss", "промахиваться", SUB_GROUP, MAIN_GROUP, POS)
add_word("wound", "ранить", SUB_GROUP, MAIN_GROUP, POS)
add_word("kill", "убивать", SUB_GROUP, MAIN_GROUP, POS)
add_word("burst", "взрываться", SUB_GROUP, MAIN_GROUP, POS)
add_word("explode", "взрываться", SUB_GROUP, MAIN_GROUP, POS)
add_word("blow up", "взрывать", SUB_GROUP, MAIN_GROUP, POS)
add_word("bomb", "бомбить", SUB_GROUP, MAIN_GROUP, POS)
add_word("fire", "обстреливать", SUB_GROUP, MAIN_GROUP, POS)

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
