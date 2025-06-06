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
add_word("sky", "небо", SUB_GROUP, MAIN_GROUP, POS)
add_word("air", "воздух", SUB_GROUP, MAIN_GROUP, POS)
add_word("cloud", "облако", SUB_GROUP, MAIN_GROUP, POS)
add_word("sun", "солнце", SUB_GROUP, MAIN_GROUP, POS)
add_word("star", "звезда", SUB_GROUP, MAIN_GROUP, POS)
add_word("moon", "луна", SUB_GROUP, MAIN_GROUP, POS)
add_word("planet", "планета", SUB_GROUP, MAIN_GROUP, POS)

earth; soil; land; continent; peninsula; island; shore; bank; coast;
SUB_GROUP = "Земля • Earth"
add_word("earth", "земля", SUB_GROUP, MAIN_GROUP, POS)
add_word("soil", "почва", SUB_GROUP, MAIN_GROUP, POS)
add_word("land", "земля", SUB_GROUP, MAIN_GROUP, POS)
add_word("continent", "континент", SUB_GROUP, MAIN_GROUP, POS)
add_word("peninsula", "полуостров", SUB_GROUP, MAIN_GROUP, POS)
add_word("island", "остров", SUB_GROUP, MAIN_GROUP, POS)
add_word("shore", "берег", SUB_GROUP, MAIN_GROUP, POS)
add_word("bank", "берег", SUB_GROUP, MAIN_GROUP, POS)
add_word("coast", "побережье", SUB_GROUP, MAIN_GROUP, POS)

water; sea; ocean; river; lake; swamp; pond; pool; puddle; creek; brook; source; mouth; stream; current; wave; waterfall;
SUB_GROUP = "Вода • Water"
add_word("water", "вода", SUB_GROUP, MAIN_GROUP, POS)
add_word("sea", "море", SUB_GROUP, MAIN_GROUP, POS)
add_word("ocean", "океан", SUB_GROUP, MAIN_GROUP, POS)
add_word("river", "река", SUB_GROUP, MAIN_GROUP, POS)
add_word("lake", "озеро", SUB_GROUP, MAIN_GROUP, POS)
add_word("swamp", "болото", SUB_GROUP, MAIN_GROUP, POS)
add_word("pond", "пруд", SUB_GROUP, MAIN_GROUP, POS)
add_word("pool", "водоем", SUB_GROUP, MAIN_GROUP, POS)
add_word("puddle", "лужа", SUB_GROUP, MAIN_GROUP, POS)
add_word("creek", "ручей", SUB_GROUP, MAIN_GROUP, POS)
add_word("brook", "ручей", SUB_GROUP, MAIN_GROUP, POS)
add_word("source", "исток", SUB_GROUP, MAIN_GROUP, POS)
add_word("mouth", "устье", SUB_GROUP, MAIN_GROUP, POS)
add_word("stream", "поток", SUB_GROUP, MAIN_GROUP, POS)
add_word("current", "течение", SUB_GROUP, MAIN_GROUP, POS)
add_word("wave", "волна", SUB_GROUP, MAIN_GROUP, POS)
add_word("waterfall", "водопад", SUB_GROUP, MAIN_GROUP, POS)

position; location; direction; aim; north; south; east; west; map;
SUB_GROUP = "Позиция • Position"
add_word("position", "позиция", SUB_GROUP, MAIN_GROUP, POS)
add_word("location", "местоположение", SUB_GROUP, MAIN_GROUP, POS)
add_word("direction", "направление", SUB_GROUP, MAIN_GROUP, POS)
add_word("aim", "цель", SUB_GROUP, MAIN_GROUP, POS)
add_word("north", "север", SUB_GROUP, MAIN_GROUP, POS)
add_word("south", "юг", SUB_GROUP, MAIN_GROUP, POS)
add_word("east", "восток", SUB_GROUP, MAIN_GROUP, POS)
add_word("west", "запад", SUB_GROUP, MAIN_GROUP, POS)
add_word("map", "карта", SUB_GROUP, MAIN_GROUP, POS)

zone; forest; meadow; steppe; desert; mountain; hill; slope; foot; summit; peak; plain; field; valley; lowland; relief;
SUB_GROUP = "Местности • Terrains"
add_word("zone", "зона", SUB_GROUP, MAIN_GROUP, POS)
add_word("forest", "лес", SUB_GROUP, MAIN_GROUP, POS)
add_word("meadow", "луг", SUB_GROUP, MAIN_GROUP, POS)
add_word("steppe", "степь", SUB_GROUP, MAIN_GROUP, POS)
add_word("desert", "пустыня", SUB_GROUP, MAIN_GROUP, POS)
add_word("mountain", "гора", SUB_GROUP, MAIN_GROUP, POS)
add_word("hill", "холм", SUB_GROUP, MAIN_GROUP, POS)
add_word("slope", "склон", SUB_GROUP, MAIN_GROUP, POS)
add_word("foot", "подножие", SUB_GROUP, MAIN_GROUP, POS)
add_word("summit", "вершина", SUB_GROUP, MAIN_GROUP, POS)
add_word("peak", "пик", SUB_GROUP, MAIN_GROUP, POS)
add_word("plain", "равнина", SUB_GROUP, MAIN_GROUP, POS)
add_word("field", "поле", SUB_GROUP, MAIN_GROUP, POS)
add_word("valley", "долина", SUB_GROUP, MAIN_GROUP, POS)
add_word("lowland", "низменность", SUB_GROUP, MAIN_GROUP, POS)
add_word("relief", "рельеф", SUB_GROUP, MAIN_GROUP, POS)



MAIN_GROUP = "Погода • Weather"

season; winter; spring; summer; autumn; climate; weather;
SUB_GROUP = "Сезон • Season"
add_word("season", "сезон", SUB_GROUP, MAIN_GROUP, POS)
add_word("winter", "зима", SUB_GROUP, MAIN_GROUP, POS)
add_word("spring", "весна", SUB_GROUP, MAIN_GROUP, POS)
add_word("summer", "лето", SUB_GROUP, MAIN_GROUP, POS)
add_word("autumn", "осень", SUB_GROUP, MAIN_GROUP, POS)
add_word("climate", "климат", SUB_GROUP, MAIN_GROUP, POS)
add_word("weather", "погода", SUB_GROUP, MAIN_GROUP, POS)

meteorology; temperature; pressure; thunderstorm; thunder; lightning; wind; hurricane; sunlight; ray; darkness;
SUB_GROUP = "Метеорология • Meteorology"
add_word("meteorology", "метеорология", SUB_GROUP, MAIN_GROUP, POS)
add_word("temperature", "температура", SUB_GROUP, MAIN_GROUP, POS)
add_word("pressure", "давление", SUB_GROUP, MAIN_GROUP, POS)
add_word("thunderstorm", "гроза", SUB_GROUP, MAIN_GROUP, POS)
add_word("thunder", "гром", SUB_GROUP, MAIN_GROUP, POS)
add_word("lightning", "молния", SUB_GROUP, MAIN_GROUP, POS)
add_word("wind", "ветер", SUB_GROUP, MAIN_GROUP, POS)
add_word("hurricane", "ураган", SUB_GROUP, MAIN_GROUP, POS)
add_word("sunlight", "солнечный свет", SUB_GROUP, MAIN_GROUP, POS)
add_word("ray", "луч", SUB_GROUP, MAIN_GROUP, POS)
add_word("darkness", "темнота", SUB_GROUP, MAIN_GROUP, POS)

rain; drop; mist; fog; steam; dew; ice; snow;
SUB_GROUP = "Осадки • Precipitation"
add_word("rain", "дождь", SUB_GROUP, MAIN_GROUP, POS)
add_word("drop", "капля", SUB_GROUP, MAIN_GROUP, POS)
add_word("mist", "туман", SUB_GROUP, MAIN_GROUP, POS)
add_word("fog", "туман", SUB_GROUP, MAIN_GROUP, POS)
add_word("steam", "пар", SUB_GROUP, MAIN_GROUP, POS)
add_word("dew", "роса", SUB_GROUP, MAIN_GROUP, POS)
add_word("ice", "лед", SUB_GROUP, MAIN_GROUP, POS)
add_word("snow", "снег", SUB_GROUP, MAIN_GROUP, POS)

disaster; catastrophe; earthquake; eruption; epicenter; volcano; flood; fire; destruction; demolition; loss; contamination; environment;
SUB_GROUP = "Стихийные Бедствия • Natural Disasters"
add_word("disaster", "катастрофа", SUB_GROUP, MAIN_GROUP, POS)
add_word("catastrophe", "катастрофа", SUB_GROUP, MAIN_GROUP, POS)
add_word("earthquake", "землетрясение", SUB_GROUP, MAIN_GROUP, POS)
add_word("eruption", "извержение", SUB_GROUP, MAIN_GROUP, POS)
add_word("epicenter", "эпицентр", SUB_GROUP, MAIN_GROUP, POS)
add_word("volcano", "вулкан", SUB_GROUP, MAIN_GROUP, POS)
add_word("flood", "наводнение", SUB_GROUP, MAIN_GROUP, POS)
add_word("fire", "пожар", SUB_GROUP, MAIN_GROUP, POS)
add_word("destruction", "разрушение", SUB_GROUP, MAIN_GROUP, POS)
add_word("demolition", "снос", SUB_GROUP, MAIN_GROUP, POS)
add_word("loss", "потеря", SUB_GROUP, MAIN_GROUP, POS)
add_word("contamination", "загрязнение", SUB_GROUP, MAIN_GROUP, POS)
add_word("environment", "окружающая среда", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Геометрия • Geometry"

size; dimension; unit; meter; centimeter; ruler; measuring tape; length; height; width; depth; thickness;
SUB_GROUP = "Размер • Size"
add_word("size", "размер", SUB_GROUP, MAIN_GROUP, POS)
add_word("dimension", "размерность", SUB_GROUP, MAIN_GROUP, POS)
add_word("unit", "единица", SUB_GROUP, MAIN_GROUP, POS)
add_word("meter", "метр", SUB_GROUP, MAIN_GROUP, POS)
add_word("centimeter", "сантиметр", SUB_GROUP, MAIN_GROUP, POS)
add_word("ruler", "линейка", SUB_GROUP, MAIN_GROUP, POS)
add_word("measuring tape", "рулетка", SUB_GROUP, MAIN_GROUP, POS)
add_word("length", "длина", SUB_GROUP, MAIN_GROUP, POS)
add_word("height", "высота", SUB_GROUP, MAIN_GROUP, POS)
add_word("width", "ширина", SUB_GROUP, MAIN_GROUP, POS)
add_word("depth", "глубина", SUB_GROUP, MAIN_GROUP, POS)
add_word("thickness", "толщина", SUB_GROUP, MAIN_GROUP, POS)

shape; body; volume; sphere; cylinder; cone; cube; pyramid; prism;
SUB_GROUP = "Форма • Shape"
add_word("shape", "форма", SUB_GROUP, MAIN_GROUP, POS)
add_word("body", "тело", SUB_GROUP, MAIN_GROUP, POS)
add_word("volume", "объем", SUB_GROUP, MAIN_GROUP, POS)
add_word("sphere", "сфера", SUB_GROUP, MAIN_GROUP, POS)
add_word("cylinder", "цилиндр", SUB_GROUP, MAIN_GROUP, POS)
add_word("cone", "конус", SUB_GROUP, MAIN_GROUP, POS)
add_word("cube", "куб", SUB_GROUP, MAIN_GROUP, POS)
add_word("pyramid", "пирамида", SUB_GROUP, MAIN_GROUP, POS)
add_word("prism", "призма", SUB_GROUP, MAIN_GROUP, POS)

plane; figure; surface; area; circle; polygon; triangle; square; rectangle;
SUB_GROUP = "Фигуры на плоскости • Plane Figures"
add_word("plane", "плоскость", SUB_GROUP, MAIN_GROUP, POS)
add_word("figure", "фигура", SUB_GROUP, MAIN_GROUP, POS)
add_word("surface", "поверхность", SUB_GROUP, MAIN_GROUP, POS)
add_word("area", "площадь", SUB_GROUP, MAIN_GROUP, POS)
add_word("circle", "окружность", SUB_GROUP, MAIN_GROUP, POS)
add_word("polygon", "многоугольник", SUB_GROUP, MAIN_GROUP, POS)
add_word("triangle", "треугольник", SUB_GROUP, MAIN_GROUP, POS)
add_word("square", "квадрат", SUB_GROUP, MAIN_GROUP, POS)
add_word("rectangle", "прямоугольник", SUB_GROUP, MAIN_GROUP, POS)

line; straight line; stripe; row; axis; level; limit; point;
SUB_GROUP = "Линии • Lines"
add_word("line", "линия", SUB_GROUP, MAIN_GROUP, POS)
add_word("straight line", "прямая линия", SUB_GROUP, MAIN_GROUP, POS)
add_word("stripe", "полоса", SUB_GROUP, MAIN_GROUP, POS)
add_word("row", "ряд", SUB_GROUP, MAIN_GROUP, POS)
add_word("axis", "ось", SUB_GROUP, MAIN_GROUP, POS)
add_word("level", "уровень", SUB_GROUP, MAIN_GROUP, POS)
add_word("limit", "граница", SUB_GROUP, MAIN_GROUP, POS)
add_word("point", "точка", SUB_GROUP, MAIN_GROUP, POS)

structure; whole; part; base; bottom; top; inside; side; flank; front; rear; back;
SUB_GROUP = "Структура • Structure"
add_word("structure", "структура", SUB_GROUP, MAIN_GROUP, POS)
add_word("whole", "целое", SUB_GROUP, MAIN_GROUP, POS)
add_word("part", "часть", SUB_GROUP, MAIN_GROUP, POS)
add_word("base", "основание", SUB_GROUP, MAIN_GROUP, POS)
add_word("bottom", "низ", SUB_GROUP, MAIN_GROUP, POS)
add_word("top", "верх", SUB_GROUP, MAIN_GROUP, POS)
add_word("inside", "внутри", SUB_GROUP, MAIN_GROUP, POS)
add_word("side", "сторона", SUB_GROUP, MAIN_GROUP, POS)
add_word("flank", "фланг", SUB_GROUP, MAIN_GROUP, POS)
add_word("front", "передняя часть", SUB_GROUP, MAIN_GROUP, POS)
add_word("rear", "задняя часть", SUB_GROUP, MAIN_GROUP, POS)
add_word("back", "задняя часть", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Время • Time"

second; minute; hour; day; week; month; year; decade; century; millennium; epoch; season; age; eternity; calendar; clock; watch; alarm clock;
SUB_GROUP = "Единицы времени • Time Units"
add_word("second", "секунда", SUB_GROUP, MAIN_GROUP, POS)
add_word("minute", "минута", SUB_GROUP, MAIN_GROUP, POS)
add_word("hour", "час", SUB_GROUP, MAIN_GROUP, POS)
add_word("day", "день", SUB_GROUP, MAIN_GROUP, POS)
add_word("week", "неделя", SUB_GROUP, MAIN_GROUP, POS)
add_word("month", "месяц", SUB_GROUP, MAIN_GROUP, POS)
add_word("year", "год", SUB_GROUP, MAIN_GROUP, POS)
add_word("decade", "десятилетие", SUB_GROUP, MAIN_GROUP, POS)
add_word("century", "век", SUB_GROUP, MAIN_GROUP, POS)
add_word("millennium", "тысячелетие", SUB_GROUP, MAIN_GROUP, POS)
add_word("epoch", "эпоха", SUB_GROUP, MAIN_GROUP, POS)
add_word("season", "сезон", SUB_GROUP, MAIN_GROUP, POS)
add_word("age", "эпоха", SUB_GROUP, MAIN_GROUP, POS)
add_word("eternity", "вечность", SUB_GROUP, MAIN_GROUP, POS)
add_word("calendar", "календарь", SUB_GROUP, MAIN_GROUP, POS)
add_word("clock", "часы", SUB_GROUP, MAIN_GROUP, POS)
add_word("watch", "наручные часы", SUB_GROUP, MAIN_GROUP, POS)
add_word("alarm clock", "будильник", SUB_GROUP, MAIN_GROUP, POS)

december; january; february; march; april; may; june; july; august; september; october; november;
SUB_GROUP = "Месяцы • Months"
add_word("december", "декабрь", SUB_GROUP, MAIN_GROUP, POS)
add_word("january", "январь", SUB_GROUP, MAIN_GROUP, POS)
add_word("february", "февраль", SUB_GROUP, MAIN_GROUP, POS)
add_word("march", "март", SUB_GROUP, MAIN_GROUP, POS)
add_word("april", "апрель", SUB_GROUP, MAIN_GROUP, POS)
add_word("may", "май", SUB_GROUP, MAIN_GROUP, POS)
add_word("june", "июнь", SUB_GROUP, MAIN_GROUP, POS)
add_word("july", "июль", SUB_GROUP, MAIN_GROUP, POS)
add_word("august", "август", SUB_GROUP, MAIN_GROUP, POS)
add_word("september", "сентябрь", SUB_GROUP, MAIN_GROUP, POS)
add_word("october", "октябрь", SUB_GROUP, MAIN_GROUP, POS)
add_word("november", "ноябрь", SUB_GROUP, MAIN_GROUP, POS)

monday; tuesday; wednesday; thursday; friday; saturday; sunday;
SUB_GROUP = "Дни Недели • Days of The Week"
add_word("monday", "понедельник", SUB_GROUP, MAIN_GROUP, POS)
add_word("tuesday", "вторник", SUB_GROUP, MAIN_GROUP, POS)
add_word("wednesday", "среда", SUB_GROUP, MAIN_GROUP, POS)
add_word("thursday", "четверг", SUB_GROUP, MAIN_GROUP, POS)
add_word("friday", "пятница", SUB_GROUP, MAIN_GROUP, POS)
add_word("saturday", "суббота", SUB_GROUP, MAIN_GROUP, POS)
add_word("sunday", "воскресенье", SUB_GROUP, MAIN_GROUP, POS)

morning; daybreak; dawn; sunrise; day; noon; afternoon; evening; sunset; night;
SUB_GROUP = "Стадии дня • Parts of Day"
add_word("morning", "утро", SUB_GROUP, MAIN_GROUP, POS)
add_word("daybreak", "рассвет", SUB_GROUP, MAIN_GROUP, POS)
add_word("dawn", "заря", SUB_GROUP, MAIN_GROUP, POS)
add_word("sunrise", "восход солнца", SUB_GROUP, MAIN_GROUP, POS)
add_word("day", "день", SUB_GROUP, MAIN_GROUP, POS)
add_word("noon", "полдень", SUB_GROUP, MAIN_GROUP, POS)
add_word("afternoon", "послеобеденное время", SUB_GROUP, MAIN_GROUP, POS)
add_word("evening", "вечер", SUB_GROUP, MAIN_GROUP, POS)
add_word("sunset", "закат", SUB_GROUP, MAIN_GROUP, POS)
add_word("night", "ночь", SUB_GROUP, MAIN_GROUP, POS)

working time; timetable; schedule; set time; delay; break; rest;
SUB_GROUP = "Рабочее время • Working Time"
add_word("working time", "рабочее время", SUB_GROUP, MAIN_GROUP, POS)
add_word("timetable", "расписание", SUB_GROUP, MAIN_GROUP, POS)
add_word("schedule", "график", SUB_GROUP, MAIN_GROUP, POS)
add_word("set time", "назначенное время", SUB_GROUP, MAIN_GROUP, POS)
add_word("delay", "задержка", SUB_GROUP, MAIN_GROUP, POS)
add_word("break", "перерыв", SUB_GROUP, MAIN_GROUP, POS)
add_word("rest", "отдых", SUB_GROUP, MAIN_GROUP, POS)

holiday; festival; anniversary; birthday; free time; vacation; leave; weekend; day off;
SUB_GROUP = "Праздник / Свободное Время • Holiday / Free Time"
add_word("holiday", "праздник", SUB_GROUP, MAIN_GROUP, POS)
add_word("festival", "фестиваль", SUB_GROUP, MAIN_GROUP, POS)
add_word("anniversary", "юбилей", SUB_GROUP, MAIN_GROUP, POS)
add_word("birthday", "день рождения", SUB_GROUP, MAIN_GROUP, POS)
add_word("free time", "свободное время", SUB_GROUP, MAIN_GROUP, POS)
add_word("vacation", "отпуск", SUB_GROUP, MAIN_GROUP, POS)
add_word("leave", "отгул", SUB_GROUP, MAIN_GROUP, POS)
add_word("weekend", "выходные", SUB_GROUP, MAIN_GROUP, POS)
add_word("day off", "выходной день", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Вещество / Материал • Substance / Material"

solid; liquid; solution; gas; vacuum;
SUB_GROUP = "Физическое Состояние • Physical State"
add_word("solid", "твердое тело", SUB_GROUP, MAIN_GROUP, POS)
add_word("liquid", "жидкость", SUB_GROUP, MAIN_GROUP, POS)
add_word("solution", "раствор", SUB_GROUP, MAIN_GROUP, POS)
add_word("gas", "газ", SUB_GROUP, MAIN_GROUP, POS)
add_word("vacuum", "вакуум", SUB_GROUP, MAIN_GROUP, POS)

metal; iron; alloy; steel; cast iron; bronze; copper; gold; silver; lead; tin; aluminum;
SUB_GROUP = "Металлы • Metals"
add_word("metal", "металл", SUB_GROUP, MAIN_GROUP, POS)
add_word("iron", "железо", SUB_GROUP, MAIN_GROUP, POS)
add_word("alloy", "сплав", SUB_GROUP, MAIN_GROUP, POS)
add_word("steel", "сталь", SUB_GROUP, MAIN_GROUP, POS)
add_word("cast iron", "чугун", SUB_GROUP, MAIN_GROUP, POS)
add_word("bronze", "бронза", SUB_GROUP, MAIN_GROUP, POS)
add_word("copper", "медь", SUB_GROUP, MAIN_GROUP, POS)
add_word("gold", "золото", SUB_GROUP, MAIN_GROUP, POS)
add_word("silver", "серебро", SUB_GROUP, MAIN_GROUP, POS)
add_word("lead", "свинец", SUB_GROUP, MAIN_GROUP, POS)
add_word("tin", "олово", SUB_GROUP, MAIN_GROUP, POS)
add_word("aluminum", "алюминий", SUB_GROUP, MAIN_GROUP, POS)

sand; stone; lime; clay; chalk; concrete; brick; cement; asphalt; wood; glass; paint; glue; rubber; plastic;
SUB_GROUP = "Строительные Материалы • Construction Materials"
add_word("sand", "песок", SUB_GROUP, MAIN_GROUP, POS)
add_word("stone", "камень", SUB_GROUP, MAIN_GROUP, POS)
add_word("lime", "известь", SUB_GROUP, MAIN_GROUP, POS)
add_word("clay", "глина", SUB_GROUP, MAIN_GROUP, POS)
add_word("chalk", "мел", SUB_GROUP, MAIN_GROUP, POS)
add_word("concrete", "бетон", SUB_GROUP, MAIN_GROUP, POS)
add_word("brick", "кирпич", SUB_GROUP, MAIN_GROUP, POS)
add_word("cement", "цемент", SUB_GROUP, MAIN_GROUP, POS)
add_word("asphalt", "асфальт", SUB_GROUP, MAIN_GROUP, POS)
add_word("wood", "дерево", SUB_GROUP, MAIN_GROUP, POS)
add_word("glass", "стекло", SUB_GROUP, MAIN_GROUP, POS)
add_word("paint", "краска", SUB_GROUP, MAIN_GROUP, POS)
add_word("glue", "клей", SUB_GROUP, MAIN_GROUP, POS)
add_word("rubber", "резина", SUB_GROUP, MAIN_GROUP, POS)
add_word("plastic", "пластик", SUB_GROUP, MAIN_GROUP, POS)

ore; oil; petroleum; gas; petrol; gasoline; coal;
SUB_GROUP = "Сырье • Raw Materials"
add_word("ore", "руда", SUB_GROUP, MAIN_GROUP, POS)
add_word("oil", "нефть", SUB_GROUP, MAIN_GROUP, POS)
add_word("petroleum", "нефть", SUB_GROUP, MAIN_GROUP, POS)
add_word("gas", "газ", SUB_GROUP, MAIN_GROUP, POS)
add_word("petrol", "бензин", SUB_GROUP, MAIN_GROUP, POS)
add_word("gasoline", "бензин", SUB_GROUP, MAIN_GROUP, POS)
add_word("coal", "уголь", SUB_GROUP, MAIN_GROUP, POS)

textile; cloth; fabric; silk; cotton; linen; wool; artificial fibre; nylon; leather; fur;
SUB_GROUP = "Ткани • Textiles"
add_word("textile", "ткань", SUB_GROUP, MAIN_GROUP, POS)
add_word("cloth", "ткань", SUB_GROUP, MAIN_GROUP, POS)
add_word("fabric", "материал", SUB_GROUP, MAIN_GROUP, POS)
add_word("silk", "шелк", SUB_GROUP, MAIN_GROUP, POS)
add_word("cotton", "хлопок", SUB_GROUP, MAIN_GROUP, POS)
add_word("linen", "лен", SUB_GROUP, MAIN_GROUP, POS)
add_word("wool", "шерсть", SUB_GROUP, MAIN_GROUP, POS)
add_word("artificial fibre", "искусственное волокно", SUB_GROUP, MAIN_GROUP, POS)
add_word("nylon", "нейлон", SUB_GROUP, MAIN_GROUP, POS)
add_word("leather", "кожа", SUB_GROUP, MAIN_GROUP, POS)
add_word("fur", "мех", SUB_GROUP, MAIN_GROUP, POS)

waste; waste paper; dust; dirt; garbage; rubbish; scrap metal;
SUB_GROUP = "Отходы • Waste"
add_word("waste", "отходы", SUB_GROUP, MAIN_GROUP, POS)
add_word("waste paper", "макулатура", SUB_GROUP, MAIN_GROUP, POS)
add_word("dust", "пыль", SUB_GROUP, MAIN_GROUP, POS)
add_word("dirt", "грязь", SUB_GROUP, MAIN_GROUP, POS)
add_word("garbage", "мусор", SUB_GROUP, MAIN_GROUP, POS)
add_word("rubbish", "мусор", SUB_GROUP, MAIN_GROUP, POS)
add_word("scrap metal", "лом металла", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Растения • Plants"

vegetable garden; vegetables; carrot; potato; pepper; cabbage; onion; beet; radish; cucumber; parsley; tomato; garlic; gourd;
SUB_GROUP = "Овощи • Vegetables"
add_word("vegetable garden", "огород", SUB_GROUP, MAIN_GROUP, POS)
add_word("vegetables", "овощи", SUB_GROUP, MAIN_GROUP, POS)
add_word("carrot", "морковь", SUB_GROUP, MAIN_GROUP, POS)
add_word("potato", "картофель", SUB_GROUP, MAIN_GROUP, POS)
add_word("pepper", "перец", SUB_GROUP, MAIN_GROUP, POS)
add_word("cabbage", "капуста", SUB_GROUP, MAIN_GROUP, POS)
add_word("onion", "лук", SUB_GROUP, MAIN_GROUP, POS)
add_word("beet", "свекла", SUB_GROUP, MAIN_GROUP, POS)
add_word("radish", "редис", SUB_GROUP, MAIN_GROUP, POS)
add_word("cucumber", "огурец", SUB_GROUP, MAIN_GROUP, POS)
add_word("parsley", "петрушка", SUB_GROUP, MAIN_GROUP, POS)
add_word("tomato", "помидор", SUB_GROUP, MAIN_GROUP, POS)
add_word("garlic", "чеснок", SUB_GROUP, MAIN_GROUP, POS)
add_word("gourd", "тыква", SUB_GROUP, MAIN_GROUP, POS)

melon; watermelon; fruit; berry; apple; pear; plum; apricot; banana; cherry; peach; grape; strawberry; raspberry; lemon; orange; tangerine; grapefruit;
SUB_GROUP = "Фрукты / Ягоды • Fruits / Berries"
add_word("melon", "дыня", SUB_GROUP, MAIN_GROUP, POS)
add_word("watermelon", "арбуз", SUB_GROUP, MAIN_GROUP, POS)
add_word("fruit", "фрукты", SUB_GROUP, MAIN_GROUP, POS)
add_word("berry", "ягода", SUB_GROUP, MAIN_GROUP, POS)
add_word("apple", "яблоко", SUB_GROUP, MAIN_GROUP, POS)
add_word("pear", "груша", SUB_GROUP, MAIN_GROUP, POS)
add_word("plum", "слива", SUB_GROUP, MAIN_GROUP, POS)
add_word("apricot", "абрикос", SUB_GROUP, MAIN_GROUP, POS)
add_word("banana", "банан", SUB_GROUP, MAIN_GROUP, POS)
add_word("cherry", "вишня", SUB_GROUP, MAIN_GROUP, POS)
add_word("peach", "персик", SUB_GROUP, MAIN_GROUP, POS)
add_word("grape", "виноград", SUB_GROUP, MAIN_GROUP, POS)
add_word("strawberry", "клубника", SUB_GROUP, MAIN_GROUP, POS)
add_word("raspberry", "малина", SUB_GROUP, MAIN_GROUP, POS)
add_word("lemon", "лимон", SUB_GROUP, MAIN_GROUP, POS)
add_word("orange", "апельсин", SUB_GROUP, MAIN_GROUP, POS)
add_word("tangerine", "мандарин", SUB_GROUP, MAIN_GROUP, POS)
add_word("grapefruit", "грейпфрут", SUB_GROUP, MAIN_GROUP, POS)

grain; cereal; wheat; rye; rice; oat; buckwheat; corn; maize;
SUB_GROUP = "Зерновые • Grains"
add_word("grain", "зерно", SUB_GROUP, MAIN_GROUP, POS)
add_word("cereal", "злак", SUB_GROUP, MAIN_GROUP, POS)
add_word("wheat", "пшеница", SUB_GROUP, MAIN_GROUP, POS)
add_word("rye", "рожь", SUB_GROUP, MAIN_GROUP, POS)
add_word("rice", "рис", SUB_GROUP, MAIN_GROUP, POS)
add_word("oat", "овёс", SUB_GROUP, MAIN_GROUP, POS)
add_word("buckwheat", "гречка", SUB_GROUP, MAIN_GROUP, POS)
add_word("corn", "кукуруза", SUB_GROUP, MAIN_GROUP, POS)
add_word("maize", "кукуруза", SUB_GROUP, MAIN_GROUP, POS)

fir; pine; birch; maple; poplar; oak; willow; chestnut; acacia; ash;
SUB_GROUP = "Деревья • Trees"
add_word("fir", "ель", SUB_GROUP, MAIN_GROUP, POS)
add_word("pine", "сосна", SUB_GROUP, MAIN_GROUP, POS)
add_word("birch", "берёза", SUB_GROUP, MAIN_GROUP, POS)
add_word("maple", "клён", SUB_GROUP, MAIN_GROUP, POS)
add_word("poplar", "тополь", SUB_GROUP, MAIN_GROUP, POS)
add_word("oak", "дуб", SUB_GROUP, MAIN_GROUP, POS)
add_word("willow", "ивa", SUB_GROUP, MAIN_GROUP, POS)
add_word("chestnut", "каштан", SUB_GROUP, MAIN_GROUP, POS)
add_word("acacia", "акация", SUB_GROUP, MAIN_GROUP, POS)
add_word("ash", "ясень", SUB_GROUP, MAIN_GROUP, POS)

root; trunk; branch; stump; leaf; bud; crown;
SUB_GROUP = "Части дерева • Parts of a Tree"
add_word("root", "корень", SUB_GROUP, MAIN_GROUP, POS)
add_word("trunk", "ствол", SUB_GROUP, MAIN_GROUP, POS)
add_word("branch", "ветка", SUB_GROUP, MAIN_GROUP, POS)
add_word("stump", "пень", SUB_GROUP, MAIN_GROUP, POS)
add_word("leaf", "лист", SUB_GROUP, MAIN_GROUP, POS)
add_word("bud", "почка", SUB_GROUP, MAIN_GROUP, POS)
add_word("crown", "крона", SUB_GROUP, MAIN_GROUP, POS)

rose; lily; tulip; lily of the valley; dandelion; daffodil;
SUB_GROUP = "Цветы • Flowers"
add_word("rose", "роза", SUB_GROUP, MAIN_GROUP, POS)
add_word("lily", "лилия", SUB_GROUP, MAIN_GROUP, POS)
add_word("tulip", "тюльпан", SUB_GROUP, MAIN_GROUP, POS)
add_word("lily of the valley", "ландыш", SUB_GROUP, MAIN_GROUP, POS)
add_word("dandelion", "одуванчик", SUB_GROUP, MAIN_GROUP, POS)
add_word("daffodil", "нарцисс", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Животные • Animals"

wolf; fox; bear; tiger; lion; elephant; ape; monkey; camel; rabbit; hare; rat; mouse
SUB_GROUP = "Дикие Животные • Wild Animals"
add_word("wolf", "волк", SUB_GROUP, MAIN_GROUP, POS)
add_word("fox", "лиса", SUB_GROUP, MAIN_GROUP, POS)
add_word("bear", "медведь", SUB_GROUP, MAIN_GROUP, POS)
add_word("tiger", "тигр", SUB_GROUP, MAIN_GROUP, POS)
add_word("lion", "лев", SUB_GROUP, MAIN_GROUP, POS)
add_word("elephant", "слон", SUB_GROUP, MAIN_GROUP, POS)
add_word("ape", "обезьяна", SUB_GROUP, MAIN_GROUP, POS)
add_word("monkey", "обезьяна", SUB_GROUP, MAIN_GROUP, POS)
add_word("camel", "верблюд", SUB_GROUP, MAIN_GROUP, POS)
add_word("rabbit", "кролик", SUB_GROUP, MAIN_GROUP, POS)
add_word("hare", "заяц", SUB_GROUP, MAIN_GROUP, POS)
add_word("rat", "крыса", SUB_GROUP, MAIN_GROUP, POS)
add_word("mouse", "мышь", SUB_GROUP, MAIN_GROUP, POS)

cow; bull; horse; goat; sheep; ram; donkey; mule; pig; cat; dog; calf; lamb; foal; piglet; kitten; puppy
SUB_GROUP = "Домашние Животные • Domestic Animals"
add_word("cow", "корова", SUB_GROUP, MAIN_GROUP, POS)
add_word("bull", "бык", SUB_GROUP, MAIN_GROUP, POS)
add_word("horse", "лошадь", SUB_GROUP, MAIN_GROUP, POS)
add_word("goat", "коза", SUB_GROUP, MAIN_GROUP, POS)
add_word("sheep", "овца", SUB_GROUP, MAIN_GROUP, POS)
add_word("ram", "баран", SUB_GROUP, MAIN_GROUP, POS)
add_word("donkey", "осёл", SUB_GROUP, MAIN_GROUP, POS)
add_word("mule", "мул", SUB_GROUP, MAIN_GROUP, POS)
add_word("pig", "свинья", SUB_GROUP, MAIN_GROUP, POS)
add_word("cat", "кот", SUB_GROUP, MAIN_GROUP, POS)
add_word("dog", "собака", SUB_GROUP, MAIN_GROUP, POS)
add_word("calf", "теленок", SUB_GROUP, MAIN_GROUP, POS)
add_word("lamb", "ягнёнок", SUB_GROUP, MAIN_GROUP, POS)
add_word("foal", "жеребёнок", SUB_GROUP, MAIN_GROUP, POS)
add_word("piglet", "поросёнок", SUB_GROUP, MAIN_GROUP, POS)
add_word("kitten", "котёнок", SUB_GROUP, MAIN_GROUP, POS)
add_word("puppy", "щенок", SUB_GROUP, MAIN_GROUP, POS)

hen; cock; chick; goose; duck; turkey; crow; sparrow; pigeon; owl; parrot; swan; eagle;
SUB_GROUP = "Птицы Начального Уровня • Birds Beginner Level"
add_word("hen", "курица", SUB_GROUP, MAIN_GROUP, POS)
add_word("cock", "петух", SUB_GROUP, MAIN_GROUP, POS)
add_word("chick", "цыплёнок", SUB_GROUP, MAIN_GROUP, POS)
add_word("goose", "гусь", SUB_GROUP, MAIN_GROUP, POS)
add_word("duck", "утка", SUB_GROUP, MAIN_GROUP, POS)
add_word("turkey", "индюк", SUB_GROUP, MAIN_GROUP, POS)
add_word("crow", "ворона", SUB_GROUP, MAIN_GROUP, POS)
add_word("sparrow", "воробей", SUB_GROUP, MAIN_GROUP, POS)
add_word("pigeon", "голубь", SUB_GROUP, MAIN_GROUP, POS)
add_word("owl", "сова", SUB_GROUP, MAIN_GROUP, POS)
add_word("parrot", "попугай", SUB_GROUP, MAIN_GROUP, POS)
add_word("swan", "лебедь", SUB_GROUP, MAIN_GROUP, POS)
add_word("eagle", "орёл", SUB_GROUP, MAIN_GROUP, POS)

gander; duckling; hawk; nightingale; crane; stork; nestling; magpie;
SUB_GROUP = "Птицы Продвинутого Уровня • Birds Advanced Level"
add_word("gander", "гусак", SUB_GROUP, MAIN_GROUP, POS)
add_word("duckling", "утёнок", SUB_GROUP, MAIN_GROUP, POS)
add_word("hawk", "ястреб", SUB_GROUP, MAIN_GROUP, POS)
add_word("nightingale", "соловей", SUB_GROUP, MAIN_GROUP, POS)
add_word("crane", "журавль", SUB_GROUP, MAIN_GROUP, POS)
add_word("stork", "аист", SUB_GROUP, MAIN_GROUP, POS)
add_word("nestling", "птенец", SUB_GROUP, MAIN_GROUP, POS)
add_word("magpie", "сорока", SUB_GROUP, MAIN_GROUP, POS)

fish; cod; salmon; carp; shark; spawn;
SUB_GROUP = "Рыба Начального Уровня • Fish Beginner Level"
add_word("fish", "рыба", SUB_GROUP, MAIN_GROUP, POS)
add_word("cod", "треска", SUB_GROUP, MAIN_GROUP, POS)
add_word("salmon", "лосось", SUB_GROUP, MAIN_GROUP, POS)
add_word("carp", "карп", SUB_GROUP, MAIN_GROUP, POS)
add_word("shark", "акула", SUB_GROUP, MAIN_GROUP, POS)
add_word("spawn", "икра", SUB_GROUP, MAIN_GROUP, POS)

crucian carp; sturgeon; flatfish; catfish; herring; roach; pike;
SUB_GROUP = "Рыба Продвинутого Уровня • Fish Advanced Level"
add_word("crucian carp", "карась", SUB_GROUP, MAIN_GROUP, POS)
add_word("sturgeon", "осётр", SUB_GROUP, MAIN_GROUP, POS)
add_word("flatfish", "камбала", SUB_GROUP, MAIN_GROUP, POS)
add_word("catfish", "сом", SUB_GROUP, MAIN_GROUP, POS)
add_word("herring", "селёдка", SUB_GROUP, MAIN_GROUP, POS)
add_word("roach", "плотва", SUB_GROUP, MAIN_GROUP, POS)
add_word("pike", "щука", SUB_GROUP, MAIN_GROUP, POS)

insect; fly; bee; wasp; butterfly; caterpillar; ant; spider; cockroach; bug; aphid; louse; grasshopper; cricket;
SUB_GROUP = "Насекомые • Insects"
add_word("insect", "насекомое", SUB_GROUP, MAIN_GROUP, POS)
add_word("fly", "муха", SUB_GROUP, MAIN_GROUP, POS)
add_word("bee", "пчела", SUB_GROUP, MAIN_GROUP, POS)
add_word("wasp", "оса", SUB_GROUP, MAIN_GROUP, POS)
add_word("butterfly", "бабочка", SUB_GROUP, MAIN_GROUP, POS)
add_word("caterpillar", "гусеница", SUB_GROUP, MAIN_GROUP, POS)
add_word("ant", "муравей", SUB_GROUP, MAIN_GROUP, POS)
add_word("spider", "паук", SUB_GROUP, MAIN_GROUP, POS)
add_word("cockroach", "таракан", SUB_GROUP, MAIN_GROUP, POS)
add_word("bug", "клоп", SUB_GROUP, MAIN_GROUP, POS)
add_word("aphid", "тля", SUB_GROUP, MAIN_GROUP, POS)
add_word("louse", "вошь", SUB_GROUP, MAIN_GROUP, POS)
add_word("grasshopper", "кузнечик", SUB_GROUP, MAIN_GROUP, POS)
add_word("cricket", "сверчок", SUB_GROUP, MAIN_GROUP, POS)

reptile; frog; toad; snake; viper; grass snake; tortoise; turtle; lizard; crocodile
SUB_GROUP = "Остальные Классы • Other Groups"
add_word("reptile", "рептилия", SUB_GROUP, MAIN_GROUP, POS)
add_word("frog", "лягушка", SUB_GROUP, MAIN_GROUP, POS)
add_word("toad", "жаба", SUB_GROUP, MAIN_GROUP, POS)
add_word("snake", "змея", SUB_GROUP, MAIN_GROUP, POS)
add_word("viper", "гадюка", SUB_GROUP, MAIN_GROUP, POS)
add_word("grass snake", "урюк", SUB_GROUP, MAIN_GROUP, POS)
add_word("tortoise", "сухопутная черепаха", SUB_GROUP, MAIN_GROUP, POS)
add_word("turtle", "водная черепаха", SUB_GROUP, MAIN_GROUP, POS)
add_word("lizard", "ящерица", SUB_GROUP, MAIN_GROUP, POS)
add_word("crocodile", "крокодил", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Человек • Human"

man; male; woman; female; age; childhood; youth; baby; child; teenager; birthday; surname; origin
SUB_GROUP = "Общие Сведения • General Information"
add_word("man", "мужчина", SUB_GROUP, MAIN_GROUP, POS)
add_word("male", "мужчина", SUB_GROUP, MAIN_GROUP, POS)
add_word("woman", "женщина", SUB_GROUP, MAIN_GROUP, POS)
add_word("female", "женщина", SUB_GROUP, MAIN_GROUP, POS)
add_word("age", "возраст", SUB_GROUP, MAIN_GROUP, POS)
add_word("childhood", "детство", SUB_GROUP, MAIN_GROUP, POS)
add_word("youth", "юность", SUB_GROUP, MAIN_GROUP, POS)
add_word("baby", "младенец", SUB_GROUP, MAIN_GROUP, POS)
add_word("child", "ребёнок", SUB_GROUP, MAIN_GROUP, POS)
add_word("teenager", "подросток", SUB_GROUP, MAIN_GROUP, POS)
add_word("birthday", "день рождения", SUB_GROUP, MAIN_GROUP, POS)
add_word("surname", "фамилия", SUB_GROUP, MAIN_GROUP, POS)
add_word("origin", "происхождение", SUB_GROUP, MAIN_GROUP, POS)

stature; bone; muscle; nerve; skin; hair; blood; artery; vein
SUB_GROUP = "Анатомия: Общая группа • Anatomy: General"
add_word("stature", "телосложение", SUB_GROUP, MAIN_GROUP, POS)
add_word("bone", "кость", SUB_GROUP, MAIN_GROUP, POS)
add_word("muscle", "мышца", SUB_GROUP, MAIN_GROUP, POS)
add_word("nerve", "нерв", SUB_GROUP, MAIN_GROUP, POS)
add_word("skin", "кожа", SUB_GROUP, MAIN_GROUP, POS)
add_word("hair", "волосы", SUB_GROUP, MAIN_GROUP, POS)
add_word("blood", "кровь", SUB_GROUP, MAIN_GROUP, POS)
add_word("artery", "артерия", SUB_GROUP, MAIN_GROUP, POS)
add_word("vein", "вена", SUB_GROUP, MAIN_GROUP, POS)


body; head; neck; chest; back; belly; waist; leg; foot; toe; knee; heel; hip; arm; hand; finger; elbow; nail
SUB_GROUP = "Анатомия: Части тела • Anatomy: Parts of Body"
add_word("body", "тело", SUB_GROUP, MAIN_GROUP, POS)
add_word("head", "голова", SUB_GROUP, MAIN_GROUP, POS)
add_word("neck", "шея", SUB_GROUP, MAIN_GROUP, POS)
add_word("chest", "грудь", SUB_GROUP, MAIN_GROUP, POS)
add_word("back", "спина", SUB_GROUP, MAIN_GROUP, POS)
add_word("belly", "живот", SUB_GROUP, MAIN_GROUP, POS)
add_word("waist", "талия", SUB_GROUP, MAIN_GROUP, POS)
add_word("leg", "нога", SUB_GROUP, MAIN_GROUP, POS)
add_word("foot", "стопа", SUB_GROUP, MAIN_GROUP, POS)
add_word("toe", "палец ноги", SUB_GROUP, MAIN_GROUP, POS)
add_word("knee", "колено", SUB_GROUP, MAIN_GROUP, POS)
add_word("heel", "пятка", SUB_GROUP, MAIN_GROUP, POS)
add_word("hip", "бедро", SUB_GROUP, MAIN_GROUP, POS)
add_word("arm", "рука", SUB_GROUP, MAIN_GROUP, POS)
add_word("hand", "кисть", SUB_GROUP, MAIN_GROUP, POS)
add_word("finger", "палец руки", SUB_GROUP, MAIN_GROUP, POS)
add_word("elbow", "локоть", SUB_GROUP, MAIN_GROUP, POS)
add_word("nail", "ноготь", SUB_GROUP, MAIN_GROUP, POS)

head; eye; eyelid; eyelash; eyebrow; ear; mouth; lip; tooth; tongue; face; nose; chin; jaw; forehead; cheek
SUB_GROUP = "Анатомия: Лицо • Anatomy: Face"
add_word("head", "голова", SUB_GROUP, MAIN_GROUP, POS)
add_word("eye", "глаз", SUB_GROUP, MAIN_GROUP, POS)
add_word("eyelid", "веко", SUB_GROUP, MAIN_GROUP, POS)
add_word("eyelash", "ресница", SUB_GROUP, MAIN_GROUP, POS)
add_word("eyebrow", "бровь", SUB_GROUP, MAIN_GROUP, POS)
add_word("ear", "ухо", SUB_GROUP, MAIN_GROUP, POS)
add_word("mouth", "рот", SUB_GROUP, MAIN_GROUP, POS)
add_word("lip", "губа", SUB_GROUP, MAIN_GROUP, POS)
add_word("tooth", "зуб", SUB_GROUP, MAIN_GROUP, POS)
add_word("tongue", "язык", SUB_GROUP, MAIN_GROUP, POS)
add_word("face", "лицо", SUB_GROUP, MAIN_GROUP, POS)
add_word("nose", "нос", SUB_GROUP, MAIN_GROUP, POS)
add_word("chin", "подбородок", SUB_GROUP, MAIN_GROUP, POS)
add_word("jaw", "челюсть", SUB_GROUP, MAIN_GROUP, POS)
add_word("forehead", "лоб", SUB_GROUP, MAIN_GROUP, POS)
add_word("cheek", "щека", SUB_GROUP, MAIN_GROUP, POS)

brain; lungs; heart; stomach; gut; liver; kidney
SUB_GROUP = "Анатомия: Внутренние органы • Anatomy: Internal organs"
add_word("brain", "мозг", SUB_GROUP, MAIN_GROUP, POS)
add_word("lungs", "легкие", SUB_GROUP, MAIN_GROUP, POS)
add_word("heart", "сердце", SUB_GROUP, MAIN_GROUP, POS)
add_word("stomach", "желудок", SUB_GROUP, MAIN_GROUP, POS)
add_word("gut", "кишка", SUB_GROUP, MAIN_GROUP, POS)
add_word("liver", "печень", SUB_GROUP, MAIN_GROUP, POS)
add_word("kidney", "почка", SUB_GROUP, MAIN_GROUP, POS)

father; mother; sister; brother; grandmother; grandfather; child; son; daughter; husband; wife; wedding; divorce
SUB_GROUP = "Семья • Family"
add_word("father", "отец", SUB_GROUP, MAIN_GROUP, POS)
add_word("mother", "мать", SUB_GROUP, MAIN_GROUP, POS)
add_word("sister", "сестра", SUB_GROUP, MAIN_GROUP, POS)
add_word("brother", "брат", SUB_GROUP, MAIN_GROUP, POS)
add_word("grandmother", "бабушка", SUB_GROUP, MAIN_GROUP, POS)
add_word("grandfather", "дедушка", SUB_GROUP, MAIN_GROUP, POS)
add_word("child", "ребенок", SUB_GROUP, MAIN_GROUP, POS)
add_word("son", "сын", SUB_GROUP, MAIN_GROUP, POS)
add_word("daughter", "дочь", SUB_GROUP, MAIN_GROUP, POS)
add_word("husband", "муж", SUB_GROUP, MAIN_GROUP, POS)
add_word("wife", "жена", SUB_GROUP, MAIN_GROUP, POS)
add_word("wedding", "свадьба", SUB_GROUP, MAIN_GROUP, POS)
add_word("divorce", "развод", SUB_GROUP, MAIN_GROUP, POS)

friend; colleague; lover; widow; relatives; ancestor; uncle; aunt; nephew; niece; cousin
SUB_GROUP = "Отношения между Людьми • Human Relationships"
add_word("friend", "друг", SUB_GROUP, MAIN_GROUP, POS)
add_word("colleague", "коллега", SUB_GROUP, MAIN_GROUP, POS)
add_word("lover", "любовник", SUB_GROUP, MAIN_GROUP, POS)
add_word("widow", "вдова", SUB_GROUP, MAIN_GROUP, POS)
add_word("relatives", "родственники", SUB_GROUP, MAIN_GROUP, POS)
add_word("ancestor", "предок", SUB_GROUP, MAIN_GROUP, POS)
add_word("uncle", "дядя", SUB_GROUP, MAIN_GROUP, POS)
add_word("aunt", "тётя", SUB_GROUP, MAIN_GROUP, POS)
add_word("nephew", "племянник", SUB_GROUP, MAIN_GROUP, POS)
add_word("niece", "племянница", SUB_GROUP, MAIN_GROUP, POS)
add_word("cousin", "двоюродный брат/сестра", SUB_GROUP, MAIN_GROUP, POS)



MAIN_GROUP = "Жилье • Dwelling"

house; building; apartment; flat; floor; yard; gate; fence; address; street; square
SUB_GROUP = "Дом • House"
add_word("house", "дом", SUB_GROUP, MAIN_GROUP, POS)
add_word("building", "здание", SUB_GROUP, MAIN_GROUP, POS)
add_word("apartment", "квартира", SUB_GROUP, MAIN_GROUP, POS)
add_word("flat", "квартира", SUB_GROUP, MAIN_GROUP, POS)
add_word("floor", "этаж", SUB_GROUP, MAIN_GROUP, POS)
add_word("yard", "двор", SUB_GROUP, MAIN_GROUP, POS)
add_word("gate", "ворота", SUB_GROUP, MAIN_GROUP, POS)
add_word("fence", "забор", SUB_GROUP, MAIN_GROUP, POS)
add_word("address", "адрес", SUB_GROUP, MAIN_GROUP, POS)
add_word("street", "улица", SUB_GROUP, MAIN_GROUP, POS)
add_word("square", "площадь", SUB_GROUP, MAIN_GROUP, POS)

roof; chimney; wall; floor; ceiling; window; corner; door; bell; lock; key; tap; faucet; light; switch; electricity; elevator
SUB_GROUP = "Устройство Дома • House Layout"
add_word("roof", "крыша", SUB_GROUP, MAIN_GROUP, POS)
add_word("chimney", "дымоход", SUB_GROUP, MAIN_GROUP, POS)
add_word("wall", "стена", SUB_GROUP, MAIN_GROUP, POS)
add_word("floor", "пол", SUB_GROUP, MAIN_GROUP, POS)
add_word("ceiling", "потолок", SUB_GROUP, MAIN_GROUP, POS)
add_word("window", "окно", SUB_GROUP, MAIN_GROUP, POS)
add_word("corner", "угол", SUB_GROUP, MAIN_GROUP, POS)
add_word("door", "дверь", SUB_GROUP, MAIN_GROUP, POS)
add_word("bell", "звонок", SUB_GROUP, MAIN_GROUP, POS)
add_word("lock", "замок", SUB_GROUP, MAIN_GROUP, POS)
add_word("key", "ключ", SUB_GROUP, MAIN_GROUP, POS)
add_word("tap", "кран", SUB_GROUP, MAIN_GROUP, POS)
add_word("faucet", "водопроводный кран", SUB_GROUP, MAIN_GROUP, POS)
add_word("light", "свет", SUB_GROUP, MAIN_GROUP, POS)
add_word("switch", "выключатель", SUB_GROUP, MAIN_GROUP, POS)
add_word("electricity", "электричество", SUB_GROUP, MAIN_GROUP, POS)
add_word("elevator", "лифт", SUB_GROUP, MAIN_GROUP, POS)

kitchen; bathroom; toilet; corridor; living room; hall; bedroom; dining room; study
SUB_GROUP = "Комнаты • Rooms"
add_word("kitchen", "кухня", SUB_GROUP, MAIN_GROUP, POS)
add_word("bathroom", "ванная", SUB_GROUP, MAIN_GROUP, POS)
add_word("toilet", "туалет", SUB_GROUP, MAIN_GROUP, POS)
add_word("corridor", "коридор", SUB_GROUP, MAIN_GROUP, POS)
add_word("living room", "гостиная", SUB_GROUP, MAIN_GROUP, POS)
add_word("hall", "холл", SUB_GROUP, MAIN_GROUP, POS)
add_word("bedroom", "спальня", SUB_GROUP, MAIN_GROUP, POS)
add_word("dining room", "столовая", SUB_GROUP, MAIN_GROUP, POS)
add_word("study", "кабинет", SUB_GROUP, MAIN_GROUP, POS)

furniture; table; chair; armchair; bed; sofa; wardrobe; cupboard; bookcase; carpet; mirror; blinds; curtain; coat rack
SUB_GROUP = "Мебель • Furniture"
add_word("furniture", "мебель", SUB_GROUP, MAIN_GROUP, POS)
add_word("table", "стол", SUB_GROUP, MAIN_GROUP, POS)
add_word("chair", "стул", SUB_GROUP, MAIN_GROUP, POS)
add_word("armchair", "кресло", SUB_GROUP, MAIN_GROUP, POS)
add_word("bed", "кровать", SUB_GROUP, MAIN_GROUP, POS)
add_word("sofa", "диван", SUB_GROUP, MAIN_GROUP, POS)
add_word("wardrobe", "шкаф", SUB_GROUP, MAIN_GROUP, POS)
add_word("cupboard", "буфет", SUB_GROUP, MAIN_GROUP, POS)
add_word("bookcase", "книжный шкаф", SUB_GROUP, MAIN_GROUP, POS)
add_word("carpet", "ковер", SUB_GROUP, MAIN_GROUP, POS)
add_word("mirror", "зеркало", SUB_GROUP, MAIN_GROUP, POS)
add_word("blinds", "жалюзи", SUB_GROUP, MAIN_GROUP, POS)
add_word("curtain", "занавеска", SUB_GROUP, MAIN_GROUP, POS)
add_word("coat rack", "вешалка", SUB_GROUP, MAIN_GROUP, POS)

bedclothes; sheet; pillowcase; blanket; pillow; mattress; bedspread
SUB_GROUP = "Кровать • Bed"
add_word("bedclothes", "постельное белье", SUB_GROUP, MAIN_GROUP, POS)
add_word("sheet", "простыня", SUB_GROUP, MAIN_GROUP, POS)
add_word("pillowcase", "наволочка", SUB_GROUP, MAIN_GROUP, POS)
add_word("blanket", "одеяло", SUB_GROUP, MAIN_GROUP, POS)
add_word("pillow", "подушка", SUB_GROUP, MAIN_GROUP, POS)
add_word("mattress", "матрас", SUB_GROUP, MAIN_GROUP, POS)
add_word("bedspread", "покрывало", SUB_GROUP, MAIN_GROUP, POS)

container; bag; suitcase; barrel; case; basket; sack; box; backpack; vessel; bucket; vase; can; jar; jug
SUB_GROUP = "Сосуды / Емкости • Vessels / Containers"
add_word("container", "контейнер", SUB_GROUP, MAIN_GROUP, POS)
add_word("bag", "сумка", SUB_GROUP, MAIN_GROUP, POS)
add_word("suitcase", "чемодан", SUB_GROUP, MAIN_GROUP, POS)
add_word("barrel", "бочка", SUB_GROUP, MAIN_GROUP, POS)
add_word("case", "чехол", SUB_GROUP, MAIN_GROUP, POS)
add_word("basket", "корзина", SUB_GROUP, MAIN_GROUP, POS)
add_word("sack", "мешок", SUB_GROUP, MAIN_GROUP, POS)
add_word("box", "ящик", SUB_GROUP, MAIN_GROUP, POS)
add_word("backpack", "рюкзак", SUB_GROUP, MAIN_GROUP, POS)
add_word("vessel", "сосуд", SUB_GROUP, MAIN_GROUP, POS)
add_word("bucket", "ведро", SUB_GROUP, MAIN_GROUP, POS)
add_word("vase", "ваза", SUB_GROUP, MAIN_GROUP, POS)
add_word("can", "банка", SUB_GROUP, MAIN_GROUP, POS)
add_word("jar", "кувшин", SUB_GROUP, MAIN_GROUP, POS)
add_word("jug", "кувшин", SUB_GROUP, MAIN_GROUP, POS)

iron; vacuum cleaner; refrigerator; fridge; washing machine; sewing machine; mixer; cooker; stove; range; utensils; broom
SUB_GROUP = "Бытовые приборы • Household Appliances"
add_word("iron", "утюг", SUB_GROUP, MAIN_GROUP, POS)
add_word("vacuum cleaner", "пылесос", SUB_GROUP, MAIN_GROUP, POS)
add_word("refrigerator", "холодильник", SUB_GROUP, MAIN_GROUP, POS)
add_word("fridge", "холодильник", SUB_GROUP, MAIN_GROUP, POS)
add_word("washing machine", "стиральная машина", SUB_GROUP, MAIN_GROUP, POS)
add_word("sewing machine", "швейная машина", SUB_GROUP, MAIN_GROUP, POS)
add_word("mixer", "миксер", SUB_GROUP, MAIN_GROUP, POS)
add_word("cooker", "кухонная плита", SUB_GROUP, MAIN_GROUP, POS)
add_word("stove", "печь", SUB_GROUP, MAIN_GROUP, POS)
add_word("range", "диапазон", SUB_GROUP, MAIN_GROUP, POS)
add_word("utensils", "кухонные принадлежности", SUB_GROUP, MAIN_GROUP, POS)
add_word("broom", "метла", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Одежда • Clothes"



coat; raincoat; fur coat; casual wear; suit; jacket; vest; shirt; trousers – pants; jeans; dress; blouse; skirt; underwear; bra; panties; nightgown; pyjamas; socks; stockings; tights;
SUB_GROUP = "Одежда / Белье • Clothes / Underwear"
add_word("coat", "пальто", SUB_GROUP, MAIN_GROUP, POS)
add_word("raincoat", "дождевик", SUB_GROUP, MAIN_GROUP, POS)
add_word("fur coat", "шуба", SUB_GROUP, MAIN_GROUP, POS)
add_word("casual wear", "повседневная одежда", SUB_GROUP, MAIN_GROUP, POS)
add_word("suit", "костюм", SUB_GROUP, MAIN_GROUP, POS)
add_word("jacket", "куртка", SUB_GROUP, MAIN_GROUP, POS)
add_word("vest", "жилет", SUB_GROUP, MAIN_GROUP, POS)
add_word("shirt", "рубашка", SUB_GROUP, MAIN_GROUP, POS)
add_word("trousers", "штаны", SUB_GROUP, MAIN_GROUP, POS)
add_word("pants", "штаны", SUB_GROUP, MAIN_GROUP, POS)
add_word("jeans", "джинсы", SUB_GROUP, MAIN_GROUP, POS)
add_word("dress", "платье", SUB_GROUP, MAIN_GROUP, POS)
add_word("blouse", "блузка", SUB_GROUP, MAIN_GROUP, POS)
add_word("skirt", "юбка", SUB_GROUP, MAIN_GROUP, POS)
add_word("underwear", "нижнее белье", SUB_GROUP, MAIN_GROUP, POS)
add_word("bra", "лифчик", SUB_GROUP, MAIN_GROUP, POS)
add_word("panties", "трусы", SUB_GROUP, MAIN_GROUP, POS)
add_word("pyjamas", "пижама", SUB_GROUP, MAIN_GROUP, POS)
add_word("socks", "носки", SUB_GROUP, MAIN_GROUP, POS)
add_word("tights", "колготки", SUB_GROUP, MAIN_GROUP, POS)

footwear; shoe; boot; sandal; slippers; trainers; shoelace; shoe polish;
SUB_GROUP = "Обувь • Footwear"
add_word("footwear", "обувь", SUB_GROUP, MAIN_GROUP, POS)
add_word("shoe", "туфля", SUB_GROUP, MAIN_GROUP, POS)
add_word("boot", "ботинок", SUB_GROUP, MAIN_GROUP, POS)
add_word("sandal", "сандалия", SUB_GROUP, MAIN_GROUP, POS)
add_word("slippers", "тапочки", SUB_GROUP, MAIN_GROUP, POS)
add_word("trainers", "кроссовки", SUB_GROUP, MAIN_GROUP, POS)
add_word("shoelace", "шнурок", SUB_GROUP, MAIN_GROUP, POS)
add_word("shoe polish", "краска для обуви", SUB_GROUP, MAIN_GROUP, POS)


headgear; hat; cap; beret; kerchief; shawl;
SUB_GROUP = "Головные уборы • Headgear"
add_word("headgear", "головной убор", SUB_GROUP, MAIN_GROUP, POS)
add_word("hat", "шляпа", SUB_GROUP, MAIN_GROUP, POS)
add_word("cap", "кепка", SUB_GROUP, MAIN_GROUP, POS)
add_word("beret", "берет", SUB_GROUP, MAIN_GROUP, POS)
add_word("kerchief", "платок", SUB_GROUP, MAIN_GROUP, POS)
add_word("shawl", "шаль", SUB_GROUP, MAIN_GROUP, POS)

sleeve; collar; cuff; button; zip; belt; hook; buckle; tie; bow tie; cravat; scarf; gloves; umbrella; handkerchief; handbag; wallet; purse;
SUB_GROUP = "Аксессуары и части одежды • Accessories and Clothing Parts"
add_word("sleeve", "рукав", SUB_GROUP, MAIN_GROUP, POS)
add_word("collar", "воротник", SUB_GROUP, MAIN_GROUP, POS)
add_word("cuff", "манжета", SUB_GROUP, MAIN_GROUP, POS)
add_word("button", "пуговица", SUB_GROUP, MAIN_GROUP, POS)
add_word("zip", "молния", SUB_GROUP, MAIN_GROUP, POS)
add_word("belt", "ремень", SUB_GROUP, MAIN_GROUP, POS)
add_word("hook", "крючок", SUB_GROUP, MAIN_GROUP, POS)
add_word("buckle", "пряжка", SUB_GROUP, MAIN_GROUP, POS)
add_word("tie", "галстук", SUB_GROUP, MAIN_GROUP, POS)
add_word("bow tie", "бабочка", SUB_GROUP, MAIN_GROUP, POS)
add_word("cravat", "шарф", SUB_GROUP, MAIN_GROUP, POS)
add_word("scarf", "шарф", SUB_GROUP, MAIN_GROUP, POS)
add_word("gloves", "перчатки", SUB_GROUP, MAIN_GROUP, POS)
add_word("umbrella", "зонт", SUB_GROUP, MAIN_GROUP, POS)
add_word("handkerchief", "носовой платок", SUB_GROUP, MAIN_GROUP, POS)
add_word("handbag", "сумочка", SUB_GROUP, MAIN_GROUP, POS)
add_word("wallet", "бумажник", SUB_GROUP, MAIN_GROUP, POS)
add_word("purse", "кошелёк", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Питание • Nourishment"

meal; breakfast; lunch; dinner; tea; supper; taste; appetite;
SUB_GROUP = "Прием Пищи • Eating"
add_word("meal", "еда", SUB_GROUP, MAIN_GROUP, POS)
add_word("breakfast", "завтрак", SUB_GROUP, MAIN_GROUP, POS)
add_word("lunch", "ланч", SUB_GROUP, MAIN_GROUP, POS)
add_word("dinner", "ужин", SUB_GROUP, MAIN_GROUP, POS)
add_word("tea", "полдник", SUB_GROUP, MAIN_GROUP, POS)
add_word("supper", "ужин", SUB_GROUP, MAIN_GROUP, POS)
add_word("taste", "вкус", SUB_GROUP, MAIN_GROUP, POS)
add_word("appetite", "аппетит", SUB_GROUP, MAIN_GROUP, POS)

the first course; the second course; dessert; soup; garnish; porridge; noodles; macaroni; fried potatoes; mashed potatoes; boiled egg; fried eggs; beefsteak; meat; beef; pork; mutton; veal; poultry;
SUB_GROUP = "Блюда • Dishes"
add_word("the first course", "первое блюдо", SUB_GROUP, MAIN_GROUP, POS)
add_word("the second course", "второе блюдо", SUB_GROUP, MAIN_GROUP, POS)
add_word("dessert", "десерт", SUB_GROUP, MAIN_GROUP, POS)
add_word("soup", "суп", SUB_GROUP, MAIN_GROUP, POS)
add_word("garnish", "гарнир", SUB_GROUP, MAIN_GROUP, POS)
add_word("porridge", "каша", SUB_GROUP, MAIN_GROUP, POS)
add_word("noodles", "лапша", SUB_GROUP, MAIN_GROUP, POS)
add_word("macaroni", "макароны", SUB_GROUP, MAIN_GROUP, POS)
add_word("fried potatoes", "жареная картошка", SUB_GROUP, MAIN_GROUP, POS)
add_word("mashed potatoes", "пюре", SUB_GROUP, MAIN_GROUP, POS)
add_word("boiled egg", "варёное яйцо", SUB_GROUP, MAIN_GROUP, POS)
add_word("fried eggs", "яичница", SUB_GROUP, MAIN_GROUP, POS)
add_word("beefsteak", "бифштекс", SUB_GROUP, MAIN_GROUP, POS)
add_word("meat", "мясо", SUB_GROUP, MAIN_GROUP, POS)
add_word("beef", "говядина", SUB_GROUP, MAIN_GROUP, POS)
add_word("pork", "свинина", SUB_GROUP, MAIN_GROUP, POS)
add_word("mutton", "баранина", SUB_GROUP, MAIN_GROUP, POS)
add_word("veal", "телятина", SUB_GROUP, MAIN_GROUP, POS)
add_word("poultry", "птица", SUB_GROUP, MAIN_GROUP, POS)

mustard; vinegar; pepper; salt; spice; herb;
SUB_GROUP = "Приправы • Condiments"
add_word("mustard", "горчица", SUB_GROUP, MAIN_GROUP, POS)
add_word("vinegar", "уксус", SUB_GROUP, MAIN_GROUP, POS)
add_word("pepper", "перец", SUB_GROUP, MAIN_GROUP, POS)
add_word("salt", "соль", SUB_GROUP, MAIN_GROUP, POS)
add_word("spice", "специя", SUB_GROUP, MAIN_GROUP, POS)
add_word("herb", "трава", SUB_GROUP, MAIN_GROUP, POS)

drink; tea; coffee; cocoa; milk; juice; mineral water; lemonade; cola; wine; beer; whisky;
SUB_GROUP = "Напитки • Drinks and Beverages"
add_word("drink", "напиток", SUB_GROUP, MAIN_GROUP, POS)
add_word("tea", "чай", SUB_GROUP, MAIN_GROUP, POS)
add_word("coffee", "кофе", SUB_GROUP, MAIN_GROUP, POS)
add_word("cocoa", "какао", SUB_GROUP, MAIN_GROUP, POS)
add_word("milk", "молоко", SUB_GROUP, MAIN_GROUP, POS)
add_word("juice", "сок", SUB_GROUP, MAIN_GROUP, POS)
add_word("mineral water", "минеральная вода", SUB_GROUP, MAIN_GROUP, POS)
add_word("lemonade", "лимонад", SUB_GROUP, MAIN_GROUP, POS)
add_word("cola", "кола", SUB_GROUP, MAIN_GROUP, POS)
add_word("wine", "вино", SUB_GROUP, MAIN_GROUP, POS)
add_word("beer", "пиво", SUB_GROUP, MAIN_GROUP, POS)
add_word("whisky", "виски", SUB_GROUP, MAIN_GROUP, POS)

sweets; chocolate; candy; jam; marmalade; cake; pie; biscuit-cookie; sugar; honey; chewing gum;
SUB_GROUP = "Сладости • Sweets"
add_word("sweets", "сладости", SUB_GROUP, MAIN_GROUP, POS)
add_word("chocolate", "шоколад", SUB_GROUP, MAIN_GROUP, POS)
add_word("candy", "конфета", SUB_GROUP, MAIN_GROUP, POS)
add_word("jam", "варенье", SUB_GROUP, MAIN_GROUP, POS)
add_word("marmalade", "мармелад", SUB_GROUP, MAIN_GROUP, POS)
add_word("cake", "торт", SUB_GROUP, MAIN_GROUP, POS)
add_word("pie", "пирог", SUB_GROUP, MAIN_GROUP, POS)
add_word("biscuit", "печенье", SUB_GROUP, MAIN_GROUP, POS)
add_word("cookie", "печенье", SUB_GROUP, MAIN_GROUP, POS)
add_word("sugar", "сахар", SUB_GROUP, MAIN_GROUP, POS)
add_word("honey", "мёд", SUB_GROUP, MAIN_GROUP, POS)
add_word("chewing gum", "жевательная резинка", SUB_GROUP, MAIN_GROUP, POS)

foodstuffs; butter; margarine; cheese; cottage cheese; cream; sour cream; buckwheat; oatmeal; salt; sausage; salami; egg; canned goods; tinned food; vegetable oil; butcher's; greengrocery; dairy; fishmonger's; grocery; confectionery;
SUB_GROUP = "Пищевые Продукты • Foodstuffs"
add_word("foodstuffs", "продукты питания", SUB_GROUP, MAIN_GROUP, POS)
add_word("butter", "масло сливочное", SUB_GROUP, MAIN_GROUP, POS)
add_word("margarine", "маргарин", SUB_GROUP, MAIN_GROUP, POS)
add_word("cheese", "сыр", SUB_GROUP, MAIN_GROUP, POS)
add_word("cottage cheese", "творог", SUB_GROUP, MAIN_GROUP, POS)
add_word("cream", "сливки", SUB_GROUP, MAIN_GROUP, POS)
add_word("sour cream", "сметана", SUB_GROUP, MAIN_GROUP, POS)
add_word("buckwheat", "гречка", SUB_GROUP, MAIN_GROUP, POS)
add_word("oatmeal", "овсянка", SUB_GROUP, MAIN_GROUP, POS)
add_word("salt", "соль", SUB_GROUP, MAIN_GROUP, POS)
add_word("sausage", "колбаса", SUB_GROUP, MAIN_GROUP, POS)
add_word("salami", "салями", SUB_GROUP, MAIN_GROUP, POS)
add_word("egg", "яйцо", SUB_GROUP, MAIN_GROUP, POS)
add_word("canned goods", "консервы", SUB_GROUP, MAIN_GROUP, POS)
add_word("tinned food", "консервы", SUB_GROUP, MAIN_GROUP, POS)
add_word("vegetable oil", "растительное масло", SUB_GROUP, MAIN_GROUP, POS)
add_word("butcher's", "мясной магазин", SUB_GROUP, MAIN_GROUP, POS)
add_word("greengrocery", "овощной магазин", SUB_GROUP, MAIN_GROUP, POS)
add_word("dairy", "молочный магазин", SUB_GROUP, MAIN_GROUP, POS)
add_word("fishmonger's", "рыбный магазин", SUB_GROUP, MAIN_GROUP, POS)
add_word("grocery", "бакалея", SUB_GROUP, MAIN_GROUP, POS)
add_word("confectionery", "кондитерская", SUB_GROUP, MAIN_GROUP, POS)

bread; loaf; roll; bun; pancake; tart; pie; doughnut; pasty; flour; dough; pastry;
SUB_GROUP = "Хлеб • Bread"
add_word("bread", "хлеб", SUB_GROUP, MAIN_GROUP, POS)
add_word("loaf", "буханка", SUB_GROUP, MAIN_GROUP, POS)
add_word("roll", "булочка", SUB_GROUP, MAIN_GROUP, POS)
add_word("bun", "сдобная булочка", SUB_GROUP, MAIN_GROUP, POS)
add_word("pancake", "блин", SUB_GROUP, MAIN_GROUP, POS)
add_word("tart", "пирожное с фруктами", SUB_GROUP, MAIN_GROUP, POS)
add_word("pie", "пирог", SUB_GROUP, MAIN_GROUP, POS)
add_word("doughnut", "пончик", SUB_GROUP, MAIN_GROUP, POS)
add_word("pasty", "пирожок", SUB_GROUP, MAIN_GROUP, POS)
add_word("flour", "мука", SUB_GROUP, MAIN_GROUP, POS)
add_word("dough", "тесто", SUB_GROUP, MAIN_GROUP, POS)
add_word("pastry", "выпечка", SUB_GROUP, MAIN_GROUP, POS)

dining table; tablecloth; napkin; spoon; tablespoon; teaspoon; fork; knife; dish; glass; cup; plate; bowl; saucer; pan; frying pan; pot; bottle opener; tin opener; ladle; kitchen utensils;
SUB_GROUP = "Кухонные Принадлежности • Kitchen Utensils"
add_word("dining table", "обеденный стол", SUB_GROUP, MAIN_GROUP, POS)
add_word("tablecloth", "скатерть", SUB_GROUP, MAIN_GROUP, POS)
add_word("napkin", "салфетка", SUB_GROUP, MAIN_GROUP, POS)
add_word("spoon", "ложка", SUB_GROUP, MAIN_GROUP, POS)
add_word("tablespoon", "столовая ложка", SUB_GROUP, MAIN_GROUP, POS)
add_word("teaspoon", "чайная ложка", SUB_GROUP, MAIN_GROUP, POS)
add_word("fork", "вилка", SUB_GROUP, MAIN_GROUP, POS)
add_word("knife", "нож", SUB_GROUP, MAIN_GROUP, POS)
add_word("dish", "блюдо", SUB_GROUP, MAIN_GROUP, POS)
add_word("glass", "стакан", SUB_GROUP, MAIN_GROUP, POS)
add_word("cup", "чашка", SUB_GROUP, MAIN_GROUP, POS)
add_word("plate", "тарелка", SUB_GROUP, MAIN_GROUP, POS)
add_word("bowl", "миска", SUB_GROUP, MAIN_GROUP, POS)
add_word("saucer", "блюдце", SUB_GROUP, MAIN_GROUP, POS)
add_word("pan", "кастрюля", SUB_GROUP, MAIN_GROUP, POS)
add_word("frying pan", "сковорода", SUB_GROUP, MAIN_GROUP, POS)
add_word("pot", "горшок", SUB_GROUP, MAIN_GROUP, POS)
add_word("bottle opener", "открывалка для бутылок", SUB_GROUP, MAIN_GROUP, POS)
add_word("tin opener", "консервный нож", SUB_GROUP, MAIN_GROUP, POS)
add_word("ladle", "половник", SUB_GROUP, MAIN_GROUP, POS)
add_word("kitchen utensils", "кухонная утварь", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Чувства / Характер • Feeling / Character"

emotion; satisfaction; pleasure; excitement; happiness; joy; enthusiasm; delight; interest; relief
SUB_GROUP = "Позитивные Эмоции • Positive Emotions"
add_word("emotion", "эмоция", SUB_GROUP, MAIN_GROUP, POS)
add_word("satisfaction", "удовлетворение", SUB_GROUP, MAIN_GROUP, POS)
add_word("pleasure", "удовольствие", SUB_GROUP, MAIN_GROUP, POS)
add_word("excitement", "возбуждение", SUB_GROUP, MAIN_GROUP, POS)
add_word("happiness", "счастье", SUB_GROUP, MAIN_GROUP, POS)
add_word("joy", "радость", SUB_GROUP, MAIN_GROUP, POS)
add_word("enthusiasm", "энтузиазм", SUB_GROUP, MAIN_GROUP, POS)
add_word("delight", "восторг", SUB_GROUP, MAIN_GROUP, POS)
add_word("interest", "интерес", SUB_GROUP, MAIN_GROUP, POS)
add_word("relief", "облегчение", SUB_GROUP, MAIN_GROUP, POS)

boredom; uneasiness; discontent; dissatisfaction; sadness; suffering; sorrow; grief; anxiety
SUB_GROUP = "Негативные Эмоции • Negative Emotions"
add_word("boredom", "скука", SUB_GROUP, MAIN_GROUP, POS)
add_word("uneasiness", "беспокойство", SUB_GROUP, MAIN_GROUP, POS)
add_word("discontent", "недовольство", SUB_GROUP, MAIN_GROUP, POS)
add_word("dissatisfaction", "неудовлетворенность", SUB_GROUP, MAIN_GROUP, POS)
add_word("sadness", "грусть", SUB_GROUP, MAIN_GROUP, POS)
add_word("suffering", "страдание", SUB_GROUP, MAIN_GROUP, POS)
add_word("sorrow", "печаль", SUB_GROUP, MAIN_GROUP, POS)
add_word("grief", "горе", SUB_GROUP, MAIN_GROUP, POS)
add_word("anxiety", "тревога", SUB_GROUP, MAIN_GROUP, POS)

patience; self-control; firmness; courage; willpower; resolution; determination; confidence; weakness; hesitation; doubt; cowardice; suspicion; disbelief; distrust
SUB_GROUP = "Терпение / Слабость • Patience / Weakness"
add_word("patience", "терпение", SUB_GROUP, MAIN_GROUP, POS)
add_word("self-control", "самоконтроль", SUB_GROUP, MAIN_GROUP, POS)
add_word("firmness", "твердость", SUB_GROUP, MAIN_GROUP, POS)
add_word("courage", "мужество", SUB_GROUP, MAIN_GROUP, POS)
add_word("willpower", "сила воли", SUB_GROUP, MAIN_GROUP, POS)
add_word("resolution", "решимость", SUB_GROUP, MAIN_GROUP, POS)
add_word("determination", "целеустремленность", SUB_GROUP, MAIN_GROUP, POS)
add_word("confidence", "уверенность", SUB_GROUP, MAIN_GROUP, POS)
add_word("weakness", "слабость", SUB_GROUP, MAIN_GROUP, POS)
add_word("hesitation", "колебание", SUB_GROUP, MAIN_GROUP, POS)
add_word("doubt", "сомнение", SUB_GROUP, MAIN_GROUP, POS)
add_word("cowardice", "трусость", SUB_GROUP, MAIN_GROUP, POS)
add_word("suspicion", "подозрение", SUB_GROUP, MAIN_GROUP, POS)
add_word("disbelief", "недоверие", SUB_GROUP, MAIN_GROUP, POS)
add_word("distrust", "недоверие", SUB_GROUP, MAIN_GROUP, POS)

sympathy; respect; friendship; admiration; love; adoration; indifference; contempt; malice; resentment; disgust; envy
SUB_GROUP = "Любовь / Ненависть • Love / Hatred"
add_word("sympathy", "сочувствие", SUB_GROUP, MAIN_GROUP, POS)
add_word("respect", "уважение", SUB_GROUP, MAIN_GROUP, POS)
add_word("friendship", "дружба", SUB_GROUP, MAIN_GROUP, POS)
add_word("admiration", "восхищение", SUB_GROUP, MAIN_GROUP, POS)
add_word("love", "любовь", SUB_GROUP, MAIN_GROUP, POS)
add_word("adoration", "обожание", SUB_GROUP, MAIN_GROUP, POS)
add_word("indifference", "безразличие", SUB_GROUP, MAIN_GROUP, POS)
add_word("contempt", "презрение", SUB_GROUP, MAIN_GROUP, POS)
add_word("malice", "злость", SUB_GROUP, MAIN_GROUP, POS)
add_word("resentment", "обида", SUB_GROUP, MAIN_GROUP, POS)
add_word("disgust", "отвращение", SUB_GROUP, MAIN_GROUP, POS)
add_word("envy", "зависть", SUB_GROUP, MAIN_GROUP, POS)

pride; vanity; arrogance; modesty; shyness; consideration; tolerance; shame; intolerance; politeness; tact; good manners; courtesy; rudeness; lack of tact; disrespect; offence; insult
SUB_GROUP = "Гордость / Скромность • Pride / Modesty"
add_word("pride", "гордость", SUB_GROUP, MAIN_GROUP, POS)
add_word("vanity", "тщеславие", SUB_GROUP, MAIN_GROUP, POS)
add_word("arrogance", "высокомерие", SUB_GROUP, MAIN_GROUP, POS)
add_word("modesty", "скромность", SUB_GROUP, MAIN_GROUP, POS)
add_word("shyness", "застенчивость", SUB_GROUP, MAIN_GROUP, POS)
add_word("consideration", "внимательность", SUB_GROUP, MAIN_GROUP, POS)
add_word("tolerance", "терпимость", SUB_GROUP, MAIN_GROUP, POS)
add_word("shame", "стыд", SUB_GROUP, MAIN_GROUP, POS)
add_word("intolerance", "нетерпимость", SUB_GROUP, MAIN_GROUP, POS)
add_word("politeness", "вежливость", SUB_GROUP, MAIN_GROUP, POS)
add_word("tact", "тактичность", SUB_GROUP, MAIN_GROUP, POS)
add_word("good manners", "хорошие манеры", SUB_GROUP, MAIN_GROUP, POS)
add_word("courtesy", "учтивость", SUB_GROUP, MAIN_GROUP, POS)
add_word("rudeness", "грубость", SUB_GROUP, MAIN_GROUP, POS)
add_word("lack of tact", "отсутствие такта", SUB_GROUP, MAIN_GROUP, POS)
add_word("disrespect", "неуважение", SUB_GROUP, MAIN_GROUP, POS)
add_word("offence", "оскорбление", SUB_GROUP, MAIN_GROUP, POS)
add_word("insult", "обида", SUB_GROUP, MAIN_GROUP, POS)

wish; desire; hope; dream; intention; aspiration; eagerness; aim; purpose; stimulus; incentive; tiredness; fatigue; laziness; diligence
SUB_GROUP = "Старание / Лень • Diligence / Laziness"
add_word("wish", "желание", SUB_GROUP, MAIN_GROUP, POS)
add_word("desire", "желание", SUB_GROUP, MAIN_GROUP, POS)
add_word("hope", "надежда", SUB_GROUP, MAIN_GROUP, POS)
add_word("dream", "мечта", SUB_GROUP, MAIN_GROUP, POS)
add_word("intention", "намерение", SUB_GROUP, MAIN_GROUP, POS)
add_word("aspiration", "стремление", SUB_GROUP, MAIN_GROUP, POS)
add_word("eagerness", "рвение", SUB_GROUP, MAIN_GROUP, POS)
add_word("aim", "цель", SUB_GROUP, MAIN_GROUP, POS)
add_word("purpose", "назначение", SUB_GROUP, MAIN_GROUP, POS)
add_word("stimulus", "стимул", SUB_GROUP, MAIN_GROUP, POS)
add_word("incentive", "побуждение", SUB_GROUP, MAIN_GROUP, POS)
add_word("tiredness", "усталость", SUB_GROUP, MAIN_GROUP, POS)
add_word("fatigue", "утомление", SUB_GROUP, MAIN_GROUP, POS)
add_word("laziness", "леность", SUB_GROUP, MAIN_GROUP, POS)
add_word("diligence", "усердие", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Мышление • Thinking"

nature; universe; world; existence; reality; being; conscience; science; philosophy
SUB_GROUP = "Сознание • Consciousness"
add_word("nature", "природа", SUB_GROUP, MAIN_GROUP, POS)
add_word("universe", "вселенная", SUB_GROUP, MAIN_GROUP, POS)
add_word("world", "мир", SUB_GROUP, MAIN_GROUP, POS)
add_word("existence", "существование", SUB_GROUP, MAIN_GROUP, POS)
add_word("reality", "реальность", SUB_GROUP, MAIN_GROUP, POS)
add_word("being", "бытие", SUB_GROUP, MAIN_GROUP, POS)
add_word("conscience", "сознание", SUB_GROUP, MAIN_GROUP, POS)
add_word("science", "наука", SUB_GROUP, MAIN_GROUP, POS)
add_word("philosophy", "философия", SUB_GROUP, MAIN_GROUP, POS)

practice; knowledge; cognition; object; subject; reflection; sensation; perception; idea; notion; concept; statement; conclusion; logic; theory
SUB_GROUP = "Познание • Cognition"
add_word("practice", "практика", SUB_GROUP, MAIN_GROUP, POS)
add_word("knowledge", "знание", SUB_GROUP, MAIN_GROUP, POS)
add_word("cognition", "познание", SUB_GROUP, MAIN_GROUP, POS)
add_word("object", "объект", SUB_GROUP, MAIN_GROUP, POS)
add_word("subject", "субъект", SUB_GROUP, MAIN_GROUP, POS)
add_word("reflection", "отражение", SUB_GROUP, MAIN_GROUP, POS)
add_word("sensation", "ощущение", SUB_GROUP, MAIN_GROUP, POS)
add_word("perception", "восприятие", SUB_GROUP, MAIN_GROUP, POS)
add_word("idea", "идея", SUB_GROUP, MAIN_GROUP, POS)
add_word("notion", "понятие", SUB_GROUP, MAIN_GROUP, POS)
add_word("concept", "концепция", SUB_GROUP, MAIN_GROUP, POS)
add_word("statement", "утверждение", SUB_GROUP, MAIN_GROUP, POS)
add_word("conclusion", "вывод", SUB_GROUP, MAIN_GROUP, POS)
add_word("logic", "логика", SUB_GROUP, MAIN_GROUP, POS)
add_word("theory", "теория", SUB_GROUP, MAIN_GROUP, POS)

regularity; accident; chance; whole; part; form; contents; essence; variety; diversity; similarity; identity; contrast; contradiction; quantity; quality; number; order; sequence; system; time; space; place; room; spot; surroundings; circumstance; factor; reason; cause; development; consequence; necessity; possibility; probability;
SUB_GROUP = "Категории Мышления • Thinking Categories"
add_word("regularity", "регулярность", SUB_GROUP, MAIN_GROUP, POS)
add_word("accident", "случайность", SUB_GROUP, MAIN_GROUP, POS)
add_word("chance", "шанс", SUB_GROUP, MAIN_GROUP, POS)
add_word("whole", "целое", SUB_GROUP, MAIN_GROUP, POS)
add_word("part", "часть", SUB_GROUP, MAIN_GROUP, POS)
add_word("form", "форма", SUB_GROUP, MAIN_GROUP, POS)
add_word("contents", "содержание", SUB_GROUP, MAIN_GROUP, POS)
add_word("essence", "суть", SUB_GROUP, MAIN_GROUP, POS)
add_word("variety", "разнообразие", SUB_GROUP, MAIN_GROUP, POS)
add_word("diversity", "многообразие", SUB_GROUP, MAIN_GROUP, POS)
add_word("similarity", "сходство", SUB_GROUP, MAIN_GROUP, POS)
add_word("identity", "тождество", SUB_GROUP, MAIN_GROUP, POS)
add_word("contrast", "контраст", SUB_GROUP, MAIN_GROUP, POS)
add_word("contradiction", "противоречие", SUB_GROUP, MAIN_GROUP, POS)
add_word("quantity", "количество", SUB_GROUP, MAIN_GROUP, POS)
add_word("quality", "качество", SUB_GROUP, MAIN_GROUP, POS)
add_word("number", "число", SUB_GROUP, MAIN_GROUP, POS)
add_word("order", "порядок", SUB_GROUP, MAIN_GROUP, POS)
add_word("sequence", "последовательность", SUB_GROUP, MAIN_GROUP, POS)
add_word("system", "система", SUB_GROUP, MAIN_GROUP, POS)
add_word("time", "время", SUB_GROUP, MAIN_GROUP, POS)
add_word("space", "пространство", SUB_GROUP, MAIN_GROUP, POS)
add_word("place", "место", SUB_GROUP, MAIN_GROUP, POS)
add_word("room", "комната", SUB_GROUP, MAIN_GROUP, POS)
add_word("spot", "пятно", SUB_GROUP, MAIN_GROUP, POS)
add_word("surroundings", "окружение", SUB_GROUP, MAIN_GROUP, POS)
add_word("circumstance", "обстоятельство", SUB_GROUP, MAIN_GROUP, POS)
add_word("factor", "фактор", SUB_GROUP, MAIN_GROUP, POS)
add_word("reason", "причина", SUB_GROUP, MAIN_GROUP, POS)
add_word("cause", "повод", SUB_GROUP, MAIN_GROUP, POS)
add_word("development", "развитие", SUB_GROUP, MAIN_GROUP, POS)
add_word("consequence", "последствие", SUB_GROUP, MAIN_GROUP, POS)
add_word("necessity", "необходимость", SUB_GROUP, MAIN_GROUP, POS)
add_word("possibility", "возможность", SUB_GROUP, MAIN_GROUP, POS)
add_word("probability", "вероятность", SUB_GROUP, MAIN_GROUP, POS)

research; theme; topic; issue; problem; phenomenon; fact; sample; specimen; example; field; indication; symptom; characteristic; feature; means; method; procedure; way; manner; laboratory; equipment; appliance; device; discovery; modification; improvement; development; creation; invention; verification
SUB_GROUP = "Исследование • Research"
add_word("research", "исследование", SUB_GROUP, MAIN_GROUP, POS)
add_word("theme", "тема", SUB_GROUP, MAIN_GROUP, POS)
add_word("topic", "топик", SUB_GROUP, MAIN_GROUP, POS)
add_word("issue", "вопрос", SUB_GROUP, MAIN_GROUP, POS)
add_word("problem", "проблема", SUB_GROUP, MAIN_GROUP, POS)
add_word("phenomenon", "явление", SUB_GROUP, MAIN_GROUP, POS)
add_word("fact", "факт", SUB_GROUP, MAIN_GROUP, POS)
add_word("sample", "образец", SUB_GROUP, MAIN_GROUP, POS)
add_word("specimen", "экземпляр", SUB_GROUP, MAIN_GROUP, POS)
add_word("example", "пример", SUB_GROUP, MAIN_GROUP, POS)
add_word("field", "поле", SUB_GROUP, MAIN_GROUP, POS)
add_word("indication", "индикация", SUB_GROUP, MAIN_GROUP, POS)
add_word("symptom", "симптом", SUB_GROUP, MAIN_GROUP, POS)
add_word("characteristic", "характеристика", SUB_GROUP, MAIN_GROUP, POS)
add_word("feature", "особенность", SUB_GROUP, MAIN_GROUP, POS)
add_word("means", "средство", SUB_GROUP, MAIN_GROUP, POS)
add_word("method", "метод", SUB_GROUP, MAIN_GROUP, POS)
add_word("procedure", "процедура", SUB_GROUP, MAIN_GROUP, POS)
add_word("way", "способ", SUB_GROUP, MAIN_GROUP, POS)
add_word("manner", "образ", SUB_GROUP, MAIN_GROUP, POS)
add_word("laboratory", "лаборатория", SUB_GROUP, MAIN_GROUP, POS)
add_word("equipment", "оборудование", SUB_GROUP, MAIN_GROUP, POS)
add_word("appliance", "прибор", SUB_GROUP, MAIN_GROUP, POS)
add_word("device", "устройство", SUB_GROUP, MAIN_GROUP, POS)
add_word("discovery", "открытие", SUB_GROUP, MAIN_GROUP, POS)
add_word("modification", "модификация", SUB_GROUP, MAIN_GROUP, POS)
add_word("improvement", "улучшение", SUB_GROUP, MAIN_GROUP, POS)
add_word("development", "разработка", SUB_GROUP, MAIN_GROUP, POS)
add_word("creation", "создание", SUB_GROUP, MAIN_GROUP, POS)
add_word("invention", "изобретение", SUB_GROUP, MAIN_GROUP, POS)
add_word("verification", "проверка", SUB_GROUP, MAIN_GROUP, POS)

analysis; comparison; data processing; classification; kind; type; interconnection; correlation; interaction; rule; law; principle; exception
SUB_GROUP = "Анализ • Analysis"
add_word("analysis", "анализ", SUB_GROUP, MAIN_GROUP, POS)
add_word("comparison", "сравнение", SUB_GROUP, MAIN_GROUP, POS)
add_word("data processing", "обработка данных", SUB_GROUP, MAIN_GROUP, POS)
add_word("classification", "классификация", SUB_GROUP, MAIN_GROUP, POS)
add_word("kind", "вид", SUB_GROUP, MAIN_GROUP, POS)
add_word("type", "тип", SUB_GROUP, MAIN_GROUP, POS)
add_word("interconnection", "взаимосвязь", SUB_GROUP, MAIN_GROUP, POS)
add_word("correlation", "корреляция", SUB_GROUP, MAIN_GROUP, POS)
add_word("interaction", "взаимодействие", SUB_GROUP, MAIN_GROUP, POS)
add_word("rule", "правило", SUB_GROUP, MAIN_GROUP, POS)
add_word("law", "закон", SUB_GROUP, MAIN_GROUP, POS)
add_word("principle", "принцип", SUB_GROUP, MAIN_GROUP, POS)
add_word("exception", "исключение", SUB_GROUP, MAIN_GROUP, POS)

success; failure; advantage; merit; effectiveness; efficiency; importance; disadvantage; deficiency; demerit; error; mistake
SUB_GROUP = "Результат • Result"
add_word("success", "успех", SUB_GROUP, MAIN_GROUP, POS)
add_word("failure", "неудача", SUB_GROUP, MAIN_GROUP, POS)
add_word("advantage", "преимущество", SUB_GROUP, MAIN_GROUP, POS)
add_word("merit", "заслуга", SUB_GROUP, MAIN_GROUP, POS)
add_word("effectiveness", "эффективность", SUB_GROUP, MAIN_GROUP, POS)
add_word("efficiency", "экономичность", SUB_GROUP, MAIN_GROUP, POS)
add_word("importance", "важность", SUB_GROUP, MAIN_GROUP, POS)
add_word("disadvantage", "недостаток", SUB_GROUP, MAIN_GROUP, POS)
add_word("deficiency", "дефицит", SUB_GROUP, MAIN_GROUP, POS)
add_word("demerit", "недостаток", SUB_GROUP, MAIN_GROUP, POS)
add_word("error", "ошибка", SUB_GROUP, MAIN_GROUP, POS)
add_word("mistake", "заблуждение", SUB_GROUP, MAIN_GROUP, POS)

statement; report; thought; idea; premise; criteria; proof; argument; conclusion
SUB_GROUP = "Сообщение • Report"
add_word("statement", "утверждение", SUB_GROUP, MAIN_GROUP, POS)
add_word("report", "отчет", SUB_GROUP, MAIN_GROUP, POS)
add_word("thought", "мысль", SUB_GROUP, MAIN_GROUP, POS)
add_word("idea", "идея", SUB_GROUP, MAIN_GROUP, POS)
add_word("premise", "предпосылка", SUB_GROUP, MAIN_GROUP, POS)
add_word("criteria", "критерии", SUB_GROUP, MAIN_GROUP, POS)
add_word("proof", "доказательство", SUB_GROUP, MAIN_GROUP, POS)
add_word("argument", "аргумент", SUB_GROUP, MAIN_GROUP, POS)
add_word("conclusion", "вывод", SUB_GROUP, MAIN_GROUP, POS)

criticism; attitude; position; point of view; definition; consent; assent; approval; recognition; confirmation; objection; rejection; refusal; overestimation; underestimation; misunderstanding
SUB_GROUP = "Критика • Criticism"
add_word("criticism", "критика", SUB_GROUP, MAIN_GROUP, POS)
add_word("attitude", "отношение", SUB_GROUP, MAIN_GROUP, POS)
add_word("position", "позиция", SUB_GROUP, MAIN_GROUP, POS)
add_word("point of view", "точка зрения", SUB_GROUP, MAIN_GROUP, POS)
add_word("definition", "определение", SUB_GROUP, MAIN_GROUP, POS)
add_word("consent", "согласие", SUB_GROUP, MAIN_GROUP, POS)
add_word("assent", "одобрение", SUB_GROUP, MAIN_GROUP, POS)
add_word("approval", "утверждение", SUB_GROUP, MAIN_GROUP, POS)
add_word("recognition", "признание", SUB_GROUP, MAIN_GROUP, POS)
add_word("confirmation", "подтверждение", SUB_GROUP, MAIN_GROUP, POS)
add_word("objection", "возражение", SUB_GROUP, MAIN_GROUP, POS)
add_word("rejection", "отклонение", SUB_GROUP, MAIN_GROUP, POS)
add_word("refusal", "отказ", SUB_GROUP, MAIN_GROUP, POS)
add_word("overestimation", "переоценка", SUB_GROUP, MAIN_GROUP, POS)
add_word("underestimation", "недооценка", SUB_GROUP, MAIN_GROUP, POS)
add_word("misunderstanding", "недоразумение", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Образование • Education"

education; upbringing; teaching; instruction; training; elementary school; primary school; high school; vocational school; college; institute; university;
SUB_GROUP = "Учебные Заведения • Educational Institutions"
add_word("education", "образование", SUB_GROUP, MAIN_GROUP, POS)
add_word("upbringing", "воспитание", SUB_GROUP, MAIN_GROUP, POS)
add_word("teaching", "преподавание", SUB_GROUP, MAIN_GROUP, POS)
add_word("instruction", "обучение", SUB_GROUP, MAIN_GROUP, POS)
add_word("training", "тренировка", SUB_GROUP, MAIN_GROUP, POS)
add_word("elementary school", "начальная школа", SUB_GROUP, MAIN_GROUP, POS)
add_word("primary school", "начальная школа", SUB_GROUP, MAIN_GROUP, POS)
add_word("high school", "средняя школа", SUB_GROUP, MAIN_GROUP, POS)
add_word("vocational school", "профессиональное училище", SUB_GROUP, MAIN_GROUP, POS)
add_word("college", "колледж", SUB_GROUP, MAIN_GROUP, POS)
add_word("institute", "институт", SUB_GROUP, MAIN_GROUP, POS)
add_word("university", "университет", SUB_GROUP, MAIN_GROUP, POS)

subject; timetable; STEM fields; mathematics; physics; biology; chemistry; engineering; drawing; humanities; history; literature; foreign language; physical education;
SUB_GROUP = "Учебные Предметы • Subjects"
add_word("subject", "предмет", SUB_GROUP, MAIN_GROUP, POS)
add_word("timetable", "расписание", SUB_GROUP, MAIN_GROUP, POS)
add_word("STEM fields", "STEM области", SUB_GROUP, MAIN_GROUP, POS)
add_word("mathematics", "математика", SUB_GROUP, MAIN_GROUP, POS)
add_word("physics", "физика", SUB_GROUP, MAIN_GROUP, POS)
add_word("biology", "биология", SUB_GROUP, MAIN_GROUP, POS)
add_word("chemistry", "химия", SUB_GROUP, MAIN_GROUP, POS)
add_word("engineering", "инженерия", SUB_GROUP, MAIN_GROUP, POS)
add_word("drawing", "рисование", SUB_GROUP, MAIN_GROUP, POS)
add_word("humanities", "гуманитарные науки", SUB_GROUP, MAIN_GROUP, POS)
add_word("history", "история", SUB_GROUP, MAIN_GROUP, POS)
add_word("literature", "литература", SUB_GROUP, MAIN_GROUP, POS)
add_word("foreign language", "иностранный язык", SUB_GROUP, MAIN_GROUP, POS)
add_word("physical education", "физическая культура", SUB_GROUP, MAIN_GROUP, POS)

year (as grade); grade; form; class; lesson; lecture; break; task; homework; teacher; pupil; student; classroom; blackboard; desk; teaching aids; textbook; pen; pencil; ruler; eraser; map; school year; vacation;
SUB_GROUP = "Учеба • Studies"
add_word("year (as grade)", "год (класс)", SUB_GROUP, MAIN_GROUP, POS)
add_word("grade", "класс", SUB_GROUP, MAIN_GROUP, POS)
add_word("form", "форма", SUB_GROUP, MAIN_GROUP, POS)
add_word("class", "класс", SUB_GROUP, MAIN_GROUP, POS)
add_word("lesson", "урок", SUB_GROUP, MAIN_GROUP, POS)
add_word("lecture", "лекция", SUB_GROUP, MAIN_GROUP, POS)
add_word("break", "перемена", SUB_GROUP, MAIN_GROUP, POS)
add_word("task", "задание", SUB_GROUP, MAIN_GROUP, POS)
add_word("homework", "домашнее задание", SUB_GROUP, MAIN_GROUP, POS)
add_word("teacher", "учитель", SUB_GROUP, MAIN_GROUP, POS)
add_word("pupil", "ученик", SUB_GROUP, MAIN_GROUP, POS)
add_word("student", "студент", SUB_GROUP, MAIN_GROUP, POS)
add_word("classroom", "классная комната", SUB_GROUP, MAIN_GROUP, POS)
add_word("blackboard", "доска", SUB_GROUP, MAIN_GROUP, POS)
add_word("desk", "парта", SUB_GROUP, MAIN_GROUP, POS)
add_word("teaching aids", "наглядные пособия", SUB_GROUP, MAIN_GROUP, POS)
add_word("textbook", "учебник", SUB_GROUP, MAIN_GROUP, POS)
add_word("pen", "ручка", SUB_GROUP, MAIN_GROUP, POS)
add_word("pencil", "карандаш", SUB_GROUP, MAIN_GROUP, POS)
add_word("ruler", "линейка", SUB_GROUP, MAIN_GROUP, POS)
add_word("eraser", "ластик", SUB_GROUP, MAIN_GROUP, POS)
add_word("map", "карта", SUB_GROUP, MAIN_GROUP, POS)
add_word("school year", "учебный год", SUB_GROUP, MAIN_GROUP, POS)
add_word("vacation", "каникулы", SUB_GROUP, MAIN_GROUP, POS)

competition; examination; exam; certificate; diploma;
SUB_GROUP = "Экзамен / Оценки • Exams / Grades"
add_word("competition", "конкурс", SUB_GROUP, MAIN_GROUP, POS)
add_word("examination", "экзамен", SUB_GROUP, MAIN_GROUP, POS)
add_word("exam", "экзамен", SUB_GROUP, MAIN_GROUP, POS)
add_word("certificate", "сертификат", SUB_GROUP, MAIN_GROUP, POS)
add_word("diploma", "диплом", SUB_GROUP, MAIN_GROUP, POS)

linguistics; language; speech; vocabulary; grammar; style; letter; alphabet; spelling; pronunciation; vowel; consonant; transcription;
SUB_GROUP = "Лингвистика • Linguistics — Part 1"
add_word("linguistics", "лингвистика", SUB_GROUP, MAIN_GROUP, POS)
add_word("language", "язык", SUB_GROUP, MAIN_GROUP, POS)
add_word("speech", "речь", SUB_GROUP, MAIN_GROUP, POS)
add_word("vocabulary", "словарный запас", SUB_GROUP, MAIN_GROUP, POS)
add_word("grammar", "грамматика", SUB_GROUP, MAIN_GROUP, POS)
add_word("style", "стиль", SUB_GROUP, MAIN_GROUP, POS)
add_word("letter", "буква", SUB_GROUP, MAIN_GROUP, POS)
add_word("alphabet", "алфавит", SUB_GROUP, MAIN_GROUP, POS)
add_word("spelling", "правописание", SUB_GROUP, MAIN_GROUP, POS)
add_word("pronunciation", "произношение", SUB_GROUP, MAIN_GROUP, POS)
add_word("vowel", "гласный", SUB_GROUP, MAIN_GROUP, POS)
add_word("consonant", "согласный", SUB_GROUP, MAIN_GROUP, POS)
add_word("transcription", "транскрипция", SUB_GROUP, MAIN_GROUP, POS)

word; phrase; idiom; sentence; simple sentence; complex sentence; clause; text; affirmation; interrogation; negation;
SUB_GROUP = "Лингвистика • Linguistics — Part 2"
add_word("word", "слово", SUB_GROUP, MAIN_GROUP, POS)
add_word("phrase", "фраза", SUB_GROUP, MAIN_GROUP, POS)
add_word("idiom", "идиома", SUB_GROUP, MAIN_GROUP, POS)
add_word("sentence", "предложение", SUB_GROUP, MAIN_GROUP, POS)
add_word("simple sentence", "простое предложение", SUB_GROUP, MAIN_GROUP, POS)
add_word("complex sentence", "сложное предложение", SUB_GROUP, MAIN_GROUP, POS)
add_word("clause", "придаточное предложение", SUB_GROUP, MAIN_GROUP, POS)
add_word("text", "текст", SUB_GROUP, MAIN_GROUP, POS)
add_word("affirmation", "утверждение", SUB_GROUP, MAIN_GROUP, POS)
add_word("interrogation", "вопрос", SUB_GROUP, MAIN_GROUP, POS)
add_word("negation", "отрицание", SUB_GROUP, MAIN_GROUP, POS)

part of speech; noun; verb; adjective; pronoun; adverb; numeral; preposition; conjunction; article; interjection;
SUB_GROUP = "Лингвистика • Linguistics — Part 3"
add_word("part of speech", "часть речи", SUB_GROUP, MAIN_GROUP, POS)
add_word("noun", "существительное", SUB_GROUP, MAIN_GROUP, POS)
add_word("verb", "глагол", SUB_GROUP, MAIN_GROUP, POS)
add_word("adjective", "прилагательное", SUB_GROUP, MAIN_GROUP, POS)
add_word("pronoun", "местоимение", SUB_GROUP, MAIN_GROUP, POS)
add_word("adverb", "наречие", SUB_GROUP, MAIN_GROUP, POS)
add_word("numeral", "числительное", SUB_GROUP, MAIN_GROUP, POS)
add_word("preposition", "предлог", SUB_GROUP, MAIN_GROUP, POS)
add_word("conjunction", "союз", SUB_GROUP, MAIN_GROUP, POS)
add_word("article", "артикль", SUB_GROUP, MAIN_GROUP, POS)
add_word("interjection", "междометие", SUB_GROUP, MAIN_GROUP, POS)

progressive aspect; perfective aspect; active voice; passive voice; case; gender; number; singular; plural;
SUB_GROUP = "Лингвистика • Linguistics — Part 4"
add_word("progressive aspect", "длительный вид", SUB_GROUP, MAIN_GROUP, POS)
add_word("perfective aspect", "совершенный вид", SUB_GROUP, MAIN_GROUP, POS)
add_word("active voice", "действительный залог", SUB_GROUP, MAIN_GROUP, POS)
add_word("passive voice", "страдательный залог", SUB_GROUP, MAIN_GROUP, POS)
add_word("case", "падеж", SUB_GROUP, MAIN_GROUP, POS)
add_word("gender", "род", SUB_GROUP, MAIN_GROUP, POS)
add_word("number", "число", SUB_GROUP, MAIN_GROUP, POS)
add_word("singular", "единственное число", SUB_GROUP, MAIN_GROUP, POS)
add_word("plural", "множественное число", SUB_GROUP, MAIN_GROUP, POS)

part of sentence; subject; predicate; object; adverbial; attribute;
SUB_GROUP = "Лингвистика • Linguistics — Part 5"
add_word("part of sentence", "член предложения", SUB_GROUP, MAIN_GROUP, POS)
add_word("subject", "подлежащее", SUB_GROUP, MAIN_GROUP, POS)
add_word("predicate", "сказуемое", SUB_GROUP, MAIN_GROUP, POS)
add_word("object", "дополнение", SUB_GROUP, MAIN_GROUP, POS)
add_word("adverbial", "обстоятельство", SUB_GROUP, MAIN_GROUP, POS)
add_word("attribute", "определение", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Культура • Culture"

cinema; film documentary; detective comedy; adventure film; thriller; horror film; box-office; ticket; seat; performance; showing;
SUB_GROUP = "Кино • Cinema"
add_word("cinema", "кино", SUB_GROUP, MAIN_GROUP, POS)
add_word("film documentary", "документальный фильм", SUB_GROUP, MAIN_GROUP, POS)
add_word("detective comedy", "детективная комедия", SUB_GROUP, MAIN_GROUP, POS)
add_word("adventure film", "приключенческий фильм", SUB_GROUP, MAIN_GROUP, POS)
add_word("thriller", "триллер", SUB_GROUP, MAIN_GROUP, POS)
add_word("horror film", "фильм ужасов", SUB_GROUP, MAIN_GROUP, POS)
add_word("box-office", "касса", SUB_GROUP, MAIN_GROUP, POS)
add_word("ticket", "билет", SUB_GROUP, MAIN_GROUP, POS)
add_word("seat", "место", SUB_GROUP, MAIN_GROUP, POS)
add_word("performance", "представление", SUB_GROUP, MAIN_GROUP, POS)
add_word("showing", "показ", SUB_GROUP, MAIN_GROUP, POS)

producer; cameramen; actor; actress; extra; artist; makeup artist; set designer; star;
SUB_GROUP = "Киносоздатели  • Cinema — People"
add_word("producer", "продюсер", SUB_GROUP, MAIN_GROUP, POS)
add_word("cameramen", "операторы", SUB_GROUP, MAIN_GROUP, POS)
add_word("actor", "актер", SUB_GROUP, MAIN_GROUP, POS)
add_word("actress", "актриса", SUB_GROUP, MAIN_GROUP, POS)
add_word("extra", "эпизодический актер", SUB_GROUP, MAIN_GROUP, POS)
add_word("artist", "художник", SUB_GROUP, MAIN_GROUP, POS)
add_word("makeup artist", "визажист", SUB_GROUP, MAIN_GROUP, POS)
add_word("set designer", "художник по декорациям", SUB_GROUP, MAIN_GROUP, POS)
add_word("star", "звезда", SUB_GROUP, MAIN_GROUP, POS)

theatre; puppet show; stage; curtain; scenery; performance; cast; audience; applause; first night; interval; auditorium; balcony
SUB_GROUP = "Театр • Theatre"
add_word("theatre", "театр", SUB_GROUP, MAIN_GROUP, POS)
add_word("puppet show", "кукольный театр", SUB_GROUP, MAIN_GROUP, POS)
add_word("stage", "сцена", SUB_GROUP, MAIN_GROUP, POS)
add_word("curtain", "занавес", SUB_GROUP, MAIN_GROUP, POS)
add_word("scenery", "декорации", SUB_GROUP, MAIN_GROUP, POS)
add_word("performance", "спектакль", SUB_GROUP, MAIN_GROUP, POS)
add_word("cast", "актёрский состав", SUB_GROUP, MAIN_GROUP, POS)
add_word("audience", "зрители", SUB_GROUP, MAIN_GROUP, POS)
add_word("applause", "аплодисменты", SUB_GROUP, MAIN_GROUP, POS)
add_word("first night", "премьера", SUB_GROUP, MAIN_GROUP, POS)
add_word("interval", "антракт", SUB_GROUP, MAIN_GROUP, POS)
add_word("auditorium", "зал", SUB_GROUP, MAIN_GROUP, POS)
add_word("balcony", "балкон", SUB_GROUP, MAIN_GROUP, POS)

song; tune; concert; program; encore; music; orchestra; chorus; choir; band; musician; composer; conductor; singer
SUB_GROUP = "Музыка • Music"
add_word("song", "песня", SUB_GROUP, MAIN_GROUP, POS)
add_word("tune", "мелодия", SUB_GROUP, MAIN_GROUP, POS)
add_word("concert", "концерт", SUB_GROUP, MAIN_GROUP, POS)
add_word("program", "программа", SUB_GROUP, MAIN_GROUP, POS)
add_word("encore", "бис", SUB_GROUP, MAIN_GROUP, POS)
add_word("music", "музыка", SUB_GROUP, MAIN_GROUP, POS)
add_word("orchestra", "оркестр", SUB_GROUP, MAIN_GROUP, POS)
add_word("chorus", "хор", SUB_GROUP, MAIN_GROUP, POS)
add_word("choir", "хор", SUB_GROUP, MAIN_GROUP, POS)
add_word("band", "группа", SUB_GROUP, MAIN_GROUP, POS)
add_word("musician", "музыкант", SUB_GROUP, MAIN_GROUP, POS)
add_word("composer", "композитор", SUB_GROUP, MAIN_GROUP, POS)
add_word("conductor", "дирижёр", SUB_GROUP, MAIN_GROUP, POS)
add_word("singer", "певец", SUB_GROUP, MAIN_GROUP, POS)

piano; violin; drum; guitar; trumpet; saxophone
SUB_GROUP = "Музыкальные инструменты • Musical Instruments"
add_word("piano", "пианино", SUB_GROUP, MAIN_GROUP, POS)
add_word("violin", "скрипка", SUB_GROUP, MAIN_GROUP, POS)
add_word("drum", "барабан", SUB_GROUP, MAIN_GROUP, POS)
add_word("guitar", "гитара", SUB_GROUP, MAIN_GROUP, POS)
add_word("trumpet", "труба", SUB_GROUP, MAIN_GROUP, POS)
add_word("saxophone", "саксофон", SUB_GROUP, MAIN_GROUP, POS)

literature; book; edition; volume; title; cover; section; chapter; page; author; writer; poet; playwright;
SUB_GROUP = "Литература • Literature"
add_word("literature", "литература", SUB_GROUP, MAIN_GROUP, POS)
add_word("book", "книга", SUB_GROUP, MAIN_GROUP, POS)
add_word("edition", "издание", SUB_GROUP, MAIN_GROUP, POS)
add_word("volume", "том", SUB_GROUP, MAIN_GROUP, POS)
add_word("title", "название", SUB_GROUP, MAIN_GROUP, POS)
add_word("cover", "обложка", SUB_GROUP, MAIN_GROUP, POS)
add_word("section", "раздел", SUB_GROUP, MAIN_GROUP, POS)
add_word("chapter", "глава", SUB_GROUP, MAIN_GROUP, POS)
add_word("page", "страница", SUB_GROUP, MAIN_GROUP, POS)
add_word("author", "автор", SUB_GROUP, MAIN_GROUP, POS)
add_word("writer", "писатель", SUB_GROUP, MAIN_GROUP, POS)
add_word("poet", "поэт", SUB_GROUP, MAIN_GROUP, POS)
add_word("playwright", "драматург", SUB_GROUP, MAIN_GROUP, POS)

work; novel; story; verse; fairy tale; fiction; library; editor
SUB_GROUP = "Издательство • Publishing House"
add_word("work", "произведение", SUB_GROUP, MAIN_GROUP, POS)
add_word("novel", "роман", SUB_GROUP, MAIN_GROUP, POS)
add_word("story", "рассказ", SUB_GROUP, MAIN_GROUP, POS)
add_word("verse", "стих", SUB_GROUP, MAIN_GROUP, POS)
add_word("fairy tale", "сказка", SUB_GROUP, MAIN_GROUP, POS)
add_word("fiction", "художественная литература", SUB_GROUP, MAIN_GROUP, POS)
add_word("library", "библиотека", SUB_GROUP, MAIN_GROUP, POS)
add_word("editor", "редактор", SUB_GROUP, MAIN_GROUP, POS)

sport; running; gymnastics; skating; skiing; football; soccer; volleyball; basketball; hockey; fan; spectator; competition; match; final; championship; olympic games; medal; victory; draw; record; score; points; team; captain; athlete; referee
SUB_GROUP = "Спорт • Sport"
add_word("sport", "спорт", SUB_GROUP, MAIN_GROUP, POS)
add_word("running", "бег", SUB_GROUP, MAIN_GROUP, POS)
add_word("gymnastics", "гимнастика", SUB_GROUP, MAIN_GROUP, POS)
add_word("skating", "катание на коньках", SUB_GROUP, MAIN_GROUP, POS)
add_word("skiing", "лыжный спорт", SUB_GROUP, MAIN_GROUP, POS)
add_word("football", "футбол", SUB_GROUP, MAIN_GROUP, POS)
add_word("soccer", "футбол", SUB_GROUP, MAIN_GROUP, POS)
add_word("volleyball", "волейбол", SUB_GROUP, MAIN_GROUP, POS)
add_word("basketball", "баскетбол", SUB_GROUP, MAIN_GROUP, POS)
add_word("hockey", "хоккей", SUB_GROUP, MAIN_GROUP, POS)
add_word("fan", "болельщик", SUB_GROUP, MAIN_GROUP, POS)
add_word("spectator", "зритель", SUB_GROUP, MAIN_GROUP, POS)
add_word("competition", "соревнование", SUB_GROUP, MAIN_GROUP, POS)
add_word("match", "матч", SUB_GROUP, MAIN_GROUP, POS)
add_word("final", "финал", SUB_GROUP, MAIN_GROUP, POS)
add_word("championship", "чемпионат", SUB_GROUP, MAIN_GROUP, POS)
add_word("olympic games", "олимпийские игры", SUB_GROUP, MAIN_GROUP, POS)
add_word("medal", "медаль", SUB_GROUP, MAIN_GROUP, POS)
add_word("victory", "победа", SUB_GROUP, MAIN_GROUP, POS)
add_word("draw", "ничья", SUB_GROUP, MAIN_GROUP, POS)
add_word("record", "рекорд", SUB_GROUP, MAIN_GROUP, POS)
add_word("score", "счет", SUB_GROUP, MAIN_GROUP, POS)
add_word("points", "очки", SUB_GROUP, MAIN_GROUP, POS)
add_word("team", "команда", SUB_GROUP, MAIN_GROUP, POS)
add_word("captain", "капитан", SUB_GROUP, MAIN_GROUP, POS)
add_word("athlete", "спортсмен", SUB_GROUP, MAIN_GROUP, POS)
add_word("referee", "судья", SUB_GROUP, MAIN_GROUP, POS)



MAIN_GROUP = "Работа • Work"

job; work; labour; activity; service; years of experience; position; role; duty; place; unemployed; unemployment;
SUB_GROUP = "Труд / Занятость • Labour / Employment"
add_word("job", "работа", SUB_GROUP, MAIN_GROUP, POS)
add_word("work", "труд", SUB_GROUP, MAIN_GROUP, POS)
add_word("labour", "труд", SUB_GROUP, MAIN_GROUP, POS)
add_word("activity", "деятельность", SUB_GROUP, MAIN_GROUP, POS)
add_word("service", "служба", SUB_GROUP, MAIN_GROUP, POS)
add_word("years of experience", "стаж работы", SUB_GROUP, MAIN_GROUP, POS)
add_word("position", "должность", SUB_GROUP, MAIN_GROUP, POS)
add_word("role", "роль", SUB_GROUP, MAIN_GROUP, POS)
add_word("duty", "обязанность", SUB_GROUP, MAIN_GROUP, POS)
add_word("place", "место", SUB_GROUP, MAIN_GROUP, POS)
add_word("unemployed", "безработный", SUB_GROUP, MAIN_GROUP, POS)
add_word("unemployment", "безработица", SUB_GROUP, MAIN_GROUP, POS)

field; industry; agriculture; construction; transport; communication; trade; culture; science; art; healthcare; education;
SUB_GROUP = "Сферы • Fields"
add_word("field", "область", SUB_GROUP, MAIN_GROUP, POS)
add_word("industry", "промышленность", SUB_GROUP, MAIN_GROUP, POS)
add_word("agriculture", "сельское хозяйство", SUB_GROUP, MAIN_GROUP, POS)
add_word("construction", "строительство", SUB_GROUP, MAIN_GROUP, POS)
add_word("transport", "транспорт", SUB_GROUP, MAIN_GROUP, POS)
add_word("communication", "связь", SUB_GROUP, MAIN_GROUP, POS)
add_word("trade", "торговля", SUB_GROUP, MAIN_GROUP, POS)
add_word("culture", "культура", SUB_GROUP, MAIN_GROUP, POS)
add_word("science", "наука", SUB_GROUP, MAIN_GROUP, POS)
add_word("art", "искусство", SUB_GROUP, MAIN_GROUP, POS)
add_word("healthcare", "здравоохранение", SUB_GROUP, MAIN_GROUP, POS)
add_word("education", "образование", SUB_GROUP, MAIN_GROUP, POS)

company; branch; firm; enterprise; plant; factory; power plant; oil refinery; coal mine;
SUB_GROUP = "Предприятие • Enterprise"
add_word("company", "компания", SUB_GROUP, MAIN_GROUP, POS)
add_word("branch", "филиал", SUB_GROUP, MAIN_GROUP, POS)
add_word("firm", "фирма", SUB_GROUP, MAIN_GROUP, POS)
add_word("enterprise", "предприятие", SUB_GROUP, MAIN_GROUP, POS)
add_word("plant", "завод", SUB_GROUP, MAIN_GROUP, POS)
add_word("factory", "фабрика", SUB_GROUP, MAIN_GROUP, POS)
add_word("power plant", "электростанция", SUB_GROUP, MAIN_GROUP, POS)
add_word("oil refinery", "нефтеперерабатывающий завод", SUB_GROUP, MAIN_GROUP, POS)
add_word("coal mine", "угольная шахта", SUB_GROUP, MAIN_GROUP, POS)

profession; trade; occupation; worker; mechanic; electrician; welder; driver; employee; engineer; lawyer; secretary; interpreter; translator; chief; director; manager; minister; ambassador;
SUB_GROUP = "Професcия • Profession"
add_word("profession", "профессия", SUB_GROUP, MAIN_GROUP, POS)
add_word("trade", "ремесло", SUB_GROUP, MAIN_GROUP, POS)
add_word("occupation", "занятие", SUB_GROUP, MAIN_GROUP, POS)
add_word("worker", "рабочий", SUB_GROUP, MAIN_GROUP, POS)
add_word("mechanic", "механик", SUB_GROUP, MAIN_GROUP, POS)
add_word("electrician", "электрик", SUB_GROUP, MAIN_GROUP, POS)
add_word("welder", "сварщик", SUB_GROUP, MAIN_GROUP, POS)
add_word("driver", "водитель", SUB_GROUP, MAIN_GROUP, POS)
add_word("employee", "служащий", SUB_GROUP, MAIN_GROUP, POS)
add_word("engineer", "инженер", SUB_GROUP, MAIN_GROUP, POS)
add_word("lawyer", "юрист", SUB_GROUP, MAIN_GROUP, POS)
add_word("secretary", "секретарь", SUB_GROUP, MAIN_GROUP, POS)
add_word("interpreter", "устный переводчик", SUB_GROUP, MAIN_GROUP, POS)
add_word("translator", "письменный переводчик", SUB_GROUP, MAIN_GROUP, POS)
add_word("chief", "начальник", SUB_GROUP, MAIN_GROUP, POS)
add_word("director", "директор", SUB_GROUP, MAIN_GROUP, POS)
add_word("manager", "менеджер", SUB_GROUP, MAIN_GROUP, POS)
add_word("minister", "министр", SUB_GROUP, MAIN_GROUP, POS)
add_word("ambassador", "посол", SUB_GROUP, MAIN_GROUP, POS)

tool; hammer; axe; drill; scissors; screwdriver; wrench; nail; bolt; screw; wire; spring; equipment; device; accessory; cutter; machinery;
SUB_GROUP = "Инструменты / Оборудование • Tools / Equipment (Beginner)"
add_word("tool", "инструмент", SUB_GROUP, MAIN_GROUP, POS)
add_word("hammer", "молоток", SUB_GROUP, MAIN_GROUP, POS)
add_word("axe", "топор", SUB_GROUP, MAIN_GROUP, POS)
add_word("drill", "дрель", SUB_GROUP, MAIN_GROUP, POS)
add_word("scissors", "ножницы", SUB_GROUP, MAIN_GROUP, POS)
add_word("screwdriver", "отвёртка", SUB_GROUP, MAIN_GROUP, POS)
add_word("wrench", "гаечный ключ", SUB_GROUP, MAIN_GROUP, POS)
add_word("nail", "гвоздь", SUB_GROUP, MAIN_GROUP, POS)
add_word("bolt", "болт", SUB_GROUP, MAIN_GROUP, POS)
add_word("screw", "винт", SUB_GROUP, MAIN_GROUP, POS)
add_word("wire", "проволока", SUB_GROUP, MAIN_GROUP, POS)
add_word("spring", "пружина", SUB_GROUP, MAIN_GROUP, POS)
add_word("equipment", "оборудование", SUB_GROUP, MAIN_GROUP, POS)
add_word("device", "устройство", SUB_GROUP, MAIN_GROUP, POS)
add_word("accessory", "аксессуар", SUB_GROUP, MAIN_GROUP, POS)
add_word("cutter", "резак", SUB_GROUP, MAIN_GROUP, POS)
add_word("machinery", "машины", SUB_GROUP, MAIN_GROUP, POS)

file; plane; pliers; jack; nut; washer; appliance; tongs; pincers; sickle;
SUB_GROUP = "Инструменты / Оборудование • Tools / Equipment (Advanced)"
add_word("file", "напильник", SUB_GROUP, MAIN_GROUP, POS)
add_word("plane", "рубанок", SUB_GROUP, MAIN_GROUP, POS)
add_word("pliers", "плоскогубцы", SUB_GROUP, MAIN_GROUP, POS)
add_word("jack", "домкрат", SUB_GROUP, MAIN_GROUP, POS)
add_word("nut", "гайка", SUB_GROUP, MAIN_GROUP, POS)
add_word("washer", "шайба", SUB_GROUP, MAIN_GROUP, POS)
add_word("appliance", "прибор", SUB_GROUP, MAIN_GROUP, POS)
add_word("tongs", "щипцы", SUB_GROUP, MAIN_GROUP, POS)
add_word("pincers", "кусачки", SUB_GROUP, MAIN_GROUP, POS)
add_word("sickle", "серп", SUB_GROUP, MAIN_GROUP, POS)


MAIN_GROUP = "Связь / Транспорт • Communication / Transport"

post office; general post office; postman; address; addressee; sender; letter; envelope; stamp; printed matter; postal order; parcel;
SUB_GROUP = "Почта • Post"
add_word("post office", "почтовое отделение", SUB_GROUP, MAIN_GROUP, POS)
add_word("general post office", "главпочтамт", SUB_GROUP, MAIN_GROUP, POS)
add_word("postman", "почтальон", SUB_GROUP, MAIN_GROUP, POS)
add_word("address", "адрес", SUB_GROUP, MAIN_GROUP, POS)
add_word("addressee", "адресат", SUB_GROUP, MAIN_GROUP, POS)
add_word("sender", "отправитель", SUB_GROUP, MAIN_GROUP, POS)
add_word("letter", "письмо", SUB_GROUP, MAIN_GROUP, POS)
add_word("envelope", "конверт", SUB_GROUP, MAIN_GROUP, POS)
add_word("stamp", "марка", SUB_GROUP, MAIN_GROUP, POS)
add_word("printed matter", "печать", SUB_GROUP, MAIN_GROUP, POS)
add_word("postal order", "почтовый перевод", SUB_GROUP, MAIN_GROUP, POS)
add_word("parcel", "посылка", SUB_GROUP, MAIN_GROUP, POS)

telegraph; text; charge; phone; dial; receiver; trunk call; international call; directory;
SUB_GROUP = "Телефон • Phone"
add_word("telegraph", "телеграф", SUB_GROUP, MAIN_GROUP, POS)
add_word("text", "текст", SUB_GROUP, MAIN_GROUP, POS)
add_word("charge", "плата", SUB_GROUP, MAIN_GROUP, POS)
add_word("phone", "телефон", SUB_GROUP, MAIN_GROUP, POS)
add_word("dial", "набирать номер", SUB_GROUP, MAIN_GROUP, POS)
add_word("receiver", "трубка", SUB_GROUP, MAIN_GROUP, POS)
add_word("trunk call", "межгородский звонок", SUB_GROUP, MAIN_GROUP, POS)
add_word("international call", "международный звонок", SUB_GROUP, MAIN_GROUP, POS)
add_word("directory", "справочник", SUB_GROUP, MAIN_GROUP, POS)

railway station; platform; track; train; locomotive; ticket collector; porter; guard; departure; arrival; timetable; departures board; upper berth; lower berth
SUB_GROUP = "Железная Дорога • Railway"
add_word("railway station", "железнодорожная станция", SUB_GROUP, MAIN_GROUP, POS)
add_word("platform", "платформа", SUB_GROUP, MAIN_GROUP, POS)
add_word("track", "путь", SUB_GROUP, MAIN_GROUP, POS)
add_word("train", "поезд", SUB_GROUP, MAIN_GROUP, POS)
add_word("locomotive", "локомотив", SUB_GROUP, MAIN_GROUP, POS)
add_word("ticket collector", "кондуктор", SUB_GROUP, MAIN_GROUP, POS)
add_word("porter", "носильщик", SUB_GROUP, MAIN_GROUP, POS)
add_word("guard", "проводник", SUB_GROUP, MAIN_GROUP, POS)
add_word("departure", "отправление", SUB_GROUP, MAIN_GROUP, POS)
add_word("arrival", "прибытие", SUB_GROUP, MAIN_GROUP, POS)
add_word("timetable", "расписание", SUB_GROUP, MAIN_GROUP, POS)
add_word("departures board", "табло отправлений", SUB_GROUP, MAIN_GROUP, POS)
add_word("upper berth", "верхняя полка", SUB_GROUP, MAIN_GROUP, POS)
add_word("lower berth", "нижняя полка", SUB_GROUP, MAIN_GROUP, POS)

passenger train; fast train; express; suburban train; train car; train coach; train carriage; wagon; first class; sleeping car; buffet car; dining car; goods van; tank wagon
SUB_GROUP = "Типы Вагонов и Поездов • Types of Trains and Cars"
add_word("passenger train", "пассажирский поезд", SUB_GROUP, MAIN_GROUP, POS)
add_word("fast train", "скорый поезд", SUB_GROUP, MAIN_GROUP, POS)
add_word("express", "экспресс", SUB_GROUP, MAIN_GROUP, POS)
add_word("suburban train", "пригородный поезд", SUB_GROUP, MAIN_GROUP, POS)
add_word("train car", "вагон", SUB_GROUP, MAIN_GROUP, POS)
add_word("train coach", "купейный вагон", SUB_GROUP, MAIN_GROUP, POS)
add_word("train carriage", "вагон", SUB_GROUP, MAIN_GROUP, POS)
add_word("wagon", "вагон", SUB_GROUP, MAIN_GROUP, POS)
add_word("first class", "первый класс", SUB_GROUP, MAIN_GROUP, POS)
add_word("sleeping car", "спальный вагон", SUB_GROUP, MAIN_GROUP, POS)
add_word("buffet car", "вагон-буфет", SUB_GROUP, MAIN_GROUP, POS)
add_word("dining car", "вагон-ресторан", SUB_GROUP, MAIN_GROUP, POS)
add_word("goods van", "товарный вагон", SUB_GROUP, MAIN_GROUP, POS)
add_word("tank wagon", "цистерна", SUB_GROUP, MAIN_GROUP, POS)

aeroplane; jet plane; propeller-driven aircraft; supersonic airliner; engine; wing; fuselage; tail; undercarriage; cockpit
SUB_GROUP = "Воздушный Транспорт • Air Transport"
add_word("aeroplane", "самолёт", SUB_GROUP, MAIN_GROUP, POS)
add_word("jet plane", "реактивный самолёт", SUB_GROUP, MAIN_GROUP, POS)
add_word("propeller-driven aircraft", "винтовой самолёт", SUB_GROUP, MAIN_GROUP, POS)
add_word("supersonic airliner", "сверхзвуковой авиалайнер", SUB_GROUP, MAIN_GROUP, POS)
add_word("engine", "двигатель", SUB_GROUP, MAIN_GROUP, POS)
add_word("wing", "крыло", SUB_GROUP, MAIN_GROUP, POS)
add_word("fuselage", "фюзеляж", SUB_GROUP, MAIN_GROUP, POS)
add_word("tail", "хвост", SUB_GROUP, MAIN_GROUP, POS)
add_word("undercarriage", "шасси", SUB_GROUP, MAIN_GROUP, POS)
add_word("cockpit", "кабина пилота", SUB_GROUP, MAIN_GROUP, POS)

airport; air terminal; take-off runway; waiting room; departure lounge; crew; pilot; navigator; air hostess; flight; journey; check-in; passport control; boarding; take-off; landing; crash
SUB_GROUP = "В аэропорту • At the Airport"
add_word("airport", "аэропорт", SUB_GROUP, MAIN_GROUP, POS)
add_word("air terminal", "аэровокзал", SUB_GROUP, MAIN_GROUP, POS)
add_word("take-off runway", "взлётная полоса", SUB_GROUP, MAIN_GROUP, POS)
add_word("waiting room", "зал ожидания", SUB_GROUP, MAIN_GROUP, POS)
add_word("departure lounge", "зал отправления", SUB_GROUP, MAIN_GROUP, POS)
add_word("crew", "экипаж", SUB_GROUP, MAIN_GROUP, POS)
add_word("pilot", "пилот", SUB_GROUP, MAIN_GROUP, POS)
add_word("navigator", "штурман", SUB_GROUP, MAIN_GROUP, POS)
add_word("air hostess", "стюардесса", SUB_GROUP, MAIN_GROUP, POS)
add_word("flight", "рейс", SUB_GROUP, MAIN_GROUP, POS)
add_word("journey", "путешествие", SUB_GROUP, MAIN_GROUP, POS)
add_word("check-in", "регистрация", SUB_GROUP, MAIN_GROUP, POS)
add_word("passport control", "паспортный контроль", SUB_GROUP, MAIN_GROUP, POS)
add_word("boarding", "посадка", SUB_GROUP, MAIN_GROUP, POS)
add_word("take-off", "взлёт", SUB_GROUP, MAIN_GROUP, POS)
add_word("landing", "посадка", SUB_GROUP, MAIN_GROUP, POS)
add_word("crash", "авария", SUB_GROUP, MAIN_GROUP, POS)

vehicle; car; bus; truck; tanker; road; highway; motorway; crossroads; bridge; flyover; underpass; guardrail
SUB_GROUP = "Vehicle Types and Infrastructure"
add_word("vehicle", "транспортное средство", SUB_GROUP, MAIN_GROUP, POS)
add_word("car", "автомобиль", SUB_GROUP, MAIN_GROUP, POS)
add_word("bus", "автобус", SUB_GROUP, MAIN_GROUP, POS)
add_word("truck", "грузовик", SUB_GROUP, MAIN_GROUP, POS)
add_word("tanker", "цистерна", SUB_GROUP, MAIN_GROUP, POS)
add_word("road", "дорога", SUB_GROUP, MAIN_GROUP, POS)
add_word("highway", "шоссе", SUB_GROUP, MAIN_GROUP, POS)
add_word("motorway", "автомагистраль", SUB_GROUP, MAIN_GROUP, POS)
add_word("crossroads", "перекрёсток", SUB_GROUP, MAIN_GROUP, POS)
add_word("bridge", "мост", SUB_GROUP, MAIN_GROUP, POS)
add_word("flyover", "эстакада", SUB_GROUP, MAIN_GROUP, POS)
add_word("underpass", "подземный переход", SUB_GROUP, MAIN_GROUP, POS)
add_word("guardrail", "ограждение", SUB_GROUP, MAIN_GROUP, POS)

traffic; traffic sign; road marking; pedestrian crossing; traffic lights; starting; braking; acceleration; car service; gas station; car wash
SUB_GROUP = "Traffic and Road Usage"
add_word("traffic", "транспортное движение", SUB_GROUP, MAIN_GROUP, POS)
add_word("traffic sign", "дорожный знак", SUB_GROUP, MAIN_GROUP, POS)
add_word("road marking", "дорожная разметка", SUB_GROUP, MAIN_GROUP, POS)
add_word("pedestrian crossing", "пешеходный переход", SUB_GROUP, MAIN_GROUP, POS)
add_word("traffic lights", "светофор", SUB_GROUP, MAIN_GROUP, POS)
add_word("starting", "треск", SUB_GROUP, MAIN_GROUP, POS)
add_word("braking", "торможение", SUB_GROUP, MAIN_GROUP, POS)
add_word("acceleration", "ускорение", SUB_GROUP, MAIN_GROUP, POS)
add_word("car service", "автосервис", SUB_GROUP, MAIN_GROUP, POS)
add_word("gas station", "заправочная станция", SUB_GROUP, MAIN_GROUP, POS)
add_word("car wash", "мойка автомобилей", SUB_GROUP, MAIN_GROUP, POS)

spare part; hood; headlight; license plate; windshield; wipers; tire; trunk; exhaust pipe; steering wheel; seat belt; gear lever; clutch; brake pedal; accelerator; ignition; fuel gauge; horn; engine; radiator; battery; spare wheel
SUB_GROUP = "Car parts"
add_word("spare part", "запасная часть", SUB_GROUP, MAIN_GROUP, POS)
add_word("hood", "капот", SUB_GROUP, MAIN_GROUP, POS)
add_word("headlight", "фара", SUB_GROUP, MAIN_GROUP, POS)
add_word("license plate", "номерной знак", SUB_GROUP, MAIN_GROUP, POS)
add_word("windshield", "лобовое стекло", SUB_GROUP, MAIN_GROUP, POS)
add_word("wipers", "стеклоочистители", SUB_GROUP, MAIN_GROUP, POS)
add_word("tire", "шина", SUB_GROUP, MAIN_GROUP, POS)
add_word("trunk", "багажник", SUB_GROUP, MAIN_GROUP, POS)
add_word("exhaust pipe", "выхлопная труба", SUB_GROUP, MAIN_GROUP, POS)
add_word("steering wheel", "руль", SUB_GROUP, MAIN_GROUP, POS)
add_word("seat belt", "ремень безопасности", SUB_GROUP, MAIN_GROUP, POS)
add_word("gear lever", "рычаг переключения передач", SUB_GROUP, MAIN_GROUP, POS)
add_word("clutch", "сцепление", SUB_GROUP, MAIN_GROUP, POS)
add_word("brake pedal", "педаль тормоза", SUB_GROUP, MAIN_GROUP, POS)
add_word("accelerator", "педаль газа", SUB_GROUP, MAIN_GROUP, POS)
add_word("ignition", "зажигание", SUB_GROUP, MAIN_GROUP, POS)
add_word("fuel gauge", "указатель топлива", SUB_GROUP, MAIN_GROUP, POS)
add_word("horn", "гудок", SUB_GROUP, MAIN_GROUP, POS)
add_word("engine", "двигатель", SUB_GROUP, MAIN_GROUP, POS)
add_word("radiator", "радиатор", SUB_GROUP, MAIN_GROUP, POS)
add_word("battery", "аккумулятор", SUB_GROUP, MAIN_GROUP, POS)
add_word("spare wheel", "запасное колесо", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Город • City"

city; town; village; street; lane; avenue; square; building; corner; pavement;
SUB_GROUP = "Улицы • Streets"
add_word("city", "город", SUB_GROUP, MAIN_GROUP, POS)
add_word("town", "городок", SUB_GROUP, MAIN_GROUP, POS)
add_word("village", "деревня", SUB_GROUP, MAIN_GROUP, POS)
add_word("street", "улица", SUB_GROUP, MAIN_GROUP, POS)
add_word("lane", "переулок", SUB_GROUP, MAIN_GROUP, POS)
add_word("avenue", "проспект", SUB_GROUP, MAIN_GROUP, POS)
add_word("square", "площадь", SUB_GROUP, MAIN_GROUP, POS)
add_word("building", "здание", SUB_GROUP, MAIN_GROUP, POS)
add_word("corner", "угол", SUB_GROUP, MAIN_GROUP, POS)
add_word("pavement", "тротуар", SUB_GROUP, MAIN_GROUP, POS)

tram; metro; underground; subway; car; taxi; conductor; ticket; seat;
SUB_GROUP = "Транспорт • Transport"
add_word("tram", "трамвай", SUB_GROUP, MAIN_GROUP, POS)
add_word("metro", "метро", SUB_GROUP, MAIN_GROUP, POS)
add_word("underground", "метро", SUB_GROUP, MAIN_GROUP, POS)
add_word("subway", "метро", SUB_GROUP, MAIN_GROUP, POS)
add_word("car", "автомобиль", SUB_GROUP, MAIN_GROUP, POS)
add_word("taxi", "такси", SUB_GROUP, MAIN_GROUP, POS)
add_word("conductor", "кондуктор", SUB_GROUP, MAIN_GROUP, POS)
add_word("ticket", "билет", SUB_GROUP, MAIN_GROUP, POS)
add_word("seat", "место", SUB_GROUP, MAIN_GROUP, POS)

cinema; theatre; museum; gallery; circus; restaurant; bar; cafe; club; park; church; hotel;
SUB_GROUP = "Культурные Учреждения • Social and Cultural institutions"
add_word("cinema", "кинотеатр", SUB_GROUP, MAIN_GROUP, POS)
add_word("theatre", "театр", SUB_GROUP, MAIN_GROUP, POS)
add_word("museum", "музей", SUB_GROUP, MAIN_GROUP, POS)
add_word("gallery", "галерея", SUB_GROUP, MAIN_GROUP, POS)
add_word("circus", "цирк", SUB_GROUP, MAIN_GROUP, POS)
add_word("restaurant", "ресторан", SUB_GROUP, MAIN_GROUP, POS)
add_word("bar", "бар", SUB_GROUP, MAIN_GROUP, POS)
add_word("cafe", "кафе", SUB_GROUP, MAIN_GROUP, POS)
add_word("club", "клуб", SUB_GROUP, MAIN_GROUP, POS)
add_word("park", "парк", SUB_GROUP, MAIN_GROUP, POS)
add_word("church", "церковь", SUB_GROUP, MAIN_GROUP, POS)
add_word("hotel", "отель", SUB_GROUP, MAIN_GROUP, POS)


MAIN_GROUP = "Общение • Communication"

deal; information; report; rumours; news; truth; lie; white lie;
SUB_GROUP = "Информация • Information"
add_word("deal", "сделка", SUB_GROUP, MAIN_GROUP, POS)
add_word("information", "информация", SUB_GROUP, MAIN_GROUP, POS)
add_word("report", "отчет", SUB_GROUP, MAIN_GROUP, POS)
add_word("rumours", "слухи", SUB_GROUP, MAIN_GROUP, POS)
add_word("news", "новости", SUB_GROUP, MAIN_GROUP, POS)
add_word("truth", "правда", SUB_GROUP, MAIN_GROUP, POS)
add_word("lie", "ложь", SUB_GROUP, MAIN_GROUP, POS)
add_word("white lie", "маленькая ложь", SUB_GROUP, MAIN_GROUP, POS)

mother tongue; foreign language; meaning; accent; dialect; slang; conversation; dialogue; dispute; discussion; question; answer; advice; warning; request; demand; observation; remark; reaction; consent; permission; promise; comment; aid; assistance; help; objection; prohibition; refusal; understanding
SUB_GROUP = "Общение / Высказывание • Communication / Expression"
add_word("mother tongue", "родной язык", SUB_GROUP, MAIN_GROUP, POS)
add_word("foreign language", "иностранный язык", SUB_GROUP, MAIN_GROUP, POS)
add_word("meaning", "значение", SUB_GROUP, MAIN_GROUP, POS)
add_word("accent", "акцент", SUB_GROUP, MAIN_GROUP, POS)
add_word("dialect", "диалект", SUB_GROUP, MAIN_GROUP, POS)
add_word("slang", "жаргон", SUB_GROUP, MAIN_GROUP, POS)
add_word("conversation", "разговор", SUB_GROUP, MAIN_GROUP, POS)
add_word("dialogue", "диалог", SUB_GROUP, MAIN_GROUP, POS)
add_word("dispute", "спор", SUB_GROUP, MAIN_GROUP, POS)
add_word("discussion", "обсуждение", SUB_GROUP, MAIN_GROUP, POS)
add_word("question", "вопрос", SUB_GROUP, MAIN_GROUP, POS)
add_word("answer", "ответ", SUB_GROUP, MAIN_GROUP, POS)
add_word("advice", "совет", SUB_GROUP, MAIN_GROUP, POS)
add_word("warning", "предупреждение", SUB_GROUP, MAIN_GROUP, POS)
add_word("request", "просьба", SUB_GROUP, MAIN_GROUP, POS)
add_word("demand", "требование", SUB_GROUP, MAIN_GROUP, POS)
add_word("observation", "наблюдение", SUB_GROUP, MAIN_GROUP, POS)
add_word("remark", "замечание", SUB_GROUP, MAIN_GROUP, POS)
add_word("reaction", "реакция", SUB_GROUP, MAIN_GROUP, POS)
add_word("consent", "согласие", SUB_GROUP, MAIN_GROUP, POS)
add_word("permission", "разрешение", SUB_GROUP, MAIN_GROUP, POS)
add_word("promise", "обещание", SUB_GROUP, MAIN_GROUP, POS)
add_word("comment", "комментарий", SUB_GROUP, MAIN_GROUP, POS)
add_word("aid", "помощь", SUB_GROUP, MAIN_GROUP, POS)
add_word("assistance", "помощь", SUB_GROUP, MAIN_GROUP, POS)
add_word("help", "помощь", SUB_GROUP, MAIN_GROUP, POS)
add_word("objection", "возражение", SUB_GROUP, MAIN_GROUP, POS)
add_word("prohibition", "запрет", SUB_GROUP, MAIN_GROUP, POS)
add_word("refusal", "отказ", SUB_GROUP, MAIN_GROUP, POS)
add_word("understanding", "понимание", SUB_GROUP, MAIN_GROUP, POS)

visit; meeting; reception; invitation; host; guest; greeting; welcome; handshake; farewell; etiquette; behaviour
SUB_GROUP = "Визит • Visit"
add_word("visit", "визит", SUB_GROUP, MAIN_GROUP, POS)
add_word("meeting", "встреча", SUB_GROUP, MAIN_GROUP, POS)
add_word("reception", "прием", SUB_GROUP, MAIN_GROUP, POS)
add_word("invitation", "приглашение", SUB_GROUP, MAIN_GROUP, POS)
add_word("host", "хозяин", SUB_GROUP, MAIN_GROUP, POS)
add_word("guest", "гость", SUB_GROUP, MAIN_GROUP, POS)
add_word("greeting", "приветствие", SUB_GROUP, MAIN_GROUP, POS)
add_word("welcome", "приветствовать", SUB_GROUP, MAIN_GROUP, POS)
add_word("handshake", "рукопожатие", SUB_GROUP, MAIN_GROUP, POS)
add_word("farewell", "прощание", SUB_GROUP, MAIN_GROUP, POS)
add_word("etiquette", "этикет", SUB_GROUP, MAIN_GROUP, POS)
add_word("behaviour", "поведение", SUB_GROUP, MAIN_GROUP, POS)


MAIN_GROUP = "Государство • State"

country; state; capital; border; flag; democracy
territory; anthem; social system; socialism; capitalism; civilization
SUB_GROUP = "Государство • State"
add_word("country", "страна", SUB_GROUP, MAIN_GROUP, POS)
add_word("state", "государство", SUB_GROUP, MAIN_GROUP, POS)
add_word("capital", "столица", SUB_GROUP, MAIN_GROUP, POS)
add_word("border", "граница", SUB_GROUP, MAIN_GROUP, POS)
add_word("flag", "флаг", SUB_GROUP, MAIN_GROUP, POS)
add_word("democracy", "демократия", SUB_GROUP, MAIN_GROUP, POS)
add_word("territory", "территория", SUB_GROUP, MAIN_GROUP, POS)
add_word("anthem", "гимн", SUB_GROUP, MAIN_GROUP, POS)
add_word("social system", "социальная система", SUB_GROUP, MAIN_GROUP, POS)
add_word("socialism", "социализм", SUB_GROUP, MAIN_GROUP, POS)
add_word("capitalism", "капитализм", SUB_GROUP, MAIN_GROUP, POS)
add_word("civilization", "цивилизация", SUB_GROUP, MAIN_GROUP, POS)

people; population; nationality; nation; custom; habit; motherland; patriot; glory; hero; religion; faith; church; christian; muslim; buddhist; catholic; protestant
SUB_GROUP = "Народ • People"
add_word("people", "народ", SUB_GROUP, MAIN_GROUP, POS)
add_word("population", "население", SUB_GROUP, MAIN_GROUP, POS)
add_word("nationality", "национальность", SUB_GROUP, MAIN_GROUP, POS)
add_word("nation", "нация", SUB_GROUP, MAIN_GROUP, POS)
add_word("custom", "обычай", SUB_GROUP, MAIN_GROUP, POS)
add_word("habit", "привычка", SUB_GROUP, MAIN_GROUP, POS)
add_word("motherland", "родина", SUB_GROUP, MAIN_GROUP, POS)
add_word("patriot", "патриот", SUB_GROUP, MAIN_GROUP, POS)
add_word("glory", "слава", SUB_GROUP, MAIN_GROUP, POS)
add_word("hero", "герой", SUB_GROUP, MAIN_GROUP, POS)
add_word("religion", "религия", SUB_GROUP, MAIN_GROUP, POS)
add_word("faith", "вера", SUB_GROUP, MAIN_GROUP, POS)
add_word("church", "церковь", SUB_GROUP, MAIN_GROUP, POS)
add_word("christian", "христианин", SUB_GROUP, MAIN_GROUP, POS)
add_word("muslim", "мусульманин", SUB_GROUP, MAIN_GROUP, POS)
add_word("buddhist", "буддист", SUB_GROUP, MAIN_GROUP, POS)
add_word("catholic", "католик", SUB_GROUP, MAIN_GROUP, POS)
add_word("protestant", "протестант", SUB_GROUP, MAIN_GROUP, POS)

social status; worker; peasant; owner; landlord; capitalist
SUB_GROUP = "Социальный Статус • Social Status"
add_word("social status", "социальный статус", SUB_GROUP, MAIN_GROUP, POS)
add_word("worker", "рабочий", SUB_GROUP, MAIN_GROUP, POS)
add_word("peasant", "крестьянин", SUB_GROUP, MAIN_GROUP, POS)
add_word("owner", "владелец", SUB_GROUP, MAIN_GROUP, POS)
add_word("landlord", "землевладелец", SUB_GROUP, MAIN_GROUP, POS)
add_word("capitalist", "капиталист", SUB_GROUP, MAIN_GROUP, POS)

justice; equality; right; human rights; duty; discrimination; violence; protest; law; police; lawyer; crime; criminal; court; judge; sentence; punishment; penalty; fine; jail; prison; obligation; oppression; offence; public prosecutor
SUB_GROUP = "Закон / Право • Law"
add_word("justice", "справедливость", SUB_GROUP, MAIN_GROUP, POS)
add_word("equality", "равенство", SUB_GROUP, MAIN_GROUP, POS)
add_word("right", "право", SUB_GROUP, MAIN_GROUP, POS)
add_word("human rights", "права человека", SUB_GROUP, MAIN_GROUP, POS)
add_word("duty", "обязанность", SUB_GROUP, MAIN_GROUP, POS)
add_word("discrimination", "дискриминация", SUB_GROUP, MAIN_GROUP, POS)
add_word("violence", "насилие", SUB_GROUP, MAIN_GROUP, POS)
add_word("protest", "протест", SUB_GROUP, MAIN_GROUP, POS)
add_word("law", "закон", SUB_GROUP, MAIN_GROUP, POS)
add_word("police", "полиция", SUB_GROUP, MAIN_GROUP, POS)
add_word("lawyer", "адвокат", SUB_GROUP, MAIN_GROUP, POS)
add_word("crime", "преступление", SUB_GROUP, MAIN_GROUP, POS)
add_word("criminal", "преступник", SUB_GROUP, MAIN_GROUP, POS)
add_word("court", "суд", SUB_GROUP, MAIN_GROUP, POS)
add_word("judge", "судья", SUB_GROUP, MAIN_GROUP, POS)
add_word("sentence", "приговор", SUB_GROUP, MAIN_GROUP, POS)
add_word("punishment", "наказание", SUB_GROUP, MAIN_GROUP, POS)
add_word("penalty", "штраф", SUB_GROUP, MAIN_GROUP, POS)
add_word("fine", "штраф", SUB_GROUP, MAIN_GROUP, POS)
add_word("jail", "тюрьма", SUB_GROUP, MAIN_GROUP, POS)
add_word("prison", "тюрьма", SUB_GROUP, MAIN_GROUP, POS)
add_word("obligation", "обязательство", SUB_GROUP, MAIN_GROUP, POS)
add_word("oppression", "угнетение", SUB_GROUP, MAIN_GROUP, POS)
add_word("offence", "правонарушение", SUB_GROUP, MAIN_GROUP, POS)
add_word("public prosecutor", "прокурор", SUB_GROUP, MAIN_GROUP, POS)

government; republic; parliament; president; election; constitution; article; party; trade union; congress; conference; discussion; program; monarchy; king; queen; emperor; dictatorship; reform; revolution
SUB_GROUP = "Политика • Politics"
add_word("government", "правительство", SUB_GROUP, MAIN_GROUP, POS)
add_word("republic", "республика", SUB_GROUP, MAIN_GROUP, POS)
add_word("parliament", "парламент", SUB_GROUP, MAIN_GROUP, POS)
add_word("president", "президент", SUB_GROUP, MAIN_GROUP, POS)
add_word("election", "выборы", SUB_GROUP, MAIN_GROUP, POS)
add_word("constitution", "конституция", SUB_GROUP, MAIN_GROUP, POS)
add_word("article", "статья", SUB_GROUP, MAIN_GROUP, POS)
add_word("party", "партия", SUB_GROUP, MAIN_GROUP, POS)
add_word("trade union", "профсоюз", SUB_GROUP, MAIN_GROUP, POS)
add_word("congress", "конгресс", SUB_GROUP, MAIN_GROUP, POS)
add_word("conference", "конференция", SUB_GROUP, MAIN_GROUP, POS)
add_word("discussion", "обсуждение", SUB_GROUP, MAIN_GROUP, POS)
add_word("program", "программа", SUB_GROUP, MAIN_GROUP, POS)
add_word("monarchy", "монархия", SUB_GROUP, MAIN_GROUP, POS)
add_word("king", "король", SUB_GROUP, MAIN_GROUP, POS)
add_word("queen", "королева", SUB_GROUP, MAIN_GROUP, POS)
add_word("emperor", "император", SUB_GROUP, MAIN_GROUP, POS)
add_word("dictatorship", "диктатура", SUB_GROUP, MAIN_GROUP, POS)
add_word("reform", "реформа", SUB_GROUP, MAIN_GROUP, POS)
add_word("revolution", "революция", SUB_GROUP, MAIN_GROUP, POS)

economics; statistics; economy; national income; wealth; finance; budget; tax; money; living standard; private property; bank; account; cash; free of charge; debt; price; increase; decrease; foreign trade; contract; customs; inspection; duty
SUB_GROUP = "Экономика • Economy"
add_word("economics", "экономика", SUB_GROUP, MAIN_GROUP, POS)
add_word("statistics", "статистика", SUB_GROUP, MAIN_GROUP, POS)
add_word("economy", "хозяйство", SUB_GROUP, MAIN_GROUP, POS)
add_word("national income", "национальный доход", SUB_GROUP, MAIN_GROUP, POS)
add_word("wealth", "богатство", SUB_GROUP, MAIN_GROUP, POS)
add_word("finance", "финансы", SUB_GROUP, MAIN_GROUP, POS)
add_word("budget", "бюджет", SUB_GROUP, MAIN_GROUP, POS)
add_word("tax", "налог", SUB_GROUP, MAIN_GROUP, POS)
add_word("money", "деньги", SUB_GROUP, MAIN_GROUP, POS)
add_word("living standard", "уровень жизни", SUB_GROUP, MAIN_GROUP, POS)
add_word("private property", "частная собственность", SUB_GROUP, MAIN_GROUP, POS)
add_word("bank", "банк", SUB_GROUP, MAIN_GROUP, POS)
add_word("account", "счёт", SUB_GROUP, MAIN_GROUP, POS)
add_word("cash", "наличные", SUB_GROUP, MAIN_GROUP, POS)
add_word("free of charge", "бесплатно", SUB_GROUP, MAIN_GROUP, POS)
add_word("debt", "долг", SUB_GROUP, MAIN_GROUP, POS)
add_word("price", "цена", SUB_GROUP, MAIN_GROUP, POS)
add_word("increase", "увеличение", SUB_GROUP, MAIN_GROUP, POS)
add_word("decrease", "уменьшение", SUB_GROUP, MAIN_GROUP, POS)
add_word("foreign trade", "внешняя торговля", SUB_GROUP, MAIN_GROUP, POS)
add_word("contract", "контракт", SUB_GROUP, MAIN_GROUP, POS)
add_word("customs", "таможня", SUB_GROUP, MAIN_GROUP, POS)
add_word("inspection", "инспекция", SUB_GROUP, MAIN_GROUP, POS)
add_word("duty", "пошлина", SUB_GROUP, MAIN_GROUP, POS)

foreign policy; peaceful coexistence; mutual assistance; cooperation; interference; intervention; aggression; diplomacy; negotiations; talks; treaty; citizen; citizenship; permanent residence; visa
SUB_GROUP = "Внешняя Политика • Foreign Policy"
add_word("foreign policy", "внешняя политика", SUB_GROUP, MAIN_GROUP, POS)
add_word("peaceful coexistence", "мирное сосуществование", SUB_GROUP, MAIN_GROUP, POS)
add_word("mutual assistance", "взаимная помощь", SUB_GROUP, MAIN_GROUP, POS)
add_word("cooperation", "сотрудничество", SUB_GROUP, MAIN_GROUP, POS)
add_word("interference", "вмешательство", SUB_GROUP, MAIN_GROUP, POS)
add_word("intervention", "интервенция", SUB_GROUP, MAIN_GROUP, POS)
add_word("aggression", "агрессия", SUB_GROUP, MAIN_GROUP, POS)
add_word("diplomacy", "дипломатия", SUB_GROUP, MAIN_GROUP, POS)
add_word("negotiations", "переговоры", SUB_GROUP, MAIN_GROUP, POS)
add_word("talks", "беседы", SUB_GROUP, MAIN_GROUP, POS)
add_word("treaty", "договор", SUB_GROUP, MAIN_GROUP, POS)
add_word("citizen", "гражданин", SUB_GROUP, MAIN_GROUP, POS)
add_word("citizenship", "гражданство", SUB_GROUP, MAIN_GROUP, POS)
add_word("permanent residence", "постоянное проживание", SUB_GROUP, MAIN_GROUP, POS)
add_word("visa", "виза", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Медицина • Medicine"

health; hygiene; preventive measures; health hazard; alcohol consumption; smoking; obesity; weight loss; illness; disease; recovery; death
SUB_GROUP = "Здоровье / болезнь • Health / Illness"
add_word("health", "здоровье", SUB_GROUP, MAIN_GROUP, POS)
add_word("hygiene", "гигиена", SUB_GROUP, MAIN_GROUP, POS)
add_word("preventive measures", "профилактические меры", SUB_GROUP, MAIN_GROUP, POS)
add_word("health hazard", "опасность для здоровья", SUB_GROUP, MAIN_GROUP, POS)
add_word("alcohol consumption", "употребление алкоголя", SUB_GROUP, MAIN_GROUP, POS)
add_word("smoking", "курение", SUB_GROUP, MAIN_GROUP, POS)
add_word("obesity", "ожирение", SUB_GROUP, MAIN_GROUP, POS)
add_word("weight loss", "потеря веса", SUB_GROUP, MAIN_GROUP, POS)
add_word("illness", "болезнь", SUB_GROUP, MAIN_GROUP, POS)
add_word("disease", "заболевание", SUB_GROUP, MAIN_GROUP, POS)
add_word("recovery", "выздоровление", SUB_GROUP, MAIN_GROUP, POS)
add_word("death", "смерть", SUB_GROUP, MAIN_GROUP, POS)

injury; wound; bruise; fracture; burn; ulcer; rash; abscess; sore
SUB_GROUP = "Наружные повреждения • Injuries"
add_word("injury", "травма", SUB_GROUP, MAIN_GROUP, POS)
add_word("wound", "рана", SUB_GROUP, MAIN_GROUP, POS)
add_word("bruise", "ушиб", SUB_GROUP, MAIN_GROUP, POS)
add_word("fracture", "перелом", SUB_GROUP, MAIN_GROUP, POS)
add_word("burn", "ожог", SUB_GROUP, MAIN_GROUP, POS)
add_word("ulcer", "язва", SUB_GROUP, MAIN_GROUP, POS)
add_word("rash", "сыпь", SUB_GROUP, MAIN_GROUP, POS)
add_word("abscess", "абсцесс", SUB_GROUP, MAIN_GROUP, POS)
add_word("sore", "язвочка", SUB_GROUP, MAIN_GROUP, POS)

infection; contagious disease; plague; flu;
SUB_GROUP = "Инфекции • Infections"
add_word("infection", "инфекция", SUB_GROUP, MAIN_GROUP, POS)
add_word("contagious disease", "заразное заболевание", SUB_GROUP, MAIN_GROUP, POS)
add_word("plague", "чума", SUB_GROUP, MAIN_GROUP, POS)
add_word("flu", "грипп", SUB_GROUP, MAIN_GROUP, POS)

mental disease; neurological disease; neurosis; allergy; AIDS; cancer
SUB_GROUP = "Остальные Заболевания • Other Diseases"
add_word("mental disease", "психическое заболевание", SUB_GROUP, MAIN_GROUP, POS)
add_word("neurological disease", "неврологическое заболевание", SUB_GROUP, MAIN_GROUP, POS)
add_word("neurosis", "невроз", SUB_GROUP, MAIN_GROUP, POS)
add_word("allergy", "аллергия", SUB_GROUP, MAIN_GROUP, POS)
add_word("AIDS", "СПИД", SUB_GROUP, MAIN_GROUP, POS)
add_word("cancer", "рак", SUB_GROUP, MAIN_GROUP, POS)

symptom; fever; blood pressure; dizziness; sweating; cough; sickness; diarrhea; ache; headache; toothache
SUB_GROUP = "Симптомы • Symptoms"
add_word("symptom", "симптом", SUB_GROUP, MAIN_GROUP, POS)
add_word("fever", "лихорадка", SUB_GROUP, MAIN_GROUP, POS)
add_word("blood pressure", "кровяное давление", SUB_GROUP, MAIN_GROUP, POS)
add_word("dizziness", "головокружение", SUB_GROUP, MAIN_GROUP, POS)
add_word("sweating", "потоотделение", SUB_GROUP, MAIN_GROUP, POS)
add_word("cough", "кашель", SUB_GROUP, MAIN_GROUP, POS)
add_word("sickness", "тошнота", SUB_GROUP, MAIN_GROUP, POS)
add_word("diarrhea", "понос", SUB_GROUP, MAIN_GROUP, POS)
add_word("ache", "боль", SUB_GROUP, MAIN_GROUP, POS)
add_word("headache", "головная боль", SUB_GROUP, MAIN_GROUP, POS)
add_word("toothache", "зубная боль", SUB_GROUP, MAIN_GROUP, POS)

medical examination; blood test; urine test; x ray; treatment; therapy; operation; anaesthesia; injection; medicine; drug; bandage; drugstore; pharmacy; prescription
SUB_GROUP = "Лечение • Treatment"
add_word("medical examination", "медицинское обследование", SUB_GROUP, MAIN_GROUP, POS)
add_word("blood test", "анализ крови", SUB_GROUP, MAIN_GROUP, POS)
add_word("urine test", "анализ мочи", SUB_GROUP, MAIN_GROUP, POS)
add_word("x ray", "рентген", SUB_GROUP, MAIN_GROUP, POS)
add_word("treatment", "лечение", SUB_GROUP, MAIN_GROUP, POS)
add_word("therapy", "терапия", SUB_GROUP, MAIN_GROUP, POS)
add_word("operation", "операция", SUB_GROUP, MAIN_GROUP, POS)
add_word("anaesthesia", "анестезия", SUB_GROUP, MAIN_GROUP, POS)
add_word("injection", "инъекция", SUB_GROUP, MAIN_GROUP, POS)
add_word("medicine", "лекарство", SUB_GROUP, MAIN_GROUP, POS)
add_word("drug", "препарат", SUB_GROUP, MAIN_GROUP, POS)
add_word("bandage", "повязка", SUB_GROUP, MAIN_GROUP, POS)
add_word("drugstore", "аптека", SUB_GROUP, MAIN_GROUP, POS)
add_word("pharmacy", "фармация", SUB_GROUP, MAIN_GROUP, POS)
add_word("prescription", "рецепт", SUB_GROUP, MAIN_GROUP, POS)

ambulance; hospital; clinic; doctor; surgeon; psychiatrist; dentist; eye doctor; nurse; patient
SUB_GROUP = "Больница • Hospital"
add_word("ambulance", "скорая помощь", SUB_GROUP, MAIN_GROUP, POS)
add_word("hospital", "больница", SUB_GROUP, MAIN_GROUP, POS)
add_word("clinic", "клиника", SUB_GROUP, MAIN_GROUP, POS)
add_word("doctor", "врач", SUB_GROUP, MAIN_GROUP, POS)
add_word("surgeon", "хирург", SUB_GROUP, MAIN_GROUP, POS)
add_word("psychiatrist", "психиатр", SUB_GROUP, MAIN_GROUP, POS)
add_word("dentist", "стоматолог", SUB_GROUP, MAIN_GROUP, POS)
add_word("eye doctor", "окулист", SUB_GROUP, MAIN_GROUP, POS)
add_word("nurse", "медсестра", SUB_GROUP, MAIN_GROUP, POS)
add_word("patient", "пациент", SUB_GROUP, MAIN_GROUP, POS)


# ADJECTIVES
POS = "adjectives"

MAIN_GROUP = "Органы чувств • Organs of senses"

dark ; light ; colourless ; transparent ; opaque ; bright ; brilliant ; pale ; dim ; distinct
large ; big ; huge ; wide ; broad ; thick ; long ; tall ; deep ; little ; small ; narrow ;
thin ; short ; shallow ; low ; far ; near
flat ; plane ; straight ; curved ; vertical ; horizontal ; round ; square

SUB_GROUP = "Глаза • Eye"
add_word("dark", "тёмный", SUB_GROUP, MAIN_GROUP, POS)
add_word("light", "светлый", SUB_GROUP, MAIN_GROUP, POS)
add_word("colourless", "бесцветный", SUB_GROUP, MAIN_GROUP, POS)
add_word("transparent", "прозрачный", SUB_GROUP, MAIN_GROUP, POS)
add_word("opaque", "непрозрачный", SUB_GROUP, MAIN_GROUP, POS)
add_word("bright", "яркий", SUB_GROUP, MAIN_GROUP, POS)
add_word("brilliant", "блестящий", SUB_GROUP, MAIN_GROUP, POS)
add_word("pale", "бледный", SUB_GROUP, MAIN_GROUP, POS)
add_word("dim", "тусклый", SUB_GROUP, MAIN_GROUP, POS)
add_word("distinct", "чёткий", SUB_GROUP, MAIN_GROUP, POS)
add_word("large", "большой", SUB_GROUP, MAIN_GROUP, POS)
add_word("big", "крупный", SUB_GROUP, MAIN_GROUP, POS)
add_word("huge", "огромный", SUB_GROUP, MAIN_GROUP, POS)
add_word("wide", "широкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("broad", "обширный", SUB_GROUP, MAIN_GROUP, POS)
add_word("thick", "толстый", SUB_GROUP, MAIN_GROUP, POS)
add_word("long", "длинный", SUB_GROUP, MAIN_GROUP, POS)
add_word("tall", "высокий", SUB_GROUP, MAIN_GROUP, POS)
add_word("deep", "глубокий", SUB_GROUP, MAIN_GROUP, POS)
add_word("little", "маленький", SUB_GROUP, MAIN_GROUP, POS)
add_word("small", "небольшой", SUB_GROUP, MAIN_GROUP, POS)
add_word("narrow", "узкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("thin", "тонкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("short", "короткий", SUB_GROUP, MAIN_GROUP, POS)
add_word("shallow", "мелкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("low", "низкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("far", "далекий", SUB_GROUP, MAIN_GROUP, POS)
add_word("near", "близкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("flat", "плоский", SUB_GROUP, MAIN_GROUP, POS)
add_word("plane", "ровный", SUB_GROUP, MAIN_GROUP, POS)
add_word("straight", "прямой", SUB_GROUP, MAIN_GROUP, POS)
add_word("curved", "изогнутый", SUB_GROUP, MAIN_GROUP, POS)
add_word("vertical", "вертикальный", SUB_GROUP, MAIN_GROUP, POS)
add_word("horizontal", "горизонтальный", SUB_GROUP, MAIN_GROUP, POS)
add_word("round", "круглый", SUB_GROUP, MAIN_GROUP, POS)
add_word("square", "квадратный", SUB_GROUP, MAIN_GROUP, POS)

uneven ; even ; smooth ; rough ; hard ; soft ; sharp ; blunt
dry; wet; humid
SUB_GROUP = "Кожа • Skin"
add_word("uneven", "неровный", SUB_GROUP, MAIN_GROUP, POS)
add_word("even", "ровный", SUB_GROUP, MAIN_GROUP, POS)
add_word("smooth", "гладкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("rough", "шероховатый", SUB_GROUP, MAIN_GROUP, POS)
add_word("hard", "твердый", SUB_GROUP, MAIN_GROUP, POS)
add_word("soft", "мягкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("sharp", "острый", SUB_GROUP, MAIN_GROUP, POS)
add_word("blunt", "тупой", SUB_GROUP, MAIN_GROUP, POS)
add_word("dry", "сухой", SUB_GROUP, MAIN_GROUP, POS)
add_word("wet", "мокрый", SUB_GROUP, MAIN_GROUP, POS)
add_word("humid", "влажный", SUB_GROUP, MAIN_GROUP, POS)

tasty ; delicious ; tasteless ; sweet ; sour ; salty ; bitter ; strong ; pungent
SUB_GROUP = "Язык • Tongue"
add_word("tasty", "вкусный", SUB_GROUP, MAIN_GROUP, POS)
add_word("delicious", "восхитительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("tasteless", "безвкусный", SUB_GROUP, MAIN_GROUP, POS)
add_word("sweet", "сладкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("sour", "кислый", SUB_GROUP, MAIN_GROUP, POS)
add_word("salty", "солёный", SUB_GROUP, MAIN_GROUP, POS)
add_word("bitter", "горький", SUB_GROUP, MAIN_GROUP, POS)
add_word("strong", "резкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("pungent", "острый", SUB_GROUP, MAIN_GROUP, POS)

loud ; noisy ; sharp ; calm ; soft ; low ; quiet ; muffled ; deaf ; inaudible
SUB_GROUP = "Ухо • Ear"
add_word("loud", "громкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("noisy", "шумный", SUB_GROUP, MAIN_GROUP, POS)
add_word("sharp", "резкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("calm", "спокойный", SUB_GROUP, MAIN_GROUP, POS)
add_word("soft", "тихий", SUB_GROUP, MAIN_GROUP, POS)
add_word("low", "низкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("quiet", "тихий", SUB_GROUP, MAIN_GROUP, POS)
add_word("muffled", "притуплённый", SUB_GROUP, MAIN_GROUP, POS)
add_word("deaf", "глухой", SUB_GROUP, MAIN_GROUP, POS)
add_word("inaudible", "неслышимый", SUB_GROUP, MAIN_GROUP, POS)

smelly ; stinking ; aromatic ; fragrant ; odourless
SUB_GROUP = "Нос • Nose"
add_word("smelly", "вонючий", SUB_GROUP, MAIN_GROUP, POS)
add_word("stinking", "зловонный", SUB_GROUP, MAIN_GROUP, POS)
add_word("aromatic", "ароматный", SUB_GROUP, MAIN_GROUP, POS)
add_word("fragrant", "приятно пахнущий", SUB_GROUP, MAIN_GROUP, POS)
add_word("odourless", "без запаха", SUB_GROUP, MAIN_GROUP, POS)


MAIN_GROUP = "Время • Time"

long ; brief ; short ; fast ; swift ; quick ; rapid ; urgent ; slow ; early ; late ; young ; adult ; old ; aged
SUB_GROUP = "Основные Свойства • Main Properties"
add_word("long", "длинный", SUB_GROUP, MAIN_GROUP, POS)
add_word("brief", "краткий", SUB_GROUP, MAIN_GROUP, POS)
add_word("short", "короткий", SUB_GROUP, MAIN_GROUP, POS)
add_word("fast", "быстрый", SUB_GROUP, MAIN_GROUP, POS)
add_word("swift", "стремительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("quick", "быстрый", SUB_GROUP, MAIN_GROUP, POS)
add_word("rapid", "быстрый", SUB_GROUP, MAIN_GROUP, POS)
add_word("urgent", "срочный", SUB_GROUP, MAIN_GROUP, POS)
add_word("slow", "медленный", SUB_GROUP, MAIN_GROUP, POS)
add_word("early", "ранний", SUB_GROUP, MAIN_GROUP, POS)
add_word("late", "поздний", SUB_GROUP, MAIN_GROUP, POS)
add_word("young", "молодой", SUB_GROUP, MAIN_GROUP, POS)
add_word("adult", "взрослый", SUB_GROUP, MAIN_GROUP, POS)
add_word("old", "старый", SUB_GROUP, MAIN_GROUP, POS)
add_word("aged", "пожилой", SUB_GROUP, MAIN_GROUP, POS)

past ; recent ; obsolete ; ancient ; present ; contemporary ; modern ; up-to-date ; future ; previous ; preceding ;
preliminary ; simultaneous ; next ; following ; the first ; the last ; initial ; final
SUB_GROUP = "Стадии • Stages"
add_word("past", "прошлый", SUB_GROUP, MAIN_GROUP, POS)
add_word("recent", "недавний", SUB_GROUP, MAIN_GROUP, POS)
add_word("obsolete", "устаревший", SUB_GROUP, MAIN_GROUP, POS)
add_word("ancient", "древний", SUB_GROUP, MAIN_GROUP, POS)
add_word("present", "настоящий", SUB_GROUP, MAIN_GROUP, POS)
add_word("contemporary", "современный", SUB_GROUP, MAIN_GROUP, POS)
add_word("modern", "современный", SUB_GROUP, MAIN_GROUP, POS)
add_word("up-to-date", "современный", SUB_GROUP, MAIN_GROUP, POS)
add_word("future", "будущий", SUB_GROUP, MAIN_GROUP, POS)
add_word("previous", "предыдущий", SUB_GROUP, MAIN_GROUP, POS)
add_word("preceding", "предшествующий", SUB_GROUP, MAIN_GROUP, POS)
add_word("preliminary", "предварительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("simultaneous", "одновременный", SUB_GROUP, MAIN_GROUP, POS)
add_word("next", "следующий", SUB_GROUP, MAIN_GROUP, POS)
add_word("following", "последующий", SUB_GROUP, MAIN_GROUP, POS)
add_word("the first", "первый", SUB_GROUP, MAIN_GROUP, POS)
add_word("the last", "последний", SUB_GROUP, MAIN_GROUP, POS)
add_word("initial", "начальный", SUB_GROUP, MAIN_GROUP, POS)
add_word("final", "окончательный", SUB_GROUP, MAIN_GROUP, POS)

constant ; temporary ; uninterrupted ; continuous ; rare ; frequent ; usual ; occasional ; sudden ; eternal
SUB_GROUP = "Продолжительность / Частота • Duration / Frequency"
add_word("constant", "постоянный", SUB_GROUP, MAIN_GROUP, POS)
add_word("temporary", "временный", SUB_GROUP, MAIN_GROUP, POS)
add_word("uninterrupted", "непрерывный", SUB_GROUP, MAIN_GROUP, POS)
add_word("continuous", "непрерывный", SUB_GROUP, MAIN_GROUP, POS)
add_word("rare", "редкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("frequent", "частый", SUB_GROUP, MAIN_GROUP, POS)
add_word("usual", "обычный", SUB_GROUP, MAIN_GROUP, POS)
add_word("occasional", "случайный", SUB_GROUP, MAIN_GROUP, POS)
add_word("sudden", "внезапный", SUB_GROUP, MAIN_GROUP, POS)
add_word("eternal", "вечный", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Способности человека • Human abilities"

gifted; capable; talented; clever; intelligent; quick; wise
SUB_GROUP = "Способность • Ability"
add_word("gifted", "одарённый", SUB_GROUP, MAIN_GROUP, POS)
add_word("capable", "способный", SUB_GROUP, MAIN_GROUP, POS)
add_word("talented", "талантливый", SUB_GROUP, MAIN_GROUP, POS)
add_word("clever", "умный", SUB_GROUP, MAIN_GROUP, POS)
add_word("intelligent", "интеллигентный", SUB_GROUP, MAIN_GROUP, POS)
add_word("quick", "быстрый", SUB_GROUP, MAIN_GROUP, POS)
add_word("wise", "мудрый", SUB_GROUP, MAIN_GROUP, POS)

silly; stolid; stupid; dull; naive; ignorant; average; mediocre; mad; crazy
SUB_GROUP = "Отсутствие Способности • Lack of Ability"
add_word("silly", "глупый", SUB_GROUP, MAIN_GROUP, POS)
add_word("stolid", "флегматичный", SUB_GROUP, MAIN_GROUP, POS)
add_word("stupid", "тупой", SUB_GROUP, MAIN_GROUP, POS)
add_word("dull", "скучный", SUB_GROUP, MAIN_GROUP, POS)
add_word("naive", "наивный", SUB_GROUP, MAIN_GROUP, POS)
add_word("ignorant", "невежественный", SUB_GROUP, MAIN_GROUP, POS)
add_word("average", "средний", SUB_GROUP, MAIN_GROUP, POS)
add_word("mediocre", "заурядный", SUB_GROUP, MAIN_GROUP, POS)
add_word("mad", "безумный", SUB_GROUP, MAIN_GROUP, POS)
add_word("crazy", "сумасшедший", SUB_GROUP, MAIN_GROUP, POS)

diligent; industrious; lazy; accurate; exact; thorough; negligent; attentive; careful; careless; absent-minded; distracted
SUB_GROUP = "Старание / Внимание • Diligence / Attention"
add_word("diligent", "прилежный", SUB_GROUP, MAIN_GROUP, POS)
add_word("industrious", "трудолюбивый", SUB_GROUP, MAIN_GROUP, POS)
add_word("lazy", "ленивый", SUB_GROUP, MAIN_GROUP, POS)
add_word("accurate", "точный", SUB_GROUP, MAIN_GROUP, POS)
add_word("exact", "аккуратный", SUB_GROUP, MAIN_GROUP, POS)
add_word("thorough", "тщательный", SUB_GROUP, MAIN_GROUP, POS)
add_word("negligent", "небрежный", SUB_GROUP, MAIN_GROUP, POS)
add_word("attentive", "внимательный", SUB_GROUP, MAIN_GROUP, POS)
add_word("careful", "осторожный", SUB_GROUP, MAIN_GROUP, POS)
add_word("careless", "беспечный", SUB_GROUP, MAIN_GROUP, POS)
add_word("absent-minded", "рассеянный", SUB_GROUP, MAIN_GROUP, POS)
add_word("distracted", "отвлечённый", SUB_GROUP, MAIN_GROUP, POS)

experienced; inexperienced; skillful; deft; dexterous; clumsy; awkward
SUB_GROUP = "Навык / Опыт • Skill / Experience"
add_word("experienced", "опытный", SUB_GROUP, MAIN_GROUP, POS)
add_word("inexperienced", "неопытный", SUB_GROUP, MAIN_GROUP, POS)
add_word("skillful", "умелый", SUB_GROUP, MAIN_GROUP, POS)
add_word("deft", "ловкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("dexterous", "искусный", SUB_GROUP, MAIN_GROUP, POS)
add_word("clumsy", "неуклюжий", SUB_GROUP, MAIN_GROUP, POS)
add_word("awkward", "неловкий", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Эмоция • Emotions"

sensitive; sentimental; hard-hearted; indifferent; irritable; calm; quiet; tranquil; nervous
SUB_GROUP = "Характер • Character"
add_word("sensitive", "чувствительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("sentimental", "сентиментальный", SUB_GROUP, MAIN_GROUP, POS)
add_word("hard-hearted", "черствый", SUB_GROUP, MAIN_GROUP, POS)
add_word("indifferent", "безразличный", SUB_GROUP, MAIN_GROUP, POS)
add_word("irritable", "раздражительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("calm", "спокойный", SUB_GROUP, MAIN_GROUP, POS)
add_word("quiet", "тихий", SUB_GROUP, MAIN_GROUP, POS)
add_word("tranquil", "умиротворённый", SUB_GROUP, MAIN_GROUP, POS)
add_word("nervous", "нервный", SUB_GROUP, MAIN_GROUP, POS)

happy; lucky; joyful; merry; cheerful; glad; satisfied; optimistic; sad; sorry; upset; pessimistic; sorrowful; high-spirited; low-spirited
SUB_GROUP = "Настроение • Mood"
add_word("happy", "счастливый", SUB_GROUP, MAIN_GROUP, POS)
add_word("lucky", "удачливый", SUB_GROUP, MAIN_GROUP, POS)
add_word("joyful", "радостный", SUB_GROUP, MAIN_GROUP, POS)
add_word("merry", "весёлый", SUB_GROUP, MAIN_GROUP, POS)
add_word("cheerful", "жизнерадостный", SUB_GROUP, MAIN_GROUP, POS)
add_word("glad", "довольный", SUB_GROUP, MAIN_GROUP, POS)
add_word("satisfied", "удовлетворённый", SUB_GROUP, MAIN_GROUP, POS)
add_word("optimistic", "оптимистичный", SUB_GROUP, MAIN_GROUP, POS)
add_word("sad", "грустный", SUB_GROUP, MAIN_GROUP, POS)
add_word("sorry", "сожаление", SUB_GROUP, MAIN_GROUP, POS)
add_word("upset", "расстроенный", SUB_GROUP, MAIN_GROUP, POS)
add_word("pessimistic", "пессимистичный", SUB_GROUP, MAIN_GROUP, POS)
add_word("sorrowful", "печальный", SUB_GROUP, MAIN_GROUP, POS)
add_word("high-spirited", "бодрый", SUB_GROUP, MAIN_GROUP, POS)
add_word("low-spirited", "унылый", SUB_GROUP, MAIN_GROUP, POS)

good; pleasant; agreeable; interesting; wonderful; excellent; splendid; gorgeous; magnificent; perfect;
surprising; astonishing; amazing; exciting; moving; touching; strange; shocking; bad; tiresome; boring; disturbing

disgusting; unpleasant; abusive; offensive; awful; terrible; dangerous; beautiful; lovely; nice; pretty; attractive; ugly; repulsive; fearful
SUB_GROUP = "Эмоциональная Оценка • Emotional Evaluation"
add_word("good", "хороший", SUB_GROUP, MAIN_GROUP, POS)
add_word("pleasant", "приятный", SUB_GROUP, MAIN_GROUP, POS)
add_word("agreeable", "согласный", SUB_GROUP, MAIN_GROUP, POS)
add_word("interesting", "интересный", SUB_GROUP, MAIN_GROUP, POS)
add_word("wonderful", "замечательный", SUB_GROUP, MAIN_GROUP, POS)
add_word("excellent", "отличный", SUB_GROUP, MAIN_GROUP, POS)
add_word("splendid", "великолепный", SUB_GROUP, MAIN_GROUP, POS)
add_word("gorgeous", "роскошный", SUB_GROUP, MAIN_GROUP, POS)
add_word("magnificent", "великолепный", SUB_GROUP, MAIN_GROUP, POS)
add_word("perfect", "идеальный", SUB_GROUP, MAIN_GROUP, POS)
add_word("surprising", "удивительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("astonishing", "потрясающий", SUB_GROUP, MAIN_GROUP, POS)
add_word("amazing", "удивительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("exciting", "волнующий", SUB_GROUP, MAIN_GROUP, POS)
add_word("moving", "трогательный", SUB_GROUP, MAIN_GROUP, POS)
add_word("touching", "трогательный", SUB_GROUP, MAIN_GROUP, POS)
add_word("strange", "странный", SUB_GROUP, MAIN_GROUP, POS)
add_word("shocking", "шокирующий", SUB_GROUP, MAIN_GROUP, POS)
add_word("bad", "плохой", SUB_GROUP, MAIN_GROUP, POS)
add_word("tiresome", "утомительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("boring", "скучный", SUB_GROUP, MAIN_GROUP, POS)
add_word("disturbing", "тревожный", SUB_GROUP, MAIN_GROUP, POS)
add_word("disgusting", "отвратительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("unpleasant", "неприятный", SUB_GROUP, MAIN_GROUP, POS)
add_word("abusive", "оскорбительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("offensive", "обидный", SUB_GROUP, MAIN_GROUP, POS)
add_word("awful", "ужасный", SUB_GROUP, MAIN_GROUP, POS)
add_word("terrible", "страшный", SUB_GROUP, MAIN_GROUP, POS)
add_word("dangerous", "опасный", SUB_GROUP, MAIN_GROUP, POS)
add_word("beautiful", "красивый", SUB_GROUP, MAIN_GROUP, POS)
add_word("lovely", "милый", SUB_GROUP, MAIN_GROUP, POS)
add_word("nice", "приятный", SUB_GROUP, MAIN_GROUP, POS)
add_word("pretty", "симпатичный", SUB_GROUP, MAIN_GROUP, POS)
add_word("attractive", "привлекательный", SUB_GROUP, MAIN_GROUP, POS)
add_word("ugly", "уродливый", SUB_GROUP, MAIN_GROUP, POS)
add_word("repulsive", "отталкивающий", SUB_GROUP, MAIN_GROUP, POS)
add_word("fearful", "боязливый", SUB_GROUP, MAIN_GROUP, POS)

excited; agitated; uneasy; moved; frightened; scared; startled; surprised; astonished; amazed; angry; cross; hurt; offended
SUB_GROUP = "Оттенки Эмоции • Shades of Emotion"
add_word("excited", "возбужденный", SUB_GROUP, MAIN_GROUP, POS)
add_word("agitated", "взволнованный", SUB_GROUP, MAIN_GROUP, POS)
add_word("uneasy", "неловкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("moved", "тронутый", SUB_GROUP, MAIN_GROUP, POS)
add_word("frightened", "испуганный", SUB_GROUP, MAIN_GROUP, POS)
add_word("scared", "испуганный", SUB_GROUP, MAIN_GROUP, POS)
add_word("startled", "испуганный", SUB_GROUP, MAIN_GROUP, POS)
add_word("surprised", "удивленный", SUB_GROUP, MAIN_GROUP, POS)
add_word("astonished", "пораженный", SUB_GROUP, MAIN_GROUP, POS)
add_word("amazed", "изумленный", SUB_GROUP, MAIN_GROUP, POS)
add_word("angry", "злой", SUB_GROUP, MAIN_GROUP, POS)
add_word("cross", "сердитый", SUB_GROUP, MAIN_GROUP, POS)
add_word("hurt", "обиженный", SUB_GROUP, MAIN_GROUP, POS)
add_word("offended", "оскорбленный", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Мораль / Поведение • Moral / Behaviour"

decent; well-behaved; noble; worthy; honest; fair; sincere; lying; mean; base; vile; innocent; criminal; guilty
SUB_GROUP = "Основные Свойства • Main Properties"
add_word("decent", "порядочный", SUB_GROUP, MAIN_GROUP, POS)
add_word("well-behaved", "послушный", SUB_GROUP, MAIN_GROUP, POS)
add_word("noble", "благородный", SUB_GROUP, MAIN_GROUP, POS)
add_word("worthy", "достойный", SUB_GROUP, MAIN_GROUP, POS)
add_word("honest", "честный", SUB_GROUP, MAIN_GROUP, POS)
add_word("fair", "справедливый", SUB_GROUP, MAIN_GROUP, POS)
add_word("sincere", "искренний", SUB_GROUP, MAIN_GROUP, POS)
add_word("lying", "лживый", SUB_GROUP, MAIN_GROUP, POS)
add_word("mean", "подлый", SUB_GROUP, MAIN_GROUP, POS)
add_word("base", "низкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("vile", "гнусный", SUB_GROUP, MAIN_GROUP, POS)
add_word("innocent", "невинный", SUB_GROUP, MAIN_GROUP, POS)
add_word("criminal", "преступный", SUB_GROUP, MAIN_GROUP, POS)
add_word("guilty", "виновный", SUB_GROUP, MAIN_GROUP, POS)

good; kind; friendly; selfish; bad; evil; hostile; obedient; true; faithful; reliable; devoted; unstable; changeable; generous; wasteful; greedy;vicious;
SUB_GROUP = "Отношение к Окружающим • Attitude towards Others"
add_word("good", "хороший", SUB_GROUP, MAIN_GROUP, POS)
add_word("kind", "добрый", SUB_GROUP, MAIN_GROUP, POS)
add_word("friendly", "дружелюбный", SUB_GROUP, MAIN_GROUP, POS)
add_word("selfish", "эгоистичный", SUB_GROUP, MAIN_GROUP, POS)
add_word("bad", "плохой", SUB_GROUP, MAIN_GROUP, POS)
add_word("evil", "злой", SUB_GROUP, MAIN_GROUP, POS)
add_word("hostile", "враждебный", SUB_GROUP, MAIN_GROUP, POS)
add_word("obedient", "послушный", SUB_GROUP, MAIN_GROUP, POS)
add_word("true", "верный", SUB_GROUP, MAIN_GROUP, POS)
add_word("faithful", "верный", SUB_GROUP, MAIN_GROUP, POS)
add_word("reliable", "надежный", SUB_GROUP, MAIN_GROUP, POS)
add_word("devoted", "преданный", SUB_GROUP, MAIN_GROUP, POS)
add_word("unstable", "неустойчивый", SUB_GROUP, MAIN_GROUP, POS)
add_word("changeable", "переменчивый", SUB_GROUP, MAIN_GROUP, POS)
add_word("generous", "щедрый", SUB_GROUP, MAIN_GROUP, POS)
add_word("wasteful", "расточительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("greedy", "жадный", SUB_GROUP, MAIN_GROUP, POS)
add_word("vicious", "злобный", SUB_GROUP, MAIN_GROUP, POS)

talkative; sociable; reserved; polite; civil; gentle; mild; rude; rough; strict; severe;
SUB_GROUP = "Качества в Общении • Communication Qualities"
add_word("talkative", "разговорчивый", SUB_GROUP, MAIN_GROUP, POS)
add_word("sociable", "общительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("reserved", "сдержанный", SUB_GROUP, MAIN_GROUP, POS)
add_word("polite", "вежливый", SUB_GROUP, MAIN_GROUP, POS)
add_word("civil", "учтивый", SUB_GROUP, MAIN_GROUP, POS)
add_word("gentle", "нежный", SUB_GROUP, MAIN_GROUP, POS)
add_word("mild", "мягкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("rude", "грубый", SUB_GROUP, MAIN_GROUP, POS)
add_word("rough", "жёсткий", SUB_GROUP, MAIN_GROUP, POS)
add_word("strict", "строгий", SUB_GROUP, MAIN_GROUP, POS)
add_word("severe", "суровый", SUB_GROUP, MAIN_GROUP, POS)

brave; audacious; courageous; cowardly; timid; modest; shy; proud; arrogant; reasonable; rational; cautious; thoughtless; rash; hasty; impulsive;
SUB_GROUP = "Качества в Поведении • Qualities in Behavior"
add_word("brave", "храбрый", SUB_GROUP, MAIN_GROUP, POS)
add_word("audacious", "дерзкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("courageous", "смелый", SUB_GROUP, MAIN_GROUP, POS)
add_word("cowardly", "трусливый", SUB_GROUP, MAIN_GROUP, POS)
add_word("timid", "застенчивый", SUB_GROUP, MAIN_GROUP, POS)
add_word("modest", "скромный", SUB_GROUP, MAIN_GROUP, POS)
add_word("shy", "робкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("proud", "гордый", SUB_GROUP, MAIN_GROUP, POS)
add_word("arrogant", "высокомерный", SUB_GROUP, MAIN_GROUP, POS)
add_word("reasonable", "разумный", SUB_GROUP, MAIN_GROUP, POS)
add_word("rational", "рациональный", SUB_GROUP, MAIN_GROUP, POS)
add_word("cautious", "осторожный", SUB_GROUP, MAIN_GROUP, POS)
add_word("thoughtless", "беспечный", SUB_GROUP, MAIN_GROUP, POS)
add_word("rash", "опрометчивый", SUB_GROUP, MAIN_GROUP, POS)
add_word("hasty", "поспешный", SUB_GROUP, MAIN_GROUP, POS)
add_word("impulsive", "импульсивный", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Абстрактные прилагательные • Abstract Adjectives"

certain; common; general; typical; single; separate; particular; special; main; chief; principal; basic; secondary; complex; simple;
SUB_GROUP = "Классификация • Classification"
add_word("certain", "определённый", SUB_GROUP, MAIN_GROUP, POS)
add_word("common", "общий", SUB_GROUP, MAIN_GROUP, POS)
add_word("general", "генеральный", SUB_GROUP, MAIN_GROUP, POS)
add_word("typical", "типичный", SUB_GROUP, MAIN_GROUP, POS)
add_word("single", "единственный", SUB_GROUP, MAIN_GROUP, POS)
add_word("separate", "отдельный", SUB_GROUP, MAIN_GROUP, POS)
add_word("particular", "особый", SUB_GROUP, MAIN_GROUP, POS)
add_word("special", "специальный", SUB_GROUP, MAIN_GROUP, POS)
add_word("main", "главный", SUB_GROUP, MAIN_GROUP, POS)
add_word("chief", "главный", SUB_GROUP, MAIN_GROUP, POS)
add_word("principal", "принципиальный", SUB_GROUP, MAIN_GROUP, POS)
add_word("basic", "базовый", SUB_GROUP, MAIN_GROUP, POS)
add_word("secondary", "второстепенный", SUB_GROUP, MAIN_GROUP, POS)
add_word("complex", "сложный", SUB_GROUP, MAIN_GROUP, POS)
add_word("simple", "простой", SUB_GROUP, MAIN_GROUP, POS)

equal; the same; different; various; similar; important; significant; essential; advanced; inferior; defective; spoiled; natural; artificial; difficult; easy;
SUB_GROUP = "Качество • Quality"
add_word("equal", "равный", SUB_GROUP, MAIN_GROUP, POS)
add_word("the same", "одинаковый", SUB_GROUP, MAIN_GROUP, POS)
add_word("different", "разный", SUB_GROUP, MAIN_GROUP, POS)
add_word("various", "различный", SUB_GROUP, MAIN_GROUP, POS)
add_word("similar", "похожий", SUB_GROUP, MAIN_GROUP, POS)
add_word("important", "важный", SUB_GROUP, MAIN_GROUP, POS)
add_word("significant", "значительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("essential", "существенный", SUB_GROUP, MAIN_GROUP, POS)
add_word("advanced", "продвинутый", SUB_GROUP, MAIN_GROUP, POS)
add_word("inferior", "низший", SUB_GROUP, MAIN_GROUP, POS)
add_word("defective", "дефектный", SUB_GROUP, MAIN_GROUP, POS)
add_word("spoiled", "испорченный", SUB_GROUP, MAIN_GROUP, POS)
add_word("natural", "естественный", SUB_GROUP, MAIN_GROUP, POS)
add_word("artificial", "искусственный", SUB_GROUP, MAIN_GROUP, POS)
add_word("difficult", "трудный", SUB_GROUP, MAIN_GROUP, POS)
add_word("easy", "лёгкий", SUB_GROUP, MAIN_GROUP, POS)

maximum; minimum; average; sufficient; excessive; numerous; full; empty;
SUB_GROUP = "Количество • Quantity"
add_word("maximum", "максимальный", SUB_GROUP, MAIN_GROUP, POS)
add_word("minimum", "минимальный", SUB_GROUP, MAIN_GROUP, POS)
add_word("average", "средний", SUB_GROUP, MAIN_GROUP, POS)
add_word("sufficient", "достаточный", SUB_GROUP, MAIN_GROUP, POS)
add_word("excessive", "избыточный", SUB_GROUP, MAIN_GROUP, POS)
add_word("numerous", "многочисленный", SUB_GROUP, MAIN_GROUP, POS)
add_word("full", "полный", SUB_GROUP, MAIN_GROUP, POS)
add_word("empty", "пустой", SUB_GROUP, MAIN_GROUP, POS)

inevitable; relative; absolute; positive; negative; real; actual; practical; conditional; hypothetical; assumed; possible; probable; desirable; theoretical; imaginary; regular; occasional; necessary
SUB_GROUP = "Категория • Category"
add_word("inevitable", "неизбежный", SUB_GROUP, MAIN_GROUP, POS)
add_word("relative", "относительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("absolute", "абсолютный", SUB_GROUP, MAIN_GROUP, POS)
add_word("positive", "положительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("negative", "отрицательный", SUB_GROUP, MAIN_GROUP, POS)
add_word("real", "реальный", SUB_GROUP, MAIN_GROUP, POS)
add_word("actual", "фактический", SUB_GROUP, MAIN_GROUP, POS)
add_word("practical", "практический", SUB_GROUP, MAIN_GROUP, POS)
add_word("conditional", "условный", SUB_GROUP, MAIN_GROUP, POS)
add_word("hypothetical", "гипотетический", SUB_GROUP, MAIN_GROUP, POS)
add_word("assumed", "предполагаемый", SUB_GROUP, MAIN_GROUP, POS)
add_word("possible", "возможный", SUB_GROUP, MAIN_GROUP, POS)
add_word("probable", "вероятный", SUB_GROUP, MAIN_GROUP, POS)
add_word("desirable", "желательный", SUB_GROUP, MAIN_GROUP, POS)
add_word("theoretical", "теоретический", SUB_GROUP, MAIN_GROUP, POS)
add_word("imaginary", "воображаемый", SUB_GROUP, MAIN_GROUP, POS)
add_word("regular", "регулярный", SUB_GROUP, MAIN_GROUP, POS)
add_word("occasional", "случайный", SUB_GROUP, MAIN_GROUP, POS)
add_word("necessary", "необходимый", SUB_GROUP, MAIN_GROUP, POS)

correct; true; precise; logical; appropriate; suitable; acceptable; satisfactory; wrong; false; illogical; approximate; absurd; legal; lawful; out of place; standard; reliable
SUB_GROUP = "Соответствие • Accordance"
add_word("correct", "правильный", SUB_GROUP, MAIN_GROUP, POS)
add_word("true", "истинный", SUB_GROUP, MAIN_GROUP, POS)
add_word("precise", "точный", SUB_GROUP, MAIN_GROUP, POS)
add_word("logical", "логичный", SUB_GROUP, MAIN_GROUP, POS)
add_word("appropriate", "соответствующий", SUB_GROUP, MAIN_GROUP, POS)
add_word("suitable", "подходящий", SUB_GROUP, MAIN_GROUP, POS)
add_word("acceptable", "приемлемый", SUB_GROUP, MAIN_GROUP, POS)
add_word("satisfactory", "удовлетворительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("wrong", "неправильный", SUB_GROUP, MAIN_GROUP, POS)
add_word("false", "ложный", SUB_GROUP, MAIN_GROUP, POS)
add_word("illogical", "нелогичный", SUB_GROUP, MAIN_GROUP, POS)
add_word("approximate", "приблизительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("absurd", "абсурдный", SUB_GROUP, MAIN_GROUP, POS)
add_word("legal", "законный", SUB_GROUP, MAIN_GROUP, POS)
add_word("lawful", "правомерный", SUB_GROUP, MAIN_GROUP, POS)
add_word("out of place", "неуместный", SUB_GROUP, MAIN_GROUP, POS)
add_word("standard", "стандартный", SUB_GROUP, MAIN_GROUP, POS)
add_word("reliable", "надежный", SUB_GROUP, MAIN_GROUP, POS)

advantageous; profitable; efficient; valid; useful; harmless; useless; harmful; cheap; expensive; free of charge; priceless
SUB_GROUP = "Преимущество • Advantage"
add_word("advantageous", "выгодный", SUB_GROUP, MAIN_GROUP, POS)
add_word("profitable", "прибыльный", SUB_GROUP, MAIN_GROUP, POS)
add_word("efficient", "эффективный", SUB_GROUP, MAIN_GROUP, POS)
add_word("valid", "действительный", SUB_GROUP, MAIN_GROUP, POS)
add_word("useful", "полезный", SUB_GROUP, MAIN_GROUP, POS)
add_word("harmless", "безвредный", SUB_GROUP, MAIN_GROUP, POS)
add_word("useless", "бесполезный", SUB_GROUP, MAIN_GROUP, POS)
add_word("harmful", "вредный", SUB_GROUP, MAIN_GROUP, POS)
add_word("cheap", "дешёвый", SUB_GROUP, MAIN_GROUP, POS)
add_word("expensive", "дорогой", SUB_GROUP, MAIN_GROUP, POS)
add_word("free of charge", "бесплатный", SUB_GROUP, MAIN_GROUP, POS)
add_word("priceless", "бесценный", SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Состояние / Статус • Condition / Status"

healthy; robust; strong; vigorous; cheerful; sick; ill; weak; drowsy; sleepy; tired; exhausted; fat; lean; slim
SUB_GROUP = "Физическое Состояние • Physical Condition"
add_word("healthy", "здоровый", SUB_GROUP, MAIN_GROUP, POS)
add_word("robust", "крепкий", SUB_GROUP, MAIN_GROUP, POS)
add_word("strong", "сильный", SUB_GROUP, MAIN_GROUP, POS)
add_word("vigorous", "энергичный", SUB_GROUP, MAIN_GROUP, POS)
add_word("cheerful", "жизнерадостный", SUB_GROUP, MAIN_GROUP, POS)
add_word("sick", "больной", SUB_GROUP, MAIN_GROUP, POS)
add_word("ill", "нездоровый", SUB_GROUP, MAIN_GROUP, POS)
add_word("weak", "слабый", SUB_GROUP, MAIN_GROUP, POS)
add_word("drowsy", "сонливый", SUB_GROUP, MAIN_GROUP, POS)
add_word("sleepy", "сонный", SUB_GROUP, MAIN_GROUP, POS)
add_word("tired", "усталый", SUB_GROUP, MAIN_GROUP, POS)
add_word("exhausted", "измученный", SUB_GROUP, MAIN_GROUP, POS)
add_word("fat", "толстый", SUB_GROUP, MAIN_GROUP, POS)
add_word("lean", "худой", SUB_GROUP, MAIN_GROUP, POS)
add_word("slim", "стройный", SUB_GROUP, MAIN_GROUP, POS)

single; married; divorced
SUB_GROUP = "Семейное Положение • Family Status"
add_word("single", "не женат / не замужем", SUB_GROUP, MAIN_GROUP, POS)
add_word("married", "женат / замужем", SUB_GROUP, MAIN_GROUP, POS)
add_word("divorced", "разведённый", SUB_GROUP, MAIN_GROUP, POS)

comfortable; convenient; complete; intact; damaged; spoiled; cooked; fried; baked; raw; packed; free; vacant; occupied; busy; clean; dirty
SUB_GROUP = "Состояние • Condition"
add_word("comfortable", "комфортный", SUB_GROUP, MAIN_GROUP, POS)
add_word("convenient", "удобный", SUB_GROUP, MAIN_GROUP, POS)
add_word("complete", "полный", SUB_GROUP, MAIN_GROUP, POS)
add_word("intact", "целый", SUB_GROUP, MAIN_GROUP, POS)
add_word("damaged", "повреждённый", SUB_GROUP, MAIN_GROUP, POS)
add_word("spoiled", "испорченный", SUB_GROUP, MAIN_GROUP, POS)
add_word("cooked", "приготовленный", SUB_GROUP, MAIN_GROUP, POS)
add_word("fried", "жареный", SUB_GROUP, MAIN_GROUP, POS)
add_word("baked", "запечённый", SUB_GROUP, MAIN_GROUP, POS)
add_word("raw", "сырой", SUB_GROUP, MAIN_GROUP, POS)
add_word("packed", "упакованный", SUB_GROUP, MAIN_GROUP, POS)
add_word("free", "свободный", SUB_GROUP, MAIN_GROUP, POS)
add_word("vacant", "свободный", SUB_GROUP, MAIN_GROUP, POS)
add_word("occupied", "занятый", SUB_GROUP, MAIN_GROUP, POS)
add_word("busy", "занятый", SUB_GROUP, MAIN_GROUP, POS)
add_word("clean", "чистый", SUB_GROUP, MAIN_GROUP, POS)
add_word("dirty", "грязный", SUB_GROUP, MAIN_GROUP, POS)


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
add_word("beside (the house)", "рядом с (домом)", SUB_GROUP, MAIN_GROUP, POS)
add_word("among (us)", "среди (нас)", SUB_GROUP, MAIN_GROUP, POS)
add_word("between (the houses)", "между (домами)", SUB_GROUP, MAIN_GROUP, POS)
add_word("by (the window)", "у (окна)", SUB_GROUP, MAIN_GROUP, POS)
add_word("at (the door)", "у (двери)", SUB_GROUP, MAIN_GROUP, POS)
add_word("round (the table)", "вокруг (стола)", SUB_GROUP, MAIN_GROUP, POS)
add_word("far from (the house)", "далеко от (дома)", SUB_GROUP, MAIN_GROUP, POS)
add_word("in front of (our office)", "перед (нашим офисом)", SUB_GROUP, MAIN_GROUP, POS)
add_word("opposite (my house)", "напротив (моего дома)", SUB_GROUP, MAIN_GROUP, POS)
add_word("behind (me)", "за (мной)", SUB_GROUP, MAIN_GROUP, POS)
add_word("above (my head)", "над (моей головой)", SUB_GROUP, MAIN_GROUP, POS)
add_word("over (the table)", "над (столом)", SUB_GROUP, MAIN_GROUP, POS)
add_word("under (the bed)", "под (кроватью)", SUB_GROUP, MAIN_GROUP, POS)
add_word("below (the ground)", "ниже (земли)", SUB_GROUP, MAIN_GROUP, POS)
add_word("in (the school)", "в (школе)", SUB_GROUP, MAIN_GROUP, POS)
add_word("inside (the house)", "внутри (дома)", SUB_GROUP, MAIN_GROUP, POS)
add_word("outside (the house)", "снаружи (дома)", SUB_GROUP, MAIN_GROUP, POS)
add_word("on (the table)", "на (столе)", SUB_GROUP, MAIN_GROUP, POS)

from (London) ; off (the field) ; out of (the room) ; along (the street) ; down (the street) ; to (the sea) ;
towards (the sea) ; across (the river) ; through (the forest) ; over (the wall) ; down (the steps) ;
up (the hill) ; past (the house) ; into (the house) ; for (Kiev)
SUB_GROUP = "Предлоги Направления • Prepositions of Direction"
add_word("from (London)", "из (Лондона)", SUB_GROUP, MAIN_GROUP, POS)
add_word("off (the field)", "с (поля)", SUB_GROUP, MAIN_GROUP, POS)
add_word("out of (the room)", "из (комнаты)", SUB_GROUP, MAIN_GROUP, POS)
add_word("along (the street)", "вдоль (улицы)", SUB_GROUP, MAIN_GROUP, POS)
add_word("down (the street)", "вниз по (улице)", SUB_GROUP, MAIN_GROUP, POS)
add_word("to (the sea)", "к (морю)", SUB_GROUP, MAIN_GROUP, POS)
add_word("towards (the sea)", "в направлении (моря)", SUB_GROUP, MAIN_GROUP, POS)
add_word("across (the river)", "через (реку)", SUB_GROUP, MAIN_GROUP, POS)
add_word("through (the forest)", "сквозь (лес)", SUB_GROUP, MAIN_GROUP, POS)
add_word("over (the wall)", "через (стену)", SUB_GROUP, MAIN_GROUP, POS)
add_word("down (the steps)", "вниз по (ступенькам)", SUB_GROUP, MAIN_GROUP, POS)
add_word("up (the hill)", "вверх по (холму)", SUB_GROUP, MAIN_GROUP, POS)
add_word("past (the house)", "мимо (дома)", SUB_GROUP, MAIN_GROUP, POS)
add_word("into (the house)", "в (дом)", SUB_GROUP, MAIN_GROUP, POS)
add_word("for (Kiev)", "для (Киева)", SUB_GROUP, MAIN_GROUP, POS)

for (two weeks) ; within (a week) ; over (the last three days) ; in (an hour) ; during (the event); in (1965 , August) ;
since (1980) ; at (four o'clock) ; till (four o'clock) ; by (three o'clock) ; from (two o'clock) ; on (Monday) ;
in (the morning) ; at (noon , night) ; before (the work) ; after (the work) ; on (the first of May) ;
(ten minutes) past (seven) ; (ten minutes) to (seven)
SUB_GROUP = "Предлоги Времени • Prepositions of Time"
add_word("for (two weeks)", "в течение (двух недель)", SUB_GROUP, MAIN_GROUP, POS)
add_word("within (a week)", "в течение (недели)", SUB_GROUP, MAIN_GROUP, POS)
add_word("over (the last three days)", "за (последние три дня)", SUB_GROUP, MAIN_GROUP, POS)
add_word("in (an hour)", "через (час)", SUB_GROUP, MAIN_GROUP, POS)
add_word("during (the event)", "во время (события)", SUB_GROUP, MAIN_GROUP, POS)
add_word("in (1965, August)", "в (августе 1965 года)", SUB_GROUP, MAIN_GROUP, POS)
add_word("since (1980)", "с (1980 года)", SUB_GROUP, MAIN_GROUP, POS)
add_word("at (four o'clock)", "в (четыре часа)", SUB_GROUP, MAIN_GROUP, POS)
add_word("till (four o'clock)", "до (четырёх часов)", SUB_GROUP, MAIN_GROUP, POS)
add_word("by (three o'clock)", "к (трём часам)", SUB_GROUP, MAIN_GROUP, POS)
add_word("from (two o'clock)", "с (двух часов)", SUB_GROUP, MAIN_GROUP, POS)
add_word("on (Monday)", "в (понедельник)", SUB_GROUP, MAIN_GROUP, POS)
add_word("in (the morning)", "утром", SUB_GROUP, MAIN_GROUP, POS)
add_word("at (noon, night)", "в (полдень, ночью)", SUB_GROUP, MAIN_GROUP, POS)
add_word("before (the work)", "до (работы)", SUB_GROUP, MAIN_GROUP, POS)
add_word("after (the work)", "после (работы)", SUB_GROUP, MAIN_GROUP, POS)
add_word("on (the first of May)", "в (первое мая)", SUB_GROUP, MAIN_GROUP, POS)
add_word("(ten minutes) past (seven)", "(десять минут) после (семи)", SUB_GROUP, MAIN_GROUP, POS)
add_word("(ten minutes) to (seven)", "(десять минут) до (семи)", SUB_GROUP, MAIN_GROUP, POS)

according (to the plan) ; in spite of (poor health) ; despite (the difference) ; regardless of (the law) ;
because of (illness) ; due to (rain) ; thanks to (your help) ; except (you) ; except for (him) ;
instead of (the teacher) ; as to (buying) ; as for (signing) ; on behalf of (my colleagues) ;
for the purpose of (improving) ; for (children) ; against (noise) ; without (money) ; (a cake) of (soap) ;
to (me) ; (a book) about (flowers)
SUB_GROUP = "Смешанная Группа • Mixed Group"
add_word("according (to the plan)", "согласно (плану)", SUB_GROUP, MAIN_GROUP, POS)
add_word("in spite of (poor health)", "несмотря на (плохое здоровье)", SUB_GROUP, MAIN_GROUP, POS)
add_word("despite (the difference)", "несмотря на (разницу)", SUB_GROUP, MAIN_GROUP, POS)
add_word("regardless of (the law)", "независимо от (закона)", SUB_GROUP, MAIN_GROUP, POS)
add_word("because of (illness)", "из-за (болезни)", SUB_GROUP, MAIN_GROUP, POS)
add_word("due to (rain)", "вследствие (дождя)", SUB_GROUP, MAIN_GROUP, POS)
add_word("thanks to (your help)", "благодаря (твоей помощи)", SUB_GROUP, MAIN_GROUP, POS)
add_word("except (you)", "кроме (тебя)", SUB_GROUP, MAIN_GROUP, POS)
add_word("except for (him)", "за исключением (его)", SUB_GROUP, MAIN_GROUP, POS)
add_word("instead of (the teacher)", "вместо (учителя)", SUB_GROUP, MAIN_GROUP, POS)
add_word("as to (buying)", "что касается (покупки)", SUB_GROUP, MAIN_GROUP, POS)
add_word("as for (signing)", "что касается (подписания)", SUB_GROUP, MAIN_GROUP, POS)
add_word("on behalf of (my colleagues)", "от имени (моих коллег)", SUB_GROUP, MAIN_GROUP, POS)
add_word("for the purpose of (improving)", "с целью (улучшения)", SUB_GROUP, MAIN_GROUP, POS)
add_word("for (children)", "для (детей)", SUB_GROUP, MAIN_GROUP, POS)
add_word("against (noise)", "против (шума)", SUB_GROUP, MAIN_GROUP, POS)
add_word("without (money)", "без (денег)", SUB_GROUP, MAIN_GROUP, POS)
add_word("(a cake) of (soap)", "(кусок) мыла", SUB_GROUP, MAIN_GROUP, POS)
add_word("to (me)", "ко мне", SUB_GROUP, MAIN_GROUP, POS)
add_word("(a book) about (flowers)", "(книга) о (цветах)", SUB_GROUP, MAIN_GROUP, POS)

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
