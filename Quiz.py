from PyQt5.QtWidgets import *

def QChanger():
    global q_on
    global point
    
    if q_on == 0 and Q3.isChecked():
        point += 1
    if q_on == 1 and Q2.isChecked():
        point += 1
    if q_on == 2 and Q2.isChecked():
        point += 1
    q_on += 1
        
    if q_on != 3:
        label.setText(Questions[q_on])
        Q1.setText(Q[q_on][0])
        Q2.setText(Q[q_on][1])
        Q3.setText(Q[q_on][2])
        Q4.setText(Q[q_on][3])
    if q_on == 3:
        Q1.hide()
        Q2.hide()
        Q3.hide()
        Q4.hide()
        Next.hide()

        label.setText('Score:'+str(point)+'/3')
    

point = 0

Questions = ['How many people are there in this class?',
            'What is 2 x 2 = ?',
            'Which letter sounds like Bee?']

Q = [['2','3','4','5'],
     ['2','4','0','7'],
     ['a','b','c','d']]

q_on = 0
app = QApplication([])
win = QWidget()

label = QLabel(Questions[q_on])
Q1 = QRadioButton(Q[q_on][0])
Q2 = QRadioButton(Q[q_on][1])
Q3 = QRadioButton(Q[q_on][2])
Q4 = QRadioButton(Q[q_on][3])

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

win.setLayout(LM)

win.show()
app.exec()
