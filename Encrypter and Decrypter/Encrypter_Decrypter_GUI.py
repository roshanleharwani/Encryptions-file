from cryptography.fernet import Fernet
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pyperclip
import os
import time

class MyApp(QMainWindow):

    def __init__(self):
        super(MyApp, self).__init__()
        uic.loadUi('design.ui', self)
        self.show()
        self.pushButton.clicked.connect(self.encrypt_decrypt)
        self.radioButton_2.clicked.connect(self.on_click_1)
        self.radioButton.clicked.connect(self.on_click_2)
        self.Genrate.triggered.connect(self.on_click_3)
        self.actionOpen_File.triggered.connect(self.on_click_5)
        self.actionSave_Encrypted_Decrypted_Text.triggered.connect(self.on_click_4)
        self.pushButton_2.clicked.connect(self.on_click_6)
        self.plainTextEdit_3.insertPlainText(" ")
        self.plainTextEdit.insertPlainText(" ")
        self.plainTextEdit_3.clear()
        self.plainTextEdit.clear()
        if self.label_5.text() == '':
            self.pushButton_2.setEnabled(False)
        else:
            self.pushButton_2.setEnabled(True)
        self.Counter = 0
        self.setWindowTitle(" ")
        self.setMaximumWidth(521)
        self.setMaximumHeight(679)
        self.text = ''

    def wrong(self):
        msg = QMessageBox()
        msg.setText('Something Went Wrong !!')
        msg.setWindowTitle('Error')

    def valid(self):
        msg = QMessageBox()
        msg.setWindowTitle("Invalid Input")
        msg.setText("Please Enter Valid Input!!")
        msg.exec()

    def encrypt_decrypt(self):
        if self.radioButton.isChecked() == True:
            key = self.plainTextEdit_3.toPlainText().encode()
            if self.text == '':
                text = self.plainTextEdit.toPlainText().encode()
            else:
                text = self.text.encode()
            try:
                encrypted_text = (Fernet(key).encrypt(text)).decode()
                self.label_5.setEnabled(True)
                for i in range(101):
                    if len(text) > 150 and len(text) < 500:
                        time.sleep(0.001)
                    elif len(text) < 150:
                        pass
                    elif len(text) > 500 and len(text) < 1000:
                        time.sleep(0.005)
                    elif len(text) > 1000:
                        time.sleep(0.01)
                    self.progressBar.setValue(i)
                self.pushButton_2.setEnabled(True)
                self.actionSave_Encrypted_Decrypted_Text.setEnabled(True)
                self.label_5.setText(encrypted_text)
                msg = QMessageBox()
                msg.setText('Do you want to Save this Encrypted Text ?')
                msg.setWindowTitle('Save File')
                msg.addButton(QPushButton('Yes'), QMessageBox.YesRole)
                msg.addButton(QPushButton('No'), QMessageBox.NoRole)
                if msg.exec_() == 0:
                    try:
                        file, _ = QFileDialog.getSaveFileName(self, 'Save File')
                        file = open(file, 'w')
                        file.write(encrypted_text)
                        file.close()
                    except:
                        self.wrong()
            except:
                self.valid()
        elif self.radioButton_2.isChecked() == True:
            key = self.plainTextEdit_3.toPlainText().encode()
            if self.text == '':
                text = self.plainTextEdit.toPlainText().encode()
            else:
                text = self.text.encode()
            try:
                decrypted_text = (Fernet(key).decrypt(text)).decode()
                self.label_5.setEnabled(True)
                for i in range(101):
                    if len(text) > 150 and len(text) < 500:
                        time.sleep(0.001)
                    elif len(text) < 150:
                        pass
                    elif len(text) > 500 and len(text) < 1000:
                        time.sleep(0.005)
                    elif len(text) > 1000:
                        time.sleep(0.01)
                    self.progressBar.setValue(i)
                self.pushButton_2.setEnabled(True)
                self.actionSave_Encrypted_Decrypted_Text.setEnabled(True)
                self.label_5.setText(decrypted_text)
                msg = QMessageBox()
                msg.setText('Do you want to Save this Encrypted Text ?')
                msg.setWindowTitle('Save File')
                msg.addButton(QPushButton('Yes'), QMessageBox.YesRole)
                msg.addButton(QPushButton('No'), QMessageBox.NoRole)
                if msg.exec_() == 0:
                    try:
                        file, _ = QFileDialog.getSaveFileName(self, 'Save File')
                        file = open(file, 'w')
                        file.write(decrypted_text)
                        file.close()
                    except:
                        self.wrong()
            except:
                self.valid()

    def on_click_4(self):
        file, _ = QFileDialog.getSaveFileName(self, 'Save File')
        text = self.label_5.text()
        if text != '':
            try:
                file = open(file, 'w')
                file.write(text)
            except:
                pass
        elif text == '':
            msg = QMessageBox()
            msg.setWindowTitle('Error')
            msg.setText('Nothing to Save !!')
            msg.exec()

    def on_click_1(self):
        self.pushButton.setText("Decrypt")
        self.label_3.setText("Decrypted")
        self.text = ''
        self.label_6.setEnabled(False)
        self.label_7.setText('')
        self.actionSave_Encrypted_Decrypted_Text.setEnabled(True) 
        self.progressBar.setValue(0)
        self.Counter += 1

    def on_click_2(self):
        self.pushButton.setText("Encrypt")
        self.label_3.setText("Encrypted")
        if self.Counter > 0:
            self.text = ''
            self.label_6.setEnabled(False)
            self.progressBar.setValue(0)
            self.label_7.setText('')
        else:
            self.Counter += 1

    def on_click_3(self):
        key = Fernet.generate_key().decode()
        msg = QMessageBox()
        msg.setText(f'Key >> {key}')
        msg.setWindowTitle('[*] Key Copied Suceessfully !!')
        msg.setStandardButtons(QMessageBox.Ok)
        pyperclip.copy(key)
        self.plainTextEdit_3.clear()
        self.plainTextEdit_3.insertPlainText(key)
        msg.exec()
        
    def on_click_5(self):
        try:
            options = QFileDialog.Options()
            file, _ = QFileDialog.getOpenFileName(self, 'Open Files', '', 'All Files (*.txt)', options=options)
            text = open(file, 'r')
            text = text.read()
            self.text = text
            self.label_6.setEnabled(True)
            self.label_7.setText(os.path.basename(file))
            self.plainTextEdit.clear()
            self.plainTextEdit.insertPlainText(text)
            msg = QMessageBox()
            msg.setWindowTitle('Info')
            msg.setText('File Loaded Successfully !!')
            msg.exec()
        except:
            self.wrong()

    def on_click_6(self):
        pyperclip.copy(self.label_5.text())
        msg = QMessageBox()
        msg.setWindowTitle('Info')
        msg.setText('Text Copied !!')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()


app = QApplication([])

window = MyApp()
app.exec_()
