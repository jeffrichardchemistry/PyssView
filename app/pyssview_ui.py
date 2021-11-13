# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PyssviewMainWindow(object):
    def setupUi(self, PyssviewMainWindow):
        PyssviewMainWindow.setObjectName("PyssviewMainWindow")
        PyssviewMainWindow.resize(500, 640)
        PyssviewMainWindow.setMinimumSize(QtCore.QSize(500, 640))
        PyssviewMainWindow.setMaximumSize(QtCore.QSize(500, 640))
        PyssviewMainWindow.setWindowOpacity(0.98)
        PyssviewMainWindow.setStyleSheet("background-color: rgb(40, 42, 54);")
        PyssviewMainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(PyssviewMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 481, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_newpass = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_newpass.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_newpass.setStyleSheet("QPushButton{\n"
"background-color: rgb(52, 101, 190);\n"
"color: rgb(238, 238, 236);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
" background-color: rgb(52, 101, 164);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(52, 101, 120);\n"
"}\n"
"")
        self.btn_newpass.setObjectName("btn_newpass")
        self.horizontalLayout.addWidget(self.btn_newpass)
        self.btn_removepass = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_removepass.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_removepass.setStyleSheet("QPushButton{\n"
"background-color: rgb(52, 101, 190);\n"
"color: rgb(238, 238, 236);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
" background-color: rgb(52, 101, 164);\n"
"}\n"
"QPushButton::pressed{\n"
"background-color: rgb(52, 101, 120);\n"
"}\n"
"")
        self.btn_removepass.setObjectName("btn_removepass")
        self.horizontalLayout.addWidget(self.btn_removepass)
        self.chk_remember = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.chk_remember.setEnabled(True)
        self.chk_remember.setMinimumSize(QtCore.QSize(60, 40))
        self.chk_remember.setMaximumSize(QtCore.QSize(100, 16777215))
        self.chk_remember.setStyleSheet("QCheckBox{\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"QCheckBox::indicator:pressed\n"
"{\n"
"background-color : rgb(52, 101, 190);\n"
"}")
        self.chk_remember.setChecked(True)
        self.chk_remember.setObjectName("chk_remember")
        self.horizontalLayout.addWidget(self.chk_remember)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 70, 481, 541))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidget = QtWidgets.QWidget()
        self.scrollAreaWidget.setGeometry(QtCore.QRect(0, 0, 479, 539))
        self.scrollAreaWidget.setObjectName("scrollAreaWidget")
        self.scrollArea.setWidget(self.scrollAreaWidget)
        PyssviewMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PyssviewMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setFocusPolicy(QtCore.Qt.TabFocus)
        self.menubar.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(114, 159, 207);")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setStyleSheet("color: rgb(255, 255, 255);")
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        PyssviewMainWindow.setMenuBar(self.menubar)
        self.saveMenu = QtWidgets.QAction(PyssviewMainWindow)
        self.saveMenu.setObjectName("saveMenu")
        self.loadMenu = QtWidgets.QAction(PyssviewMainWindow)
        self.loadMenu.setObjectName("loadMenu")
        self.quitMenu = QtWidgets.QAction(PyssviewMainWindow)
        self.quitMenu.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.quitMenu.setObjectName("quitMenu")
        self.showhide_allMenu = QtWidgets.QAction(PyssviewMainWindow)
        self.showhide_allMenu.setCheckable(True)
        self.showhide_allMenu.setChecked(True)
        self.showhide_allMenu.setObjectName("showhide_allMenu")
        self.removeAll_Menu = QtWidgets.QAction(PyssviewMainWindow)
        self.removeAll_Menu.setObjectName("removeAll_Menu")
        self.menuFile.addAction(self.saveMenu)
        self.menuFile.addAction(self.loadMenu)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.quitMenu)
        self.menuEdit.addAction(self.showhide_allMenu)
        self.menuEdit.addAction(self.removeAll_Menu)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(PyssviewMainWindow)
        QtCore.QMetaObject.connectSlotsByName(PyssviewMainWindow)

    def retranslateUi(self, PyssviewMainWindow):
        _translate = QtCore.QCoreApplication.translate
        PyssviewMainWindow.setWindowTitle(_translate("PyssviewMainWindow", "Pyssview"))
        self.btn_newpass.setText(_translate("PyssviewMainWindow", "New Password"))
        self.btn_removepass.setText(_translate("PyssviewMainWindow", "Remove Passwords"))
        self.chk_remember.setText(_translate("PyssviewMainWindow", "Remember"))
        self.menuFile.setTitle(_translate("PyssviewMainWindow", "File"))
        self.menuEdit.setTitle(_translate("PyssviewMainWindow", "Edit"))
        self.saveMenu.setText(_translate("PyssviewMainWindow", "Save"))
        self.saveMenu.setShortcut(_translate("PyssviewMainWindow", "Ctrl+S"))
        self.loadMenu.setText(_translate("PyssviewMainWindow", "Load"))
        self.quitMenu.setText(_translate("PyssviewMainWindow", "Quit"))
        self.quitMenu.setShortcut(_translate("PyssviewMainWindow", "Ctrl+Q"))
        self.showhide_allMenu.setText(_translate("PyssviewMainWindow", "Show/Hide all passwords"))
        self.removeAll_Menu.setText(_translate("PyssviewMainWindow", "Remove all passwords"))
