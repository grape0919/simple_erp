from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont

buttonSize = QSize(100,40)

#버튼 폰트
buttonFont = QFont()
buttonFont.setBold(False)
buttonFont.setFamily("NanumGothic")
#버튼 styleSheet
grayButtonStyleSheet = "color: white;"
grayButtonStyleSheet += "background-color: #5E5E5E;"
grayButtonStyleSheet += "border-style: solid;"
grayButtonStyleSheet += "border-width: 2px;"
grayButtonStyleSheet += "border-color: #5E5E5E;"
grayButtonStyleSheet += "border-radius: 5px"

blueButtonStyleSheet = "color: white;"
blueButtonStyleSheet += "background-color: #2F92FA;"
blueButtonStyleSheet += "border-style: solid;"
blueButtonStyleSheet += "border-width: 2px;"
blueButtonStyleSheet += "border-color: #2F92FA;"
blueButtonStyleSheet += "border-radius: 5px"

redButtonStyleSheet = "color: white;"
redButtonStyleSheet += "background-color: #F15F5F;"
redButtonStyleSheet += "border-style: solid;"
redButtonStyleSheet += "border-width: 2px;"
redButtonStyleSheet += "border-color: #F15F5F;"
redButtonStyleSheet += "border-radius: 5px"
#disabled styleSheet
disabledStyleSheet = "color: #aaaaaa;"

#enabled styleSheet
enabledStyleSheet = "color: #000000;"

#solid stylesheet
solidStyleSheet = "border-style: solid;"
solidStyleSheet += "border-width: 1px;"
solidStyleSheet += "border-radius: 5px"

        # #메인 화면 색상py
        # self.setStyleSheet("color: black;"
        #                 "background-color: white")

        #  #버튼 스타일 변경
        # self.button_activate.setStyleSheet(staticValues.buttonStyleSheet)
        # self.button_activate.setFont(staticValues.buttonFont)