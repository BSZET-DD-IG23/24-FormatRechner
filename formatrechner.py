#!/usr/bin/python3

# This Python file uses the following encoding: utf-8
# main_widget.py BSZET-DD Template
# Copyright © 2022 SRE

import os
import sys
from builtins import *

from PySide6.QtUiTools import QUiLoader

sys.dont_write_bytecode = True  # noqa: E402
sys.path.insert(0, os.path.abspath(
                os.path.join(os.path.dirname(__file__), '..')))  # noqa: E402

from PySide6.QtUiTools import loadUiType

from PySide6.QtCore import (
     QCoreApplication,
     Signal,
     Slot,
     Qt,
     QFile,
     QIODevice
     )

from PySide6.QtWidgets import (
     QApplication,
     QMainWindow,
     QWidget,
     QListWidgetItem
     )

from PySide6.QtGui import (
    QAction
    )

UIsPath = "ui/"

mainUIfilePath = UIsPath + "form.ui"
Form, Base = loadUiType(os.path.join(sys.path[1], mainUIfilePath))


def fromBase(inbase, number):
    return int(str(number), base=inbase)


def toBase(inbase, number):
    if inbase == 2:
        return str(bin(number))
    elif inbase == 8:
        return str(oct(number))
    elif inbase == 10:
        return str(str(number))
    elif inbase == 16:
        return str(hex(number))
    else:
        print("Conversion error. base does not exist.")
        print("Base is: {inBase}")
    return


def calcbases(inbase, outbase, number):
    return toBase(outbase, fromBase(inbase, number))



class FormatRechner(Base, Form):
    inBase = 2
    outBase = 10

    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.setupUi(self)

    def appendInput(self, input, text):
        txt = input.text()
        input.setText(txt + text)

    @Slot()
    def on_btn_txtdel_clicked(self):
        txt = self.leInput.text()
        self.leInput.setText(txt[:-1])

    # Input buttons
    @Slot()
    def on_btntxt_0_clicked(self):
        self.appendInput(self.leInput, "0")

    @Slot()
    def on_btntxt_1_clicked(self):
        self.appendInput(self.leInput, "1")

    @Slot()
    def on_btntxt_2_clicked(self):
        self.appendInput(self.leInput, "2")

    @Slot()
    def on_btntxt_3_clicked(self):
        self.appendInput(self.leInput, "3")

    @Slot()
    def on_btntxt_4_clicked(self):
        self.appendInput(self.leInput, "4")

    @Slot()
    def on_btntxt_5_clicked(self):
        self.appendInput(self.leInput, "5")

    @Slot()
    def on_btntxt_6_clicked(self):
        self.appendInput(self.leInput, "6")

    @Slot()
    def on_btntxt_7_clicked(self):
        self.appendInput(self.leInput, "7")

    @Slot()
    def on_btntxt_8_clicked(self):
        self.appendInput(self.leInput, "8")

    @Slot()
    def on_btntxt_9_clicked(self):
        self.appendInput(self.leInput, "9")

    @Slot()
    def on_btntxt_a_clicked(self):
        self.appendInput(self.leInput, "A")

    @Slot()
    def on_btntxt_b_clicked(self):
        self.appendInput(self.leInput, "B")

    @Slot()
    def on_btntxt_c_clicked(self):
        self.appendInput(self.leInput, "C")

    @Slot()
    def on_btntxt_d_clicked(self):
        self.appendInput(self.leInput, "D")

    @Slot()
    def on_btntxt_e_clicked(self):
        self.appendInput(self.leInput, "E")

    @Slot()
    def on_btntxt_f_clicked(self):
        self.appendInput(self.leInput, "F")

    # in base
    @Slot()
    def on_cbDual_clicked(self):
        self.inBase = 2

    @Slot()
    def on_cbOct_clicked(self):
        self.inBase = 8

    @Slot()
    def on_cbDec_clicked(self):
        self.inBase = 10

    @Slot()
    def on_cbHex_clicked(self):
        self.inBase = 16

    # out base
    @Slot()
    def on_cbDual_2_clicked(self):
        self.outBase = 2

    @Slot()
    def on_cbOct_2_clicked(self):
        self.outBase = 8

    @Slot()
    def on_cbDec_2_clicked(self):
        self.outBase = 10

    @Slot()
    def on_cbHex_2_clicked(self):
        self.outBase = 16

    # GUI
        # get Number
    def getNumber(self):
        return self.leInput.text()

    @Slot()
    def on_btnCalc_clicked(self):
        num = self.getNumber()
        try:
            res = calcbases(self.inBase, self.outBase, num)
        except:
            self.output.append("Error!")
            return
        self.output.append(res)

if __name__ == "__main__":
    os.environ['PYSIDE_DESIGNER_PLUGINS'] = "."
    os.environ["QT_LOGGING_RULES"] = '*.debug=false;qt.pysideplugin=false'

    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    os.chdir(sys.path[1])
    widget = FormatRechner()
    widget.show()

    sys.exit(app.exec())
