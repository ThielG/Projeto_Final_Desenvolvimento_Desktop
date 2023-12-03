# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import view.resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/logo/pilha.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(234, 224, 213)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout.addWidget(self.label_13, 0, 7, 1, 1)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"font: 44pt \"Calibri\";\n"
"color: #100907;")

        self.gridLayout.addWidget(self.label_10, 0, 5, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 0, 3, 1, 1)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 9, 1, 1)

        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout.addWidget(self.label_14, 0, 2, 1, 1)

        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 0, 8, 1, 1)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"image: url(:/logo/pilha.png);")

        self.gridLayout.addWidget(self.widget_4, 0, 4, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"background-color: rgb(244, 243, 238);")
        self.tab_emprestimo = QWidget()
        self.tab_emprestimo.setObjectName(u"tab_emprestimo")
        self.verticalLayout_8 = QVBoxLayout(self.tab_emprestimo)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.tab_emprestimo)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 16pt \"Calibri\";")

        self.verticalLayout_7.addWidget(self.label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.txt_pesquisar = QLineEdit(self.tab_emprestimo)
        self.txt_pesquisar.setObjectName(u"txt_pesquisar")
        self.txt_pesquisar.setStyleSheet(u"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: #EAE0D6;")

        self.horizontalLayout_7.addWidget(self.txt_pesquisar)

        self.btn_pesquisar = QPushButton(self.tab_emprestimo)
        self.btn_pesquisar.setObjectName(u"btn_pesquisar")
        self.btn_pesquisar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pesquisar.setStyleSheet(u"background-color: rgb(224, 175, 160);\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px;")

        self.horizontalLayout_7.addWidget(self.btn_pesquisar)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.label_3 = QLabel(self.tab_emprestimo)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 16pt \"Calibri\";")

        self.verticalLayout_7.addWidget(self.label_3)

        self.tb_acervo = QTableWidget(self.tab_emprestimo)
        header_tb_acervo = self.tb_acervo.horizontalHeader()
        header_tb_acervo.setSectionResizeMode(QHeaderView.Stretch)
        if (self.tb_acervo.columnCount() < 6):
            self.tb_acervo.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_acervo.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_acervo.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_acervo.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_acervo.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_acervo.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_acervo.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tb_acervo.setObjectName(u"tb_acervo")
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(12)
        self.tb_acervo.setFont(font)
        self.tb_acervo.setStyleSheet(u"QTableView {\n"
"background-color: #6ceada3;\n"
"selection-background-color:#EAE0D;\n"
"}\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.tb_acervo)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_emprestimo = QPushButton(self.tab_emprestimo)
        self.btn_emprestimo.setObjectName(u"btn_emprestimo")
        self.btn_emprestimo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_emprestimo.setStyleSheet(u"background-color: rgb(224, 175, 160);\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;")

        self.horizontalLayout_4.addWidget(self.btn_emprestimo)

        self.btn_devolucao = QPushButton(self.tab_emprestimo)
        self.btn_devolucao.setObjectName(u"btn_devolucao")
        self.btn_devolucao.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_devolucao.setStyleSheet(u"background-color: rgb(224, 175, 160);\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;")

        self.horizontalLayout_4.addWidget(self.btn_devolucao)

        self.btn_reserva = QPushButton(self.tab_emprestimo)
        self.btn_reserva.setObjectName(u"btn_reserva")
        self.btn_reserva.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_reserva.setStyleSheet(u"background-color: rgb(224, 175, 160);\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;")

        self.horizontalLayout_4.addWidget(self.btn_reserva)

        self.btn_renovacao = QPushButton(self.tab_emprestimo)
        self.btn_renovacao.setObjectName(u"btn_renovacao")
        self.btn_renovacao.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_renovacao.setStyleSheet(u"background-color: rgb(224, 175, 160);\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;")

        self.horizontalLayout_4.addWidget(self.btn_renovacao)

        self.btn_expostar = QPushButton(self.tab_emprestimo)
        self.btn_expostar.setObjectName(u"btn_expostar")
        self.btn_expostar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_expostar.setStyleSheet(u"background-color: rgb(224, 175, 160);\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;")

        self.horizontalLayout_4.addWidget(self.btn_expostar)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.tabWidget.addTab(self.tab_emprestimo, "")
        self.tab_livro = QWidget()
        self.tab_livro.setObjectName(u"tab_livro")
        self.gridLayout_2 = QGridLayout(self.tab_livro)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.tab_livro)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 16pt \"Calibri\";")

        self.verticalLayout_2.addWidget(self.label_4)

        self.lbl_titulo_livro = QLabel(self.tab_livro)
        self.lbl_titulo_livro.setObjectName(u"lbl_titulo_livro")
        self.lbl_titulo_livro.setStyleSheet(u"font: 12pt \"Calibri\";")

        self.verticalLayout_2.addWidget(self.lbl_titulo_livro)

        self.txt_titulo_livro = QLineEdit(self.tab_livro)
        self.txt_titulo_livro.setObjectName(u"txt_titulo_livro")
        self.txt_titulo_livro.setStyleSheet(u"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: #EAE0D6;")

        self.verticalLayout_2.addWidget(self.txt_titulo_livro)

        self.lbl_autor_livro = QLabel(self.tab_livro)
        self.lbl_autor_livro.setObjectName(u"lbl_autor_livro")
        self.lbl_autor_livro.setStyleSheet(u"font: 12pt \"Calibri\";")

        self.verticalLayout_2.addWidget(self.lbl_autor_livro)

        self.txt_autor_livro = QLineEdit(self.tab_livro)
        self.txt_autor_livro.setObjectName(u"txt_autor_livro")
        self.txt_autor_livro.setStyleSheet(u"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: #EAE0D6;")

        self.verticalLayout_2.addWidget(self.txt_autor_livro)

        self.lbl_ano_livro = QLabel(self.tab_livro)
        self.lbl_ano_livro.setObjectName(u"lbl_ano_livro")
        self.lbl_ano_livro.setStyleSheet(u"font: 12pt \"Calibri\";")

        self.verticalLayout_2.addWidget(self.lbl_ano_livro)

        self.txt_ano_livro = QLineEdit(self.tab_livro)
        self.txt_ano_livro.setObjectName(u"txt_ano_livro")
        self.txt_ano_livro.setStyleSheet(u"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: #EAE0D6;")

        self.verticalLayout_2.addWidget(self.txt_ano_livro)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_adicionar_livro = QPushButton(self.tab_livro)
        self.btn_adicionar_livro.setObjectName(u"btn_adicionar_livro")
        self.btn_adicionar_livro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adicionar_livro.setStyleSheet(u"background-color: rgb(224, 175, 160);\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;")

        self.horizontalLayout_2.addWidget(self.btn_adicionar_livro)

        self.btn_editar_livro = QPushButton(self.tab_livro)
        self.btn_editar_livro.setObjectName(u"btn_editar_livro")
        self.btn_editar_livro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_editar_livro.setStyleSheet(u"background-color: rgb(224, 175, 160);\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;")

        self.horizontalLayout_2.addWidget(self.btn_editar_livro)

        self.btn_remover_livro = QPushButton(self.tab_livro)
        self.btn_remover_livro.setObjectName(u"btn_remover_livro")
        self.btn_remover_livro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remover_livro.setStyleSheet(u"background-color: rgb(224, 175, 160);\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;")

        self.horizontalLayout_2.addWidget(self.btn_remover_livro)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tb_acervo_livro = QTableWidget(self.tab_livro)
        header_tb_acervo_livro = self.tb_acervo_livro.horizontalHeader()
        header_tb_acervo_livro.setSectionResizeMode(QHeaderView.Stretch)
        if (self.tb_acervo_livro.columnCount() < 4):
            self.tb_acervo_livro.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_acervo_livro.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_acervo_livro.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_acervo_livro.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_acervo_livro.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        self.tb_acervo_livro.setObjectName(u"tb_acervo_livro")
        self.tb_acervo_livro.setStyleSheet(u"QTableView {\n"
"background-color: #6ceada3;\n"
"selection-background-color:#EAE0D;\n"
"}\n"
"\n"
"")
        self.tb_acervo_livro.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_acervo_livro.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.tb_acervo_livro)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_livro, "")
        self.tab_usuario = QWidget()
        self.tab_usuario.setObjectName(u"tab_usuario")
        self.verticalLayout_10 = QVBoxLayout(self.tab_usuario)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.tab_usuario)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 16pt \"Calibri\";")

        self.verticalLayout_4.addWidget(self.label_8)

        self.lbl_nome_usuario = QLabel(self.tab_usuario)
        self.lbl_nome_usuario.setObjectName(u"lbl_nome_usuario")
        self.lbl_nome_usuario.setStyleSheet(u"font: 12pt \"Calibri\";")

        self.verticalLayout_4.addWidget(self.lbl_nome_usuario)

        self.txt_nome_usuario = QLineEdit(self.tab_usuario)
        self.txt_nome_usuario.setObjectName(u"txt_nome_usuario")
        self.txt_nome_usuario.setStyleSheet(u"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: #EAE0D6;")

        self.verticalLayout_4.addWidget(self.txt_nome_usuario)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_adicionar_usuario = QPushButton(self.tab_usuario)
        self.btn_adicionar_usuario.setObjectName(u"btn_adicionar_usuario")
        self.btn_adicionar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adicionar_usuario.setStyleSheet(u"background-color: rgb(224, 175, 160);\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;")

        self.horizontalLayout.addWidget(self.btn_adicionar_usuario)

        self.btn_editar_usuario = QPushButton(self.tab_usuario)
        self.btn_editar_usuario.setObjectName(u"btn_editar_usuario")
        self.btn_editar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_editar_usuario.setStyleSheet(u"background-color: rgb(224, 175, 160);\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;")

        self.horizontalLayout.addWidget(self.btn_editar_usuario)

        self.btn_remover_usuario = QPushButton(self.tab_usuario)
        self.btn_remover_usuario.setObjectName(u"btn_remover_usuario")
        self.btn_remover_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remover_usuario.setStyleSheet(u"background-color: rgb(224, 175, 160);\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;")

        self.horizontalLayout.addWidget(self.btn_remover_usuario)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.tb_usuarios = QTableWidget(self.tab_usuario)
        header_tb_usuarios = self.tb_usuarios.horizontalHeader()
        header_tb_usuarios.setSectionResizeMode(QHeaderView.Stretch)
        if (self.tb_usuarios.columnCount() < 2):
            self.tb_usuarios.setColumnCount(2)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_usuarios.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_usuarios.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        self.tb_usuarios.setObjectName(u"tb_usuarios")
        self.tb_usuarios.setStyleSheet(u"QTableView {\n"
"background-color: #6ceada3;\n"
"selection-background-color:#EAE0D;\n"
"}\n"
"\n"
"")

        self.verticalLayout_4.addWidget(self.tb_usuarios)


        self.verticalLayout_10.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.tab_usuario, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 10)

        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 0, 6, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"bibl.io", None))
        self.label_13.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"bibl.io", None))
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_2.setText("")
        self.label_14.setText("")
        self.label_15.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pesquisar:", None))
        self.btn_pesquisar.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Empr\u00e9stimos:", None))
        ___qtablewidgetitem = self.tb_acervo.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem1 = self.tb_acervo.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None));
        ___qtablewidgetitem2 = self.tb_acervo.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Autor", None));
        ___qtablewidgetitem3 = self.tb_acervo.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Data de empr\u00e9stimo", None));
        ___qtablewidgetitem4 = self.tb_acervo.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Data de retorno", None));
        ___qtablewidgetitem5 = self.tb_acervo.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        self.btn_emprestimo.setText(QCoreApplication.translate("MainWindow", u"Empr\u00e9stimo", None))
        self.btn_devolucao.setText(QCoreApplication.translate("MainWindow", u"Devolu\u00e7\u00e3o", None))
        self.btn_reserva.setText(QCoreApplication.translate("MainWindow", u"Reserva", None))
        self.btn_renovacao.setText(QCoreApplication.translate("MainWindow", u"Renova\u00e7\u00e3o", None))
        self.btn_expostar.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_emprestimo), QCoreApplication.translate("MainWindow", u"Empr\u00e9stimo", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Cadastro de livros:", None))
        self.lbl_titulo_livro.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo:", None))
        self.lbl_autor_livro.setText(QCoreApplication.translate("MainWindow", u"Autor:", None))
        self.lbl_ano_livro.setText(QCoreApplication.translate("MainWindow", u"Ano de publica\u00e7\u00e3o:", None))
        self.btn_adicionar_livro.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_editar_livro.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_remover_livro.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        ___qtablewidgetitem6 = self.tb_acervo_livro.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None));
        ___qtablewidgetitem7 = self.tb_acervo_livro.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Autor", None));
        ___qtablewidgetitem8 = self.tb_acervo_livro.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Ano de publica\u00e7\u00e3o", None));
        ___qtablewidgetitem9 = self.tb_acervo_livro.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Resumo", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_livro), QCoreApplication.translate("MainWindow", u"Livro", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Cadastro de usu\u00e1rios:", None))
        self.lbl_nome_usuario.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.btn_adicionar_usuario.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_editar_usuario.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_remover_usuario.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        ___qtablewidgetitem10 = self.tb_usuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem11 = self.tb_usuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_usuario), QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.label_16.setText("")
    # retranslateUi

