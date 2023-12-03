from PySide6.QtWidgets import QMessageBox

from infra.entities.livro import Livro
from infra.repository.emprestimo_repository import EmprestimoRepository
from infra.repository.usuario_repository import UsuarioRepository
from infra.repository.livro_repository import LivroRepository
from services.main_window_service import MainWindowService


class LivroService:
    def __init__(self):
        self.service_main_window = MainWindowService()
        self.emprestimo_repository = EmprestimoRepository()
        self.livro_repository = LivroRepository()
        self.usuario_repository = UsuarioRepository()
        self.main_window_service = MainWindowService()

    def insert_livro(self, main_window):
        livro = Livro()
        livro.titulo = main_window.txt_titulo_livro.text()
        livro.autor = main_window.txt_autor_livro.text()
        livro.ano = main_window.txt_ano_livro.text()
        livro.ativo = True
        try:
            self.livro_repository.insert_one_livro(livro)
            main_window.txt_titulo_livro.setText('')
            main_window.txt_autor_livro.setText('')
            main_window.txt_ano_livro.setText('')
            self.main_window_service.populate_tb_livro(main_window)
            QMessageBox.information(main_window, 'Cadastro de livro:', 'Livro cadastrado com sucesso!')
        except Exception as e:
            QMessageBox.warning(main_window, 'Atenção!', f'Problemas ao cadastrar o livro.\nErro: {e}')


'''
    def select_livro(self, main):
'''
# TODO Parei aqui ^
