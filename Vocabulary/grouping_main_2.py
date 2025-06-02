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


sky ; air; cloud; sun; star; moon; planet;
SUB_GROUP = "Небо • Sky"

earth; soil; land; continent; peninsula; island; shore; bank; coast;
SUB_GROUP = "Земля • Earth"

water; sea; ocean; river; lake; swamp; pond; pool; puddle; creek; brook; source; mouth; stream; current; wave; waterfall;
SUB_GROUP = "Вода • Water"

position; location; direction; aim; north; south; east; west; map;
SUB_GROUP = "Позиция • Position"

zone; forest; meadow; steppe; desert; mountain; hill; slope; foot; summit; peak; plain; field; valley; lowland; relief;
SUB_GROUP = "Местности • Terrains"



MAIN_GROUP = "Погода • Weather"

season; winter; spring; summer; autumn; climate; weather;
SUB_GROUP = "Сезон • Season"

meteorology; temperature; pressure; thunderstorm; thunder; lightning; wind; hurricane; sunlight; ray; darkness;
SUB_GROUP = "Метеорология • Meteorology"

rain; drop; mist; fog; steam; dew; ice; snow;
SUB_GROUP = "Осадки • Precipitation"

disaster; catastrophe; earthquake; eruption; epicenter; volcano; flood; fire; destruction; demolition; loss; contamination; environment;
SUB_GROUP = "Стихийные Бедствия • Natural Disasters"

MAIN_GROUP = "Геометрия • Geometry"

size; dimension; unit; meter; centimeter; ruler; measuring tape; length; height; width; depth; thickness;
SUB_GROUP = "Размер • Size"

shape; body; volume; sphere; cylinder; cone; cube; pyramid; prism;
SUB_GROUP = "Форма • Shape"

plane; figure; surface; area; circle; polygon; triangle; square; rectangle;
SUB_GROUP = "Фигуры на плоскости • Plane Figures"

line; straight line; stripe; row; axis; level; limit; point;
SUB_GROUP = "Линии • Lines"

structure; whole; part; base; bottom; top; inside; side; flank; front; rear; back;
SUB_GROUP = "Структура • Structure"

MAIN_GROUP = "Время • Time"

second; minute; hour; day; week; month; year; decade; century; millennium; epoch; season; age; eternity; calendar; clock; watch; alarm clock;
SUB_GROUP = "Единицы времени • Time Units"

december; january; february; march; april; may; june; july; august; september; october; november;
SUB_GROUP = "Месяцы • Months"

monday; tuesday; wednesday; thursday; friday; saturday; sunday;
SUB_GROUP = "Дни Недели • Days of The Week"

morning; daybreak; dawn; sunrise; day; noon; afternoon; evening; sunset; night;
SUB_GROUP = "Стадии дня • Parts of Day"

working time; timetable; schedule; set time; delay; break; rest;
SUB_GROUP = "Рабочее время • Working Time"

holiday; festival; anniversary; birthday; free time; vacation; leave; weekend; day off;
SUB_GROUP = "Праздник / Свободное Время • Holiday / Free Time"

MAIN_GROUP = "Вещество / Материал • Substance / Material"

solid; liquid; solution; gas; vacuum;
SUB_GROUP = "Физическое Состояние • Physical State"

metal; iron; alloy; steel; cast iron; bronze; copper; gold; silver; lead; tin; aluminum;
SUB_GROUP = "Металлы • Metals"

sand; stone; lime; clay; chalk; concrete; brick; cement; asphalt; wood; glass; paint; glue; rubber; plastic;
SUB_GROUP = "Строительные Материалы • Construction Materials"

ore; oil; petroleum; gas; petrol; gasoline; coal;
SUB_GROUP = "Сырье • Raw Materials"

textile; cloth; fabric; silk; cotton; linen; wool; artificial fibre; nylon; leather; fur;
SUB_GROUP = "Ткани • Textiles"

waste; waste paper; dust; dirt; garbage; rubbish; scrap metal;
SUB_GROUP = "Отходы • Waste"

MAIN_GROUP = "Растения • Plants"

vegetable garden; vegetables; carrot; potato; pepper; cabbage; onion; beet; radish; cucumber; parsley; tomato; garlic; gourd;
SUB_GROUP = "Овощи • Vegetables"

melon; watermelon; fruit; berry; apple; pear; plum; apricot; banana; cherry; peach; grape; strawberry; raspberry; lemon; orange; tangerine; grapefruit;
SUB_GROUP = "Фрукты / Ягоды • Fruits / Berries"

grain; cereal; wheat; rye; rice; oat; buckwheat; corn; maize;
SUB_GROUP = "Зерновые • Grains"

fir; pine; birch; maple; poplar; oak; willow; chestnut; acacia; ash;
SUB_GROUP = "Деревья • Trees"

root; trunk; branch; stump; leaf; bud; crown;
SUB_GROUP = "Части дерева • Parts of a Tree"

rose; lily; tulip; lily of the valley; dandelion; daffodil;
SUB_GROUP = "Цветы • Flowers"

MAIN_GROUP = "Животные • Animals"

wolf; fox; bear; tiger; lion; elephant; ape; monkey; camel; rabbit; hare; rat; mouse
SUB_GROUP = "Дикие Животные • Wild Animals"

cow; bull; horse; goat; sheep; ram; donkey; mule; pig; cat; dog; calf; lamb; foal; piglet; kitten; puppy
SUB_GROUP = "Домашние Животные • Domestic Animals"

hen; cock; chick; goose; duck; turkey; crow; sparrow; pigeon; owl; parrot; swan; eagle;
SUB_GROUP = "Птицы Начального Уровня • Birds Beginner Level"

gander; duckling; hawk; nightingale; crane; stork; nestling; magpie;
SUB_GROUP = "Птицы Продвинутого Уровня • Birds Advanced Level"

fish; cod; salmon; carp; shark; spawn;
SUB_GROUP = "Рыба Начального Уровня • Fish Beginner Level"

crucian carp; sturgeon; flatfish; catfish; herring; roach; pike;
SUB_GROUP = "Рыба Продвинутого Уровня • Fish Advanced Level"

insect; fly; bee; wasp; butterfly; caterpillar; ant; spider; cockroach; bug; aphid; louse; grasshopper; cricket;
SUB_GROUP = "Насекомые • Insects"

reptile; frog; toad; snake; viper; grass snake; tortoise; turtle; lizard; crocodile
SUB_GROUP = "Остальные Классы • Other Groups"

MAIN_GROUP = "Человек • Human"

SUB_GROUP = "Общие Сведения • General Information"
SUB_GROUP = "Анатомия • Anatomy"
SUB_GROUP = "Отношения между Людьми • Human Relationships"

MAIN_GROUP = "Жилье • Dwelling"

house; building; apartment; flat; floor; yard; gate; fence; address; street; square
SUB_GROUP = "Дом • House"

roof; chimney; wall; floor; ceiling; window; corner; door; bell; lock; key; tap; faucet; light; switch; electricity; elevator
SUB_GROUP = "Устройство Дома • House Layout"

kitchen; bathroom; toilet; corridor; living room; hall; bedroom; dining room; study
SUB_GROUP = "Комнаты • Rooms"

furniture; table; chair; armchair; bed; sofa; wardrobe; cupboard; bookcase; carpet; mirror; blinds; curtain; coat rack
SUB_GROUP = "Мебель • Furniture"

bedclothes; sheet; pillowcase; blanket; pillow; mattress; bedspread
SUB_GROUP = "Кровать • Bed"

container; bag; suitcase; barrel; case; basket; sack; box; backpack; vessel; bucket; vase; can; jar; jug
SUB_GROUP = "Сосуды / Емкости • Vessels / Containers"

iron; vacuum cleaner; refrigerator; fridge; washing machine; sewing machine; mixer; cooker; stove; range; utensils; broom
SUB_GROUP = "Бытовые приборы • Household Appliances"

MAIN_GROUP = "Одежда • Clothes"


SUB_GROUP = "Верхняя Одежда • Outer Clothing"

coat; raincoat; fur coat; casual wear; suit; jacket; vest; shirt; trousers – pants; jeans; dress; blouse; skirt; underwear; bra; panties; nightgown; pyjamas; socks; stockings; tights;
SUB_GROUP = "Одежда / Белье • Clothes / Underwear"

footwear; shoe; boot; sandal; slippers; trainers; shoelace; shoe polish;
SUB_GROUP = "Обувь • Footwear"


headgear; hat; cap; beret; kerchief; shawl;
SUB_GROUP = "Головные уборы • Headgear"

sleeve; collar; cuff; button; zip; belt; hook; buckle; tie; bow tie; cravat; scarf; gloves; umbrella; handkerchief; handbag; wallet; purse;
SUB_GROUP = "Аксессуары и части одежды • Accessories and Clothing Parts"

MAIN_GROUP = "Питание • Nourishment"

meal; breakfast; lunch; dinner; tea; supper; taste; appetite;
SUB_GROUP = "Прием Пищи • Eating"

the first course; the second course; dessert; soup; garnish; porridge; noodles; macaroni; fried potatoes; mashed potatoes; boiled egg; fried eggs; beefsteak; meat; beef; pork; mutton; veal; poultry;
SUB_GROUP = "Блюда • Dishes"

mustard; vinegar; pepper; salt; spice; herb;
SUB_GROUP = "Приправы • Condiments"

drink; tea; coffee; cocoa; milk; juice; mineral water; lemonade; cola; wine; beer; whisky;
SUB_GROUP = "Напитки • Drinks and Beverages"

sweets; chocolate; candy; jam; marmalade; cake; pie; biscuit-cookie; sugar; honey; chewing gum;
SUB_GROUP = "Сладости • Sweets"

foodstuffs; butter; margarine; cheese; cottage cheese; cream; sour cream; buckwheat; oatmeal; salt; sausage; salami; egg; canned goods; tinned food; vegetable oil; butcher's; greengrocery; dairy; fishmonger's; grocery; confectionery;
SUB_GROUP = "Пищевые Продукты • Foodstuffs"

bread; loaf; roll; bun; pancake; tart; pie; doughnut; pasty; flour; dough; pastry;
SUB_GROUP = "Хлеб • Bread"

dining table; tablecloth; napkin; spoon; tablespoon; teaspoon; fork; knife; dish; glass; cup; plate; bowl; saucer; pan; frying pan; pot; bottle opener; tin opener; ladle; kitchen utensils;
SUB_GROUP = "Кухонные Принадлежности • Kitchen Utensils"

MAIN_GROUP = "Чувства / Характер • Feeling / Character"

emotion; satisfaction; pleasure; excitement; happiness; joy; enthusiasm; delight; interest; relief
SUB_GROUP = "Позитивные Эмоции • Positive Emotions"

boredom; uneasiness; discontent; dissatisfaction; sadness; suffering; sorrow; grief; anxiety
SUB_GROUP = "Негативные Эмоции • Negative Emotions"

patience; self-control; firmness; courage; willpower; resolution; determination; confidence; weakness; hesitation; doubt; cowardice; suspicion; disbelief; distrust
SUB_GROUP = "Терпение / Слабость • Patience / Weakness"

sympathy; respect; friendship; admiration; love; adoration; indifference; contempt; malice; resentment; disgust; envy
SUB_GROUP = "Любовь / Ненависть • Love / Hatred"

pride; vanity; arrogance; modesty; shyness; consideration; tolerance; shame; intolerance; politeness; tact; good manners; courtesy; rudeness; lack of tact; disrespect; offence; insult
SUB_GROUP = "Гордость / Скромность • Pride / Modesty"

wish; desire; hope; dream; intention; aspiration; eagerness; aim; purpose; stimulus; incentive; tiredness; fatigue; laziness; diligence
SUB_GROUP = "Старание / Лень • Diligence / Laziness"

MAIN_GROUP = "Мышление • Thinking"

nature; universe; world; existence; reality; being; conscience; science; philosophy
SUB_GROUP = "Сознание • Consciousness"

practice; knowledge; cognition; object; subject; reflection; sensation; perception; idea; notion; concept; statement; conclusion; logic; theory
SUB_GROUP = "Познание • Cognition"

regularity; accident; chance; whole; part; form; contents; essence; variety; diversity; similarity; identity; contrast; contradiction; quantity; quality; number; order; sequence; system; time; space; place; room; spot; surroundings; circumstance; factor; reason; cause; development; consequence; necessity; possibility; probability;
SUB_GROUP = "Категории Мышления • Thinking Categories"

research; theme; topic; issue; problem; phenomenon; fact; sample; specimen; example; field; indication; symptom; characteristic; feature; means; method; procedure; way; manner; laboratory; equipment; appliance; device; discovery; modification; improvement; development; creation; invention; verification
SUB_GROUP = "Исследование • Research"

analysis; comparison; data processing; classification; kind; type; interconnection; correlation; interaction; rule; law; principle; exception
SUB_GROUP = "Анализ • Analysis"

success; failure; advantage; merit; effectiveness; efficiency; importance; disadvantage; deficiency; demerit; error; mistake
SUB_GROUP = "Результат • Result"

statement; report; thought; idea; premise; criteria; proof; argument; conclusion
SUB_GROUP = "Сообщение • Report"

criticism; attitude; position; point of view; definition; consent; assent; approval; recognition; confirmation; objection; rejection; refusal; overestimation; underestimation; misunderstanding
SUB_GROUP = "Критика • Criticism"

MAIN_GROUP = "Образование • Education"

education; upbringing; teaching; instruction; training; elementary school; primary school; high school; vocational school; college; institute; university;
SUB_GROUP = "Учебные Заведения • Educational Institutions"

subject; timetable; STEM fields; mathematics; physics; biology; chemistry; engineering; drawing; humanities; history; literature; foreign language; physical education;
SUB_GROUP = "Учебные Предметы • Subjects"

year (as grade); grade; form; class; lesson; lecture; break; task; homework; teacher; pupil; student; classroom; blackboard; desk; teaching aids; textbook; pen; pencil; ruler; eraser; map; school year; vacation;
SUB_GROUP = "Учеба • Studies"

competition; examination; exam; certificate; diploma;
SUB_GROUP = "Экзамен / Оценки • Exams / Grades"

linguistics; language; speech; vocabulary; grammar; style; letter; alphabet; spelling; pronunciation; vowel; consonant; transcription;
SUB_GROUP = "Лингвистика • Linguistics — Part 1"

word; phrase; idiom; sentence; simple sentence; complex sentence; clause; text; affirmation; interrogation; negation;
SUB_GROUP = "Лингвистика • Linguistics — Part 2"

part of speech; noun; verb; adjective; pronoun; adverb; numeral; preposition; conjunction; article; interjection;
SUB_GROUP = "Лингвистика • Linguistics — Part 3"

progressive aspect; perfective aspect; active voice; passive voice; case; gender; number; singular; plural;
SUB_GROUP = "Лингвистика • Linguistics — Part 4"

part of sentence; subject; predicate; object; adverbial; attribute;
SUB_GROUP = "Лингвистика • Linguistics — Part 5"

MAIN_GROUP = "Культура • Culture"

cinema; film documentary; detective comedy; adventure film; thriller; horror film; box-office; ticket; seat; performance; showing;
SUB_GROUP = "Кино • Cinema"

producer; cameramen; actor; actress; extra; artist; makeup artist; set designer; star;
SUB_GROUP = "Киносоздатели  • Cinema — People"

theatre; puppet show; stage; curtain; scenery; performance; cast; audience; applause; first night; interval; auditorium; balcony
SUB_GROUP = "Театр • Theatre"

song; tune; concert; program; encore; music; orchestra; chorus; choir; band; musician; composer; conductor; singer
SUB_GROUP = "Музыка • Music"

piano; violin; drum; guitar; trumpet; saxophone
SUB_GROUP = "Музыкальные инструменты • Musical Instruments"

literature; book; edition; volume; title; cover; section; chapter; page; author; writer; poet; playwright;
SUB_GROUP = "Литература • Literature"

work; novel; story; verse; fairy tale; fiction; library; editor
SUB_GROUP = "Издательство • Publishing House"


SUB_GROUP = "Спорт • Sport"



MAIN_GROUP = "Работа • Work"

job; work; labour; activity; service; years of experience; position; role; duty; place; unemployed; unemployment;
SUB_GROUP = "Труд / Занятость • Labour / Employment"

field; industry; agriculture; construction; transport; communication; trade; culture; science; art; healthcare; education;
SUB_GROUP = "Сферы • Fields"

company; branch; firm; enterprise; plant; factory; power plant; oil refinery; coal mine;
SUB_GROUP = "Предприятие • Enterprise"

profession; trade; occupation; worker; mechanic; electrician; welder; driver; employee; engineer; lawyer; secretary; interpreter; translator; chief; director; manager; minister; ambassador;
SUB_GROUP = "Професcия • Profession"

tool; hammer; axe; drill; scissors; screwdriver; wrench; nail; bolt; screw; wire; spring; equipment; device; accessory; cutter; machinery;
SUB_GROUP = "Инструменты / Оборудование • Tools / Equipment (Beginner)"

file; plane; pliers; jack; nut; washer; appliance; tongs; pincers; sickle;
SUB_GROUP = "Инструменты / Оборудование • Tools / Equipment (Advanced)"


MAIN_GROUP = "Связь / Транспорт • Communication / Transport"

post office; general post office; postman; address; addressee; sender; letter; envelope; stamp; printed matter; postal order; parcel;
SUB_GROUP = "Почта • Post"

telegraph; text; charge; phone; dial; receiver; trunk call; international call; directory;
SUB_GROUP = "Телефон • Phone"

railway station; platform; track; train; locomotive; ticket collector; porter; guard; departure; arrival; timetable; departures board; upper berth; lower berth
SUB_GROUP = "Железная Дорога • Railway"

passenger train; fast train; express; suburban train; train car; train coach; train carriage; wagon; first class; sleeping car; buffet car; dining car; goods van; tank wagon
SUB_GROUP = "Типы Вагонов и Поездов • Types of Trains and Cars"

aeroplane; jet plane; propeller-driven aircraft; supersonic airliner; engine; wing; fuselage; tail; undercarriage; cockpit
SUB_GROUP = "Воздушный Транспорт • Air Transport"

airport; air terminal; take-off runway; waiting room; departure lounge; crew; pilot; navigator; air hostess; flight; journey; check-in; passport control; boarding; take-off; landing; crash
SUB_GROUP = "В аэропорту • At the Airport"

vehicle; car; bus; truck; tanker; road; highway; motorway; crossroads; bridge; flyover; underpass; guardrail
SUB_GROUP = "Vehicle Types and Infrastructure"

traffic; traffic sign; road marking; pedestrian crossing; traffic lights; starting; braking; acceleration; car service; gas station; car wash
SUB_GROUP = "Traffic and Road Usage"

spare part; hood; headlight; license plate; windshield; wipers; tire; trunk; exhaust pipe; steering wheel; seat belt; gear lever; clutch; brake pedal; accelerator; ignition; fuel gauge; horn; engine; radiator; battery; spare wheel
SUB_GROUP = "Car parts"

MAIN_GROUP = "Город • City"

city; town; village; street; lane; avenue; square; building; corner; pavement;
SUB_GROUP = "Улицы • Streets"

tram; metro; underground; subway; car; taxi; conductor; ticket; seat;
SUB_GROUP = "Транспорт • Transport"

cinema; theatre; museum; gallery; circus; restaurant; bar; cafe; club; park; church; hotel;
SUB_GROUP = "Культурные Учреждения • Social and Cultural institutions"


MAIN_GROUP = "Общение • Communication"

deal; information; report; rumours; news; truth; lie; white lie;
SUB_GROUP = "Информация • Information"

mother tongue; foreign language; meaning; accent; dialect; slang; conversation; dialogue; dispute; discussion; question; answer; advice; warning; request; demand; observation; remark; reaction; consent; permission; promise; comment; aid; assistance; help; objection; prohibition; refusal; understanding
SUB_GROUP = "Общение / Высказывание • Communication / Expression"

visit; meeting; reception; invitation; host; guest; greeting; welcome; handshake; farewell; etiquette; behaviour
SUB_GROUP = "Визит • Visit"


MAIN_GROUP = "Государство • State"

country; state; capital; border; flag; democracy
territory; anthem; social system; socialism; capitalism; civilization
SUB_GROUP = "Государство • State"

people; population; nationality; nation; custom; habit; motherland; patriot; glory; hero; religion; faith; church; christian; muslim; buddhist; catholic; protestant
SUB_GROUP = "Народ • People"

social status; worker; peasant; owner; landlord; capitalist
SUB_GROUP = "Социальный Статус • Social Status"

justice; equality; right; human rights; duty; discrimination; violence; protest; law; police; lawyer; crime; criminal; court; judge; sentence; punishment; penalty; fine; jail; prison; obligation; oppression; offence; public prosecutor
SUB_GROUP = "Закон / Право • Law"

government; republic; parliament; president; election; constitution; article; party; trade union; congress; conference; discussion; program; monarchy; king; queen; emperor; dictatorship; reform; revolution
SUB_GROUP = "Политика • Politics"

economics; statistics; economy; national income; wealth; finance; budget; tax; money; living standard; private property; bank; account; cash; free of charge; debt; price; increase; decrease; foreign trade; contract; customs; inspection; duty
SUB_GROUP = "Экономика • Economy"

foreign policy; peaceful coexistence; mutual assistance; cooperation; interference; intervention; aggression; diplomacy; negotiations; talks; treaty; citizen; citizenship; permanent residence; visa
SUB_GROUP = "Внешняя Политика • Foreign Policy"

MAIN_GROUP = "Медицина • Medicine"

health; hygiene; preventive measures; health hazard; alcohol consumption; smoking; obesity; weight loss; illness; disease; recovery; death
SUB_GROUP = "Здоровье / болезнь • Health / Illness"

injury; wound; bruise; fracture; burn; ulcer; rash; abscess; sore
SUB_GROUP = "Наружные повреждения • Injuries"

infection; contagious disease; plague; flu;
SUB_GROUP = "Инфекции • Infections"

mental disease; neurological disease; neurosis; allergy; AIDS; cancer
SUB_GROUP = "Остальные Заболевания • Other Diseases"

symptom; fever; blood pressure; dizziness; sweating; cough; sickness; diarrhea; ache; headache; toothache
SUB_GROUP = "Симптомы • Symptoms"

medical examination; blood test; urine test; x ray; treatment; therapy; operation; anaesthesia; injection; medicine; drug; bandage; drugstore; pharmacy; prescription
SUB_GROUP = "Лечение • Treatment"

ambulance; hospital; clinic; doctor; surgeon; psychiatrist; dentist; eye doctor; nurse; patient
SUB_GROUP = "Больница • Hospital"


# ADJECTIVES
POS = "adjectives"

MAIN_GROUP = "Органы чувств • Organs of senses"

dark ; light ; colourless ; transparent ; opaque ; bright ; brilliant ; pale ; dim ; distinct
large ; big ; huge ; wide ; broad ; thick ; long ; tall ; deep ; little ; small ; narrow ;
thin ; short ; shallow ; low ; far ; near
flat ; plane ; straight ; curved ; vertical ; horizontal ; round ; square

SUB_GROUP = "Глаза • Eye"

uneven ; even ; smooth ; rough ; hard ; soft ; sharp ; blunt
dry; wet; humid
SUB_GROUP = "Кожа • Skin"

tasty ; delicious ; tasteless ; sweet ; sour ; salty ; bitter ; strong ; pungent
SUB_GROUP = "Язык • Tongue"

loud ; noisy ; sharp ; calm ; soft ; low ; quiet ; muffled ; deaf ; inaudible
SUB_GROUP = "Ухо • Ear"

smelly ; stinking ; aromatic ; fragrant ; odourless
SUB_GROUP = "Нос • Nose"


MAIN_GROUP = "Время • Time"

long ; brief ; short ; fast ; swift ; quick ; rapid ; urgent ; slow ; early ; late ; young ; adult ; old ; aged
SUB_GROUP = "Основные Свойства • Main Properties"

past ; recent ; obsolete ; ancient ; present ; contemporary ; modern ; up-to-date ; future ; previous ; preceding ;
preliminary ; simultaneous ; next ; following ; the first ; the last ; initial ; final
SUB_GROUP = "Стадии • Stages"

constant ; temporary ; uninterrupted ; continuous ; rare ; frequent ; usual ; occasional ; sudden ; eternal
SUB_GROUP = "Продолжительность / Частота • Duration / Frequency"

MAIN_GROUP = "Способности человека • Human abilities"

gifted; capable; talented; clever; intelligent; quick; wise
SUB_GROUP = "Способность • Ability"

silly; stolid; stupid; dull; naive; ignorant; average; mediocre; mad; crazy
SUB_GROUP = "Отсутствие Способности • Lack of Ability"

diligent; industrious; lazy; accurate; exact; thorough; negligent; attentive; careful; careless; absent-minded; distracted
SUB_GROUP = "Старание / Внимание • Diligence / Attention"

experienced; inexperienced; skillful; deft; dexterous; clumsy; awkward
SUB_GROUP = "Навык / Опыт • Skill / Experience"

MAIN_GROUP = "Эмоция • Emotions"

sensitive; sentimental; hard-hearted; indifferent; irritable; calm; quiet; tranquil; nervous
SUB_GROUP = "Характер • Character"

happy; lucky; joyful; merry; cheerful; glad; satisfied; optimistic; sad; sorry; upset; pessimistic; sorrowful; high-spirited; low-spirited
SUB_GROUP = "Настроение • Mood"

good; pleasant; agreeable; interesting; wonderful; excellent; splendid; gorgeous; magnificent; perfect;
surprising; astonishing; amazing; exciting; moving; touching; strange; shocking; bad; tiresome; boring; disturbing

disgusting; unpleasant; abusive; offensive; awful; terrible; dangerous; beautiful; lovely; nice; pretty; attractive; ugly; repulsive; fearful
SUB_GROUP = "Эмоциональная Оценка • Emotional Evaluation"

excited; agitated; uneasy; moved; frightened; scared; startled; surprised; astonished; amazed; angry; cross; hurt; offended
SUB_GROUP = "Оттенки Эмоции • Shades of Emotion"

MAIN_GROUP = "Мораль / Поведение • Moral / Behaviour"

decent; well-behaved; noble; worthy; honest; fair; sincere; lying; mean; base; vile; innocent; criminal; guilty
SUB_GROUP = "Основные Свойства • Main Properties"

good; kind; friendly; selfish; bad; evil; hostile; obedient; true; faithful; reliable; devoted; unstable; changeable; generous; wasteful; greedy;vicious;
SUB_GROUP = "Отношение к Окружающим • Attitude towards Others"

talkative; sociable; reserved; polite; civil; gentle; mild; rude; rough; strict; severe;
SUB_GROUP = "Качества в Общении • Communication Qualities"

brave; audacious; courageous; cowardly; timid; modest; shy; proud; arrogant; reasonable; rational; cautious; thoughtless; rash; hasty; impulsive;
SUB_GROUP = "Качества в Поведении • Qualities in Behavior"

MAIN_GROUP = "Абстрактные прилагательные • Abstract Adjectives"

certain; common; general; typical; single; separate; particular; special; main; chief; principal; basic; secondary; complex; simple;
SUB_GROUP = "Классификация • Classification"

equal; the same; different; various; similar; important; significant; essential; advanced; inferior; defective; spoiled; natural; artificial; difficult; easy;
SUB_GROUP = "Качество • Quality"

maximum; minimum; average; sufficient; excessive; numerous; full; empty;
SUB_GROUP = "Количество • Quantity"

inevitable; relative; absolute; positive; negative; real; actual; practical; conditional; hypothetical; assumed; possible; probable; desirable; theoretical; imaginary; regular; occasional; necessary
SUB_GROUP = "Категория • Category"

correct; true; precise; logical; appropriate; suitable; acceptable; satisfactory; wrong; false; illogical; approximate; absurd; legal; lawful; out of place; standard; reliable
SUB_GROUP = "Соответствие • Accordance"

advantageous; profitable; efficient; valid; useful; harmless; useless; harmful; cheap; expensive; free of charge; priceless
SUB_GROUP = "Преимущество • Advantage"

MAIN_GROUP = "Состояние / Статус • Condition / Status"

healthy; robust; strong; vigorous; cheerful; sick; ill; weak; drowsy; sleepy; tired; exhausted; fat; lean; slim
SUB_GROUP = "Физическое Состояние • Physical Condition"

single; married; divorced
SUB_GROUP = "Семейное Положение • Family Status"

comfortable; convenient; complete; intact; damaged; spoiled; cooked; fried; baked; raw; packed; free; vacant; occupied; busy; clean; dirty
SUB_GROUP = "Состояние • Condition"


# # ADVERBS
# POS = "adverbs"
#
# MAIN_GROUP = "Наречия Без группы • Ungrouped Adverbs"
#
# SUB_GROUP = "Вопросительные Наречия • Interrogative Adverbs"
#
#
# SUB_GROUP = "Наречия Образа действий • Adverbs of Manner"
# SUB_GROUP = "Наречия относящиеся к Предложениям • Sentence Adverbs"
# SUB_GROUP = "Наречия соединения Предложений • Conjunctive Adverbs"
#
# MAIN_GROUP = "Наречия Места • Adverbs of Place"
#
# SUB_GROUP = "Наречия со значением Места • Adverbs of meaning Place"
# SUB_GROUP = "Собственно Наречия Места • Adverbs of Place itself"
# SUB_GROUP = "Наречия Направления • Adverbs of Direction"
#
# MAIN_GROUP = "Наречия Времени • Adverbs of Time "
#
# SUB_GROUP = "Последовательность • Sequence"
# SUB_GROUP = "Частота • Frequency"
# SUB_GROUP = "Вчера / Сегодня / Завтра • Yesterday / Today / Tomorrow"
# SUB_GROUP = "Все Еще / Уже • Still / Already"
#
# MAIN_GROUP = "Наречия Меры, Степени и Количества • Adverbs of Degree, Measure and Quantity"
#
# SUB_GROUP = "Большая Степень • High Degree"
# SUB_GROUP = "Средняя Степень • Medium Degree"
# SUB_GROUP = "Небольшая Степень • Low Degree"
#
#
#


# # PRONOUNS
# POS = "pronouns"
# MAIN_GROUP = "Местоимения  • Pronouns"
#
# SUB_GROUP = "Личные Местоимения • Personal Pronouns"
# SUB_GROUP = "Указательные Местоимения • Demonstrative Pronouns"
# SUB_GROUP = "Вопросительные Местоимения • Interrogative Pronouns"
# SUB_GROUP = "Неопределенные Местоимения • Indefinite Pronouns"
# SUB_GROUP = "Определенные Местоимения • Definite Pronouns"
# SUB_GROUP = "Отрицательные Местоимения • Negative Pronouns"
#


# PREPOSITIONS
POS = "prepositions"
MAIN_GROUP = "Предлоги  • Prepositions"

beside (the house) ; among (us) ; between (the houses) ; by (the window) ; at (the door) ; round (the table) ;
far from (the house) ; in front of (our office) ; opposite (my house) ; behind (me) ; above (my head) ;
over (the table) ; under (the bed) ; below (the ground) ; in (the school) ; inside (the house) ;
outside (the house) ; on (the table)
SUB_GROUP = "Предлоги Места • Prepositions of place"

from (London) ; off (the field) ; out of (the room) ; along (the street) ; down (the street) ; to (the sea) ;
towards (the sea) ; across (the river) ; through (the forest) ; over (the wall) ; down (the steps) ;
up (the hill) ; past (the house) ; into (the house) ; for (Kiev)
SUB_GROUP = "Предлоги Направления • Prepositions of Direction"

for (two weeks) ; within (a week) ; over (the last three days) ; in (an hour) ; during (the event); in (1965 , August) ;
since (1980) ; at (four o'clock) ; till (four o'clock) ; by (three o'clock) ; from (two o'clock) ; on (Monday) ;
in (the morning) ; at (noon , night) ; before (the work) ; after (the work) ; on (the first of May) ;
(ten minutes) past (seven) ; (ten minutes) to (seven)
SUB_GROUP = "Предлоги Времени • Prepositions of Time"

according (to the plan) ; in spite of (poor health) ; despite (the difference) ; regardless of (the law) ;
because of (illness) ; due to (rain) ; thanks to (your help) ; except (you) ; except for (him) ;
instead of (the teacher) ; as to (buying) ; as for (signing) ; on behalf of (my colleagues) ;
for the purpose of (improving) ; for (children) ; against (noise) ; without (money) ; (a cake) of (soap) ;
to (me) ; (a book) about (flowers)
SUB_GROUP = "Смешанная Группа • Mixed Group"

#
# # NUMERALS
# POS = "numerals"
# MAIN_GROUP = "Числительные • Numerals"
#
# SUB_GROUP = "Количественные Числительные • Cardinal Numerals"
# SUB_GROUP = "Порядковые Числительные • Ordinal Numerals"
# SUB_GROUP = "Дроби • Fractions"
#
#

end_time = time.time()
elapsed_time = end_time - start_time
print(f"\nTime spent: {elapsed_time:.6f} seconds")
