import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog

from gestao_de_biblioteca.services.main_window_service import MainWindowService
from services.emprestimo_service import EmprestimoService
from services.livro_service import LivroService
from services.usuario_service import UsuarioService

from view.main_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.service_main_window = MainWindowService()
        
        self.service_usuario = UsuarioService()
        self.service_livro = LivroService()
        self.service_emprestimo = EmprestimoService()
        # self.service_main_window.populate_relatorio(self)
        # self.service_main_window.populate_tb_acervo(self)
        self.service_main_window.populate_tb_livro(self)
        self.service_main_window.populate_tb_usuarios(self)

    def adicionar_usuario(self):
        self.service_usuario.insert_usuario(self)
        
    def atualizar_usuario(self):
        self.service_usuario.update_usuario()

    def remover_usuario(self):
        self.service_usuario.delete_usuario()

    def adicionar_livro(self):
        self.service_livro.insert_livro()

    def atualizar_livro(self):
        self.service_livro.update_livro()

    def remover_livro(self):
        self.service_livro.delete_livro()








if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
