# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'out.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(426, 257)
        Dialog.setMinimumSize(QtCore.QSize(426, 257))
        Dialog.setMaximumSize(QtCore.QSize(426, 257))
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 40, 301, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pid_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.pid_label.setObjectName("pid_label")
        self.verticalLayout.addWidget(self.pid_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.run_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.run_label.setObjectName("run_label")
        self.horizontalLayout_2.addWidget(self.run_label)
        self.run_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.run_line.setObjectName("run_line")
        self.horizontalLayout_2.addWidget(self.run_line)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.arr_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.arr_label.setObjectName("arr_label")
        self.horizontalLayout.addWidget(self.arr_label)
        self.arr_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.arr_line.setObjectName("arr_line")
        self.horizontalLayout.addWidget(self.arr_line)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.enter_button = QtWidgets.QPushButton(Dialog)
        self.enter_button.setGeometry(QtCore.QRect(100, 210, 93, 28))
        self.enter_button.setObjectName("enter_button")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 210, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "按提示输入程序"))
        self.pid_label.setText(_translate("Dialog", "按 下项 记录程序"))
        self.run_label.setText(_translate("Dialog", "运行时间"))
        self.arr_label.setText(_translate("Dialog", "到达时间"))
        self.enter_button.setText(_translate("Dialog", "确认"))
        self.pushButton_2.setText(_translate("Dialog", "下项"))
