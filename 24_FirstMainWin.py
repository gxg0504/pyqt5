# 主窗口类型，3种窗口：
# QMainWindow：包含菜单栏、工具栏、状态栏和标题栏，最常见的窗口形式
# QDialog：对话窗口的基类。没有菜单栏、工具栏、状态栏
# QWidget：不确定窗口的用途，就使用QWidget

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class FirstWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__()

        self.setWindowTitle('first window')
        self.resize(400,300)
        self.status = self.statusBar()
        self.status.showMessage('stay 5 second',5000)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon(./))
    main = FirstWindow()
    main.show()
    sys.exit(app.exec_())

