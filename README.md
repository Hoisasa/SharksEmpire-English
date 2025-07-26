# Sharks

<div align="center">
  <img height="333" src="https://github.com/Hoisasa/English-word-learning/blob/readme/assets/images/sharkonamiTransparent.png?raw=true">
</div>

> ### An English Learning app for windows in a form of flashcards. 
> ### Provides words upto B2 level of English without the need for subscription

<div align="center">
    <p>
    <img alt="Static Badge" src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=ffd242">
    <img alt="Static Badge" src="https://img.shields.io/badge/Kokoro-TTS-ebb434">
    <img alt="Static Badge" src="https://img.shields.io/badge/StyleTTS2-TTS-cc8a33">
    <img alt="Static Badge" src="https://img.shields.io/badge/TinyDB-DB-587896">
    <img alt="Static Badge" src="https://img.shields.io/badge/PySide-6.9-41CD52?logo=qt">
    <img alt="Static Badge" src="https://img.shields.io/badge/English Level-B2-ba5df0">
    <img alt="Static Badge" src="https://img.shields.io/badge/Licence-MIT-green">
    </p>
</div>

##

- [Key Features](#Key-Features)
- [Installation](#Installation)
- [Tweaking project](#How-to-tweak-project-for-your-own-uses)


## Key Features

There are three modes Overview Practice and Exam. 
While overview just straight up shows the translation others provide it after pressing a designated button.
In the end all mistakes are shown as so to provide you with a feature to reflect on your answers. 
To gauge the progress of learning each word they have points assigned to them. 
When you are ready - complete the exam: a more strict area which punishes mistakes more. 
The exam goal is to make as few mistakes as possible 
But in order to not be utterly strict it allows one mistake to be completed

**The features of an app are as follows:**
- **Only one part of speech per group, less confusion**  
- **Groups consist of subgroups** 
- **Mostly just 10 words per subgroup** flashcards organised into quite small groups for easier memorisation.
- **self evaluation** We don't put a goal of checking your typing speed or pronunciation thus it's your responsibility to evaluate the answer. We also wanted to reduce guessing factor which `four options` introduces so if you see that your translation didn't align with given one - press a `wrong answer` button
- **context-sensitive translations** it aims to show beginner how words meanings can vary depending on context 
- **target learner language russian**
> (**you can provide your own translations for db**) [Example]()


## Installation

[**Download**](https://github.com/Hoisasa/English-word-learning/releases/download/v0.2.1/UnoLingoLearn.rar) the portable version from [releases](https://github.com/Hoisasa/English-word-learning/releases).

## How to tweak project for your own uses
    
[Filling DB](#Add-your-vocabulary-or-locale)

### Setup

```bash
git clone https://github.com/Hoisasa/English-word-learning.git
cd English-word-learning
pip install -r requirements.txt
```
Then run `audio_dev_ver.py`

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
* [`audio_dev_ver.py`](audio_dev_ver.py) aka `main file`
* [`audio_dev_ver.spec`](audio_dev_ver.spec) build config

### Add your vocabulary or locale




uses icons from  https://icons8.com/icon/LATsUneHQg4J/u-turn-to-left
uses tts from repository https://github.com/hexgrad/kokoro



