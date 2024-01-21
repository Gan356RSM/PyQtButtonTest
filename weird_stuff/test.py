from PyQt5.QtWidgets import *

def clear_text():
    text_edit.clear()

def set_text():
    text_edit.setPlainText("default text")

def get_text():
    text = text_edit.toPlainText()
    print(text)

app = QApplication([])
win = QWidget()

text_edit = QTextEdit()

clear_button = QPushButton("Clear")
set_button = QPushButton("Set to Default Text")
get_button = QPushButton("Print Current Text")

layout = QVBoxLayout()
layout.addWidget(text_edit)
layout.addWidget(clear_button)
layout.addWidget(set_button)
layout.addWidget(get_button)

win.setLayout(layout)
win.show()
app.exec()