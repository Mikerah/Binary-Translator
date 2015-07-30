import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit,QLabel, \
QPushButton, QVBoxLayout, QShortcut
from PyQt5.QtGui import QKeySequence
from binary import toStrFrBin

class BinaryDecoder(QWidget):

    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.textTitle = QLabel('Text to Decode')
        self.textEdit = QTextEdit()
        
        self.binaryTitle = QLabel('Decoded text')
        self.binaryEdit = QTextEdit()
        
        self.translateButton = QPushButton('Translate', self)
        self.translateButton.clicked.connect(self.translateData)
        
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.textTitle)
        self.vbox.addWidget(self.textEdit)
        self.vbox.addWidget(self.binaryTitle)
        self.vbox.addWidget(self.binaryEdit)
        self.vbox.addWidget(self.translateButton)

        self.binaryCopy = QShortcut(QKeySequence("Ctrl-C"), self.binaryEdit)
        self.binaryPaste = QShortcut(QKeySequence("Ctrl-V"), self.binaryEdit)
        self.textCopy = QShortcut(QKeySequence("Ctrl-C"), self.textEdit)
        self.textPaste = QShortcut(QKeySequence("Ctrl-V"), self.textEdit)         

        self.setLayout(self.vbox)
    
        self.setGeometry(300,300,550,600)
        self.setWindowTitle('Binary Decoder')
        self.show()

    def translateData(self):
        text = self.textEdit.toPlainText()
        self.binaryEdit.setText(toStrFrBin(str(text)))
        
    def keyPressEvent(self, k):
    
        if k.key() == self.binaryCopy:
            binaryEdit.copy(self)

        elif k.key() == self.binaryPaste:
            binaryEdit.paste(self) 

        elif k.key() == self.textCopy:
            textEdit.copy(self)

        elif k.key() == self.textPaste:
            textEdit.paste(self)

if __name__ == '__main__':            
    app = QApplication(sys.argv)
    bin = BinaryDecoder()
    sys.exit(app.exec_())