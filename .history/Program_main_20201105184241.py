import os
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from view.main import Ui_MainWindow
from view.formDialog import FormDialog
import static.staticValues as staticValues
import rdbms.rdbms as rdbms 
from data.mbrInfo import Member
from view import QtUtil
import openpyxl


class WindowClass(Ui_MainWindow) :

    def __init__(self) :
        super(WindowClass, self).__init__()
        self.setupUi(self)
        
        self.button_add.clicked.connect(self.addMbr)
        self.button_del.clicked.connect(self.delMbr)
        self.button_modi.clicked.connect(self.modiMbr)
        self.button_upload.clicked.connect(self.upload)
        self.button_search.clicked.connect(self.search)

        if not self.showData():
            self.showData()

    def addMbr(self):
        print("clicked add button")
        self.dc = False
        self.formDialog = FormDialog()
        self.formDialog.button_submit.clicked.connect(self.submit)
        self.formDialog.button_doubleCheck.clicked.connect(self.double_check)
        self.formDialog.exec_()
        # self.formDialog.show()
        self.showData()


    def delMbr(self):
        print("clicked del button")
        if(self.tableWidget.currentRow() == -1):
            QMessageBox.warning(self, "Warning", "삭제할 회원을 선택해주세요")
            return

        id = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        delMsgBox = QMessageBox.question(self, "회원 삭제", "회원 ["+id+"] 정보를 정말 삭제하시겠습니까?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)

        if delMsgBox == QMessageBox.Yes:
            print("clicked YES")
            rdbms.deleteMBR(id)
            self.showData()
            


    def modiMbr(self):
        print("clicked modi button")
        if(self.tableWidget.currentRow() == -1):
            QMessageBox.warning(self, "Warning", "수정할 회원을 선택해주세요")
            return
        self.formDialog = FormDialog()
        self.formDialog.button_submit.clicked.connect(self.update)
        self.formDialog.button_doubleCheck.setText("")
        self.formDialog.button_doubleCheck.setStyleSheet(staticValues.grayButtonStyleSheet)
        self.formDialog.button_doubleCheck.setEnabled(False)

        self.formDialog.button_submit.setText("수정")
        self.formDialog.edit_id.setEnabled(False)
        self.formDialog.edit_id.setStyleSheet(staticValues.solidStyleSheet+";background-color: #aaaaaa;")
        
        #"MBR_ID, TALK, COIN, PURCHASE, DEPOSIT, SALE, WITHDRAW, RESERVE, \
        #    TOTAL_PUR, TOTAL_SAL, REVENUE, RATING, WALLET"
        print("!@#!@# ", self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        mbrInfo = rdbms.selectMBR(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())

        self.formDialog.edit_id.setText(mbrInfo[0])
        self.formDialog.edit_talk.setText(mbrInfo[1])
        self.formDialog.edit_coin.setText(mbrInfo[2])
        self.formDialog.edit_pur.setText(mbrInfo[3])
        self.formDialog.edit_dep.setText(mbrInfo[4])
        self.formDialog.edit_sal.setText(mbrInfo[5])
        self.formDialog.edit_withd.setText(mbrInfo[6])
        self.formDialog.edit_reserve.setText(mbrInfo[7])
        self.formDialog.edit_totpur.setText(mbrInfo[8])
        self.formDialog.edit_totsal.setText(mbrInfo[9])
        self.formDialog.edit_revenue.setText(mbrInfo[10])
        self.formDialog.edit_rating.setText(mbrInfo[11])
        self.formDialog.edit_wallet.setText(mbrInfo[12])

        self.formDialog.exec_()
        
        self.showData()
        # 수정 formDialog

    def upload(self):
        # 일괄 데이터 업로드
        print("clicked upload button")
        file = QtUtil.showFileDialog(self)
        if(file):
            load_wb = openpyxl.load_workbook(file)
            mylist = []
            for load_ws in load_wb:
                mylist = [ [c.value for c in r]  for r in load_ws ]
                break

            doubleList = []
            for i in range(1, len(mylist)):
                if(mylist[i][1] != ''):
                    checked = rdbms.checkID(mylist[i][1])
                    if(checked != None):
                        if(checked[0]):
                            doubleList.append((mylist[i][1],checked[1],mylist[i][2]))
                        else:
                            mbr = Member()
                            mbr.MBR_ID = mylist[i][1]
                            mbr.TALK = mylist[i][2]
                            mbr.COIN = mylist[i][3]
                            mbr.PURCHASE = mylist[i][4]
                            mbr.DEPOSIT = mylist[i][5]
                            mbr.SALE = mylist[i][6]
                            mbr.WITHDRAW = mylist[i][7]
                            mbr.RESERVE = mylist[i][8]
                            mbr.TOTAL_PUR = mylist[i][9]
                            mbr.TOTAL_SAL = mylist[i][10]
                            mbr.REVENUE = mylist[i][11]
                            mbr.RATING = mylist[i][12]
                            mbr.WALLET = mylist[i][13]

                            rdbms.excute_sql(mbr.toInsertSql())

            self.showData()

            if len(doubleList) == 0:
                QMessageBox.about(self, "일괄업로드", "정상적으로 업로드를 완료하였습니다.")
            else:
                strList = "\n".join(map(str, doubleList))
                outputFile = os.path.abspath(os.path.join(file, os.pardir))+"\FailedList.txt"
                print(outputFile)
                fw = open(outputFile, "w")
                fw.write(strList)
                fw.close()

                self.tableWidget2.setRowCount(len(doubleList))

                for i in range(self.tableWidget2.rowCount()):
                    self.tableWidget2.setItem(i, 0, QTableWidgetItem(doubleList[0]))
                    self.tableWidget2.setItem(i, 1, QTableWidgetItem(doubleList[1]))
                    self.tableWidget2.setItem(i, 2, QTableWidgetItem(doubleList[2]))

                QMessageBox.about(self, "일괄업로드", "업로드를 완료하였지만, 일부 중복데이터가 존재합니다.\n아래 파일을 확인하세요.\n"+outputFile)

    def closeEvent(self, event):
       event.accept()
    

    def double_check(self):
        print("clicked double check")
        if(self.formDialog.edit_id.text() != ''):
            checked = rdbms.checkID(self.formDialog.edit_id.text())
            if(checked[0]):
                QMessageBox.warning(self.formDialog, "Warning", f"단톡방 [{checked[1]}] 에 ID가 이미 존재 합니다.")
                self.formDialog.button_doubleCheck.setStyleSheet(staticValues.redButtonStyleSheet)
                self.formDialog.button_doubleCheck.setEnabled(True)
                self.dc = False
            else:
                QMessageBox.about(self.formDialog, "중복체크", "등록가능한 ID 입니다.")
                self.formDialog.button_doubleCheck.setStyleSheet(staticValues.grayButtonStyleSheet)
                self.formDialog.button_doubleCheck.setEnabled(False)
                self.formDialog.edit_id.setEnabled(False)
                self.formDialog.edit_id.setStyleSheet(staticValues.solidStyleSheet+";background-color: #aaaaaa;")
                self.dc = True
        else:
            QMessageBox.warning(self.formDialog, "Warning", "ID 를 입력해주세요.")


    def submit(self):
        if(self.formDialog.edit_id.text() == '' or self.formDialog.edit_talk.text() == ''):
            QMessageBox.warning(self.formDialog, "필수등록", "ID 와 단톡방은 필수 입력사항입니다.")
            return

        if(self.dc):
            mbr = Member()
            mbr.MBR_ID = self.formDialog.edit_id.text()
            mbr.TALK = self.formDialog.edit_talk.text()
            mbr.COIN = self.formDialog.edit_coin.text()
            mbr.PURCHASE = self.formDialog.edit_pur.text()
            mbr.DEPOSIT = self.formDialog.edit_dep.text()
            mbr.SALE = self.formDialog.edit_sal.text()
            mbr.WITHDRAW = self.formDialog.edit_withd.text()
            mbr.RESERVE = self.formDialog.edit_reserve.text()
            mbr.TOTAL_PUR = self.formDialog.edit_totpur.text()
            mbr.TOTAL_SAL = self.formDialog.edit_totsal.text()
            mbr.REVENUE = self.formDialog.edit_revenue.text()
            mbr.RATING = self.formDialog.edit_rating.text()
            mbr.WALLET = self.formDialog.edit_wallet.text()
            
            rdbms.excute_sql(mbr.toInsertSql())
            
            if rdbms.checkID(self.formDialog.edit_id.text())[0]:
                QMessageBox.about(self.formDialog, "회원등록", "회원이 정상적으로 등록되었습니다.")
                self.formDialog.close()
            else:
                QMessageBox.warning(self.formDialog, "회원등록", "회원 등록을 실패하였습니다.")
                self.formDialog.close()
            
            self.showData()
        else:
            QMessageBox.about(self.formDialog, "중복체크", "등록전 중복체크를 하세요")
    

    def update(self, id):
        if(self.formDialog.edit_id.text() == '' or self.formDialog.edit_talk.text() == ''):
            QMessageBox.warning(self.formDialog, "필수등록", "ID 와 단톡방은 필수 입력사항입니다.")
            return

        mbr = Member()
        mbr.MBR_ID = self.formDialog.edit_id.text()
        mbr.TALK = self.formDialog.edit_talk.text()
        mbr.COIN = self.formDialog.edit_coin.text()
        mbr.PURCHASE = self.formDialog.edit_pur.text()
        mbr.DEPOSIT = self.formDialog.edit_dep.text()
        mbr.SALE = self.formDialog.edit_sal.text()
        mbr.WITHDRAW = self.formDialog.edit_withd.text()
        mbr.RESERVE = self.formDialog.edit_reserve.text()
        mbr.TOTAL_PUR = self.formDialog.edit_totpur.text()
        mbr.TOTAL_SAL = self.formDialog.edit_totsal.text()
        mbr.REVENUE = self.formDialog.edit_revenue.text()
        mbr.RATING = self.formDialog.edit_rating.text()
        mbr.WALLET = self.formDialog.edit_wallet.text()
        
        rdbms.excute_sql(mbr.toUpdateSql())

        if rdbms.checkID(self.formDialog.edit_id.text())[0]:
            QMessageBox.about(self.formDialog, "회원수정", "회원이 정상적으로 수정되었습니다.")
            self.formDialog.close()
        else:
            QMessageBox.warning(self.formDialog, "회원수정", "회원 수정을 실패하였습니다.")
            self.formDialog.close()

        self.showData()
    

    def showData(self):
        print("showData")
        datas = rdbms.selectAll()
        if not datas:
            QMessageBox.warning(self, "초기DB생성", "보유중인 DB가 없어 새로 생성합니다.")
            return False
        self.tableWidget.setRowCount(len(datas))
        for i, d in enumerate(datas):
            for j, c in enumerate(d):
                self.tableWidget.setItem(i, j, QTableWidgetItem(c))

    def search(self):
        print("search")
        search_id = self.edit_search.text()
        if search_id != "":
            for i in range(self.tableWidget.rowCount()):
                if(self.tableWidget.item(i,0).text() == self.edit_search.text()):
                    self.tableWidget.setCurrentCell(i,1)
                    return
            
            QMessageBox.warning(self, "검색", "해당 ID가 존재하지 않습니다.")
        else:
            QMessageBox.warning(self, "검색", "검색할 ID를 입력해주세요.")

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    #프로그램 화면을 보여주는 코드
    myWindow.showMaximized()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
