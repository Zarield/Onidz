import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic


class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled1.ui', self)
        self.setWindowTitle('Желтые кружки')
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circ(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circ(self, qp):
        d = random.randint(1, 200)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(400, 200, d, d)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    exit(app.exec())
