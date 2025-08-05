from tokenize import group

from tinydb import TinyDB, where, Query

tb = TinyDB('db.json')
tb.update({'weight': 1})
tb.drop_table("exam grades")
tb.drop_table("focused review")
