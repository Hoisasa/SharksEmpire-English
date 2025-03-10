import os
import random
import sys
import re
import time
import soundfile as sf
import sounddevice as sd
from PyQt6.QtCore import QPropertyAnimation
from PyQt6.QtGui import QColor, QFont, QPalette
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QTableWidgetItem, QPushButton, QLabel
from colorama import Fore, Style, init
from tinydb import TinyDB, Query, where
from PyQt6 import QtWidgets,QtCore,QtGui
from python_gui import Ui_UNOlingo
from python_gui2 import Ui_Form


def get_to_learn_list(group_name):
	return tb.search((where("Sub group") == group_name) & (Word.weight > 0.0))


def get_learned_list(group_name):
	return tb.search((where("Sub group") == group_name) & (Word.weight <= 0.0))


def get_pos(target_list, start, finish, banned_word):
	if banned_word:
		banned = target_list.index(banned_word)
	else:
		banned = banned_word
	pos_range = range(start, finish)
	new_pos = random.choice([i for i in pos_range if i != banned])
	return new_pos


def switch_pos(target_list, start, destination, word):
	temp_word = target_list.pop(destination)
	target_list.insert(destination, word)
	target_list.pop(start)
	target_list.insert(start, temp_word)


def shuffle_to_learn(learn_list):
	
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
			new_pos = get_pos(learn_list, allowed_start_second_last, list_length, None)
			switch_pos(learn_list, 0, new_pos, last_word)
			print(f"{last_word['Name']}{Fore.RED}{Style.BRIGHT}worked")
			print("".join(i["Name"] + "\n" for i in learn_list))


def shuffle_learned(learned):
	random.shuffle(learned)


class TransparentShadowLabel(QLabel):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		
		self.setText("Styled Label with Fading Shadow")
		self.setStyleSheet("""
            QLabel {
                padding: 10px;
                border-radius: 15px;
                background-color: rgba(255, 255, 255, 255);  /* Initial background color */
                color: black;  /* Text color */
            }
        """)
		
		# Set up the shadow effect for the label
		self.shadow_effect = QGraphicsDropShadowEffect()
		self.shadow_effect.setOffset(0, 0)  # No shadow offset
		self.shadow_effect.setBlurRadius(20)  # Blur radius for the shadow
		self.shadow_effect.setColor(QColor(0, 0, 0, 255))  # Start with opaque black shadow
		self.setGraphicsEffect(self.shadow_effect)
		
		# Create the animation for the shadow color (fade effect)
		self.shadow_anim = QPropertyAnimation(self.shadow_effect, b"color")
		self.shadow_anim.setDuration(1500)  # Animation duration (in milliseconds)
		self.shadow_anim.setStartValue(QColor(0, 255, 0, 155))  # Opaque shadow (fully visible)
		self.shadow_anim.setKeyValueAt(0.66, QColor(0, 255, 0, 100))
		self.shadow_anim.setEndValue(QColor(0, 0, 0, 50))  # Semi-transparent shadow (fading effect)

class WordShortcut:
	def __init__(self, word_full):
		self.word_meta = word_full
	
	def name(self):
		return self.word_meta.get("Name")
	
	def transl(self):
		return self.word_meta.get("translation")
	
	def transcript(self):
		return self.word_meta.get("transcription")
	
	def weight(self):
		return self.word_meta.get("weight")
	
	def sub_group(self):
		return self.word_meta.get("Sub group")

class EnglishApp(Ui_UNOlingo, QMainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		
		# Variables init
		self.learned = None
		self.to_learn = None
		self.word_iterating = None
		self.wd = None
		self.current_word = None
		self.study_mode = None
		self.group_name = None
		self.mistakes = []
		self.glow = False
		self.Flag = False
		
		self.dock = MistakesDock()
		
		# StyleSheets
		self.stylesheet_prpl = """
				QPushButton {
		    		color: #eee;
		    		border: none;
		    		border-radius: 30px;
		    		border-style: outset;
		    		background: qradialgradient(
		        		cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
		        		radius: 1.35, stop: 0 #fff, stop: 1 #7612b8
		        		);
		    		padding: 5px;
		    		}

				QPushButton:hover {
		    		background: qradialgradient(
		        		cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
		        		radius: 1.35, stop: 0 #fff, stop: 1 #954af7
		        		);
		    		}

				QPushButton:pressed {
		    		border-style: inset;
		    		background: qradialgradient(
		        		cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,
		        		radius: 1.35, stop: 0 #fff, stop: 1 #5b29f2
		        		);
		    		}
				"""
		
		self.stylesheet_red = """
				QPushButton {
					color: #333;
					border: none;
					border-top-right-radius: 40px;
        			border-bottom-right-radius: 40px;
					border-style: outset;
					background: qradialgradient(
						cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
						radius: 1.35, stop: 0 #fff, stop: 1 rgb(199, 20, 47)
						);
					padding: 5px;
					}
				
				QPushButton:hover {
					background: qradialgradient(
						cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
						radius: 1.35, stop: 0 #fff, stop: 1 rgb(224, 53, 78)
						);
					}
				
				QPushButton:pressed {
					border-style: inset;
					background: qradialgradient(
						cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,
						radius: 1.35, stop: 0 #fff, stop: 1 rgb(232, 0, 0)
						);
					}

				"""
		
		# New widgets
		self.prev_page_strip = QPushButton('', self)
		self.prev_page_strip.clicked.connect(self.go_back)
		self.prev_page_strip.setFixedSize(60, 500)
		self.prev_page_strip.setStyleSheet(self.stylesheet_red)
		self.prev_page_strip.setIconSize(QtCore.QSize(100, 300))
		
		self.points_display = TransparentShadowLabel(parent=self.Back_widget)
		self.points_display.setGeometry(QtCore.QRect(650, 70, 341, 50))
		font = QtGui.QFont()
		font.setPointSize(20)
		self.points_display.setFont(font)
		self.points_display.setStyleSheet("")
		self.points_display.setText("")
		self.points_display.setStyleSheet("padding: 0 {:d}px; border-radius: {:d}px;".format(5,10))
		self.points_display.setAlignment(
			QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.points_display.setObjectName("points_display")
		
		# Images
		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap(os.path.join(image_files_path, "audio.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
		self.repeat_audio.setIcon(icon1)
		
		icon2 = QtGui.QIcon()
		icon2.addPixmap(QtGui.QPixmap(os.path.join(image_files_path, "restart.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
		self.restart_lesson.setIcon(icon2)
		
		icon3 = QtGui.QIcon()
		icon3.addPixmap(QtGui.QPixmap(os.path.join(image_files_path, "cross.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
		self.L_answer.setIcon(icon3)
		
		icon4 = QtGui.QIcon()
		icon4.addPixmap(QtGui.QPixmap(os.path.join(image_files_path, "checked.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
		self.W_answer.setIcon(icon4)
		
		icon5 = QtGui.QIcon()
		icon5.addPixmap(QtGui.QPixmap(os.path.join(image_files_path, "return.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
		self.prev_page.setIcon(icon5)
		
		icon6 = QtGui.QIcon()
		icon6.addPixmap(QtGui.QPixmap(os.path.join(image_files_path, "BACK.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
		self.prev_page_strip.setIcon(icon6)
		
		# Mode choose page section
		self.prev_page_2.clicked.connect(self.go_back)
		self.mode1intro.clicked.connect(self.lesson_start)
		self.mode1intro.setStyleSheet(self.stylesheet_prpl)
		self.mode2stud.clicked.connect(self.lesson_start)
		self.mode2stud.setStyleSheet(self.stylesheet_prpl)
		self.mode3ex.setEnabled(True)
		self.mode3ex.clicked.connect(self.lesson_start)
		self.mode3ex.setStyleSheet(self.stylesheet_prpl)

		
		# Lesson section
		self.prev_page.clicked.connect(self.go_back)
		self.repeat_audio.clicked.connect(self.voice_word)
		self.restart_lesson.clicked.connect(self.teach)
		self.translation.clicked.connect(self.reveal_translation)
		self.W_answer.clicked.connect(self.answer)
		self.L_answer.clicked.connect(self.answer)
		
		self.groupGrid.setContentsMargins(60, 10, 0, 0)
		self.groupGrid_2.setContentsMargins(60, 10, 0, 0)
		
		self.spacer, self.spacer_2 = QLabel(), QLabel()
		self.groupGrid.addWidget(self.spacer, 0, 1, 20, 1)
		self.groupGrid_2.addWidget(self.spacer_2, 0, 1, 20, 1)
		self.groupGrid.setColumnMinimumWidth(0, 1250)
		self.groupGrid_2.setColumnMinimumWidth(0, 1250)
		
		self.shadowLabel = QGraphicsDropShadowEffect()
		self.shadowLabel.setColor(QColor(255, 0, 255))  # Set glow color
		self.shadowLabel.setBlurRadius(50)  # Set blur intensity
		self.shadowLabel.setOffset(0, 0)  # Set offset

		self.populate_main_group()
		
		# Effects
		self.shadow = QGraphicsDropShadowEffect()
		
		group_target = "Глаголы Наличия/Количества • Verbs of Presence/Quantity"
		


	# Button functions
	
	def lesson_start(self):
		self.pages.setCurrentIndex(0)
		button_group = self.sender()
		self.study_mode = button_group.objectName()
		if self.study_mode == "mode2stud":
			self.learned  = get_learned_list(self.group_name)
			self.to_learn = get_to_learn_list(self.group_name)
		self.teach()
		
	def go_back(self):
		we_are_here = self.pages.currentIndex()
		print("leaving page" + str(we_are_here))
		self.pages.setCurrentIndex(we_are_here + 1)
		if self.pages.currentIndex() == 3:
			self.prev_page_strip.setVisible(False)
	
	def reveal_translation(self):
		if self.study_mode == "mode1intro":
			self.word_iterator()
		elif self.study_mode == "mode2stud" or self.study_mode == "mode3ex":
			self.word_translation.setVisible(True)
			
			
	def answer(self):
		# Flag is study mode. not Flag is exam mode
		mark = 1 if self.Flag else 3
		mark *= -1 if self.sender().objectName() == self.L_answer.objectName() else 1
		self.mark(mark)
		self.word_iterator()
	
	# Common use functions
	def update_weight_info(self):
		if len(self.to_learn) >= 5:
			last = self.to_learn[-1]
			prelast = self.to_learn[-2]
			self.to_learn = get_to_learn_list(self.group_name)
			for word in self.to_learn:
				if word["Name"] == prelast["Name"]:
					self.to_learn.remove(word)
					self.to_learn.append(word)
			
			for word in self.to_learn:
				if word["Name"] == last["Name"]:
					self.to_learn.remove(word)
					self.to_learn.append(word)
		
		elif len(self.to_learn) >= 3:
			last = self.to_learn[-1]
			self.to_learn = get_to_learn_list(self.group_name)
			for word in self.to_learn:
				if word["Name"] == last["Name"]:
					self.to_learn.remove(word)
					self.to_learn.append(word)
		else:
			self.to_learn = get_to_learn_list(self.group_name)
		self.learned = get_learned_list(self.group_name)
		
	def teach(self):
		self.enable_buttons(True)
		self.W_answer.setEnabled(False)
		self.L_answer.setEnabled(False)
		self.mistakes.clear()
		self.dock.tableWidget.clear()
		if self.study_mode == "mode2stud":
			self.update_weight_info()
			shuffle_to_learn(self.to_learn)
			shuffle_learned(self.learned)
			full_list = []
			if self.to_learn:
				full_list.extend(self.to_learn)
			if self.learned:
				if len(self.to_learn) < 3:
					full_list.extend(self.learned[:2])
				elif len(self.to_learn) < 5:
					full_list.extend(self.learned[:4])
		elif self.study_mode == 'mode1intro' or self.study_mode == 'mode3ex':
			full_list = tb.search(where("Sub group") == self.group_name)
		
		self.word_iterating = iter(full_list)
		self.word_iterator()
		
	def voice_word(self):
		audio, samplerate = sf.read(self.file_path)
		sd.play(audio, samplerate)
		
	def word_iterator(self):
		self.Flag = self.study_mode == "mode2stud"
		if self.study_mode == "mode1intro":
			if self.W_answer.isVisible():
				self.W_answer.setVisible(False)
			if self.L_answer.isVisible():
				self.L_answer.setVisible(False)
			if self.checkBox.isVisible():
				self.checkBox.setVisible(False)
			if self.restart_lesson.isEnabled():
				self.restart_lesson.setEnabled(False)
			self.word_translation.setVisible(True)
			self.translation.setText("Next Word")
			try:
				self.current_word = next(self.word_iterating)
			
			except StopIteration:
				self.teach()
				return
			
			self.wd = WordShortcut(self.current_word)
			self.The_word.setText(self.wd.name())
			self.word_transcription.setText(self.wd.transcript())
			self.word_translation.setText(self.wd.transl())
		
		elif self.Flag or self.study_mode == "mode3ex":
			self.translation.setText("translation")
			self.word_translation.setVisible(False)
			self.W_answer.setEnabled(False)
			self.L_answer.setEnabled(False)
			if not self.checkBox.isVisible():
				self.checkBox.setVisible(True)
			if not self.restart_lesson.isEnabled():
				self.restart_lesson.setEnabled(True)
			
			try:
				self.current_word = next(self.word_iterating)
				
			except StopIteration:
				self.The_word.setText("Lesson Done!")
				if self.checkBox.isChecked():
					self.lesson_resume()
				self.enable_buttons(False)
				return
			if self.Flag and not self.glow and self.current_word in self.learned:
				self.glow = True
				self.shadow = QGraphicsDropShadowEffect()
				self.shadow.setColor(QColor(255, 0, 255))  # Set glow color
				self.shadow.setBlurRadius(50)  # Set blur intensity
				self.shadow.setOffset(0, 0)  # Set offset
				self.restart_lesson.setGraphicsEffect(self.shadow)
				self.restart_lesson.setEnabled(True)
			elif  self.Flag and self.glow and self.current_word in self.to_learn:
				self.glow = False
				self.restart_lesson.setGraphicsEffect(None)
				self.restart_lesson.setEnabled(True)
			else:
				self.restart_lesson.setEnabled(False)
			self.wd = WordShortcut(self.current_word)
			self.show_points()
			self.The_word.setText(self.wd.name())
			self.word_transcription.setText(self.wd.transcript())
			self.word_translation.setText(self.wd.transl())
			self.W_answer.setEnabled(True)
			self.L_answer.setEnabled(True)
		
		QApplication.processEvents()
		self.file_path = os.path.join(audio_base_path, f"{self.wd.sub_group().replace('/', '-')}",
									  f"{self.wd.name().split(' (')[0]}.wav")
		self.voice_word()
		
		
	def populate_main_group(self):
		self.pages.setCurrentIndex(3)
		self.prev_page_strip.setVisible(False)
		self.groups = list(dict.fromkeys([group.get('Group') for group in tb.all()]))
		for num, group in enumerate(self.groups):
			
			self.Group_button = QPushButton(f'{group}', self)
			self.Group_button.clicked.connect(self.populate_group)
			self.Group_button.setFont(QFont('Arial', 32))
			self.Group_button.setMinimumHeight(70)
			self.Group_button.setStyleSheet(self.stylesheet_prpl)
			self.groupGrid_2.addWidget(self.Group_button, num, 0)

		
	def populate_group(self):
		self.clear_grid_column()
		self.prev_page_strip.setVisible(True)
		self.pages.setCurrentIndex(2)
		group_target = self.sender().text()
		self.groups = list(dict.fromkeys(
				[group.get('Sub group') for group in tb.search(where("Group") == group_target)]))
		for num, group in enumerate(self.groups):
			self.Group_button = QPushButton(f'{group}', self)
			self.Group_button.clicked.connect(self.switch_to_WordLearn)
			self.Group_button.setFont(QFont('Arial', 32))
			self.Group_button.setMinimumHeight(70)
			self.Group_button.setStyleSheet(self.stylesheet_prpl)
			self.groupGrid.addWidget(self.Group_button, num, 0)

	
	def clear_grid_column(self):
		for i in reversed(range(self.groupGrid.count())):  # Iterate in reverse to avoid index shifting
			item = self.groupGrid.itemAt(i)
			if item is not None:
				widget = item.widget()
				_, column, _, _ = self.groupGrid.getItemPosition(i)  # Get the column position
				if column == 0:
					self.groupGrid.removeWidget(widget)  # Remove from layout
					widget.deleteLater()  # Delete widget
	
	def mark(self, num):
		new_value = round((self.wd.weight() - (self.wd.weight() * max_points % 1 / max_points ) - num / max_points),2)
		new_value = min(1, max(new_value, 0))
		tb.update({"weight": new_value}, (where('Sub group') == self.wd.sub_group()) & (where("Name") == self.wd.name()))
	
	def enable_buttons(self, on_off):
		self.W_answer.setVisible(on_off)
		self.L_answer.setVisible(on_off)
		self.translation.setVisible(on_off)
		
	def show_points(self):
		self.points_display.shadow_anim.stop()
		amount = max_points - self.wd.weight()*max_points
		self.points_display.setText(" 🐟" * int(amount))
		if amount == max_points:
			self.points_display.setText("MAX" + " 🐟" * int(amount))
			self.points_display.shadow_anim.start()

	

		
	
	def lesson_resume(self):
		self.dock.populate(self.mistakes)
		self.dock.show()
	
	def switch_to_WordLearn(self, group):
		self.pages.setCurrentIndex(1)
		self.group_name = self.sender().text()
		pass


class MistakesDock(Ui_Form, QMainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
	
	def populate(self, mistakes):
		self.tableWidget.setRowCount(len(mistakes))  # Set row count based on the number of mistakes
		self.tableWidget.setColumnCount(2)
		self.tableWidget.setColumnWidth(0, 350)  # Set width for the 'Name' column
		self.tableWidget.setColumnWidth(1, 530)
		for row, mistake in enumerate(mistakes):


			# Set the Name in the first column
			self.tableWidget.setItem(row, 0, QTableWidgetItem(mistake["Name"]))
			
			# Set the Translation in the second column
			self.tableWidget.setItem(row, 1, QTableWidgetItem(mistake["translation"]))
			
		
		
		
# Build command
# pyinstaller --onefile --add-data "images;images" --add-data "audiofiles;audiofiles" --add-data "db_test.json;." --add-data "python_gui.py;." --add-data "python_gui2.py;." audio_dev_ver.py --exclude-module "PySide6" --icon=images/unolingo_P64_icon.ico --windowed


if __name__ == '__main__':
	init(autoreset=True)
	app = QApplication(sys.argv)

	
	max_points = 5

	if getattr(sys, 'frozen', False):
		# Running as a packaged app (PyInstaller)
		base_path = sys._MEIPASS
	else:
		# Running as a script
		base_path = os.getcwd()  # Current working directory
	audio_base_path = os.path.join(base_path, 'audiofiles')
	image_files_path = os.path.join(base_path, 'images')
	tb = TinyDB(os.path.join(base_path, "db_test.json"))
	Word = Query()
	
	appIcon = QtGui.QIcon()
	appIcon.addPixmap(QtGui.QPixmap(os.path.join(image_files_path, "UNOlingo.png")), QtGui.QIcon.Mode.Normal,
					QtGui.QIcon.State.On)
	QApplication.setWindowIcon(appIcon)
	# Create and show the app window
	window = EnglishApp()
	window.show()

	sys.exit(app.exec())