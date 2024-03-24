from PyQt5.QtWidgets import *

class MyWin(QWidget):
    def __init__(self):
        super().__init__()
        self.number = 0
        self.label = QLabel("0")
        self.butu = QPushButton("Up")
        self.butd = QPushButton("Down")

        self.butu.clicked.connect(self.up)
        self.butd.clicked.connect(self.down)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.butu)
        self.layout.addWidget(self.butd)
    
        self.setLayout(self.layout)
        self.show()

    def up(self):
        self.number += 1
        self.label.setText(str(self.number))

    def down(self):
        self.number -= 1
        self.label.setText(str(self.number))


app = QApplication([])
win = MyWin()
app.exec()