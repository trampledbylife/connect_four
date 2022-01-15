from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt, QSize, pyqtSignal
import sys


class BoardSquare(QWidget):
    position = pyqtSignal(int, int)
    direction = pyqtSignal(int, int)

    def __init__(self, x, y, *args, **kwargs):
        super(BoardSquare, self).__init__(*args, **kwargs)

        # self.setFixedSize(QSize(80, 80))
        self.x = 0
        self.y = 0
        self.color = Qt.blue
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.blue, 1, Qt.SolidLine))

        painter.setPen(QPen(Qt.blue, 1, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.blue, Qt.SolidPattern))
        painter.drawRect(self.x, self.y, 80, 80)
        painter.setPen(QPen(Qt.white, 1, Qt.SolidLine))
        painter.setBrush(QBrush(self.color, Qt.SolidPattern))
        painter.drawEllipse(self.x + 5, self.y + 5, 70, 70)
        self.update()
