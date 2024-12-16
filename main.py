import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
                             QFileDialog, QLabel, QHBoxLayout, )
from PyQt6.QtCore import Qt, QTimer, QTime
from PyQt6.QtGui import QIcon


class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stopwatch')
        self.setGeometry(100, 100, 300, 100)
        self.time= QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00:00", self)
        self.start_button = QPushButton('Start', self)
        self.stop_button = QPushButton('Stop', self)
        self.reset_button = QPushButton('Reset', self)
        self.timer = QTimer(self)
        self.init_ui()
        self.setWindowIcon(QIcon('stopwatch.png'))

    def init_ui(self):
        self.setWindowTitle('Stopwatch')


        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)

        self.setLayout(vbox)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        hbox = QHBoxLayout()
        
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.stop_button.setCursor((Qt.CursorShape.PointingHandCursor))
        self.start_button.setCursor((Qt.CursorShape.PointingHandCursor))
        self.reset_button.setCursor((Qt.CursorShape.PointingHandCursor))

        self.setStyleSheet("""
        QPushButton, QLabel {
            font-size: 20px;
            font-weight: bold;
            color: #333;
            ;
        }
        QPushButton {
            background-color: #f0f0f0;
            border: 1px solid #f0f0f0;
            border-radius: 5px;
            padding: 5px;
                       
        }
        QPushButton:hover {
            background-color: gray;
            border: 1px solid #f0f0f0;
            border-radius: 5px;
            padding: 5px;
            
        }
        QLabel {
            font-size: 120px;
            font-weight: bold;
            color: #333;
            
        }
        """)

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText("00:00:00:00")

    def format_time(self,time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec()  //10
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:02d}"
       
    def update(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    app.exec()