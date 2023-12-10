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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Bibl.io")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u"view/pilha.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(234, 224, 213)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"image: url(view/pilha.png)")

        self.horizontalLayout_6.addWidget(self.widget)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_titulo_app = QLabel(self.centralwidget)
        self.lbl_titulo_app.setObjectName(u"lbl_titulo_app")
        font = QFont()
        font.setFamilies([u"Georgia"])
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(False)
        self.lbl_titulo_app.setFont(font)
        self.lbl_titulo_app.setStyleSheet(u"font: 48pt \"Georgia\";\n"
"color: #100907;")

        self.horizontalLayout_5.addWidget(self.lbl_titulo_app)

        self.verticalSpacer_2 = QSpacerItem(17, 71, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.horizontalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

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
        self.lbl_pesquisar = QLabel(self.tab_emprestimo)
        self.lbl_pesquisar.setObjectName(u"lbl_pesquisar")
        self.lbl_pesquisar.setStyleSheet(u"font: 16pt \"Calibri\";")

        self.verticalLayout_7.addWidget(self.lbl_pesquisar)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.txt_pesquisa_inicio = QLineEdit(self.tab_emprestimo)
        self.txt_pesquisa_inicio.setObjectName(u"txt_pesquisa_inicio")
        self.txt_pesquisa_inicio.setStyleSheet(u"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: #EAE0D6;")

        self.horizontalLayout_7.addWidget(self.txt_pesquisa_inicio)

        self.cb_tipo_pesquisa = QComboBox(self.tab_emprestimo)
        self.cb_tipo_pesquisa.addItem("")
        self.cb_tipo_pesquisa.addItem("")
        self.cb_tipo_pesquisa.addItem("")
        self.cb_tipo_pesquisa.setObjectName(u"cb_tipo_pesquisa")
        self.cb_tipo_pesquisa.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_tipo_pesquisa.setStyleSheet(u"QComboBox {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    min-width: 6em;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"     background:#EAE0D6;\n"
"}\n"
"\n"
"/* QComboBox gets the \"on\" state when the popup is open */\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background: #EAE0D6;\n"
"}\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 1px;\n"
"    border-left-color: #e0afa0;\n"
"    border-left-style: solid; /* just a single line */\n"
"    border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(view/down.png);\n"
"	ma"
                        "x-width: 22px;\n"
"	\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")

        self.horizontalLayout_7.addWidget(self.cb_tipo_pesquisa)

        self.btn_pesquisar = QPushButton(self.tab_emprestimo)
        self.btn_pesquisar.setObjectName(u"btn_pesquisar")
        self.btn_pesquisar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_pesquisar.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_7.addWidget(self.btn_pesquisar)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.lbl_obras = QLabel(self.tab_emprestimo)
        self.lbl_obras.setObjectName(u"lbl_obras")
        self.lbl_obras.setStyleSheet(u"font: 16pt \"Calibri\";")

        self.verticalLayout_7.addWidget(self.lbl_obras)

        self.tb_acervo_emprestimos = QTableWidget(self.tab_emprestimo)
        header_acervo_emprestimos = self.tb_acervo_emprestimos.horizontalHeader()
        header_acervo_emprestimos.setSectionResizeMode(QHeaderView.Stretch)
        self.tb_acervo_emprestimos.verticalHeader().hide()
        self.tb_acervo_emprestimos.setSelectionBehavior(QTableWidget.SelectRows)
        self.tb_acervo_emprestimos.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tb_acervo_emprestimos.setSelectionMode(QAbstractItemView.SingleSelection)

        if (self.tb_acervo_emprestimos.columnCount() < 4):
            self.tb_acervo_emprestimos.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_acervo_emprestimos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_acervo_emprestimos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_acervo_emprestimos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_acervo_emprestimos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tb_acervo_emprestimos.setObjectName(u"tb_acervo_emprestimos")
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(12)
        self.tb_acervo_emprestimos.setFont(font1)
        self.tb_acervo_emprestimos.setStyleSheet(u"QTableView {\n"
"background-color: #6ceada3;\n"
"selection-background-color:#EAE0D;\n"
"}\n"
"\n"
"")

        self.verticalLayout_7.addWidget(self.tb_acervo_emprestimos)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_emprestimo = QPushButton(self.tab_emprestimo)
        self.btn_emprestimo.setObjectName(u"btn_emprestimo")
        self.btn_emprestimo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_emprestimo.setStyleSheet(u"QPushButton {\n"
"background-color: #e0afa0;\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  #ca9e90;\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_emprestimo)

        self.btn_devolucao = QPushButton(self.tab_emprestimo)
        self.btn_devolucao.setObjectName(u"btn_devolucao")
        self.btn_devolucao.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_devolucao.setStyleSheet(u"QPushButton {\n"
"background-color: #e0afa0;\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  #ca9e90;\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_devolucao)

        self.btn_renovacao = QPushButton(self.tab_emprestimo)
        self.btn_renovacao.setObjectName(u"btn_renovacao")
        self.btn_renovacao.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_renovacao.setStyleSheet(u"QPushButton {\n"
"background-color: #e0afa0;\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  #ca9e90;\n"
"}")

        self.horizontalLayout_4.addWidget(self.btn_renovacao)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)


        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.tabWidget.addTab(self.tab_emprestimo, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_4 = QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_data_inicial = QLabel(self.tab)
        self.lbl_data_inicial.setObjectName(u"lbl_data_inicial")
        self.lbl_data_inicial.setStyleSheet(u"font: 12pt \"Calibri\";")

        self.horizontalLayout_9.addWidget(self.lbl_data_inicial)

        self.txt_data_inicial = QLineEdit(self.tab)
        self.txt_data_inicial.setObjectName(u"txt_data_inicial")
        self.txt_data_inicial.setStyleSheet(u"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: #EAE0D6;\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_9.addWidget(self.txt_data_inicial)

        self.lbl_data_final = QLabel(self.tab)
        self.lbl_data_final.setObjectName(u"lbl_data_final")
        self.lbl_data_final.setStyleSheet(u"font: 12pt \"Calibri\";")

        self.horizontalLayout_9.addWidget(self.lbl_data_final)

        self.txt_data_final = QLineEdit(self.tab)
        self.txt_data_final.setObjectName(u"txt_data_final")
        self.txt_data_final.setStyleSheet(u"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: #EAE0D6;\n"
"font: 12pt \"Calibri\";")

        self.horizontalLayout_9.addWidget(self.txt_data_final)

        self.btn_consultar = QPushButton(self.tab)
        self.btn_consultar.setObjectName(u"btn_consultar")
        self.btn_consultar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_consultar.setStyleSheet(u"background-color: rgb(224, 175, 160);\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 5px;")

        self.horizontalLayout_9.addWidget(self.btn_consultar)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.lbl_emprestimos = QLabel(self.tab)
        self.lbl_emprestimos.setObjectName(u"lbl_emprestimos")
        self.lbl_emprestimos.setStyleSheet(u"font: 16pt \"Calibri\";")

        self.verticalLayout_3.addWidget(self.lbl_emprestimos)

        self.tb_emprestimos = QTableWidget(self.tab)
        header_emprestimos = self.tb_emprestimos.horizontalHeader()
        header_emprestimos.setSectionResizeMode(QHeaderView.Stretch)
        self.tb_emprestimos.verticalHeader().hide()
        self.tb_emprestimos.setSelectionBehavior(QTableWidget.SelectRows)
        self.tb_emprestimos.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tb_emprestimos.setSelectionMode(QAbstractItemView.SingleSelection)

        if (self.tb_emprestimos.columnCount() < 5):
            self.tb_emprestimos.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_emprestimos.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_emprestimos.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_emprestimos.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_emprestimos.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_emprestimos.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.tb_emprestimos.setObjectName(u"tb_emprestimos")
        self.tb_emprestimos.setFont(font1)
        self.tb_emprestimos.setStyleSheet(u"QTableView {\n"
"background-color: #6ceada3;\n"
"selection-background-color:#EAE0D;\n"
"}\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.tb_emprestimos)

        self.btn_exportar = QPushButton(self.tab)
        self.btn_exportar.setObjectName(u"btn_exportar")
        self.btn_exportar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exportar.setStyleSheet(u"\n"
"QPushButton {\n"
"background-color: #e0afa0;\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;\n"
"margin: 0 150px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  #ca9e90;\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_exportar)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.tab, "")
        self.tab_livro = QWidget()
        self.tab_livro.setObjectName(u"tab_livro")
        self.verticalLayout_9 = QVBoxLayout(self.tab_livro)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_cadastro_livros = QLabel(self.tab_livro)
        self.lbl_cadastro_livros.setObjectName(u"lbl_cadastro_livros")
        self.lbl_cadastro_livros.setStyleSheet(u"font: 16pt \"Calibri\";")

        self.verticalLayout_2.addWidget(self.lbl_cadastro_livros)

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

        self.txt_anodePublicacao_livro = QLineEdit(self.tab_livro)
        self.txt_anodePublicacao_livro.setObjectName(u"txt_anodePublicacao_livro")
        self.txt_anodePublicacao_livro.setStyleSheet(u"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: #EAE0D6;")

        self.verticalLayout_2.addWidget(self.txt_anodePublicacao_livro)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_adicionar_livro = QPushButton(self.tab_livro)
        self.btn_adicionar_livro.setObjectName(u"btn_adicionar_livro")
        self.btn_adicionar_livro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adicionar_livro.setStyleSheet(u"QPushButton {\n"
"background-color: #e0afa0;\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  #ca9e90;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_adicionar_livro)

        self.btn_editar_livro = QPushButton(self.tab_livro)
        self.btn_editar_livro.setObjectName(u"btn_editar_livro")
        self.btn_editar_livro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_editar_livro.setStyleSheet(u"QPushButton {\n"
"background-color: #e0afa0;\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  #ca9e90;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_editar_livro)

        self.btn_remover_livro = QPushButton(self.tab_livro)
        self.btn_remover_livro.setObjectName(u"btn_remover_livro")
        self.btn_remover_livro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remover_livro.setStyleSheet(u"QPushButton {\n"
"background-color: #e0afa0;\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  #ca9e90;\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_remover_livro)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.tb_acervo_livro = QTableWidget(self.tab_livro)
        header_acervo_livro = self.tb_acervo_livro.horizontalHeader()
        header_acervo_livro.setSectionResizeMode(QHeaderView.Stretch)
        self.tb_acervo_livro.verticalHeader().hide()
        self.tb_acervo_livro.setSelectionBehavior(QTableWidget.SelectRows)
        self.tb_acervo_livro.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tb_acervo_livro.setSelectionMode(QAbstractItemView.SingleSelection)

        if (self.tb_acervo_livro.columnCount() < 4):
            self.tb_acervo_livro.setColumnCount(4)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_acervo_livro.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_acervo_livro.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_acervo_livro.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_acervo_livro.setHorizontalHeaderItem(3, __qtablewidgetitem12)
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


        self.verticalLayout_9.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tab_livro, "")
        self.tab_usuario = QWidget()
        self.tab_usuario.setObjectName(u"tab_usuario")
        self.horizontalLayout_8 = QHBoxLayout(self.tab_usuario)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_cadastro_usuario = QLabel(self.tab_usuario)
        self.lbl_cadastro_usuario.setObjectName(u"lbl_cadastro_usuario")
        self.lbl_cadastro_usuario.setStyleSheet(u"font: 16pt \"Calibri\";")

        self.verticalLayout.addWidget(self.lbl_cadastro_usuario)

        self.lbl_nome_usuario = QLabel(self.tab_usuario)
        self.lbl_nome_usuario.setObjectName(u"lbl_nome_usuario")
        self.lbl_nome_usuario.setStyleSheet(u"font: 12pt \"Calibri\";")

        self.verticalLayout.addWidget(self.lbl_nome_usuario)

        self.txt_nome_usuario = QLineEdit(self.tab_usuario)
        self.txt_nome_usuario.setObjectName(u"txt_nome_usuario")
        self.txt_nome_usuario.setStyleSheet(u"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: #EAE0D6;")

        self.verticalLayout.addWidget(self.txt_nome_usuario)

        self.lbl_cpf_usuario = QLabel(self.tab_usuario)
        self.lbl_cpf_usuario.setObjectName(u"lbl_cpf_usuario")
        self.lbl_cpf_usuario.setStyleSheet(u"font: 12pt \"Calibri\";")

        self.verticalLayout.addWidget(self.lbl_cpf_usuario)

        self.txt_cpf_usuario = QLineEdit(self.tab_usuario)
        self.txt_cpf_usuario.setObjectName(u"txt_cpf_usuario")
        #self.txt_cpf_usuario.setInputMask("000.000.000-00")
        self.txt_cpf_usuario.setStyleSheet(u"padding: 5px;\n"
"border-radius: 5px;\n"
"background-color: #EAE0D6;")

        self.verticalLayout.addWidget(self.txt_cpf_usuario)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_adicionar_usuario = QPushButton(self.tab_usuario)
        self.btn_adicionar_usuario.setObjectName(u"btn_adicionar_usuario")
        self.btn_adicionar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_adicionar_usuario.setStyleSheet(u"QPushButton {\n"
"background-color: #e0afa0;\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  #ca9e90;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_adicionar_usuario)

        self.btn_editar_usuario = QPushButton(self.tab_usuario)
        self.btn_editar_usuario.setObjectName(u"btn_editar_usuario")
        self.btn_editar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_editar_usuario.setStyleSheet(u"QPushButton {\n"
"background-color: #e0afa0;\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  #ca9e90;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_editar_usuario)

        self.btn_remover_usuario = QPushButton(self.tab_usuario)
        self.btn_remover_usuario.setObjectName(u"btn_remover_usuario")
        self.btn_remover_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_remover_usuario.setStyleSheet(u"QPushButton {\n"
"background-color: #e0afa0;\n"
"font: 12pt \"Calibri\";\n"
"border: none;\n"
"border-radius: 5px;\n"
"padding: 7px 0;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color:  #ca9e90;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_remover_usuario)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tb_usuario = QTableWidget(self.tab_usuario)
        header_usuario = self.tb_usuario.horizontalHeader()
        header_usuario.setSectionResizeMode(QHeaderView.Stretch)
        self.tb_usuario.verticalHeader().hide()
        self.tb_usuario.setSelectionBehavior(QTableWidget.SelectRows)
        self.tb_usuario.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tb_usuario.setSelectionMode(QAbstractItemView.SingleSelection)

        if (self.tb_usuario.columnCount() < 2):
            self.tb_usuario.setColumnCount(2)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_usuario.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_usuario.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        self.tb_usuario.setObjectName(u"tb_usuario")
        self.tb_usuario.setStyleSheet(u"QTableView {\n"
"background-color: #6ceada3;\n"
"selection-background-color:#EAE0D;\n"
"}\n"
"\n"
"")

        self.verticalLayout.addWidget(self.tb_usuario)


        self.horizontalLayout_8.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab_usuario, "")

        self.verticalLayout_5.addWidget(self.tabWidget)


        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("bibl.io", u"bibl.io", None))
        self.lbl_titulo_app.setText(QCoreApplication.translate("MainWindow", u"bibl.io", None))
        self.lbl_pesquisar.setText(QCoreApplication.translate("MainWindow", u"Pesquisar:", None))
        self.cb_tipo_pesquisa.setItemText(0, QCoreApplication.translate("MainWindow", u"T\u00edtulo", None))
        self.cb_tipo_pesquisa.setItemText(1, QCoreApplication.translate("MainWindow", u"Autor", None))
        self.cb_tipo_pesquisa.setItemText(2, QCoreApplication.translate("MainWindow", u"Ano de publica\u00e7\u00e3o", None))

        self.btn_pesquisar.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.lbl_obras.setText(QCoreApplication.translate("MainWindow", u"Obras:", None))
        ___qtablewidgetitem = self.tb_acervo_emprestimos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem1 = self.tb_acervo_emprestimos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None));
        ___qtablewidgetitem2 = self.tb_acervo_emprestimos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Autor", None));
        ___qtablewidgetitem3 = self.tb_acervo_emprestimos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Ano", None));
        self.btn_emprestimo.setText(QCoreApplication.translate("MainWindow", u"Empr\u00e9stimo", None))
        self.btn_devolucao.setText(QCoreApplication.translate("MainWindow", u"Devolu\u00e7\u00e3o", None))
        self.btn_renovacao.setText(QCoreApplication.translate("MainWindow", u"Renova\u00e7\u00e3o", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_emprestimo), QCoreApplication.translate("MainWindow", u"Empr\u00e9stimo", None))
        self.lbl_data_inicial.setText(QCoreApplication.translate("MainWindow", u"Data Inicial:", None))
        self.txt_data_inicial.setText("")
        self.lbl_data_final.setText(QCoreApplication.translate("MainWindow", u"Data Final:", None))
        self.txt_data_final.setText("")
        self.btn_consultar.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.lbl_emprestimos.setText(QCoreApplication.translate("MainWindow", u"Empr\u00e9stimos:", None))
        ___qtablewidgetitem4 = self.tb_emprestimos.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None));
        ___qtablewidgetitem5 = self.tb_emprestimos.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Data de empr\u00e9stimo", None));
        ___qtablewidgetitem6 = self.tb_emprestimos.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Data de retorno", None));
        ___qtablewidgetitem7 = self.tb_emprestimos.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None));
        ___qtablewidgetitem8 = self.tb_emprestimos.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Autor", None));
        self.btn_exportar.setText(QCoreApplication.translate("MainWindow", u"Exportar relat\u00f3rio", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Relat\u00f3rio", None))
        self.lbl_cadastro_livros.setText(QCoreApplication.translate("MainWindow", u"Livros", None))
        self.lbl_titulo_livro.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo:", None))
        self.lbl_autor_livro.setText(QCoreApplication.translate("MainWindow", u"Autor:", None))
        self.lbl_ano_livro.setText(QCoreApplication.translate("MainWindow", u"Ano de publica\u00e7\u00e3o:", None))
        self.btn_adicionar_livro.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_editar_livro.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_remover_livro.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        ___qtablewidgetitem9 = self.tb_acervo_livro.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"T\u00edtulo", None));
        ___qtablewidgetitem10 = self.tb_acervo_livro.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Autor", None));
        ___qtablewidgetitem11 = self.tb_acervo_livro.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Ano de publica\u00e7\u00e3o", None));
        ___qtablewidgetitem12 = self.tb_acervo_livro.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Resumo", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_livro), QCoreApplication.translate("MainWindow", u"Livro", None))
        self.lbl_cadastro_usuario.setText(QCoreApplication.translate("MainWindow", u"Cadastro de usu\u00e1rios:", None))
        self.lbl_nome_usuario.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.lbl_cpf_usuario.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.btn_adicionar_usuario.setText(QCoreApplication.translate("MainWindow", u"Adicionar", None))
        self.btn_editar_usuario.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btn_remover_usuario.setText(QCoreApplication.translate("MainWindow", u"Remover", None))
        ___qtablewidgetitem13 = self.tb_usuario.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem14 = self.tb_usuario.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_usuario), QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
    # retranslateUi

