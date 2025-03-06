import random
import time
import PySide6

from colorama import Fore, Style, init
from tinydb import TinyDB, Query, where




class WordShortcut:
    def __init__(self, word_full):
        self.word_meta = word_full

    def name(self):
        return self.word_meta.get("Name")

    def transl(self):
        return self.word_meta.get("translation")

    def transcript(self):
        return self.word_meta.get("trasncription")

    def weight(self):
        return self.word_meta.get("weight")

    def sub_group(self):
        return self.word_meta.get("Sub group")


    
def points_func(weight_got):
    points_got = max_points - weight_got*max_points
    return round(points_got)

def rearange_weights():
    for word in this_group_full:
        wd = WordShortcut(word)
        rand_mark, = random.choices(weight, probability, k=1)
        print(points_func(rand_mark), end=' ')
        print(wd.name())
        tb.update({"weight": rand_mark}, (where("Sub group") == group_name) & (Word.Name == wd.name()))
        
def get_TO_LEARN_list():
    return tb.search((where("Sub group") == group_name) & (Word.weight >  0.0))
    
def get_LEARNED_list():
    return tb.search((where("Sub group") == group_name) & (Word.weight == 0.0))

def get_pos(target_list, start, finish, banned_word):
    if banned_word:
        banned = target_list.index(banned_word)
    else:
        banned = banned_word
    pos_range = range(start, finish)
    new_pos = random.choice([i for i in pos_range if i != banned ])
    return new_pos

def switch_pos(target_list, start, destination, word):
    temp_word = target_list.pop(destination)
    target_list.insert(destination, word)
    target_list.pop(start)
    target_list.insert(start, temp_word)

def shuffle_Learned(learn_list):
    
    start_time = time.perf_counter()
    list_length = len(learn_list)
    allowed_start_last, allowed_start_second_last = 2, 1
    
    if list_length >= 5:
        last_word = learn_list[-1]
        second_last_word = learn_list[-2]
        random.shuffle(learn_list)
        if learn_list[0] == last_word:
            new_pos = get_pos(learn_list, allowed_start_last, list_length, second_last_word)
            switch_pos(learn_list, 0, new_pos, last_word)
            print(f"{last_word['Name']}{Fore.BLUE}{Style.BRIGHT}worked0")
            end_time = time.perf_counter()
            
            elapsed_time = end_time - start_time
            print(f"Time spent: {elapsed_time:.6f} seconds")
            print("".join(i["Name"] + "\n" for i in learn_list))

        elif learn_list[1] == last_word:
            new_pos = get_pos(learn_list, allowed_start_last, list_length, None)
            switch_pos(learn_list, 1, new_pos, last_word)
            print(f"{last_word['Name']}{Fore.BLUE}{Style.BRIGHT}worked1")
            end_time = time.perf_counter()
            
            elapsed_time = end_time - start_time
            print(f"Time spent: {elapsed_time:.6f} seconds")
            print("".join(i["Name"] + "\n" for i in learn_list))
        
        elif learn_list[0] == second_last_word:
            new_pos = get_pos(learn_list, allowed_start_second_last, list_length, last_word)
            switch_pos(learn_list, 0, new_pos, second_last_word)
            print(f"{second_last_word['Name']}{Fore.GREEN}{Style.BRIGHT}worked")
            end_time = time.perf_counter()
            
            elapsed_time = end_time - start_time
            print(f"Time spent: {elapsed_time:.6f} seconds")
            print("".join(i["Name"] + "\n" for i in learn_list))
        else:
            print("".join(i["Name"] + "\n" for i in learn_list))
            
        
    elif list_length >= 3:
        last_word = learn_list[-1]
        random.shuffle(learn_list)
        if learn_list[0] == last_word:
            new_pos = get_pos(learn_list, allowed_start_last, list_length, None)
            switch_pos(learn_list, 0, new_pos, last_word)
            print(f"{Fore.RED}{Style.BRIGHT}worked")
            print("".join(i["Name"] + "\n" for i in learn_list))
    
def prepare_lesson():
    to_learn = get_TO_LEARN_list()
    learned = get_LEARNED_list()
    list_length = len(to_learn)
    
    shuffle_Learned(learned)
    random.shuffle(learned)

    if list_length <= 3:
        learned = learned[:2]
    elif list_length <= 5:
        learned = learned[:4]
        
    
    
    return learned, to_learn
 
#
# def weights(word_full):
#     word_full.

init(autoreset=True)
		
tb = TinyDB('db_test.json')
Word = Query()
max_points = 5

group_name = "Наличие/Принадлежность • Presence/Belonging"

this_group_full = tb.search((where("Sub group") == group_name))

weight_probability_map_dict = {
    1.0: 30,
    0.8: 20,
    0.6: 10,
    0.4:  5,
    0.2:  5,
    0.0: 30
}

weight, probability = zip(*weight_probability_map_dict.items())

rearange_weights()

print("\n")

learned, to_learn = prepare_lesson()

for word in learned:
    wd = WordShortcut(word)
    name = wd.name()
    if wd.weight():  pts = points_func(wd.weight());
    else: pts = "+";
    print(f'{name.replace(" ", "-")}{Fore.RED}{Style.BRIGHT}{pts}', end='')

for word in to_learn:
    wd = WordShortcut(word)
    name = wd.name()
    if 1 - wd.weight():  pts = points_func(wd.weight());
    else: pts = "■"
    print(f'{name.replace(" ", "-")}{Fore.RED}{Style.BRIGHT}{pts}', end='')






