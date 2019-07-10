import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget

class CenterForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('set center')
        self.resize(400,300)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        NewLeft = (screen.width() - size.width())/2
        NewTop = (screen.height() - size.height())/2
        self.move(NewLeft,NewTop)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CenterForm()
    main.show()
    sys.exit(app.exec_())