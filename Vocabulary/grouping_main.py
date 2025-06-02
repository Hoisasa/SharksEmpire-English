import time
import timeit

from tinydb import TinyDB, Query, where

tb = TinyDB("db.json")
query = Query()
c = 0

def add_word(name, transl, weight, transcr, s_group, group):
	global c
	doc = {"Name": name, "translation": transl, "weight": weight, "transcription": transcr, "Sub group": s_group, "Group": group}
	if tb.search((where("Name") == name) & (where("Sub group") == s_group)):
		c += 1
		print(f"{c}", end=' ')
	
	else:
		tb.insert(doc)


print(tb.all())

def time_check():
	add_word("beginning", "начало", 1.0, '', "Начало • Begining", "Глаголы этапов • Verbs of Stage")
	add_word("begin", "начинать", 1.0, '', "Начало • Begining", "Глаголы этапов • Verbs of Stage")
	add_word("start", "начинать", 1.0, '', "Начало • Begining", "Глаголы этапов • Verbs of Stage")
	add_word("grow (+adj)", "становиться (+прил)", 1.0, '', "Начало • Begining", "Глаголы этапов • Verbs of Stage")
	add_word("become", "становиться", 1.0, '', "Начало • Begining", "Глаголы этапов • Verbs of Stage")
	add_word("get (+adj)", "становиться (+прил)", 1.0, '', "Начало • Begining", "Глаголы этапов • Verbs of Stage")
	add_word("appear", "появляться", 1.0, '', "Начало • Begining", "Глаголы этапов • Verbs of Stage")
	add_word("prepare", "готовиться", 1.0, '', "Начало • Begining", "Глаголы этапов • Verbs of Stage")
	add_word("be late", "опаздывать", 1.0, '', "Начало • Begining", "Глаголы этапов • Verbs of Stage")
	
	
	add_word("continue", "продолжать(ся)", 1.0, '', "Продолжение • Continuation", "Глаголы этапов • Verbs of Stage")
	add_word("go on", "продолжать", 1.0, '', "Продолжение • Continuation", "Глаголы этапов • Verbs of Stage")
	add_word("last", "длиться", 1.0, '', "Продолжение • Continuation", "Глаголы этапов • Verbs of Stage")
	add_word("take (time)", "занимать (время)", 1.0, '', "Продолжение • Continuation", "Глаголы этапов • Verbs of Stage")
	add_word("delay", "задерживать", 1.0, '', "Продолжение • Continuation", "Глаголы этапов • Verbs of Stage")
	add_word("put off", "откладывать", 1.0, '', "Продолжение • Continuation", "Глаголы этапов • Verbs of Stage")
	add_word("repeat", "повторять", 1.0, '', "Продолжение • Continuation", "Глаголы этапов • Verbs of Stage")
	add_word("resume", "возобновлять", 1.0, '', "Продолжение • Continuation", "Глаголы этапов • Verbs of Stage")
	
	
	add_word("finish", "завершать(ся)", 1.0, '', "Завершение • End", "Глаголы этапов • Verbs of Stage")
	add_word("end", "завершать(ся)", 1.0, '', "Завершение • End", "Глаголы этапов • Verbs of Stage")
	add_word("complete", "завершать", 1.0, '', "Завершение • End", "Глаголы этапов • Verbs of Stage")
	add_word("break", "прерывать", 1.0, '', "Завершение • End", "Глаголы этапов • Verbs of Stage")
	add_word("stop", "прекращать", 1.0, '', "Завершение • End", "Глаголы этапов • Verbs of Stage")
	
	
	add_word("move", "двигать(ся)", 1.0, '', "Виды движений • Ways of Movement", "Глаголы Движения • Verbs of Movement")
	add_word("stop", "останавливать(ся)", 1.0, '', "Виды движений • Ways of Movement", "Глаголы Движения • Verbs of Movement")
	add_word("go", "идти / ехать", 1.0, '', "Виды движений • Ways of Movement", "Глаголы Движения • Verbs of Movement")
	add_word("turn", "поворачивать(ся)", 1.0, '', "Виды движений • Ways of Movement", "Глаголы Движения • Verbs of Movement")
	add_word("bend", "гнуть", 1.0, '', "Виды движений • Ways of Movement", "Глаголы Движения • Verbs of Movement")
	add_word("wave", "махать рукой", 1.0, '', "Виды движений • Ways of Movement", "Глаголы Движения • Verbs of Movement")
	add_word("shake", "трясти(сь)", 1.0, '', "Виды движений • Ways of Movement", "Глаголы Движения • Verbs of Movement")
	add_word("swing", "раскачиваться", 1.0, '', "Виды движений • Ways of Movement", "Глаголы Движения • Verbs of Movement")
	add_word("swim", "плыть", 1.0, '', "Виды движений • Ways of Movement", "Глаголы Движения • Verbs of Movement")
	add_word("ski", "кататься на лыжах", 1.0, '', "Виды движений • Ways of Movement", "Глаголы Движения • Verbs of Movement")
	
	
	add_word("raise", "поднимать", 1.0, '', "Движение вверх/вниз • Upward/Downward Movement", "Глаголы Движения • Verbs of Movement")
	add_word("lift", "поднимать", 1.0, '', "Движение вверх/вниз • Upward/Downward Movement", "Глаголы Движения • Verbs of Movement")
	add_word("rise", "подниматься", 1.0, '', "Движение вверх/вниз • Upward/Downward Movement", "Глаголы Движения • Verbs of Movement")
	add_word("climb", "взбираться", 1.0, '', "Движение вверх/вниз • Upward/Downward Movement", "Глаголы Движения • Verbs of Movement")
	add_word("lower", "опускать", 1.0, '', "Движение вверх/вниз • Upward/Downward Movement", "Глаголы Движения • Verbs of Movement")
	add_word("sink", "опускаться (тонуть)", 1.0, '', "Движение вверх/вниз • Upward/Downward Movement", "Глаголы Движения • Verbs of Movement")
	add_word("drop", "ронять / подать", 1.0, '', "Движение вверх/вниз • Upward/Downward Movement", "Глаголы Движения • Verbs of Movement")
	add_word("fall", "падать", 1.0, '', "Движение вверх/вниз • Upward/Downward Movement", "Глаголы Движения • Verbs of Movement")
	
	
	add_word("fly", "лететь", 1.0, '', "Скорость • Speed", "Глаголы Движения • Verbs of Movement")
	add_word("ride", "скакать / ехать", 1.0, '', "Скорость • Speed", "Глаголы Движения • Verbs of Movement")
	add_word("run", "бежать", 1.0, '', "Скорость • Speed", "Глаголы Движения • Verbs of Movement")
	add_word("walk", "идти / гулять", 1.0, '', "Скорость • Speed", "Глаголы Движения • Verbs of Movement")
	add_word("speed up", "ускорять", 1.0, '', "Скорость • Speed", "Глаголы Движения • Verbs of Movement")
	add_word("slow down", "замедлять", 1.0, '', "Скорость • Speed", "Глаголы Движения • Verbs of Movement")
	
	
	add_word("pursue", "преследовать", 1.0, '', "Преследование • Pursuit", "Глаголы Движения • Verbs of Movement")
	add_word("catch up", "догонять", 1.0, '', "Преследование • Pursuit", "Глаголы Движения • Verbs of Movement")
	add_word("leave behind", "оставлять позади", 1.0, '', "Преследование • Pursuit", "Глаголы Движения • Verbs of Movement")
	add_word("catch", "схватить", 1.0, '', "Преследование • Pursuit", "Глаголы Движения • Verbs of Movement")
	add_word("escape", "убежать", 1.0, '', "Преследование • Pursuit", "Глаголы Движения • Verbs of Movement")
	add_word("flee", "спасаться бегством", 1.0, '', "Преследование • Pursuit", "Глаголы Движения • Verbs of Movement")
	add_word("avoid", "избегать", 1.0, '', "Преследование • Pursuit", "Глаголы Движения • Verbs of Movement")
	
	
	add_word("depart", "отправляться", 1.0, '', "Из начальной точки в конец 1 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	add_word("start", "отправляться", 1.0, '', "Из начальной точки в конец 1 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	add_word("leave", "отправляться", 1.0, '', "Из начальной точки в конец 1 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	add_word("go out", "выходить", 1.0, '', "Из начальной точки в конец 1 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	add_word("advance", "продвигаться", 1.0, '', "Из начальной точки в конец 1 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	add_word("meet", "встречать(ся)", 1.0, '', "Из начальной точки в конец 1 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	add_word("come across", "встречаться", 1.0, '', "Из начальной точки в конец 1 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	add_word("follow", "следовать", 1.0, '', "Из начальной точки в конец 1 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	add_word("go along", "идти (вдоль)", 1.0, '', "Из начальной точки в конец 1 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	add_word("cross", "пересекать", 1.0, '', "Из начальной точки в конец 1 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	
	
	add_word("run into", "врезаться (в)", 1.0, '', "Из начальной точки в конец 2 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	add_word("pass", "проходить мимо", 1.0, '', "Из начальной точки в конец 2 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	add_word("turn left", "повернуть (налево)", 1.0, '', "Из начальной точки в конец 2 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	add_word("arrive", "прибывать", 1.0, '', "Из начальной точки в конец 2 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	add_word("come", "приходить", 1.0, '', "Из начальной точки в конец 2 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	add_word("reach", "достигать", 1.0, '', "Из начальной точки в конец 2 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	add_word("return", "возвращаться", 1.0, '', "Из начальной точки в конец 2 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	add_word("enter", "входить / вводить", 1.0, '', "Из начальной точки в конец 2 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	add_word("go in", "входить", 1.0, '', "Из начальной точки в конец 2 • Movement form start to finish", "Глаголы Движения • Verbs of Movement")
	
	add_word("flow", "течь", 1.0, '', "Движение в Воде • Movement in Water", "Глаголы Движения • Verbs of Movement")
	add_word("float", "не тонуть", 1.0, '', "Движение в Воде • Movement in Water", "Глаголы Движения • Verbs of Movement")
	add_word("row", "грести", 1.0, '', "Движение в Воде • Movement in Water", "Глаголы Движения • Verbs of Movement")
	add_word("emerge", "входить", 1.0, '', "Движение в Воде • Movement in Water", "Глаголы Движения • Verbs of Movement")
	add_word("goin", "всплывать", 1.0, '', "Движение в Воде • Movement in Water", "Глаголы Движения • Verbs of Movement")
	
	
	add_word("exist", "существовать", 1.0, '', "Наличие/Принадлежность • Presence/Belonging", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("be", "быть", 1.0, '', "Наличие/Принадлежность • Presence/Belonging", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("there is", "имееться", 1.0, '', "Наличие/Принадлежность • Presence/Belonging", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("that will do", "хватит", 1.0, '', "Наличие/Принадлежность • Presence/Belonging", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("be present", "присутствовать", 1.0, '', "Наличие/Принадлежность • Presence/Belonging", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("be available", "быть в наличии", 1.0, '', "Наличие/Принадлежность • Presence/Belonging", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("possess", "владеть", 1.0, '', "Наличие/Принадлежность • Presence/Belonging", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("have", "иметь", 1.0, '', "Наличие/Принадлежность • Presence/Belonging", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("have enough", "иметь в достаточном кол-ве", 1.0, '', "Наличие/Принадлежность • Presence/Belonging", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("be sufficient", "быть достаточным", 1.0, '', "Наличие/Принадлежность • Presence/Belonging", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("belong", "принадлежать", 1.0, '', "Наличие/Принадлежность • Presence/Belonging", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("contain", "содержать", 1.0, '', "Наличие/Принадлежность • Presence/Belonging", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("include", "включать", 1.0, '', "Наличие/Принадлежность • Presence/Belonging", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	
	
	add_word("need", "нуждаться", 1.0, '', "Нехватка • Lack", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("require", "требовать", 1.0, '', "Нехватка • Lack", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("be necessary", "быть необходимым", 1.0, '', "Нехватка • Lack", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("lack", "не хватать", 1.0, '', "Нехватка • Lack", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("be absent", "отсутствовать", 1.0, '', "Нехватка • Lack", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("empty", "опорожнять", 1.0, '', "Нехватка • Lack", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("be empty", "быть пустым", 1.0, '', "Нехватка • Lack", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	
	
	add_word("gather", "собирать", 1.0, '', "Добавление/Избыток • Addition/Excess", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("collect", "собирать", 1.0, '', "Добавление/Избыток • Addition/Excess", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("add", "добавлять", 1.0, '', "Добавление/Избыток • Addition/Excess", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("fill", "наполнять", 1.0, '', "Добавление/Избыток • Addition/Excess", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("be full", "быть полным", 1.0, '', "Добавление/Избыток • Addition/Excess", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	
	
	add_word("reduce", "сокращать", 1.0, '', "Сокращение/Остаток • Shortening/Remainder", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("eliminate", "устранять", 1.0, '', "Сокращение/Остаток • Shortening/Remainder", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("lose", "терять", 1.0, '', "Сокращение/Остаток • Shortening/Remainder", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("do without", "обходиться", 1.0, '', "Сокращение/Остаток • Shortening/Remainder", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("spend", "тратить", 1.0, '', "Сокращение/Остаток • Shortening/Remainder", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("consume", "потреблять", 1.0, '', "Сокращение/Остаток • Shortening/Remainder", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("damage", "повреждать", 1.0, '', "Сокращение/Остаток • Shortening/Remainder", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	
	
	add_word("remain", "оставаться", 1.0, '', "Сохранение • Preservation", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("be left", "оставаться", 1.0, '', "Сохранение • Preservation", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("keep", "удерживать", 1.0, '', "Сохранение • Preservation", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("maintain", "поддерживать", 1.0, '', "Сохранение • Preservation", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("preserve", "сохранять", 1.0, '', "Сохранение • Preservation", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("retain", "сохранять за собой", 1.0, '', "Сохранение • Preservation", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("store", "хранить", 1.0, '', "Сохранение • Preservation", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	
	
	add_word("put", "класть", 1.0, '', "Положение 1 • Position 1", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("place", "помещать", 1.0, '', "Положение 1 • Position 1", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("set", "класть", 1.0, '', "Положение 1 • Position 1", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("lay", "положить", 1.0, '', "Положение 1 • Position 1", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("be situated", "находиться", 1.0, '', "Положение 1 • Position 1", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("be located", "находиться", 1.0, '', "Положение 1 • Position 1", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("stay", "пребывать", 1.0, '', "Положение 1 • Position 1", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("lie", "лежать", 1.0, '', "Положение 1 • Position 1", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("hang", "висеть / вешать", 1.0, '', "Положение 1 • Position 1", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("stand", "собирать", 1.0, '', "Положение 1 • Position 1", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	
	
	add_word("locate", "определять место", 1.0, '', "Положение 2 • Position 2", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("lie down", "ложиться", 1.0, '', "Положение 2 • Position 2", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("stand up", "вставать", 1.0, '', "Положение 2 • Position 2", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("sit", "сидеть", 1.0, '', "Положение 2 • Position 2", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("sit down", "садиться", 1.0, '', "Положение 2 • Position 2", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("seat", "посадить", 1.0, '', "Положение 2 • Position 2", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	add_word("seat (oneself)", "садиться", 1.0, '', "Положение 2 • Position 2", "Глаголы Наличия/Количества • Verbs of Presence/Quantity")
	
	
	add_word("bear", "рождать", 1.0, '', "Жить • Live", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("give birth", "родить", 1.0, '', "Жить • Live", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("be born", "родиться", 1.0, '', "Жить • Live", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("live", "жить", 1.0, '', "Жить • Live", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("be alive", "быть живым", 1.0, '', "Жить • Live", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("breathe", "дышать", 1.0, '', "Жить • Live", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("name", "называть", 1.0, '', "Жить • Live", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("marry", "жениться", 1.0, '', "Жить • Live", "Бытовые Глаголы • Verbs of Everyday Life")
	
	
	add_word("work", "работать", 1.0, '', "Работать • Work", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("take a job", "устраиваться на работу", 1.0, '', "Работать • Work", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("employ", "нанимать", 1.0, '', "Работать • Work", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("dismiss", "увольнять", 1.0, '', "Работать • Work", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("earn", "зарабатывать", 1.0, '', "Работать • Work", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("pay", "платить", 1.0, '', "Работать • Work", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("spend", "тратить", 1.0, '', "Работать • Work", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("save", "копить", 1.0, '', "Работать • Work", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("waste", "расточительно тратить", 1.0, '', "Работать • Work", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("rest", "отдыхать", 1.0, '', "Работать • Work", "Бытовые Глаголы • Verbs of Everyday Life")
	
	
	add_word("eat", "есть", 1.0, '', "Есть/Пить • Eat/Drink", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("be hungry", "быть голодным", 1.0, '', "Есть/Пить • Eat/Drink", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("feed", "кормить", 1.0, '', "Есть/Пить • Eat/Drink", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("bite", "кусать", 1.0, '', "Есть/Пить • Eat/Drink", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("chew", "жевать", 1.0, '', "Есть/Пить • Eat/Drink", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("swallow", "глотать", 1.0, '', "Есть/Пить • Eat/Drink", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("drink", "пить", 1.0, '', "Есть/Пить • Eat/Drink", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("be thirsty", "хотеть пить (жажда)", 1.0, '', "Есть/Пить • Eat/Drink", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("cook", "готовить (пищу)", 1.0, '', "Есть/Пить • Eat/Drink", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("bake", "печь", 1.0, '', "Есть/Пить • Eat/Drink", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("fry", "жарить", 1.0, '', "Есть/Пить • Eat/Drink", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("boil", "кипятить", 1.0, '', "Есть/Пить • Eat/Drink", "Бытовые Глаголы • Verbs of Everyday Life")
	
	
	add_word("wear", "носить", 1.0, '', "Одеваться • Dress", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("dress", "одеваться", 1.0, '', "Одеваться • Dress", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("put on", "одевать", 1.0, '', "Одеваться • Dress", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("take off", "снимать", 1.0, '', "Одеваться • Dress", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("wash", "стирать", 1.0, '', "Одеваться • Dress", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("iron", "гладить", 1.0, '', "Одеваться • Dress", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("order", "заказывать", 1.0, '', "Одеваться • Dress", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("fit", "хорошо сидеть", 1.0, '', "Одеваться • Dress", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("suit", "идти (тебе идет)", 1.0, '', "Одеваться • Dress", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("be in fashion", "быть в моде", 1.0, '', "Одеваться • Dress", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("be out of fashion", "выйти из моды", 1.0, '', "Одеваться • Dress", "Бытовые Глаголы • Verbs of Everyday Life")
	
	
	add_word("sleep", "спать", 1.0, '', "Спать/ Приводить себя в порядок • Sleep/Tidy Oneself up", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("fall asleep", "уснуть", 1.0, '', "Спать/ Приводить себя в порядок • Sleep/Tidy Oneself up", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("go to bed", "ложиться спать", 1.0, '', "Спать/ Приводить себя в порядок • Sleep/Tidy Oneself up", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("awake", "будить / просыпаться", 1.0, '', "Спать/ Приводить себя в порядок • Sleep/Tidy Oneself up", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("wake", "будить / просыпаться", 1.0, '', "Спать/ Приводить себя в порядок • Sleep/Tidy Oneself up", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("get up", "вставать", 1.0, '', "Спать/ Приводить себя в порядок • Sleep/Tidy Oneself up", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("wash oneself", "умываться", 1.0, '', "Спать/ Приводить себя в порядок • Sleep/Tidy Oneself up", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("brush teeth", "чистить зубы", 1.0, '', "Спать/ Приводить себя в порядок • Sleep/Tidy Oneself up", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("comb ones hair", "причесываться", 1.0, '', "Спать/ Приводить себя в порядок • Sleep/Tidy Oneself up", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("dry oneself", "вытираться", 1.0, '', "Спать/ Приводить себя в порядок • Sleep/Tidy Oneself up", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("shave", "бриться", 1.0, '', "Спать/ Приводить себя в порядок • Sleep/Tidy Oneself up", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("make up", "делать макияж", 1.0, '', "Спать/ Приводить себя в порядок • Sleep/Tidy Oneself up", "Бытовые Глаголы • Verbs of Everyday Life")
	add_word("do ones hair", "делать прическу", 1.0, '', "Спать/ Приводить себя в порядок • Sleep/Tidy Oneself up", "Бытовые Глаголы • Verbs of Everyday Life")
	

# add_word("fry", "собирать", 1.0, '', "Спать/ Приводить себя в порядок • Sleep/Tidy Oneself up", "Бытовые Глаголы • Verbs of Everyday Life")


print('\n', timeit.timeit(time_check, number=1))