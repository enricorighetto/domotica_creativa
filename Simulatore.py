import time
import datetime
import sys
import string
import sys


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QDialog, QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1077, 781)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(430, 350, 31, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("spento.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.dial = QtWidgets.QDial(Form)
        self.dial.setGeometry(QtCore.QRect(800, 480, 111, 101))
        self.dial.setMaximum(6)
        self.dial.setSingleStep(2)
        self.dial.setPageStep(6)
        self.dial.setObjectName("dial")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(777, 413, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.toolButton_5 = QtWidgets.QToolButton(Form)
        self.toolButton_5.setGeometry(QtCore.QRect(240, 434, 71, 71))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("tasto.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon)
        self.toolButton_5.setIconSize(QtCore.QSize(80, 80))
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_2 = QtWidgets.QToolButton(Form)
        self.toolButton_2.setGeometry(QtCore.QRect(170, 350, 71, 71))
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(80, 80))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(Form)
        self.toolButton_3.setGeometry(QtCore.QRect(500, 250, 71, 71))
        self.toolButton_3.setIcon(icon)
        self.toolButton_3.setIconSize(QtCore.QSize(80, 80))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(170, 250, 71, 71))
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(80, 80))
        self.toolButton.setObjectName("toolButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 150, 931, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("caldaia.gif"))
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(290, 350, 101, 31))
        self.label_8.setObjectName("label_8")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 213, 121))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("pergio.jpg"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.toolButton_7 = QtWidgets.QToolButton(Form)
        self.toolButton_7.setGeometry(QtCore.QRect(433, 434, 71, 71))
        self.toolButton_7.setIcon(icon)
        self.toolButton_7.setIconSize(QtCore.QSize(80, 80))
        self.toolButton_7.setObjectName("toolButton_7")
        self.toolButton_6 = QtWidgets.QToolButton(Form)
        self.toolButton_6.setGeometry(QtCore.QRect(340, 434, 71, 71))
        self.toolButton_6.setIcon(icon)
        self.toolButton_6.setIconSize(QtCore.QSize(80, 80))
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_4 = QtWidgets.QToolButton(Form)
        self.toolButton_4.setGeometry(QtCore.QRect(500, 350, 71, 71))
        self.toolButton_4.setIcon(icon)
        self.toolButton_4.setIconSize(QtCore.QSize(80, 80))
        self.toolButton_4.setObjectName("toolButton_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(290, 290, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setTabletTracking(False)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setMaxLength(10)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(840, 406, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setTabletTracking(False)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setMaxLength(10)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(590, 60, 381, 91))
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 740, 61, 21))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(290, 256, 71, 27))
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(400, 256, 41, 27))
        self.label_9.setObjectName("label_9")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 290, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setTabletTracking(False)
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setMaxLength(10)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(130, 710, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono L")
        font.setPointSize(36)
        font.setItalic(False)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(240, 710, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono L")
        font.setPointSize(36)
        font.setItalic(False)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(350, 710, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono L")
        font.setPointSize(36)
        font.setItalic(False)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(470, 710, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono L")
        font.setPointSize(36)
        font.setItalic(False)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(690, 710, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono L")
        font.setPointSize(36)
        font.setItalic(False)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(570, 710, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Nimbus Mono L")
        font.setPointSize(36)
        font.setItalic(False)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 620, 91, 81))
        self.pushButton.setText("")
        self.pushButton.setIconSize(QtCore.QSize(100, 100))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 620, 91, 81))
        self.pushButton_2.setText("")
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 620, 91, 81))
        self.pushButton_3.setText("")
        self.pushButton_3.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 620, 91, 81))
        self.pushButton_4.setText("")
        self.pushButton_4.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 620, 91, 81))
        self.pushButton_5.setText("")
        self.pushButton_5.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(650, 620, 91, 81))
        self.pushButton_6.setText("")
        self.pushButton_6.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label.raise_()
        self.label_2.raise_()
        self.dial.raise_()
        self.label_4.raise_()
        self.toolButton_5.raise_()
        self.toolButton_2.raise_()
        self.toolButton_3.raise_()
        self.toolButton.raise_()
        self.label_8.raise_()
        self.label_6.raise_()
        self.toolButton_7.raise_()
        self.toolButton_6.raise_()
        self.toolButton_4.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.textEdit.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_9.raise_()
        self.lineEdit_3.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Bar"))
        self.toolButton_5.setText(_translate("Form", "..."))
        self.toolButton_2.setText(_translate("Form", "..."))
        self.toolButton_3.setText(_translate("Form", "..."))
        self.toolButton.setText(_translate("Form", "..."))
        self.label_8.setText(_translate("Form", "Info"))
        self.toolButton_7.setText(_translate("Form", "..."))
        self.toolButton_6.setText(_translate("Form", "..."))
        self.toolButton_4.setText(_translate("Form", "..."))
        self.lineEdit.setText(_translate("Form", "1"))
        self.lineEdit_2.setText(_translate("Form", "1"))
        self.label_3.setText(_translate("Form", "0"))
        self.label_5.setText(_translate("Form", "TextLabel"))
        self.label_9.setText(_translate("Form", "TextLabel"))
        self.lineEdit_3.setText(_translate("Form", "1"))
        self.label_10.setText(_translate("Form", "G"))
        self.label_11.setText(_translate("Form", "AC"))
        self.label_12.setText(_translate("Form", "AF"))
        self.label_13.setText(_translate("Form", "SC"))
        self.label_14.setText(_translate("Form", "M"))
        self.label_15.setText(_translate("Form", "R"))



#######################################################################
# 
#  
#
######################################################################
       
        
        self.Inizializza()
        
        self.toolButton.clicked.connect(self.onButtonClick)
        self.toolButton_2.clicked.connect(self.onButtonClick2)
        self.toolButton_3.clicked.connect(self.onButtonClick3) 
        self.toolButton_4.clicked.connect(self.onButtonClick4)
        self.toolButton_5.clicked.connect(self.onButtonClick5)
        self.toolButton_6.clicked.connect(self.onButtonClick6)
        self.toolButton_7.clicked.connect(self.onButtonClick7)
        self.pushButton.clicked.connect(self.onButtonClick8)
       

        
        self.dial.valueChanged.connect(self.cambiavaloredial)
       
  #############################################################################acs 
    def onButtonClick(self):
        print ("------------",self.ctr)
        if (self.ctr == 3):
           self.lineEdit_3.setVisible(False)
           temp_A = int(self.lineEdit.text())
           self.aum_ACS(temp_A)
        else:
           if (self.ctr == 4):
               self.lineEdit_3.setVisible(False)
               self.lineEdit.setVisible(True)
               temp_A = int(self.lineEdit.text())
               self.aum_ACS(temp_A) 
               
           
        print ("1")
        
    def onButtonClick2(self):
        print ("------------",self.ctr)
        if (self.ctr == 3):
           self.lineEdit_3.setVisible(False)
           temp_A = int(self.lineEdit.text())
           self.dim_ACS(temp_A)
        else:
           if (self.ctr == 4):
               self.lineEdit_3.setVisible(False)
               self.lineEdit.setVisible(True)
               temp_A = int(self.lineEdit.text())
               self.dim_ACS(temp_A) 
                
             
        print ("2")

   #############################################################################riscaldamento     
    def onButtonClick3(self):
        print ("------------",self.ctr)
        if (self.ctr == 4):
           self.lineEdit.setVisible(False)
           temp_R = int(self.lineEdit_3.text())
           self.aum_RIS(temp_R) 
        print ("3")
    def onButtonClick4(self):
        print ("------------",self.ctr)
        if (self.ctr == 4):
           self.lineEdit.setVisible(False)
           temp_R = int(self.lineEdit_3.text())
           self.dim_RIS(temp_R) 
        print ("4")
  ##################################################################################à 
        
    def onButtonClick5(self):
        print ("5")
        self.Inizializza()
    def onButtonClick6(self):
        print ("6")
    def cambiavaloredial(self):
        val = (self.dial.value())
        if (val == 1):
            self.lineEdit_2.setText("1")
        if (val == 2):
            self.lineEdit_2.setText("1.5")
        if (val == 3):
            self.lineEdit_2.setText("2")
        if (val == 4):
            self.lineEdit_2.setText("2.5")
        if (val == 5):
            self.lineEdit_2.setText("3")
        if (val == 6):
            self.lineEdit_2.setText("3.5")   
        if (val == 7):
            self.lineEdit_2.setText("4")
        if (val == 8):
            self.lineEdit_2.setText("4.5")
        if (val == 9):
            self.lineEdit_2.setText("5")   
        if (val == 0):
            self.lineEdit_2.setText("0")
        self.check_errori()
       
    
    def onButtonClick7(self):
        print ("7")
        self.check_errori()
      
        if (self.sw_err == 0):
     
           if (self.ctr == 1):
               self.lineEdit.setText("0")
               self.label_2.setPixmap(QtGui.QPixmap("spento.gif"))
               self.label_5.setPixmap(QtGui.QPixmap("fiamma_0.gif"))
               self.ctr = self.ctr +1
           else:   
               if (self.ctr == 2):
                  self.ctr = self.ctr +1
                  self.lineEdit.setText("47")
                  self.label_2.setPixmap(QtGui.QPixmap("estate.gif"))
                  self.label_5.setPixmap(QtGui.QPixmap("fiamma_3.gif"))
                  self.simula_ACS()
               else:
                  if (self.ctr == 3):
                     self.ctr = self.ctr +1
                     self.lineEdit_3.setText("65")
                     self.label_2.setPixmap(QtGui.QPixmap("inverno.gif"))
                     self.label_5.setPixmap(QtGui.QPixmap("fiamma_1.gif"))
                     self.simula_RIS()
                  else:
                     self.lineEdit.setText("0")
                     self.label_2.setPixmap(QtGui.QPixmap("spento.gif"))
                     self.label_5.setPixmap(QtGui.QPixmap("fiamma_0.gif"))
                     self.ctr = 2
                     self.simula_OFF()
                 
    def onButtonClick8(self):
        
        if (self.sw_on == 1):
           self.sw_on = 0
           self.valvola_gas = 1
           self.pushButton.setIcon(QtGui.QIcon('valvolaa.gif'))
        else:
           self.sw_on = 1
           self.valvola_gas = 0
           self.pushButton.setIcon(QtGui.QIcon('valvolac.gif'))

        self.check_errori()
        print ("8")
        

    def check_errori(self):
                 
        pressione = float(self.lineEdit_2.text())
        
        print (self.ctr)
        #if (self.lineEdit.text() == "E10"):
        #   self.sw_err=1
        #   return

        if (pressione == 0):
           self.lineEdit.setText("E10")
           self.label_5.setPixmap(QtGui.QPixmap("fiamma_0.gif"))
           self.sw_err=1
           return
        else:
           if (pressione > 2.5):
              self.lineEdit.setText("HP")
              self.label_5.setPixmap(QtGui.QPixmap("fiamma_0.gif"))
              self.sw_err=1
              return
           else:   
              #self.lineEdit.setText("")
              self.sw_err=0
              
              
     
        if (self.ctr > 1):
            if (self.valvola_gas == 0):
                self.lineEdit.setText("E01")
                self.label_5.setPixmap(QtGui.QPixmap("fiamma_0.gif"))
                self.sw_err=1
                return
        
        
        
        
##################################################################
# RISCALDAMENTO
##################################################################

    def simula_RIS(self):
        print(self.lineEdit_3.text())
        self.lineEdit_3.setVisible(True)
        self.lineEdit.setVisible(False)
        
    def aum_RIS(self,temp_R):
        temp_R = int(self.lineEdit_3.text())
        temp_R = temp_R + 1
        self.lineEdit_3.setText(str(temp_R))

    def dim_RIS(self,temp_R):
        temp_R = int(self.lineEdit_3.text())
        temp_R = temp_R - 1
        self.lineEdit_3.setText(str(temp_R))  
           
           
##################################################################
# ACS
##################################################################

    def simula_ACS(self):
        print(self.lineEdit.text())
        self.lineEdit_3.setVisible(False)
        self.lineEdit.setVisible(True)
           
    def aum_ACS(self,temp_A):
        
        temp_A = int(self.lineEdit.text())
        temp_A = temp_A + 1
        self.lineEdit.setText(str(temp_A))

    def dim_ACS(self,temp_A):
        
        temp_A = int(self.lineEdit.text())
        temp_A = temp_A - 1
        self.lineEdit.setText(str(temp_A))
##################################################################
# OFF
##################################################################

    def simula_OFF(self):
        self.lineEdit_3.setVisible(False) #riscaldamento
        self.lineEdit_3.setText("0")
        self.lineEdit.setVisible(True)    #acs
        self.lineEdit.setText("0")
        
        
##################################################################
# loppa e lancia thread bluethoot
##################################################################

    def attivo_scheda(self):
        try:
           print("attivoooooooooooo")
        except:
           mes = "Comando non riuscito"
           self.Box_M(mes)
        return 0

################################################################    

    def Leggiloop(self):

        sw_first_on = 1
        sw_first_off = 1

        sw_loop = 1
        
        while (sw_loop == 1):
            
            Timelog = datetime.datetime.now()
            WK_hh = int(Timelog.hour)
            WK_mm = int(Timelog.minute)
            WK_ss = int(Timelog.second)
                
            if (WK_hh == self.CK_hh and WK_mm == self.CK_mm):
                if (WK_ss < 15):
                       if (sw_first_on == 1):
                           sw_first_on = 0
                           sw_first_off = 1
                           self.attivo_scheda()
     
              
##################################################################
# MESSAGGI DI ERRORE 
##################################################################

    def Box_M(self,mes):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(msg.Ok)
        msg.setText(mes)
        msg.setInformativeText('Controlla dati inseriti')
        msg.setWindowTitle("Error")
        msg.exec_()
####################################################################

    def Inizializza(self):

        self.ctr = 2
        self.sw_on = 1
        self.switch_accensione = 0
                
        self.lineEdit_2.setText("1.5")
        self.dial.setValue(2)
        self.label_2.setPixmap(QtGui.QPixmap("spento.gif"))
        self.label_5.setPixmap(QtGui.QPixmap("fiamma_0.gif"))

        self.valvola_gas = 0
        self.pushButton.setIcon(QtGui.QIcon('valvolac.gif'))
        
        
        
        self.lineEdit_3.setVisible(False) #riscaldamento
        self.lineEdit_3.setText("0")
        self.lineEdit.setVisible(True)    #acs
        self.lineEdit.setText("0")
       
        self.sw_err = 0
              
        Timelog=datetime.datetime.now()
        WK_Anno = Timelog.year
        WK_Anno_Str= str(WK_Anno)
        WK_Mese = Timelog.month
        
        if (WK_Mese < 10):
            WK_Mese_Str = '0' + str(WK_Mese)
        else:
            WK_Mese_Str = str(WK_Mese)
                         
        WK_Giorno = Timelog.day + 1
        
        if (WK_Giorno < 10):
            WK_Giorno_Str = '0' + str(WK_Giorno)
        else:
            WK_Giorno_Str = str(WK_Giorno)

       
          
if __name__ == "__main__":
    import sys
    import subprocess
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
