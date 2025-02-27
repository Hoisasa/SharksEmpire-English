from tinydb import TinyDB, Query, where

tb = TinyDB("db.json")
user = Query()

# result = tb.search(where("Sub group") == "Движение вверх/вниз • Upward/Downward Movement")
# groups = list(dict. fromkeys([group.get('Sub group') for group in tb.all()]))
# group = list(dict.fromkeys([group.get('Group') for group in tb.all()]))
new_value = 0.8
result = tb.update({"weight": new_value}, (where("Name") == "stand up"))

# set({"weight": new_value})
print(result[1])
# print(groups)