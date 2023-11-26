from PyQt5.QtWidgets import *

def QChanger():
    Q1.setText(Q[0][0])
    Q2.setText(Q[0][1])
    Q3.setText(Q[0][2])
    Q4.setText(Q[0][3])

Q = [['2','3','4','5'],
     ['2','4','0','7'],
     ['a','b','c','d']]

app = QApplication([])
win = QWidget()

label = QLabel('How many people are there in this class?')
Q1 = QRadioButton('')
Q2 = QRadioButton('')
Q3 = QRadioButton('')
Q4 = QRadioButton('')

Next = QPushButton('Next')
Next.clicked.connect(QChanger)

L1 = QHBoxLayout()
L2 = QHBoxLayout()
LM = QVBoxLayout()

L1.addWidget(Q1)
L1.addWidget(Q2)

L2.addWidget(Q3)
L2.addWidget(Q4)

LM.addWidget(label)
LM.addLayout(L1)
LM.addLayout(L2)
LM.addWidget(Next)

win.setLayout(LM)

win.show()
app.exec()