from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image

class MainW(QWidget):
    def __init__(self):
        super().__init__()
        self.pbutt = QPushButton()
        self.listw = QListWidget()

        self.butt1 = QPushButton("Nostalgia")
        self.butt2 = QPushButton("Rotate 90")
        self.butt3 = QPushButton("Flip Flop")
        self.butt4 = QPushButton("Flop Flip")
        self.butt5 = QPushButton("Rotate 180")

        self.butt1.clicked.connect(self.bw)
        self.butt2.clicked.connect(self.rot)
        self.butt3.clicked.connect(self.flip_flop)
        self.butt4.clicked.connect(self.flop_flip)
        self.butt5.clicked.connect(self.rot180)

        self.lab = QLabel("Hi")
        self.pixmap = QPixmap("Beef-Tacos.jpg")
        self.pixmap = self.pixmap.scaled(self.lab.width(), self.lab.height(), Qt.KeepAspectRatio)
        self.lab.setPixmap(self.pixmap)

        self.laysH = QHBoxLayout()
        self.laysV1 = QVBoxLayout()
        self.laysV2 = QVBoxLayout()
        self.laysM = QHBoxLayout()

        self.laysV2.addWidget(self.pbutt)
        self.laysV2.addWidget(self.listw)

        self.laysV1.addWidget(self.lab)

        self.laysV1.addLayout(self.laysH)

        self.laysH.addWidget(self.butt1)
        self.laysH.addWidget(self.butt2)
        self.laysH.addWidget(self.butt3)
        self.laysH.addWidget(self.butt4)
        self.laysH.addWidget(self.butt5)

        self.laysM.addLayout(self.laysV2)
        self.laysM.addLayout(self.laysV1)

        self.setLayout(self.laysM)
        self.show()

    def bw(self):
        with Image.open("Beef-Tacos.jpg") as self.im:
            im = self.im.convert("L")
            im.save("bw.png")
    
        self.pixmap = QPixmap("bw.png")
        self.pixmap = self.pixmap.scaled(self.lab.width(), self.lab.height(), Qt.KeepAspectRatio)
        self.lab.setPixmap(self.pixmap)

    def rot(self):
        with Image.open("Beef-Tacos.jpg") as im:
            im = im.transpose(Image.ROTATE_90)
            im.save("rot.png")
    
        self.pixmap = QPixmap("rot.png")
        self.pixmap = self.pixmap.scaled(self.lab.width(), self.lab.height(), Qt.KeepAspectRatio)
        self.lab.setPixmap(self.pixmap)

    def flip_flop(self):
        with Image.open("Beef-Tacos.jpg") as im:
            im = im.transpose(Image.FLIP_LEFT_RIGHT)
            im.save("flip-flop.png")
    
        self.pixmap = QPixmap("flip-flop.png")
        self.pixmap = self.pixmap.scaled(self.lab.width(), self.lab.height(), Qt.KeepAspectRatio)
        self.lab.setPixmap(self.pixmap)

    def flop_flip(self):
        with Image.open("Beef-Tacos.jpg") as im:
            im = self.im.transpose(Image.FLIP_TOP_BOTTOM)
            im.save("flop-flip.png")
    
        self.pixmap = QPixmap("flip-flop.png")
        self.pixmap = self.pixmap.scaled(self.lab.width(), self.lab.height(), Qt.KeepAspectRatio)
        self.lab.setPixmap(self.pixmap)

    def rot180(self):
        with Image.open("Beef-Tacos.jpg") as im:
            im = im.transpose(Image.ROTATE_180)
            im.save("rot180.png")
    
        self.pixmap = QPixmap("rot180.png")
        self.pixmap = self.pixmap.scaled(self.lab.width(), self.lab.height(), Qt.KeepAspectRatio)
        self.lab.setPixmap(self.pixmap)

app = QApplication([])
win = MainW()
app.exec()