from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])

my_win = QWidget()
my_win.setWindowTitle('Identificador de ganador')
my_win.move(100, 100)
my_win.resize(400, 200)

button = QPushButton('Generar')
text = QLabel('Haz clic para conocer al ganador')
winner = QLabel('?')

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(winner, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
my_win.setLayout(line)

def show_winner():
    number = randint(0, 50)
    winner.setText(str(number))
    text.setText('Ganador:')

button.clicked.connect(show_winner)
my_win.show()
app.exec_()