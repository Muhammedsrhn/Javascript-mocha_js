import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow


class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm,self).__init__()

        self.setWindowTitle('Calculater')
        self.setGeometry(200, 200, 500, 500)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText('Sayı 1 :')

        self.lbl_sayi1.move(50,30)
        
        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,32)
        

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText('Sayı 2 :')
        self.lbl_sayi2.move(50,80)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText('Toplama')
        self.btn_topla.move(200, 120)
        self.btn_topla.clicked.connect(self.topla)


        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText('Çıkarma')
        self.btn_cikar.move(200, 160)
        self.btn_cikar.clicked.connect(self.topla)

        
        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.setText('Bölme')
        self.btn_bol.move(200, 200)
        self.btn_bol.clicked.connect(self.topla)

        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText('Çarpma')
        self.btn_carp.move(200, 240)
        self.btn_carp.clicked.connect(self.topla)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.move(240, 280)
        self.lbl_result.resize(215, 32)
    
    def topla(self):
        sender = self.sender().text()
        if sender == "Toplama":
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        elif sender == "Çıkarma":
            result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        elif sender == "Bölme":
            result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
        elif sender == "Çarpma":
            result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        
        self.lbl_result.setText(str(result))

def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()
