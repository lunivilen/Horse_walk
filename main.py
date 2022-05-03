from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import sys
from board import board


class UiMainWindow(object):
    def __init__(self):
        self.place_horse = None
        self.timer = None
        self.btn = None
        self.label = None
        self.centralwidget = None
        self.field_size = None

    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.setFixedSize(600, 600)
        centerPoint = QtWidgets.QApplication.screens()[0].geometry().center()
        main_window.move(centerPoint - main_window.frameGeometry().center())
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 600, 600))
        self.label.setMinimumSize(QtCore.QSize(600, 600))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("background.png"))
        self.label.setObjectName("label")
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(191, 450, 200, 69))
        self.btn.setStyleSheet("background-image: url(button.png);\n"
                               "background-color: rgb(167, 210, 183);\n"
                               "")
        self.btn.clicked.connect(self.click)

        self.btn.setText("")
        self.btn.setObjectName("btn")
        self.field_size = QtWidgets.QTextEdit(self.centralwidget)
        self.field_size.setGeometry(QtCore.QRect(270, 280, 191, 41))
        self.field_size.setText("6")
        font = QtGui.QFont()
        font.setFamily("Diary of an 8-bit mage")

        self.field_size.setFont(font)
        self.field_size.setStyleSheet("font: 18pt \"Diary of an 8-bit mage\";\n"
                                      "text-align: \"center\"")
        self.field_size.setObjectName("field_size")

        self.timer = QtWidgets.QTextEdit(self.centralwidget)
        self.timer.setGeometry(QtCore.QRect(410, 45, 70, 36))
        font = QtGui.QFont()
        font.setFamily("Diary of an 8-bit mage")
        font.setPointSize(18)
        font.setWeight(50)
        self.timer.setFont(font)
        self.timer.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.timer.setStyleSheet("font: 18pt \"Diary of an 8-bit mage\";\n"
                                 "text-align: \"center\"")
        self.timer.setObjectName("timer")
        self.timer.setText("10")
        self.place_horse = QtWidgets.QTextEdit(self.centralwidget)
        self.place_horse.setGeometry(QtCore.QRect(270, 390, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Diary of an 8-bit mage")
        self.place_horse.setFont(font)
        self.place_horse.setStyleSheet("font: 18pt \"Diary of an 8-bit mage\";\n"
                                       "text-align: \"center\"")
        self.place_horse.setObjectName("place_horse")
        self.place_horse.setText("1")
        main_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Chess"))

    def click(self):
        try:
            if 1 > int(self.timer.toPlainText()):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setWindowTitle("Неверное значение")
                msg.setText("Время игры должно быть положительным")
                button = msg.exec()
            elif int(self.field_size.toPlainText()) < 6:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setWindowTitle("Неверное значение")
                msg.setText("Размер поля должен быть больше или равен 6")
                button = msg.exec()
            elif not (0 < int(self.place_horse.toPlainText()) <= int(self.field_size.toPlainText()) ** 2):
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setWindowTitle("Неверное значение")
                msg.setText(
                    "Положение коня должно быть в диапазоне от 1 до " + str(int(self.field_size.toPlainText()) ** 2))
                button = msg.exec()
            else:
                main_window.hide()
                board(int(self.field_size.toPlainText()), int(self.place_horse.toPlainText()),
                      int(self.timer.toPlainText()))
                main_window.show()
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowTitle("Неверное значение")
            msg.setText("Во всех полях могут быть только целые положительные числа")
            button = msg.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec())
