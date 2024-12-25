# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uart.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1201, 856)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(900, 90))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(304, 0, 0, 0)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setContentsMargins(25, 12, 25, 12)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.port_text = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port_text.setFont(font)
        self.port_text.setObjectName("port_text")
        self.horizontalLayout_2.addWidget(self.port_text)
        self.port_List = QtWidgets.QComboBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.port_List.setFont(font)
        self.port_List.setStyleSheet("")
        self.port_List.setObjectName("port_List")
        self.horizontalLayout_2.addWidget(self.port_List)
        self.baud_text = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.baud_text.setFont(font)
        self.baud_text.setObjectName("baud_text")
        self.horizontalLayout_2.addWidget(self.baud_text)
        self.baud_List = QtWidgets.QComboBox(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.baud_List.setFont(font)
        self.baud_List.setStyleSheet("")
        self.baud_List.setObjectName("baud_List")
        self.horizontalLayout_2.addWidget(self.baud_List)
        self.update_Button = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.update_Button.setFont(font)
        self.update_Button.setStyleSheet("")
        self.update_Button.setObjectName("update_Button")
        self.horizontalLayout_2.addWidget(self.update_Button)
        self.connect_Button = QtWidgets.QPushButton(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.connect_Button.setFont(font)
        self.connect_Button.setStyleSheet("")
        self.connect_Button.setCheckable(True)
        self.connect_Button.setObjectName("connect_Button")
        self.horizontalLayout_2.addWidget(self.connect_Button)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox.setMaximumSize(QtCore.QSize(500, 400))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(15, 25, 25, 25)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setText("")
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.port_text_2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port_text_2.setFont(font)
        self.port_text_2.setStyleSheet("")
        self.port_text_2.setObjectName("port_text_2")
        self.gridLayout.addWidget(self.port_text_2, 0, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("\n"
"QTextEdit {\n"
"    color: rgb(255, 0, 0);\n"
"    border: 0.5px solid black;\n"
"    border-radius: 2px;\n"
"    \n"
"\n"
"}\n"
"\n"
"")
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 2, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setText("")
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.port_text_3 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port_text_3.setFont(font)
        self.port_text_3.setStyleSheet("")
        self.port_text_3.setObjectName("port_text_3")
        self.gridLayout.addWidget(self.port_text_3, 1, 1, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("QTextEdit {\n"
"    color: rgb(0, 0, 255);\n"
"    border: 0.5px solid black;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"")
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 1, 2, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setText("")
        self.checkBox_3.setCheckable(True)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 2, 0, 1, 1)
        self.port_text_4 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port_text_4.setFont(font)
        self.port_text_4.setStyleSheet("")
        self.port_text_4.setObjectName("port_text_4")
        self.gridLayout.addWidget(self.port_text_4, 2, 1, 1, 1)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setStyleSheet("QTextEdit {\n"
"    color: rgb(0, 209, 0);\n"
"    border: 0.5px solid black;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"")
        self.textBrowser_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayout.addWidget(self.textBrowser_3, 2, 2, 1, 1)
        self.port_text_9 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port_text_9.setFont(font)
        self.port_text_9.setStyleSheet("")
        self.port_text_9.setObjectName("port_text_9")
        self.gridLayout.addWidget(self.port_text_9, 3, 1, 1, 1)
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_4.setFont(font)
        self.textBrowser_4.setStyleSheet("QTextEdit {\n"
"    color: rgb(170, 85, 127);\n"
"    border: 0.5px solid black;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"\n"
"")
        self.textBrowser_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.gridLayout.addWidget(self.textBrowser_4, 3, 2, 1, 1)
        self.port_text_13 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port_text_13.setFont(font)
        self.port_text_13.setObjectName("port_text_13")
        self.gridLayout.addWidget(self.port_text_13, 4, 1, 1, 1)
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_8.setFont(font)
        self.textBrowser_8.setStyleSheet("QTextEdit {\n"
"    border: 0.5px solid black;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"")
        self.textBrowser_8.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_8.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.gridLayout.addWidget(self.textBrowser_8, 4, 2, 1, 1)
        self.port_text_11 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port_text_11.setFont(font)
        self.port_text_11.setObjectName("port_text_11")
        self.gridLayout.addWidget(self.port_text_11, 5, 1, 1, 1)
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser_7.sizePolicy().hasHeightForWidth())
        self.textBrowser_7.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_7.setFont(font)
        self.textBrowser_7.setStyleSheet("QTextEdit {\n"
"    border: 0.5px solid black;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"")
        self.textBrowser_7.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_7.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.gridLayout.addWidget(self.textBrowser_7, 5, 2, 1, 1)
        self.port_text_10 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port_text_10.setFont(font)
        self.port_text_10.setObjectName("port_text_10")
        self.gridLayout.addWidget(self.port_text_10, 6, 1, 1, 1)
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_6.setFont(font)
        self.textBrowser_6.setStyleSheet("QTextEdit {\n"
"    border: 0.5px solid black;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"")
        self.textBrowser_6.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_6.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.gridLayout.addWidget(self.textBrowser_6, 6, 2, 1, 1)
        self.port_text_12 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port_text_12.setFont(font)
        self.port_text_12.setObjectName("port_text_12")
        self.gridLayout.addWidget(self.port_text_12, 7, 1, 1, 1)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.textBrowser_5.setFont(font)
        self.textBrowser_5.setStyleSheet("QTextEdit {\n"
"    border: 0.5px solid black;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"")
        self.textBrowser_5.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_5.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.gridLayout.addWidget(self.textBrowser_5, 7, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 250))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setContentsMargins(30, 30, 30, 30)
        self.gridLayout_2.setHorizontalSpacing(35)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.port_text_8 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port_text_8.setFont(font)
        self.port_text_8.setObjectName("port_text_8")
        self.gridLayout_2.addWidget(self.port_text_8, 0, 0, 1, 1)
        self.send_Text = QtWidgets.QTextEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.send_Text.setFont(font)
        self.send_Text.setStyleSheet("QTextEdit {\n"
"    border: 0.5px solid black;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"")
        self.send_Text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.send_Text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.send_Text.setObjectName("send_Text")
        self.gridLayout_2.addWidget(self.send_Text, 0, 1, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2.addWidget(self.frame_5, 1, 0, 1, 3)
        self.port_text_5 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port_text_5.setFont(font)
        self.port_text_5.setObjectName("port_text_5")
        self.gridLayout_2.addWidget(self.port_text_5, 2, 0, 1, 1)
        self.send_Text_2 = QtWidgets.QTextEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.send_Text_2.setFont(font)
        self.send_Text_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.send_Text_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.send_Text_2.setObjectName("send_Text_2")
        self.gridLayout_2.addWidget(self.send_Text_2, 2, 1, 1, 1)
        self.port_text_6 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port_text_6.setFont(font)
        self.port_text_6.setObjectName("port_text_6")
        self.gridLayout_2.addWidget(self.port_text_6, 3, 0, 1, 1)
        self.send_Text_3 = QtWidgets.QTextEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.send_Text_3.setFont(font)
        self.send_Text_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.send_Text_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.send_Text_3.setObjectName("send_Text_3")
        self.gridLayout_2.addWidget(self.send_Text_3, 3, 1, 1, 1)
        self.port_text_7 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port_text_7.setFont(font)
        self.port_text_7.setObjectName("port_text_7")
        self.gridLayout_2.addWidget(self.port_text_7, 4, 0, 1, 1)
        self.send_Text_4 = QtWidgets.QTextEdit(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.send_Text_4.setFont(font)
        self.send_Text_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.send_Text_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.send_Text_4.setObjectName("send_Text_4")
        self.gridLayout_2.addWidget(self.send_Text_4, 4, 1, 1, 1)
        self.send_Button_2 = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.send_Button_2.setFont(font)
        self.send_Button_2.setObjectName("send_Button_2")
        self.gridLayout_2.addWidget(self.send_Button_2, 0, 2, 1, 1)
        self.send_Button = QtWidgets.QPushButton(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.send_Button.setFont(font)
        self.send_Button.setObjectName("send_Button")
        self.gridLayout_2.addWidget(self.send_Button, 4, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setContentsMargins(30, 5, 30, 5)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scale = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.scale.setFont(font)
        self.scale.setStyleSheet("")
        self.scale.setCheckable(True)
        self.scale.setObjectName("scale")
        self.horizontalLayout_3.addWidget(self.scale)
        self.clear_Button = QtWidgets.QPushButton(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.clear_Button.setFont(font)
        self.clear_Button.setStyleSheet("")
        self.clear_Button.setObjectName("clear_Button")
        self.horizontalLayout_3.addWidget(self.clear_Button)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.graphicsView = QtWidgets.QGraphicsView(self.groupBox_5)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_6.addWidget(self.graphicsView)
        self.horizontalLayout_4.addWidget(self.groupBox_5)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1201, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTool = QtWidgets.QMenu(self.menubar)
        self.menuTool.setObjectName("menuTool")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionad = QtWidgets.QAction(MainWindow)
        self.actionad.setObjectName("actionad")
        self.menuFile.addAction(self.actionImport)
        self.menuFile.addAction(self.actionExport)
        self.menuFile.addSeparator()
        self.menuFile.addSeparator()
        self.menuTool.addAction(self.actionad)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTool.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Port Control"))
        self.port_text.setText(_translate("MainWindow", "Port:"))
        self.baud_text.setText(_translate("MainWindow", "Baud:"))
        self.update_Button.setText(_translate("MainWindow", "Update"))
        self.connect_Button.setText(_translate("MainWindow", "Connect"))
        self.groupBox.setTitle(_translate("MainWindow", "System Parameters"))
        self.port_text_2.setText(_translate("MainWindow", "SP (°C):"))
        self.port_text_3.setText(_translate("MainWindow", "PV1 (°C):"))
        self.port_text_4.setText(_translate("MainWindow", "PV2 (°C):"))
        self.port_text_9.setText(_translate("MainWindow", "PWM:"))
        self.port_text_13.setText(_translate("MainWindow", "Time (s):"))
        self.port_text_11.setText(_translate("MainWindow", "Kp:"))
        self.port_text_10.setText(_translate("MainWindow", "Ki:"))
        self.port_text_12.setText(_translate("MainWindow", "Kd:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Parameter Config"))
        self.port_text_8.setText(_translate("MainWindow", "SP:"))
        self.port_text_5.setText(_translate("MainWindow", "Kp:"))
        self.send_Text_2.setStyleSheet(_translate("MainWindow", "QTextEdit {\n"
"    border: 0.5px solid black;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
""))
        self.port_text_6.setText(_translate("MainWindow", "Ki:"))
        self.send_Text_3.setStyleSheet(_translate("MainWindow", "QTextEdit {\n"
"    border: 0.5px solid black;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
""))
        self.port_text_7.setText(_translate("MainWindow", "Kd:"))
        self.send_Text_4.setStyleSheet(_translate("MainWindow", "QTextEdit {\n"
"    border: 0.5px solid black;\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
""))
        self.send_Button_2.setText(_translate("MainWindow", "➤"))
        self.send_Button.setText(_translate("MainWindow", "➤"))
        self.scale.setText(_translate("MainWindow", "Scale"))
        self.clear_Button.setText(_translate("MainWindow", "Clear"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Real-time Data"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTool.setTitle(_translate("MainWindow", "Tool"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionad.setText(_translate("MainWindow", "Ziggler Nichols 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
