from PyQt5.QtWidgets import QFileDialog, QMessageBox

def alert(self):
    QMessageBox.about(self, "Warning", "url은 .com/ 까지만 작성해주세요.")

def showFileDialog(self):
    print("Clicked button")
    fname = QFileDialog.getOpenFileName(self, 'Open excel for paragraph', 'Desktop',
                                        "Excel (*.xls *.xlsx *csv)")
    if fname[0]:
        return fname[0]