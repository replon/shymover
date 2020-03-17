import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import pyautogui


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.duration_le = QLineEdit(self)
        self.start_btn = QPushButton('Start', self)
        self.stop_btn = QPushButton('Stop', self)
        self.timer = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Shy Mover')
        self.setGeometry(400, 300, 200, 80)

        self.duration_le.setGeometry(20, 10, 100, 20)
        self.duration_le.setPlaceholderText('Duration(sec)')

        self.start_btn.setGeometry(20, 40, 80, 30)
        self.start_btn.clicked.connect(self.start_btn_click)

        self.stop_btn.setGeometry(100, 40, 80, 30)
        self.stop_btn.clicked.connect(self.stop_btn_click)
        self.stop_btn.setDisabled(True)

        self.show()

    def start_btn_click(self):
        try:
            self.duration = float(self.duration_le.text())
        except Exception:
            self.duration = 10.0
            self.duration_le.setText('10')

        self.duration_le.setDisabled(True)
        self.start_btn.setDisabled(True)
        self.stop_btn.setDisabled(False)
        self.move()
        self.timer = QTimer()
        self.timer.start(self.duration*1000)
        self.timer.timeout.connect(self.move)
        self.repaint()

    def stop_btn_click(self):
        if self.timer:
            self.timer.stop()
        self.duration_le.setDisabled(False)
        self.start_btn.setDisabled(False)
        self.stop_btn.setDisabled(True)
        self.repaint()

    def move(self):
        x, y = pyautogui.position()
        pyautogui.moveTo(x+1, y+1, 0.01)
        x, y = pyautogui.position()
        pyautogui.moveTo(x+1, y-1, 0.01)
        x, y = pyautogui.position()
        pyautogui.moveTo(x-1, y-1, 0.01)
        x, y = pyautogui.position()
        pyautogui.moveTo(x-1, y+1, 0.01)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
