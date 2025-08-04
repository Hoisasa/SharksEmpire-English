import os
from tinydb import TinyDB

tb = TinyDB('db.json')

valid = 0
total = 0
for entry in tb:
#     entry = tb.get(doc_id=3)


    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_path = os.path.dirname(script_dir)
    audio_base_path = os.path.join(base_path, 'assets', 'audiofiles')

    file_path = os.path.join(audio_base_path, f"{entry['Sub group'].replace('/', '-').replace(':', '-')}",
                                  f"{entry['Name'].split(' (')[0]}.wav")

    try:
        with open(file_path, 'rb'):
            valid += 1
    except FileNotFoundError:
        relative_path = os.path.relpath(file_path, base_path).replace('/', ' / ')
        print(f'Filepath causing error:  {relative_path}')

    total += 1

print(valid, '/', total)