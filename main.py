import sys
from random import randint

from Ui import Ui_MainWindow
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Circle(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.resize(300, 400)
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor(randint(0, 256), randint(0, 256), randint(0, 256)))
        d = randint(1, 100)
        qp.drawEllipse(QPoint(150, 300), d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Circle()
    wnd.show()
    sys.exit(app.exec())

