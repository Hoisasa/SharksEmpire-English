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

        rect = QRect(62, 2, self.width - self.progress_width, self.height - self.progress_width)

        pen = QPen()
        pen.setWidth(self.progress_width)
        pen.setColor(self.progress_color)

        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.PenCapStyle.RoundCap)

        paint.setPen(pen)
        paint.drawArc(margin + 60, margin, width, height, 90 * 16, -value * 16)

        paint.drawText(rect, Qt.AlignmentFlag.AlignCenter, f"{self.value}/{self.max_value}")
        paint.end()

    def set_values(self, value, max_value):
        self.value = value
        self.max_value = max_value

    def showEvent(self, event):
        self.update()
        super().showEvent(event)
