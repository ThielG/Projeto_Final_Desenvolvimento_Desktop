# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'emprestimo_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"bibl.io")
        Dialog.resize(298, 277)
        icon = QIcon()
        icon.addFile(u"view/pilha.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background-color: rgb(244, 243, 238);")
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_emprestimo_livro = QLabel(Dialog)
        self.lbl_emprestimo_livro.setObjectName(u"lbl_emprestimo_livro")
        self.lbl_emprestimo_livro.setStyleSheet(u"font: 16pt \"Calibri\";")

        self.verticalLayout.addWidget(self.lbl_emprestimo_livro)

        self.lbl_livro_emprestimo = QLabel(Dialog)
        self.lbl_livro_emprestimo.setObjectName(u"lbl_livro_emprestimo")
        self.lbl_livro_emprestimo.setStyleSheet(u"font: 12pt \"Calibri\";")

        self.verticalLayout.addWidget(self.lbl_livro_emprestimo)

        self.txt_livro_emprestimo = QLineEdit(Dialog)
        self.txt_livro_emprestimo.setObjectName(u"txt_livro_emprestimo")
        self.txt_livro_emprestimo.setStyleSheet(u"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: #EAE0D6;")
        self.txt_livro_emprestimo.setReadOnly(True)

        self.verticalLayout.addWidget(self.txt_livro_emprestimo)

        self.lbl_cpf_emprestimo = QLabel(Dialog)
        self.lbl_cpf_emprestimo.setObjectName(u"lbl_cpf_emprestimo")
        self.lbl_cpf_emprestimo.setStyleSheet(u"font: 12pt \"Calibri\";")

        self.verticalLayout.addWidget(self.lbl_cpf_emprestimo)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_cpf_emprestimo = QLineEdit(Dialog)
        self.txt_cpf_emprestimo.setObjectName(u"txt_cpf_emprestimo")
        self.txt_cpf_emprestimo.setStyleSheet(u"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: #EAE0D6;")

        self.horizontalLayout.addWidget(self.txt_cpf_emprestimo)

        self.btn_consultar_emprestimo = QPushButton(Dialog)
        self.btn_consultar_emprestimo.setObjectName(u"btn_consultar_emprestimo")
        self.btn_consultar_emprestimo.setStyleSheet(u"QPushButton {\n"
"background-color: #e0afa0;\n"
"font: 10pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  #ca9e90;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_consultar_emprestimo)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lbl_nome_emprestimo = QLabel(Dialog)
        self.lbl_nome_emprestimo.setObjectName(u"lbl_nome_emprestimo")
        self.lbl_nome_emprestimo.setStyleSheet(u"font: 12pt \"Calibri\";")

        self.verticalLayout.addWidget(self.lbl_nome_emprestimo)

        self.txt_nome_emprestimo = QLineEdit(Dialog)
        self.txt_nome_emprestimo.setObjectName(u"txt_nome_emprestimo")
        self.txt_nome_emprestimo.setStyleSheet(u"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: #EAE0D6;")
        self.txt_nome_emprestimo.setReadOnly(True)

        self.verticalLayout.addWidget(self.txt_nome_emprestimo)

        self.btn_confirmar_emprestimo = QPushButton(Dialog)
        self.btn_confirmar_emprestimo.setObjectName(u"btn_confirmar_emprestimo")
        self.btn_confirmar_emprestimo.setStyleSheet(u"QPushButton {\n"
"background-color: #e0afa0;\n"
"font: 10pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px;\n"
"margin:10px 40px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  #ca9e90;\n"
"}")

        self.verticalLayout.addWidget(self.btn_confirmar_emprestimo)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("bibl.io", u"bibl.io", None))
        self.lbl_emprestimo_livro.setText(QCoreApplication.translate("Dialog", u"Empr\u00e9stimo:", None))
        self.lbl_livro_emprestimo.setText(QCoreApplication.translate("Dialog", u"Livro:", None))
        self.lbl_cpf_emprestimo.setText(QCoreApplication.translate("Dialog", u"CPF:", None))
        self.btn_consultar_emprestimo.setText(QCoreApplication.translate("Dialog", u"Consultar", None))
        self.lbl_nome_emprestimo.setText(QCoreApplication.translate("Dialog", u"Nome:", None))
        self.btn_confirmar_emprestimo.setText(QCoreApplication.translate("Dialog", u"Confirmar", None))
    # retranslateUi
