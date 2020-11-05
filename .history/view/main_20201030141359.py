# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtWidgets import QMainWindow, QTableWidget, QVBoxLayout, QWidget, QLabel, QPushButton \
                            , QTabWidget, QApplication, QAbstractItemView, QTableWidget

from PyQt5.QtCore import QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont

import static.staticValues as staticValues


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):

        QDesktopWidget.screenGeometry

        MainWindow.resize(1200, 800)
        #메인 화면 색상py
        self.setStyleSheet("color: black;"
                        "background-color: white;")

        font = QFont()
        font.setFamily("NanumGothic")
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(20, 20, 101, 31))
        font = QFont()
        font.setFamily("NanumGothic")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.button_add = QPushButton(self.centralwidget)
        self.button_add.setGeometry(QRect(60, 730, 131, 34))
        #버튼 스타일 변경
        self.button_add.setStyleSheet(staticValues.blueButtonStyleSheet)
        self.button_add.setFont(staticValues.buttonFont)

        self.button_modi = QPushButton(self.centralwidget)
        self.button_modi.setGeometry(QRect(260, 730, 131, 34))
        self.button_modi.setStyleSheet(staticValues.blueButtonStyleSheet)
        self.button_modi.setFont(staticValues.buttonFont)

        self.button_del = QPushButton(self.centralwidget)
        self.button_del.setGeometry(QRect(460, 730, 131, 34))
        self.button_del.setStyleSheet(staticValues.redButtonStyleSheet)
        self.button_del.setFont(staticValues.buttonFont)

        self.button_upload = QPushButton(self.centralwidget)
        self.button_upload.setGeometry(QRect(790, 730, 131, 34))
        self.button_upload.setStyleSheet(staticValues.grayButtonStyleSheet)
        self.button_upload.setFont(staticValues.buttonFont)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QRect(40, 70, 1121, 621))
        self.tab = QWidget()
        self.tab.layout = QVBoxLayout()
        self.tabWidget.addTab(self.tab, "회원 목록")
        self.tableWidget = QTableWidget(self.tab)
        self.tableWidget.setGeometry(QRect(0, 0, 1111, 591))
        self.tableWidget.setObjectName("회원 목록")
        self.tableWidget.setColumnCount(13)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        self.tableWidget.setHorizontalHeaderLabels(["회원 ID", "단톡방", "코인명", "구매", "입금", "판매", "출근"
        , "보유잔량", "총구매금액", "총판매금액", "수익", "평단가", "지갑주소"])
        # self.tableView = QTableWidget()
        # self.tableView.setColumnCount(5)
        # self.tableView.setRowCount(3)

        # self.tab.layout.addWidget(self.tableView)
        # self.tab.setLayout(self.tab.layout)
        # self.tab_2 = QWidget()
        # self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("Pickbang")
        self.label.setText("COPLE")
        self.button_add.setText("회원추가")
        self.button_modi.setText("회원 정보 수정")
        self.button_del.setText("회원 삭제")
        self.button_upload.setText("일괄 업로드")
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Tab 1")
        # self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "Tab 2")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
