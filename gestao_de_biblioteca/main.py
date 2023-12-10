import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtCore import Signal

from services.main_window_service import MainWindowService
from services.emprestimo_service import EmprestimoService
from services.livro_service import LivroService
from services.usuario_service import UsuarioService

from view.main_ui import Ui_MainWindow
from view.emprestimo_ui import Ui_Dialog


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.service_main_window = MainWindowService()
        self.service_usuario = UsuarioService()
        self.service_main_window.populate_tb_usuarios(self)
        self.service_main_window.populate_tb_livro(self)
        self.service_livro = LivroService()
        self.service_emprestimo = EmprestimoService()

        self.service_main_window.populate_tb_acervo(self)
        self.service_main_window.populate_tb_usuarios(self)
        self.service_main_window.populate_tb_livro(self)
        self.service_main_window.populate_relatorio(self)

        # tela emprestimo
        self.btn_pesquisar.clicked.connect(self.pesquisar_livro)
        self.btn_emprestimo.clicked.connect(self.emprestar_livro)
        self.btn_devolucao.clicked.connect(self.devolver_emprestimo)
        self.btn_renovacao.clicked.connect(self.remover_emprestimo)

        # tela relatorio
        # self.btn_consultar.clicked.connect(self.adicionar_usuario)
        # self.btn_exportar.clicked.connect(self.atualizar_usuario)


        #tela livro
        self.btn_adicionar_livro.clicked.connect(self.adicionar_livro)
        self.btn_editar_livro.clicked.connect(self.atualizar_livro)
        self.btn_remover_livro.clicked.connect(self.remover_livro)

        #tela usuario
        self.btn_adicionar_usuario.clicked.connect(self.adicionar_usuario)
        self.btn_editar_usuario.clicked.connect(self.atualizar_usuario)
        self.btn_remover_usuario.clicked.connect(self.remover_usuario)

    def pesquisar_livro(self):
        self.service_main_window.pesquisar_livro(self)

    def emprestar_livro(self):
        livro = self.service_emprestimo.select_livro_emprestimo(self)
        if livro is not None:
            emprestimo_ui = EmprestimoDialog(self, livro)
            emprestimo_ui.exec_()

    def devolver_emprestimo(self):
        self.service_emprestimo.devolver_emprestimo(self)

    def remover_emprestimo(self):
        self.service_emprestimo.devolver_emprestimo(self)

    def adicionar_livro(self):
        self.service_livro.insert_livro(self)

    def atualizar_livro(self):
        self.service_livro.update_livro(self)

    def remover_livro(self):
        self.service_livro.delete_livro(self)

    def adicionar_usuario(self):
        self.service_usuario.insert_usuario(self)

    def atualizar_usuario(self):
        self.service_usuario.update_usuario(self)

    def remover_usuario(self):
        self.service_usuario.delete_usuario(self)


class EmprestimoDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None, livro=None):
        super(EmprestimoDialog, self).__init__(parent)
        self.selected_usuario = None
        self.livro = livro
        self.setupUi(self)
        self.service_main_window = MainWindowService()
        self.service_usuario = UsuarioService()
        self.service_emprestimo = EmprestimoService()
        self.service_livro = LivroService()
        self.txt_livro_emprestimo.setText(livro.titulo)

        self.btn_consultar_emprestimo.clicked.connect(self.select_usuario)
        self.btn_confirmar_emprestimo.clicked.connect(self.adicionar_emprestimo)

    def select_usuario(self):
        self.service_usuario.select_usuario(self)

    def adicionar_emprestimo(self):
        self.service_emprestimo.adicionar_emprestimo(self, self.livro)
        self.service_main_window.populate_tb_acervo(main_window=MainWindow)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
