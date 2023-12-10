from PyQt5.QtWidgets import *
import random
def QChanger():
    global Q_List
    global q_on
    global point
    L1.removeWidget(Q_List[0])
    L1.removeWidget(Q_List[1])
    L2.removeWidget(Q_List[2])
    L2.removeWidget(Q_List[3])
    random.shuffle(Q_List)
    L1.addWidget(Q_List[0])
    L1.addWidget(Q_List[1])
    L2.addWidget(Q_List[2])
    L2.addWidget(Q_List[3])


    if Q1.isChecked():
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

Q = [['4','3','2','5'],
     ['4','2','0','7'],
     ['b','a','c','d']]

q_on = 0
app = QApplication([])
win = QWidget()

label = QLabel(Questions[q_on])
Q1 = QRadioButton(Q[q_on][0])
Q2 = QRadioButton(Q[q_on][1])
Q3 = QRadioButton(Q[q_on][2])
Q4 = QRadioButton(Q[q_on][3])

Q_List = [Q1, Q2, Q3, Q4]

Next = QPushButton('Next')
Next.clicked.connect(QChanger)

L1 = QHBoxLayout()
L2 = QHBoxLayout()
LM = QVBoxLayout()

L1.addWidget(Q_List[0])
L1.addWidget(Q_List[1])

L2.addWidget(Q_List[2])
L2.addWidget(Q_List[3])

LM.addWidget(label)
LM.addLayout(L1)
LM.addLayout(L2)
LM.addWidget(Next)

win.setLayout(LM)

win.show()
app.exec()
