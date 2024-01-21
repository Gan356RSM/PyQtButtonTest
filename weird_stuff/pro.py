from PyQt5.QtWidgets import *

dic = {}

app = QApplication([])
win = QWidget()

def Add():
    word, ok = QInputDialog.getText(win, "Add Word", "Enter word:")
    if ok:
        lw.addItem(word)

def Selective_Items():
    items = lw.selectedItems()
    if len(items) == 0:
        return

    item = items[0].text()
    dic[item] = text_e.setPlainText("cat")


lw = QListWidget()
text_e = QTextEdit()

lw.itemClicked.connect(Selective_Items)
butt1 = QPushButton("Add")
butt2 = QPushButton("Delete")
butt3 = QPushButton("Save")

butt1.clicked.connect(Add)

laysV1 = QVBoxLayout()
laysV2 = QVBoxLayout()
laysH = QHBoxLayout()

laysH.addLayout(laysV1)
laysH.addLayout(laysV2)
laysV1.addWidget(lw)
laysV2.addWidget(text_e)
laysV2.addWidget(butt1)
laysV2.addWidget(butt2)
laysV2.addWidget(butt3)

win.setLayout(laysH)
win.show()
app.exec()