from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from os import path
import speed_typing
import snake
import Connect_4
import sys

FROM_CLASS, _ = loadUiType(path.join(path.dirname(__file__), "304_Games.ui"))
                                                                        #relation to QtDesigner

class MainApp(QMainWindow, FROM_CLASS):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("Gaming Project")
        self.button1()                                                   
        self.button2()
        self.button3()


    def button1(self):                                                     
        self.pushButton_1.clicked.connect(self.button1_effect)             

    def button1_effect(self):
        Connect_4.ConnectFour()


    def button2(self):                                                    
        self.pushButton_2.clicked.connect(self.button2_effect)             

    def button2_effect(self):
        speed_typing.SpeedTyping()


    def button3(self):                                                    
        self.pushButton_3.clicked.connect(self.button3_effect)             

    def button3_effect(self):
        snake.snake_game()



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()

    