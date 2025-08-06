# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/gpl-3.0.txt>.


import os
import platform
import random
import sys

import soundfile as sf
import sounddevice as sd

from PySide6 import QtCore, QtGui
from PySide6.QtCore import QPropertyAnimation, Qt, QEasingCurve, QSize
from PySide6.QtGui import QColor, QFont, QPainterPath, QRegion, QIcon
from PySide6.QtWidgets import (
	QApplication, QMainWindow, QGraphicsDropShadowEffect,
	QPushButton, QLabel, QSpacerItem, QSizePolicy
)

from tinydb import TinyDB, Query, where

from src.circular_progress.circular_progressbar import CircularProgress
from GUI.python_gui import Ui_SEEnglish



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
	list_length = len(learn_list)
	allowed_start_last, allowed_start_second_last = 2, 1

	if list_length >= 5:
		last_word = learn_list[-1]
		second_last_word = learn_list[-2]
		random.shuffle(learn_list)
		if learn_list[0] == last_word:
			new_pos = get_pos(learn_list, allowed_start_last, list_length, second_last_word)
			switch_pos(learn_list, 0, new_pos, last_word)
		elif learn_list[1] == last_word:
			new_pos = get_pos(learn_list, allowed_start_last, list_length, None)
			switch_pos(learn_list, 1, new_pos, last_word)
		elif learn_list[0] == second_last_word:
			new_pos = get_pos(learn_list, allowed_start_second_last, list_length, last_word)
			switch_pos(learn_list, 0, new_pos, second_last_word)

	elif list_length >= 3:
		last_word = learn_list[-1]
		random.shuffle(learn_list)
		if learn_list[0] == last_word:
			new_pos = get_pos(learn_list, allowed_start_second_last, list_length, None)
			switch_pos(learn_list, 0, new_pos, last_word)


def shuffle_learned(learned):
	random.shuffle(learned)

class TransparentShadowLabel(QLabel):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setText("Styled Label with Fading Shadow")

		# Set up the shadow effect for the label
		self.shadow_effect = QGraphicsDropShadowEffect()
		self.shadow_effect.setOffset(0, 0)
		self.shadow_effect.setBlurRadius(20)
		self.shadow_effect.setColor(QColor(0, 0, 0, 255))
		self.setGraphicsEffect(self.shadow_effect)

		# Animation for fading shadow color
		self.shadow_anim = QPropertyAnimation(self.shadow_effect, b"color")
		self.shadow_anim.setStartValue(QColor(0, 0, 0, 190))
		self.shadow_anim.setEndValue(QColor(0, 0, 0, 0))
		self.shadow_anim.setDuration(1500)
		self.shadow_anim.setEasingCurve(QEasingCurve.Type.InOutSine)

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


class EnglishApp(Ui_SEEnglish, QMainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		# Variables init
		self.size = None
		self.learned = None
		self.to_learn = None
		self.word_iterating = None
		self.wd = None
		self.current_word = None
		self.study_mode = None
		self.group_name = None
		self.grade = None
		self.grades_list = None
		self.mistakes = []
		self.glow = False
		self.Flag = False
		self.dock = None  # MistakesDock()

		self.grades_table = tb.table('exam grades')
		self.grades_objects = [self.Grade1, self.Grade2, self.Grade3, self.Grade4, self.Grade5]

		self.focus = tb.table('focused review')

		# self.dock = MistakesDock()
		self.progress = CircularProgress()
		self.progress.setFixedSize(120, 60)

		# StyleSheets
		self.AnswersLabel.setStyleSheet("font-size: 48px; color: #00007f; font-weight: bold;")

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

		self.stylesheet_gray = """
				QPushButton {
					color: #333;
					border: none;
					border-radius: 30px;
					border-style: outset;
					background: qradialgradient(
						cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
						radius: 1.35, stop: 0 #fff, stop: 1 #ccc
						);
					padding: 5px;
					}

				QPushButton:hover {
					background: qradialgradient(
						cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,
						radius: 1.35, stop: 0 #fff, stop: 1 #aaa
						);
					}

				QPushButton:pressed {
					border-style: inset;
					background: qradialgradient(
						cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,
						radius: 1.35, stop: 0 #fff, stop: 1 #bbb
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
		self.points_display.setStyleSheet("padding: 0 {:d}px; border-radius: {:d}px;".format(5, 10))
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
		self.prev_page_2.setIcon(icon5)

		icon6 = QtGui.QIcon()
		icon6.addPixmap(QtGui.QPixmap(os.path.join(image_files_path, "BACK.png")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
		self.prev_page_strip.setIcon(icon6)
		
		icon = QIcon()
		icon.addFile(os.path.join(image_files_path, "io.github.hoisasa.SharksEmpire-English.ico"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
		self.setWindowIcon(icon)

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
		self.Repeat.clicked.connect(lambda _: (self.pages.setCurrentIndex(1), self.teach()))
		self.SaveAndExit.clicked.connect(self.choose_next_lesson)
		self.Layout_type.toggled.connect(self.toggle_translation)

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

	# Button functions

	def lesson_start(self):
		self.pages.setCurrentIndex(1)
		self.size = len(tb.search(where("Sub group") == self.group_name))
		button_group = self.sender()
		self.study_mode = button_group.objectName()
		if self.study_mode == "mode2stud":
			self.learned = get_learned_list(self.group_name)
			self.to_learn = get_to_learn_list(self.group_name)
		self.teach()

	def go_back(self):
		we_are_here = self.pages.currentIndex()
		self.pages.setCurrentIndex(we_are_here + 1)
		if self.pages.currentIndex() == 4:
			self.prev_page_strip.setVisible(False)
			self.populate_main_group()
		if self.pages.currentIndex() == 3:
			self.populate_group()

	def reveal_translation(self):
		if self.study_mode == "mode1intro":
			self.word_iterator()
		elif self.study_mode == "mode2stud" or self.study_mode == "mode3ex":
			self.word_translation.setVisible(True)

	def answer(self):
		if self.Layout_type.isChecked() and self.word_translation.isHidden():
			self.word_translation.setVisible(True)
			return

		# Flag is study mode. not Flag is exam mode
		wrong = self.sender().objectName() == "L_answer"
		exam = not self.Flag
		mark = 3 if exam else 1
		mark *= -1 if wrong else 1
		if wrong:
			self.mistakes.insert(0, self.current_word)
		self.mark(mark)
		self.word_iterator()

	def choose_next_lesson(self):
		if len(self.mistakes)==1:
			self.focus.upsert(*self.mistakes)
		self.populate_group()

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
		self.mistakes.clear()
		self.enable_buttons(True)
		self.toggle_translation()
		self.W_answer.setEnabled(False)
		self.L_answer.setEnabled(False)
		if self.dock:
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


		if self.study_mode == "mode3ex":
			shuffle_to_learn(full_list)

		self.size = len(full_list)

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
			if self.Layout_type.isVisible():
				self.Layout_type.setVisible(False)
			if self.restart_lesson.isEnabled():
				self.restart_lesson.setEnabled(False)
			self.points_display.setText('')
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
			self.show_points()

		else:
			self.translation.setText("translation")
			self.word_translation.setVisible(False)
			self.W_answer.setEnabled(False)
			self.L_answer.setEnabled(False)

			if not self.checkBox.isVisible():
				self.checkBox.setVisible(True)
			if not self.Layout_type.isVisible():
				self.Layout_type.setVisible(True)
			if not self.restart_lesson.isEnabled():
				self.restart_lesson.setEnabled(True)

			try:
				self.current_word = next(self.word_iterating)
			except StopIteration:
				self.The_word.setText("Lesson Done!")
				sd.stop()
				if self.checkBox.isChecked() or self.study_mode == "mode3ex":
					self.lesson_resume()
				self.enable_buttons(False)
				self.translation.setVisible(False)
				return
			if self.Flag and not self.glow and self.current_word in self.learned:
				self.glow = True
				self.shadow = QGraphicsDropShadowEffect()
				self.shadow.setColor(QColor(255, 0, 255))  # Set glow color
				self.shadow.setBlurRadius(50)  # Set blur intensity
				self.shadow.setOffset(0, 0)  # Set offset
				self.restart_lesson.setGraphicsEffect(self.shadow)
				self.restart_lesson.setEnabled(True)
			elif self.Flag and self.glow and self.current_word in self.to_learn:
				self.glow = False
				self.restart_lesson.setGraphicsEffect(None)
				self.restart_lesson.setEnabled(True)
			else:
				self.restart_lesson.setEnabled(True)
			self.wd = WordShortcut(self.current_word)
			self.show_points()
			self.The_word.setText(self.wd.name())
			self.word_transcription.setText(self.wd.transcript())
			self.word_translation.setText(self.wd.transl())
			self.W_answer.setEnabled(True)
			self.L_answer.setEnabled(True)

		QApplication.processEvents()
		self.file_path = os.path.join(audio_base_path, f"{self.wd.sub_group().replace('/', '-').replace(':', '-')}",
									  f"{self.wd.name().split(' (')[0]}.ogg")
		self.voice_word()

	def progress_value(self, querry, group):
		max_value = len(tb.search(where(group) == querry))
		value = len(tb.search((where(group) == querry) & (where('weight') == 0)))
		return value, max_value

	def populate_main_group(self):
		self.pages.setCurrentIndex(4)
		self.clear_grid_column(self.groupGrid_2)
		self.prev_page_strip.setVisible(False)
		self.groups = list(dict.fromkeys([group.get('Group') for group in tb.all()]))
		for num, group in enumerate(self.groups):

			self.Group_button = QPushButton(f'{group}', self)
			self.Group_button.clicked.connect(self.populate_group)
			self.Group_button.setFont(QFont('Arial', 24))
			self.Group_button.setFixedSize(1150, 70)
			self.Group_button.setStyleSheet(self.stylesheet_prpl)
			self.groupGrid_2.addWidget(self.Group_button, num, 0, alignment=Qt.AlignJustify)

			self.progress = CircularProgress()
			self.progress.setFixedSize(120, 60)
			self.progress.set_values(*self.progress_value(group, "Group"))
			self.groupGrid_2.addWidget(self.progress, num, 0)
			self.progress.raise_()

	def populate_group(self):
		self.clear_grid_column(self.groupGrid)
		self.prev_page_strip.setVisible(True)
		self.pages.setCurrentIndex(3)
		sendby = self.sender().text()
		if sendby!='Save and switch Lesson' and sendby!='':
			self.supergroup_name = self.sender().text()
		self.groups = list(
			dict.fromkeys([group.get('Sub group') for group in tb.search(where("Group") == self.supergroup_name)]))
		for num, group in enumerate(self.groups):
			self.Group_button = QPushButton(f'{group}', self)
			self.Group_button.clicked.connect(self.switch_to_WordLearn)
			self.Group_button.setFont(QFont('Arial', 28))
			self.Group_button.setFixedSize(1150, 70)
			self.Group_button.setStyleSheet(self.stylesheet_prpl)

			self.groupGrid.addWidget(self.Group_button, num, 0, alignment=Qt.AlignJustify)

			self.progress = CircularProgress()
			self.progress.setFixedSize(120, 60)
			self.progress.set_values(*self.progress_value(group, "Sub group"))
			self.groupGrid.addWidget(self.progress, num, 0)
			self.progress.raise_()

	def clear_grid_column(self, obj):
		for i in reversed(range(obj.count())):  # Iterate in reverse to avoid index shifting
			item = obj.itemAt(i)
			if item is not None:
				widget = item.widget()
				_, column, _, _ = obj.getItemPosition(i)  # Get the column position
				if column == 0:
					obj.removeWidget(widget)  # Remove from layout
					widget.deleteLater()  # Delete widget

	def clear_mistakes(self):
		for i in reversed(range(self.scrollGrid.count())):  # Iterate in reverse to avoid index shifting
			item = self.scrollGrid.itemAt(i)
			if item is not None:
				widget = item.widget()
				if widget is not None and item != self.scrollSpacer:
					self.scrollGrid.removeWidget(widget)  # Remove from layout
					widget.deleteLater()  # Delete widget
				else:
					self.scrollGrid.removeItem(item)  # Remove non-widget items like spacers

	def mark(self, num):
		new_value = round((self.wd.weight() - (self.wd.weight() * max_points % 1 / max_points) - num / max_points), 2)
		new_value = min(1, max(new_value, 0))
		tb.update({"weight": new_value},
				  (where('Sub group') == self.wd.sub_group()) & (where("Name") == self.wd.name()))

	def enable_buttons(self, on_off):
		self.W_answer.setVisible(on_off)
		self.L_answer.setVisible(on_off)
		self.points_display.setVisible(on_off)
		self.repeat_audio.setEnabled(on_off)
		self.checkBox.setVisible(on_off)
		self.Layout_type.setVisible(on_off)

	def	toggle_translation(self):
		if self.study_mode == 'mode1intro':
			self.translation.setVisible(True)
		else:
			self.translation.setVisible(not self.Layout_type.isChecked())

	def show_points(self):
		self.points_display.shadow_anim.stop()
		amount = max_points - self.wd.weight() * max_points
		self.points_display.setText(" 🐟" * int(amount))
		if amount == max_points:
			self.points_display.setText("MAX" + " 🐟" * int(amount))
			self.points_display.shadow_anim.start()


	def lesson_resume(self):
		if self.dock:
			self.dock.populate(self.mistakes)
			self.dock.show()
		else:
			self.clear_mistakes()

			for num, mistake in enumerate(self.mistakes):

				self.redLabel = QLabel(f"{mistake['Name']}", self.ResultsLabel)
				self.redLabel.setStyleSheet("font-size: 24px; color: #810031; font-weight: bold;")
				self.redLabel.setFixedSize(400, 50)
				self.redLabel.setAlignment(Qt.AlignmentFlag.AlignRight)
				self.scrollGrid.addWidget(self.redLabel, num, 0)
				self.redLabel = QLabel("-", self.ResultsLabel)
				self.redLabel.setStyleSheet("font-size: 24px; color: #810031; font-weight: bold;")
				self.redLabel.setFixedSize(50, 50)
				self.redLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
				self.scrollGrid.addWidget(self.redLabel, num, 1)
				self.redLabel = QLabel(f"{mistake['translation']}", self.ResultsLabel)
				self.redLabel.setStyleSheet("font-size: 24px; color: #810031; font-weight: bold;")
				self.redLabel.setFixedSize(450, 50)
				self.redLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
				self.scrollGrid.addWidget(self.redLabel, num, 2)
			self.scrollSpacer = QSpacerItem(0, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
			self.scrollGrid.addItem(self.scrollSpacer, 6, 1)
			self.AnswersLabel.setText(f"Correct Answers: {self.size - len(self.mistakes)}/{self.size}")
			self.SaveAndExit.setVisible(not self.Flag)
			self.Grade1.setVisible(not self.Flag)
			self.Grade2.setVisible(not self.Flag)
			self.Grade3.setVisible(not self.Flag)
			self.Grade4.setVisible(not self.Flag)
			self.Grade5.setVisible(not self.Flag)
			self.GradesLabel.setVisible(not self.Flag)

			if self.Flag:
				self.Repeat.setText("next Lesson")

			else:
				self.grades_list = self.grades_table.get(where('group grades') == self.group_name)
				self.grades_list = self.grades_list.get('list', [])
				self.grade = self.size - len(self.mistakes)
				self.Repeat.setText("repeat Exam")
				if len(self.mistakes) <= 1:
					self.SaveAndExit.setStyleSheet(self.stylesheet_prpl)
					self.SaveAndExit.setEnabled(True)

				else:
					self.SaveAndExit.setStyleSheet(self.stylesheet_gray)
					self.SaveAndExit.setEnabled(False)

				self.grades_list.insert(0, self.grade)
				if len(self.grades_list) > 5:
					self.grades_list.pop()

				for grade, label_object in zip(self.grades_list, self.grades_objects):
					label_object.setText(str(grade))
					label_object.setStyleSheet(self.get_grade_color(grade))

				self.grades_table.update({'list': self.grades_list}, where('group grades') == self.group_name)

			self.pages.setCurrentIndex(0)

	def switch_to_WordLearn(self, group):
		self.pages.setCurrentIndex(2)
		self.group_name = self.sender().text()
		self.grades_table.upsert({"group grades": self.group_name}, where('group grades') == self.group_name)
		pass

	def get_grade_color(self, grade):
		percent_grade = round(grade / self.size, 2) * 100
		if percent_grade == 100:
			style_sheet = "font-size: 48px; color: #e8c40e; font-weight: bold;"
		elif percent_grade >= 80:
			style_sheet = "font-size: 48px; color: #0a912e; font-weight: bold;"
		elif percent_grade >= 60:
			style_sheet = "font-size: 48px; color: #177fcf; font-weight: bold;"
		else:
			style_sheet = "font-size: 48px; color: #512f9c; font-weight: bold;"
		return style_sheet


if __name__ == '__main__':
	app = QApplication(sys.argv)
	debug = True

	max_points = 5

	base_path = os.path.dirname(__file__)
	audio_base_path = os.path.join(base_path, 'assets', 'audiofiles')
	image_files_path = os.path.join(base_path, 'assets', 'images')
	if platform.system()=="Windows":
		db_path = os.path.join(base_path, "Vocabulary", "db.json")
		tb = TinyDB(db_path)
		
		appIcon = QtGui.QIcon()
		appIcon.addPixmap(QtGui.QPixmap(os.path.join(image_files_path, "io.github.hoisasa.SharksEmpire-English.ico")), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.On)
		app.setWindowIcon(appIcon)
		
		import ctypes
		
		myappid = 'io.github.hoisasa.SharksEmpire-English'  # arbitrary string
		ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
	else:
		try:
			db_path = os.path.join(base_path, "Vocabulary", "db.json")
			tb = TinyDB(db_path)
		except Exception as e:
			data_dir = os.environ.get("XDG_DATA_HOME", os.path.expanduser("~/.local/share"))
			app_data_path = os.path.join(data_dir, "se-english")
			os.makedirs(app_data_path, exist_ok=True)
			db_path = os.path.join(app_data_path, "db.json")
			if not os.path.exists(db_path):
				try:
					with open("/app/lib/se-english/db.json", "rb") as src, open(db_path, "wb") as dst:
						dst.write(src.read())
				except Exception as e:
					print("Manual copy failed:", e)
			tb = TinyDB(db_path)




	Word = Query()

	window = EnglishApp()
	window.show()

	sys.exit(app.exec())