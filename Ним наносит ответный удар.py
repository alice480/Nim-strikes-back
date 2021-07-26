import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('nim.ui', self)
        self.x = random.randint(1, 500)
        self.y = random.randint(1, 100)
        self.z = random.randint(1, 100)
        self.count = 10
        self.lcdNumber.display(self.count)
        self.lcdNumber_2.display(self.x)
        self.pushButton.setText('+' + str(self.y))
        self.pushButton_2.setText('-' + str(self.z))
        self.pushButton.clicked.connect(self.addition)
        self.pushButton_2.clicked.connect(self.subtraction)

    def addition(self):
        self.label_3.clear()
        self.x += self.y
        self.count -= 1
        self.lcdNumber_2.display(self.x)
        self.lcdNumber.display(self.count)
        if self.x == 0 or self.count == 0:
            self.new_game()

    def subtraction(self):
        self.label_3.clear()
        self.x -= self.z
        self.count -= 1
        self.lcdNumber_2.display(self.x)
        self.lcdNumber.display(self.count)
        if self.x == 0 or self.count == 0:
            self.new_game()

    def new_game(self):
        if self.count >= 0 and self.x == 0:
            self.label_3.setText('Вы победили, начинаем новую игру')
        else:
            self.label_3.setText('Вы проиграли, начинаем новую игру')
        self.count = 10
        self.lcdNumber.display(self.count)
        self.x = random.randint(1, 500)
        self.y = random.randint(1, 100)
        self.z = random.randint(1, 100)
        self.lcdNumber_2.display(self.x)
        self.pushButton.setText('+' + str(self.y))
        self.pushButton_2.setText('-' + str(self.z))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    ex.setWindowTitle("Ним наносит ответный удар")
    sys.exit(app.exec())