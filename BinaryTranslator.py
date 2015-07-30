import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit,QLabel, \
QPushButton, QVBoxLayout, QInputDialog
from binary import toBinFrStr

class BinaryTranslator(QWidget):

    def __init__(self):
        super().__init__()
        
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
    
        self.setGeometry(300,300,550,600)
        self.setWindowTitle('Binary Translator')
        self.show()

    def translateData(self):
        text = self.textEdit.toPlainText()
        self.binaryEdit.setText(toBinFrStr(str(text)))
        
    
if __name__ == '__main__':

    app = QApplication(sys.argv)
    bin = BinaryTranslator()
    sys.exit(app.exec_())