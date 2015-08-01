import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit,QLabel, \
QPushButton, QVBoxLayout, QShortcut
from PyQt5.QtGui import QKeySequence
from pyperclip import copy, paste
from binary import toBinFrStr

class BinaryTranslator(QWidget):

    def __init__(self):
        super().__init__()
        
        #self.clipboard = QApplication.clipboard()
        
        self.initUI()
        
    def initUI(self):
        self.textTitle = QLabel('Text to Translate')
        self.textEdit = QTextEdit()
        
        self.binaryTitle = QLabel('Translated text')
        self.binaryEdit = QTextEdit()
        
        self.translateButton = QPushButton('Translate', self)
        self.translateButton.clicked.connect(self.translateData)
        
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.textTitle)
        self.vbox.addWidget(self.textEdit)
        self.vbox.addWidget(self.binaryTitle)
        self.vbox.addWidget(self.binaryEdit)
        self.vbox.addWidget(self.translateButton)

        self.setLayout(self.vbox)
        
        self.binaryCopy = QShortcut(QKeySequence("Ctrl-C"), self.binaryEdit)
        self.binaryPaste = QShortcut(QKeySequence("Ctrl-V"), self.binaryEdit)
        self.textCopy = QShortcut(QKeySequence("Ctrl-C"), self.textEdit)
        self.textPaste = QShortcut(QKeySequence("Ctrl-V"), self.textEdit)
    
        self.setGeometry(300,300,550,600)
        self.setWindowTitle('Binary Translator')
        self.show()

    def translateData(self):
        self.text = self.textEdit.toPlainText()
        self.translatedText = toBinFrStr(str(self.text))
        self.binaryEdit.setText(self.translatedText)
        
    def keyPresEvent(self, k):
        
        if k.key() == self.binaryCopy:
            binaryEdit.copy(self)
            copy(self.translatedText)
           
        elif k.key() == self.binaryPaste:
            binaryEdit.paste(self)
            

        elif k.key() == self.textCopy:
            textEdit.copy(self)
            copy(self.translatedText) 

        elif k.key() == self.textPaste:
            textEdit.paste(self)
                      
            
if __name__ == '__main__':

    app = QApplication(sys.argv)
    bin = BinaryTranslator()
    sys.exit(app.exec_())