from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt, QSize, pyqtSignal
import sys

from boardInput import BoardInput
from boardSquare import BoardSquare


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.board_multiplier = [['0', '0', '0', '0', '0', '0'],
                                 ['0', '0', '0', '0', '0', '0'],
                                 ['0', '0', '0', '0', '0', '0'],
                                 ['0', '0', '0', '0', '0', '0'],
                                 ['0', '0', '0', '0', '0', '0'],
                                 ['0', '0', '0', '0', '0', '0']]

        self.title = "Connect Four"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 800
        self.boardPosX = 50
        self.boardPosY = 200
        w = QWidget()
        self.grid = QGridLayout()
        self.grid.setSpacing(0)
        self.grid.maximumSize()
        w.setLayout(self.grid)
        w.setFixedWidth(560)
        w.setFixedHeight(570)
        self.setCentralWidget(w)
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.drawBoard()
        self.show()

    def drawBoard(self):
        for i in range(0, 7):
            # w = BoardInput(i, 0)
            # self.grid.addWidget(w, 0, i)
            button = QPushButton("Button %d" % i)
            button.setStyleSheet("width: 80; height: 80")
            button.clicked.connect(self.buttonClick)
            self.grid.addWidget(button, 0, i)

        for posX in range(1, 7):  # pionowo
            for posY in range(0, 7):  # poziomo
                w = BoardSquare(posX, posY)
                self.grid.addWidget(w, posX, posY)
        print(self.board_multiplier)

    def create_board_multiplier(self):
        return self.board_multiplier

        # xd = self.grid.itemAtPosition(1, 1).widget()
        # xd.color = Qt.red

    def buttonClick(self):
        print("działa")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())
