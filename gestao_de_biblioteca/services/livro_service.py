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
        livro.ano = main_window.txt_anodePublicacao_livro.text()
        livro.ativo = True
        livro.status_disponivel = True
        try:
            self.livro_repository.insert_one_livro(livro)
            main_window.txt_titulo_livro.setText('')
            main_window.txt_autor_livro.setText('')
            main_window.txt_anodePublicacao_livro.setText('')
            self.main_window_service.populate_tb_livro(main_window)
            QMessageBox.information(main_window, 'Cadastro de livro:', 'Livro cadastrado com sucesso!')
        except Exception as e:
            QMessageBox.warning(main_window, 'Atenção!', f'Problemas ao cadastrar o livro.\nErro: {e}')

    def update_livro(self, main_window):
        if main_window.btn_editar_livro.text() == 'Editar':
            selected_rows = main_window.tb_acervo_livro.selectionModel().selected_rows()
            if not selected_rows:
                QMessageBox.warning(main_window, 'Livro', 'Selecione um livro.')
                return
            selected_rows = selected_rows[0].row()
            main_window.txt_titulo_livro.setText(main_window.tb_acervo_livro.item(selected_rows, 0).text())
            main_window.txt_autor_livro.setText(main_window.tb_acervo_livro.item(selected_rows, 1).text())
            main_window.txt_anodePublicacao_livro.setText(main_window.tb_acervo_livro.item(selected_rows, 2).text())
            main_window.btn_editar_livro.setText('Atualizar')
        else:
            titulo_livro = main_window.txt_titulo_livro.text()
            update_livro = self.livro_repository.select_livro_by_titulo(titulo_livro)
            # TODO Perguntar para o Titione se a atualização de livro usando o parametro "titulo" faz sentido
            update_livro.titulo = main_window.txt_titulo_livro.text()
            update_livro.autor = main_window.txt_autor_livro.text()
            update_livro.ano = main_window.txt_anodePublicacao_livro.text()
            try:
                self.livro_repository.update_livro(update_livro)
                QMessageBox.information(main_window, "Cadastro de livro", "Livro atualizado com sucesso!")
                main_window.btn_editar_livro.setText('Editar')
                main_window.txt_titulo_livro.clear()
                main_window.txt_autor_livro.clear()
                main_window.txt_anodePublicacao_livro.clear()
                self.service_main_window.populate_tb_livro(main_window)
            except Exception as e:
                QMessageBox.warning(main_window, "Atenção", f"Problema ao atualizar livro.\nErro: {e}")


    def delete_livro(self, main_window):
        selected_rows = main_window.tb_acervo_livro.selectionModel().selectedRows()
        if not selected_rows:
            return
        selected_row = selected_rows[0].row()
        delete_livro = self.livro_repository.select_livro_by_titulo(main_window.tb_acervo_livro.item(selected_row, 0).text())
        msg_box = QMessageBox(main_window)
        msg_box.setWindowTitle("Remover livro")
        msg_box.setIcon(QMessageBox.Question)
        yes_button = msg_box.addButton('Sim', QMessageBox.YesRole)
        no_button = msg_box.addButton('Não', QMessageBox.NoRole)
        msg_box.exec()
        if msg_box.clickedButton() == yes_button:
            try:
                self.livro_repository.delete_livro(delete_livro)
                self.main_window_service.populate_tb_livro(main_window)
            except Exception as e:
                QMessageBox.warning(main_window, "Atenção", f"Erro ao remover livro.\nErro: {e}")

