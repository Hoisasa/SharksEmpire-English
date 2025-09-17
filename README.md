# Sharks' Empire: English

<div align="center">
  <img height="333" src="https://github.com/Hoisasa/English-word-learning/blob/readme/assets/images/sharkonamiTransparent.png?raw=true">
</div>

> ### An English Learning app for windows in a form of flashcards.  
>  Provides words upto B2 level of English without the need for subscription

<p align=center>
<img alt="Static Badge" src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=ffd242">
<img alt="Static Badge" src="https://img.shields.io/badge/Kokoro-TTS-ebb434">
<img alt="Static Badge" src="https://img.shields.io/badge/StyleTTS2-TTS-cc8a33">
<img alt="Static Badge" src="https://img.shields.io/badge/TinyDB-DB-587896">
<img alt="Static Badge" src="https://img.shields.io/badge/PySide-6.9-41CD52?logo=qt">
<img alt="Static Badge" src="https://img.shields.io/badge/English Level-B2-ba5df0">
<img alt="Static Badge" src="https://img.shields.io/badge/Licence-GPL3.0-green">
</p>

## Table of contents

- ### [Screenshots](#camera-Screenshots)
- ### [Key Features](#Key-Features)
- ### [Installation](#Installation)
- ### [Tweaking project](#How-to-tweak-project-for-your-own-needs)
- ### [Credits](#Credits)


## :camera: Screenshots

<p align=center style="overflow-x:auto; white-space:nowrap; border:1px solid #ccc; padding:5px;">
<img width="850" height="530" alt="Image" src="https://github.com/user-attachments/assets/84281d8b-7da3-4d3f-9337-677998790cdc" />
<img width="353" height="220" alt="Image" src="https://github.com/user-attachments/assets/7464bd62-bfdc-43ad-b055-d8b610a2e27d" />
<img width="353" height="220" alt="Image" src="https://github.com/user-attachments/assets/0c491664-08f2-4d61-9cdc-93337646b19c" />
</p>
<details>
<summary align="center">
  <span style="color:blue; font-weight:bold;">Show more screenshots</span>
</summary>
<p align=center style="overflow-x:auto; white-space:nowrap; border:1px solid #ccc; padding:5px;">
<img width="353" height="220" alt="Image" src="https://github.com/user-attachments/assets/8909e0a5-6241-4d0c-8960-a0708b184c55" />
<img width="353" height="220" alt="Image" src="https://github.com/user-attachments/assets/cda5121e-394c-4588-9351-1bbd87bf9cb4" />
<img width="353" height="220" alt="Image" src="https://github.com/user-attachments/assets/66151a11-65d9-4bbe-aae3-5d92a5923d98" />
<img width="353" height="220" alt="Image" src="https://github.com/user-attachments/assets/4e85d2d6-d9a6-46cf-a403-58833056542f" />
</p>
</details>


## Key Features

There are three modes Overview Practice and Exam. 
While overview just straight up shows the translation others provide it after pressing a designated button.
In the end all mistakes are shown as so to provide you with a feature to reflect on your answers. 
To gauge the progress of learning each word they have points assigned to them. 
When you are ready - complete the exam: a more strict area which punishes mistakes more. 
The exam goal is to make as few mistakes as possible 
But in order to not be utterly strict it allows one mistake to be completed

✅**The features of an app are as follows:**
- 1️⃣**Only one part of speech per group, less confusion**  
- 📦**Groups consist of subgroups** 
- 🧮**Mostly just 10 words per subgroup** flashcards organised into quite small groups for easier memorization.
- 🎯**self evaluation** We don't put a goal of checking your typing speed or pronunciation thus it's your responsibility to evaluate the answer. We also wanted to reduce guessing factor which `four options` introduces so if you see that your translation didn't align with given one - press a `wrong answer` button
- 🌊👋.**context-sensitive translations** it aims to show beginner how words meanings can vary depending on context 
- 🗣️**target learner language Russian**
> (**you can provide your own translations for db**) [Example](#add-your-vocabulary-or-locale)


## Installation

👜[**Download**](https://github.com/Hoisasa/English-word-learning/releases/download/v0.2.1/UnoLingoLearn.rar) the portable version from [releases](https://github.com/Hoisasa/English-word-learning/releases). (Windows/Linux x86-64)\
**or**\
⬇️[**Install**](https://flathub.org/ru/apps/io.github.hoisasa.SharksEmpire-English) the app from flathub on any Linux

## How to tweak project for your own needs
    
[Filling DB](#Add-your-vocabulary-or-locale)

### Setup

```bash

git clone https://github.com/Hoisasa/English-word-learning.git
pip install -r requirements.txt
```
Then run `main.py`

### Project File structure

* [`assets`](assets)
  * [`audiofiles`](assets/audiofiles)
  * [`images`](assets/images)
* [`GUI`](GUI) contains qt files with their generated py files
    * [`untitled.ui`](GUI/untitled.ui) corresponds to [`python_gui.py`](GUI/python_gui.py)
    * [`mistakes.ui`](GUI/mistakes.ui) corresponds to [`python_gui2.py`](GUI/python_gui2.py)
    * [`loading.ui`](GUI/loading.ui) corresponds to [`python_gui_loader.py`](GUI/python_gui_loader.py) and [`python_gui_updater.py`](GUI/python_gui_updater.py) 
* [`src`](src) basically a playground
* [`Vocabulary`](Vocabulary) 
    * [`3000_english_words.txt`](Vocabulary/3000_english_words.txt) a reference list
    * [`db.json`](Vocabulary/db.json) a TinyDB file 
    * [`grouping_main.py`](Vocabulary/grouping_main.py) The file used to populate Database. [`Filling DB`](#Add-your-vocabulary-or-locale)
* [`main.py`](main.py) aka `main file`
* [`main.spec`](main.spec) build config for linux
* [`main_win.spec`](main_win.spec) build config for windows

### Add your vocabulary or locale

#### Adding words comes in three steps
* #### [Add](#Add-each-word-entries-in-code) each word entries in code
* #### [populate](#Populating-database) them in database
* #### [run](#Generating-Audio-files) Kokoro StyleTTS2 to generate audio files

### Add each word entries in code

> **Note:** Latest commit populates SqlLite database refer to [**This**](https://github.com/Hoisasa/English-word-learning/blob/665618e074a5cd49b6386147cfb8ed05e2fcf5b4/Vocabulary/grouping_main_2.py) commit to view how TinyDB population was implemented

> **Disclaimer:** The specified commit was work in progress and may contain errors / dupes. Use just as an example

The process is as simple as it is notorious  
First lets look at structure

```json
{
  "Name": "beginning",
  "translation": "начало",
  "weight": 1,
  "transcription": "",
  "Sub group": "Начало • Begining",
  "Group": "Глаголы этапов • Verbs of Stage"
}
```

So we have Name of word and its translation and if you want to add words independent of context then you can easily just provide words and use translator API to do so 
> make sure to provide any dummy subgroup and group so that your custom one has entrypoint    

issues are coming when you want context-sensitive translations (mostly due to `grouping of words` Problem) if words are already grouped, AI can easily unpack those to meet this pattern of filling database:

```python
POS = "verb"
MAIN_GROUP = "Бытовые Глаголы • Verbs of Everyday Life"

SUB_GROUP = "Болеть • Feel sick"
add_word("be ill", "болеть (болезнь)", SUB_GROUP, MAIN_GROUP, POS)
...
add_word("bury", "хоронить",SUB_GROUP, MAIN_GROUP, POS)

MAIN_GROUP = "Глаголы Чувства • Verbs of Feeling" #next group
```

### Populating database

The filling process is passing constructed dictionary as doc to a TinyDB

To provide clear from dupes db our Primary key here *even though tiny db doesnt need one* is the combination of word and subgroup. Simply you want to avoid ambiguity of translation

```python
def add_word(name, transl, s_group, group, pos):
	global c
	doc = {"Name": name, "translation": transl, "weight": 1.0, "transcription": '', "Sub group": s_group,
		   "Group": group, "Part of speech": pos}
	if tb.search((where("Name") == name) & (where("Sub group") == s_group)):
		c += 1
		print(f"{c}", end=' ')
	
	else:
		tb.insert(doc)
```

### Generating Audio files

Following the instructions provided on TTS repository install [**Kokoro**](https://github.com/hexgrad/kokoro) if it doesn't work most probably you missed this part of their readme 

`Windows Installation To install espeak-ng on Windows:`

`Go to espeak-ng releases`  
`Click on Latest release`  
`Download the appropriate *.msi file (e.g. espeak-ng-20191129-b702b03-x64.msi)`  
`Run the downloaded installer`  

**setting up database iterator**  
you can scope it to only newly added items; just mess with the first loop

<details>
<summary> Imports (click to expand)</summary>

```python
from kokoro import KPipeline
from IPython.display import display, Audio
import soundfile as sf
import os

from regex import regex
from tinydb import TinyDB, where
```
</details>


```python
pipeline = KPipeline(lang_code='a') # <= make sure lang_code matches voice

tb = TinyDB('db.json')
groups = []
for group in tb.all():
    if group.get('Sub group') not in groups:
        groups.append(group.get('Sub group'))
word_dict = {}
for group in groups:
    group_words = []
    words = tb.search(where("Sub group") == group)
    for word in words:
        group_words.append(word.get("Name").split(' (')[0])
    group_words = '\n'.join(group_words)
    word_dict.update({group.replace('/', '-').replace(':', '-'): group_words})

print(word_dict)
```

and pass it to tts 

```python
for group, dictionary in word_dict.items():
      text = regex.split(r' (?=\p{Lu})', dictionary, maxsplit=1)[0]
      text += '.'
      generator = pipeline(
          text, voice='af_heart', # <= change voice here
          speed=1, split_pattern=r'\n+'
      )
  
      for i, (gs, ps, audio) in enumerate(generator):
          print(i)  # i => index
          print(gs) # gs => graphemes/text
          print(ps) # ps => phonemes
          # This will not raise an error if the directory already exists
          os.makedirs(f'audiofiles/testing/{group}', exist_ok=True)
          sf.write(f'audiofiles/testing/{gs[:-1]}.wav', audio, 24000) # save each audio file
```

without additional tuning tts makes around 5% of errors in pronunciation this errors may occur or may not occur depending on the surrounding silent symbols or chosen american or british english so youd want to gather and refine them

### Build

```bash
pyinstaller --workpath 'updates/build' --distpath 'updates/dist' main.spec   
```

## Credits

This software uses the following packages and resources:

* uses icons8 from  [This Site](https://icons8.com/icon/LATsUneHQg4J/u-turn-to-left)
* uses Kokoro tts from [This repository](https://github.com/hexgrad/kokoro)



