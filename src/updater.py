import os
import sys

from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QApplication

from assets.GUI.python_gui_updater import Ui_Splash


class SplashScreen(Ui_Splash, QDialog):
	def __init__(self):
		super().__init__()
		self.asset = None
		self.release = None
		self.repo = None
		self.g = None
		self.token = None
		self.setupUi(self)
		self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
		self.getUpdate.setVisible(False)
		screen = QApplication.primaryScreen().geometry()
		self.move(screen.center().x() - self.width() // 2,
						  screen.center().y() - self.height() // 2)


if __name__ == '__main__':
	# init(autoreset=True)
	app = QApplication(sys.argv)
	debug = True
	
	max_points = 5
	
	base_path = os.path.dirname(__file__)
	audio_base_path = os.path.join(base_path, 'assets', 'audiofiles')
	image_files_path = os.path.join(base_path, 'assets', 'images')
	# tb = TinyDB(os.path.join(base_path, "Vocabulary", "db_test.json"))
	# Word = Query()
	
	appIcon = QtGui.QIcon()
	appIcon.addPixmap(QtGui.QPixmap(os.path.join(image_files_path, "UNOlingo.png")), QtGui.QIcon.Mode.Normal,
					  QtGui.QIcon.State.On)
	app.setWindowIcon(appIcon)
	
	update_check = SplashScreen()
	update_check.show()

	sys.exit(app.exec())