from PyQt5.QtWidgets import *
from random import randint

def Add():
    n = int(label1.text()) + 1
    label1.setText(str(n))

def Randomanzo():
    rn = randint(0, 100)
    label2.setText(str(rn))

def Togger():
    boo = label3.text()
    if boo == 'True':
        boo = 'False'
    elif boo == 'False':
        boo = 'True'

    label3.setText(str(boo))

app = QApplication([])
win = QWidget()

label1 = QLabel('0')
button1 = QPushButton('Add +1')
button1.clicked.connect(Add)

label2 = QLabel('0')
button2 = QPushButton('Randomizer')
button2.clicked.connect(Randomanzo)

label3 = QLabel('True')
button3 = QPushButton('Boolean Toggle')
button3.clicked.connect(Togger)

lay = QVBoxLayout()

lay.addWidget(label1)
lay.addWidget(button1)
lay.addWidget(label2)
lay.addWidget(button2)
lay.addWidget(label3)
lay.addWidget(button3)

win.setLayout(lay)
win.show()
app.exec()