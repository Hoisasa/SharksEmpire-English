from PySide6.QtCore import Qt, QRect
from PySide6.QtGui import QPainter, QPen, QFont
from PySide6.QtWidgets import QWidget


class CircularProgress(QWidget):
    def __init__(self):
        super().__init__()

        self.value = 70
        self.width = 60
        self.height = 60
        self.progress_width = 7
        self.progress_rounded_cap = True
        self.progress_color = 0x0ddb45
        self.max_value = 100
        self.font_family = "Segoe UI"
        self.font_size = 14
        self.font = QFont(self.font_family, self.font_size)
        self.font.setWeight(QFont.Weight.Bold)
        self.suffix = "%"
        self.text_color = 0x00a32c
        self.enable_shadow = True

        self.resize(self.width, self.height)

    def paintEvent(self, event):
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = int(self.progress_width / 2)
        value = int(self.value * 360 / self.max_value)

        paint = QPainter(self)
        paint.setRenderHint(QPainter.RenderHint.Antialiasing)
        paint.setFont(self.font)

        rect = QRect(30, 3, self.width - self.progress_width, self.height - self.progress_width)

        pen = QPen()
        pen.setWidth(self.progress_width)
        pen.setColor(self.progress_color)

        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.PenCapStyle.RoundCap)

        paint.setPen(pen)
        paint.drawArc(margin + 30, margin, width, height, 90 * 16, -value * 16)

        paint.drawText(rect, Qt.AlignmentFlag.AlignCenter, f"{self.value}/{self.max_value}")
        paint.end()

    def set_values(self, value, max_value):
        self.value = value
        self.max_value = max_value

    def showEvent(self, event):
        self.update()
        super().showEvent(event)
