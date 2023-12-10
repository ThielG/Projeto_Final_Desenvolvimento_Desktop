from PySide6.QtWidgets import QMessageBox
from infra.repository.emprestimo_repository import EmprestimoRepository
from infra.repository.usuario_repository import UsuarioRepository
from infra.repository.livro_repository import LivroRepository
from services.main_window_service import MainWindowService
from .usuario_service import UsuarioService


class EmprestimoService:
    def __init__(self):
        self.service_main_window = MainWindowService()
        self.emprestimo_repository = EmprestimoRepository()
        self.livro_repository = LivroRepository()
        self.usuario_repository = UsuarioRepository()
        self.service_usuario = UsuarioService()

    def select_livro_emprestimo(self, main_window):
        selected_rows = main_window.tb_acervo_emprestimos.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(main_window, 'Livro', 'Selecione um livro.')
            return
        selected_row = selected_rows[0].row()
        if main_window.tb_acervo_emprestimos.item(selected_row, 0).text() == 'Emprestado':
            QMessageBox.warning(main_window, 'Livro', 'Livro indisponível')
            return
        livro_emprestimo = self.livro_repository.select_livro_by_titulo(
            main_window.tb_acervo_emprestimos.item(selected_row, 1).text())
        return livro_emprestimo

    def adicionar_emprestimo(self, emprestimo_ui, livro):
        if emprestimo_ui.selected_usuario is not None:
            selected_usuario = self.service_usuario.select_usuario(emprestimo_ui)
            try:
                self.emprestimo_repository.insert_emprestimo(selected_usuario, livro)
                QMessageBox.information(emprestimo_ui, "Emprestimos", "Empréstimo cadastrado com sucesso!")
            except Exception as e:
                QMessageBox.warning(emprestimo_ui, "Atenção", "Erro ao cadastrar empréstimo!")
        else:
            QMessageBox.warning(emprestimo_ui, "Atenção", "Nenhum funcionario informado!")

    def devolver_emprestimo(self, main_window):
        selected_rows = main_window.tb_acervo_emprestimos.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(main_window, 'Livro', 'Selecione um livro.')
            return
        selected_row = selected_rows[0].row()
        if main_window.tb_acervo_emprestimos.item(selected_row, 0).text() != 'Emprestado':
            QMessageBox.warning(main_window, 'Livro', 'Não há emprestimos deste livro!')
            return
        livro_devolucao = main_window.tb_acervo_emprestimos.item(selected_row, 1).text()
        emprestimo_devolucao = self.emprestimo_repository.select_emprestimo_by_livro(livro_devolucao)
        try:
            self.emprestimo_repository.finalize_emprestimo(emprestimo_devolucao)
            QMessageBox.information(main_window, "Devolução", "Devolução efetuada com sucesso!")
        except Exception as e:
            QMessageBox.warning(main_window, "Atenção", "Erro ao efetuar devolução!")



