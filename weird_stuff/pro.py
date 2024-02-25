from PyQt5.QtWidgets import *
import requests
import json

dic = {}
select_word = ""

app = QApplication([])
win = QWidget()

def Add():
    word, ok = QInputDialog.getText(win, "Add Word", "Enter word:")
    response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)
    d = json.loads(response.text)
    dic[word] = d[0]['meanings'][0]['definitions'][0]['definition']
    if ok:
        lw.addItem(word)


def Delete():
    text_e.clear()

def Selective_Items():
    global dic
    global select_word
    
    watever = text_e.toPlainText()

    if select_word != "":
        dic[select_word] = watever

    items = lw.selectedItems()
    if len(items) == 0:
        return

    item = items[0].text()
    text_e.setPlainText(dic[item])
    select_word = item

def showDialog():
    msgBox = QMessageBox()
    msgBox.setText("Message box pop up window")
    msgBox.setWindowTitle("Introduction")
    msgBox.exec()



lw = QListWidget()
text_e = QTextEdit()

lw.itemClicked.connect(Selective_Items)
butt1 = QPushButton("Add")
butt2 = QPushButton("Delete")
butt3 = QPushButton("Introduction")

butt1.clicked.connect(Add)
butt2.clicked.connect(Delete)
butt3.clicked.connect(showDialog)

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
