import sys, random
import os

import soundfile as sf
import sounddevice as sd


from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QHBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from tinydb import TinyDB, Query, where


# Function to load word-translation pairs from a text file

class WordShortcut:
    def __init__(self, word_dict):
        self.word_dict = word_dict
        self.word_weights = [word.get("weight") for word in word_dict]
        if sum(self.word_weights):
            self.word_meta = random.choices(self.word_dict, self.word_weights, k=1)[0]
        else:
            self.word_meta = {"Name": "Lesson Complete!", "translation": "", "weight": 1.0, "transcription": '', "Sub group": '',
             "Group": ''}


    def name(self):
        return self.word_meta.get("Name")

    def trsl(self):
        return self.word_meta.get("translation")

    def tcpt(self):
        return self.word_meta.get("trasncription")

    def wght(self):
        return self.word_meta.get("weight")

    def sgrp(self):
        return self.word_meta.get("Sub group")

    def updateWgth(self, new_value):
        tb.update({"weight": new_value}, (where('Sub group') == self.sgrp()) & (where("Name") == self.name()))
        self.word_weights = [word.get("weight") for word in self.word_dict]



class WordLearn(QWidget):

    def __init__(self, words):
        super().__init__()

        self.S_Group_words = tb.search(where("Sub group") == f"{words}")
        self.translation_visible = False
        self.wd = None
        self.blacklist = []

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('UNOlingo')
        self.setGeometry(200, 200, 1280, 720)

        # Layout
        self.study_layout = QVBoxLayout()
        self.learning_hub_layout = QVBoxLayout()
        self.layout_buttons1 = QHBoxLayout()
        self.layout_buttons2 = QHBoxLayout()

        # Dropdown for selecting word groups
        # self.group_selector = QComboBox(self)
        # self.group_selector.adjustSize()
        # self.group_selector.addItems(self.group_names)  # Add group names
        # self.group_selector.currentIndexChanged.connect(self.update_word_group)
        # self.group_selector.setCurrentIndex(0)
        # self.update_word_group()
        # self.group_selector.setFont(QFont('Arial', 28))
        # self.study_layout.addWidget(self.group_selector)

        self.button = QPushButton("Выбор групп")
        self.button.clicked.connect(self.switch_to_GroupSelect)
        self.button.setFont(QFont('Arial', 32))
        self.study_layout.addWidget(self.button)

        # Label for the word
        self.word_label = QLabel('Click "✅✅✅" to see a word', self)
        if sum([weight["weight"] for weight in self.S_Group_words]) == 0:
            self.word_label = QLabel('Lesson Complete!', self)
        self.word_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.word_label.setFont(QFont('Arial', 48))
        self.study_layout.addWidget(self.word_label)

        # Button to load the next random word
        self.Wnext_button = QPushButton('✅✅✅', self)
        self.Wnext_button.clicked.connect(self.next_word)
        self.Wnext_button.setFont(QFont('Arial', 32))
        self.layout_buttons1.addWidget(self.Wnext_button)

        self.Lnext_button = QPushButton('❌❌❌', self)
        self.Lnext_button.clicked.connect(self.next_word)
        self.Lnext_button.setFont(QFont('Arial', 32))
        self.layout_buttons1.addWidget(self.Lnext_button)

        # Button to load the next random word
        self.repeat_word = QPushButton('Repeat', self)
        self.repeat_word.clicked.connect(lambda: self.repeat_words())
        self.repeat_word.setFont(QFont('Arial', 32))
        self.layout_buttons2.addWidget(self.repeat_word)

        # Button to reveal translation
        self.translate_button = QPushButton('Reveal Translation', self)
        self.translate_button.clicked.connect(self.reveal_translation)
        self.translate_button.setFont(QFont('Arial', 32))
        self.layout_buttons2.addWidget(self.translate_button)

        self.study_layout.addLayout(self.layout_buttons1)
        self.study_layout.addLayout(self.layout_buttons2)

        # Set the layout
        self.setLayout(self.study_layout)

    def switch_to_GroupSelect(self):
        # Hide the current window (Window 1)
        self.hide()

        # Create and show Window 2
        self.window2 = GroupSelect()
        self.window2.show()

    def repeat_words(self):
        print(self.wd)
        if self.wd:
            # Construct the file path
            audio, samplerate = sf.read(self.file_path)
            sd.play(audio, samplerate)

    def next_word(self):
        self.from_button = self.sender()
        if self.from_button.text() == '✅✅✅' and self.wd and (self.wd!="Lesson Complete!"):
            self.new_weight = max(round(self.wd.wght() - 0.2, 1), 0)
            self.wd.updateWgth(self.new_weight)
            self.S_Group_words = tb.search(where("Sub group") == self.wd.sgrp())
        elif self.from_button.text() == '❌❌❌' and self.wd and (self.wd!="Lesson Complete!"):
            self.new_weight = min(round(self.wd.wght() + 0.1, 1), 1)
            self.wd.updateWgth(self.new_weight)
            self.S_Group_words = tb.search(where("Sub group") == self.wd.sgrp())
        else:
            pass
        
        self.translation_visible = False
        self.wd = WordShortcut(self.S_Group_words)
        if self.wd!='Lesson Complete!' and self.wd!=None:
            self.translation_visible = False
            self.wd = WordShortcut(self.S_Group_words)
            self.word_label.setText(self.wd.name())  # Show the word
            
            QApplication.processEvents()
            self.file_path = os.path.join(audio_base_path, f"{self.wd.sgrp().replace('/', '-')}",
                                          f"{self.wd.name().split(' (')[0]}.wav")
            audio, samplerate = sf.read(self.file_path)
            sd.play(audio, samplerate)
        else:
            self.translation_visible = False
            self.switch_to_GroupSelect()
        # self.blacklist.append(self.wd.name())
        # if len(self.blacklist) > 4: self.blacklist.pop(0)


        

    def reveal_translation(self):
        if self.wd.name():
            self.word_label.setText(f"{self.wd.name()} - {self.wd.trsl()}")  # Show word and translation
            self.translation_visible = True

    # def update_word_group(self):
    #     self.ind = self.group_selector.currentIndex()
    #     self.word_dict = self.word_BOOK[self.ind][1]
    #     self.word_weights = [ i["weight"] for i in (self.word_dict.values()) ]
    
class GroupSelect(QWidget):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Group Select")
        self.setGeometry(200, 200, 1280, 720)
        
        # Create the layout
        self.layout = QVBoxLayout(self)
        
        self.groups = list(dict.fromkeys([group.get('Group') for group in tb.all()]))
        for group in self.groups:
            self.Group_button = QPushButton(f'{group}', self)
            self.Group_button.clicked.connect(lambda checked, g=group: self.switch_to_SUBGroupSelect())
            self.Group_button.setFont(QFont('Arial', 32))
            self.layout.addWidget(self.Group_button)
            
        self.setLayout(self.layout)
    
    
    def switch_to_SUBGroupSelect(self):
        # Hide the current window (Window 1)
        self.hide()
        self.button_group = self.sender()
        # Create and show Window 2
        self.window2 = SUBGroupSelect(self.button_group.text())
        self.window2.show()
    
class SUBGroupSelect(QWidget):
    def __init__(self, group_target):
        super().__init__()
        self.target = group_target

        self.setWindowTitle("Sub Group Select")
        self.setGeometry(200, 200, 1280, 720)

        # Create the layout
        self.layout = QVBoxLayout(self)

        self.groups = list(dict.fromkeys([group.get('Sub group') for group in tb.search(where("Group") == group_target)]))
        for group in self.groups:
            self.Group_button = QPushButton(f'{group}', self)
            self.Group_button.clicked.connect(lambda checked, g=group:  self.switch_to_WordLearn(group))
            self.Group_button.setFont(QFont('Arial', 32))
            self.layout.addWidget(self.Group_button)
        
        self.Group_button = QPushButton(f'Back', self)
        self.Group_button.clicked.connect(lambda checked: self.switch_back())
        self.Group_button.setFont(QFont('Arial', 32))
        self.layout.addWidget(self.Group_button)

        self.setLayout(self.layout)

    def switch_to_WordLearn(self, group):
        # Hide the current window (Window 1)
        self.hide()

        # Create and show Window 2
        self.window1 = WordLearn(group)
        self.window1.show()

    def switch_back(self):
        self.hide()

        # Create and show Window 2
        self.window = GroupSelect()
        self.window.show()



# Main function
if __name__ == '__main__':
    app = QApplication(sys.argv)


    # Load words from file
        # Determine the base path once during initialization
    if getattr(sys, 'frozen', False):
        # Running as a packaged app (PyInstaller)
        base_path = sys._MEIPASS
    else:
        # Running as a script
        base_path = os.getcwd()  # Current working directory
    audio_base_path = os.path.join(base_path, 'audiofiles')
    # tb = TinyDB(os.path.join(base_path, "db.json"))

    # Create and show the app window
    window = GroupSelect()
    window.show()

    sys.exit(app.exec())
