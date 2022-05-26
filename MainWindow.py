from PyQt5.QtWidgets import QApplication,QPushButton,QWidget,QMainWindow,QLineEdit,QComboBox,QStackedWidget
# import sys
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from matplotlib.pyplot import show
from matplotlib.widgets import Widget
from best_fit import best_fit
from worst_fit import worst_fit
from first_fit import first_fit

class secondscreen(QWidget):
    def __init__(self,output,Request):
        super(secondscreen,self).__init__()
        uic.loadUi('D:\\Programs\\Python\\OS Mini Project\\Output.ui',self)
        p1=self.findChild(QLineEdit,'Process1')
        p2=self.findChild(QLineEdit,'Process2')
        p3=self.findChild(QLineEdit,'Process3')
        p4=self.findChild(QLineEdit,'Process4')
        p5=self.findChild(QLineEdit,'Process5')
        p6=self.findChild(QLineEdit,'Process6')
        r1=self.findChild(QLineEdit,'Block1')
        r2=self.findChild(QLineEdit,'Block2')
        r3=self.findChild(QLineEdit,'Block3')
        r4=self.findChild(QLineEdit,'Block4')
        r5=self.findChild(QLineEdit,'Block5')
        r6=self.findChild(QLineEdit,'Block6')
        re1=self.findChild(QLineEdit,'Remain1')
        re2=self.findChild(QLineEdit,'Remain2')
        re3=self.findChild(QLineEdit,'Remain3')
        re4=self.findChild(QLineEdit,'Remain4')
        re5=self.findChild(QLineEdit,'Remain5')
        re6=self.findChild(QLineEdit,'Remain6')
        self.Process1.setText(Request[0])
        self.Process2.setText(Request[1])
        self.Process3.setText(Request[2])
        self.Process4.setText(Request[3])
        self.Process5.setText(Request[4])
        self.Process6.setText(Request[5])
        self.Block1.setText(str(output['p1']))
        self.Block2.setText(str(output['p2']))
        self.Block3.setText(str(output['p3']))
        self.Block4.setText(str(output['p4']))
        self.Block5.setText(str(output['p5']))
        self.Block6.setText(str(output['p6']))
        self.Remain1.setText(str(output['p1']-int(Request[0])))
        self.Remain2.setText(str(output['p2']-int(Request[1])))
        self.Remain3.setText(str(output['p3']-int(Request[2])))
        self.Remain4.setText(str(output['p4']-int(Request[3])))
        self.Remain5.setText(str(output['p5']-int(Request[4])))
        self.Remain6.setText(str(output['p6']-int(Request[5])))

class UI(QWidget):
    Request=[]
    Block_size=[]
    alloc=''
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi('D:\\Programs\\Python\\OS Mini Project\\Interface.ui',self)
        btn=self.findChild(QPushButton,'Submit')
        btn.clicked.connect(self.submitAction)
        p1=self.findChild(QLineEdit,'Process1')
        p2=self.findChild(QLineEdit,'Process2')
        p3=self.findChild(QLineEdit,'Process3')
        p4=self.findChild(QLineEdit,'Process4')
        p5=self.findChild(QLineEdit,'Process5')
        p6=self.findChild(QLineEdit,'Process6')
        r1=self.findChild(QLineEdit,'Block1')
        r2=self.findChild(QLineEdit,'Block2')
        r3=self.findChild(QLineEdit,'Block3')
        r4=self.findChild(QLineEdit,'Block4')
        r5=self.findChild(QLineEdit,'Block5')
        r6=self.findChild(QLineEdit,'Block6')
        type=self.findChild(QComboBox,'Type')
        # self.show()
    def submitAction(self):
        UI.Request.append(self.Process1.text())
        UI.Request.append(self.Process2.text())
        UI.Request.append(self.Process3.text())
        UI.Request.append(self.Process4.text())
        UI.Request.append(self.Process5.text())
        UI.Request.append(self.Process6.text())
        UI.Block_size.append(self.Block1.text())
        UI.Block_size.append(self.Block2.text())        
        UI.Block_size.append(self.Block3.text())
        UI.Block_size.append(self.Block4.text())
        UI.Block_size.append(self.Block5.text())
        UI.Block_size.append(self.Block6.text())
        UI.alloc+=self.Type.currentText()
        if(UI.alloc=='First-Fit'):
            output=first_fit(UI.Request,UI.Block_size)
        elif(UI.alloc=="Best-Fit"):
            output=best_fit(UI.Request,UI.Block_size)
        else:
           output=worst_fit(UI.Request,UI.Block_size)
        o=secondscreen(output,UI.Request)
        widget.addWidget(o)
        widget.setCurrentIndex(widget.currentIndex()+1)
app=QApplication([])
Window=UI()
widget=QStackedWidget()
widget.addWidget(Window)
widget.setFixedHeight(1080)
widget.setFixedWidth(1920)
widget.show()
app.exec_() 
