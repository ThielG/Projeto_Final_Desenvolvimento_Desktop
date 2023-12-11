from PySide6.QtWidgets import QMessageBox
from datetime import datetime
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
        if livro.status_disponivel:
            if emprestimo_ui.selected_usuario is not None:
                try:
                    self.emprestimo_repository.insert_emprestimo(emprestimo_ui.selected_usuario, livro)
                    QMessageBox.information(emprestimo_ui, "Emprestimos", "Empréstimo cadastrado com sucesso!")
                    emprestimo_ui.parent().repopulate_all_tables()
                except Exception as e:
                    QMessageBox.warning(emprestimo_ui, "Atenção", "Erro ao cadastrar empréstimo!")
            else:
                QMessageBox.warning(emprestimo_ui, "Atenção", "Nenhum usuário informado!")
        else:
            QMessageBox.warning(emprestimo_ui, "Atenção", "Livro indisponível.")

    def devolver_emprestimo(self, main_window):
        selected_rows = main_window.tb_acervo_emprestimos.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(main_window, 'Livro', 'Selecione um livro.')
            return
        selected_row = selected_rows[0].row()
        if main_window.tb_acervo_emprestimos.item(selected_row, 0).text() != 'Emprestado':
            QMessageBox.warning(main_window, 'Livro', 'Não há emprestimos deste livro!')
            return
        livro_titulo = main_window.tb_acervo_emprestimos.item(selected_row, 1).text()
        livro_devolucao = self.livro_repository.select_livro_by_titulo(livro_titulo)
        emprestimo_devolucao = self.emprestimo_repository.select_one_emprestimo(livro_devolucao)
        dias_atraso = max((datetime.now() - emprestimo_devolucao.data_devolucao).days, 0)

        try:
            self.emprestimo_repository.finalize_emprestimo(emprestimo_devolucao)
            QMessageBox.information(main_window, "Devolução", f"Devolução efetuada com sucesso! Dias de atraso: {dias_atraso}")
            main_window.repopulate_all_tables()
        except Exception as e:
            QMessageBox.warning(main_window, "Atenção", f"Erro ao efetuar devolução! Erro: {e}")

    def renovar_emprestimo(self, main_window):
        selected_rows = main_window.tb_acervo_emprestimos.selectionModel().selectedRows()
        if not selected_rows:
            QMessageBox.warning(main_window, 'Livro', 'Selecione um livro.')
            return
        selected_row = selected_rows[0].row()
        if main_window.tb_acervo_emprestimos.item(selected_row, 0).text() != 'Emprestado':
            QMessageBox.warning(main_window, 'Livro', 'Não há emprestimos deste livro!')
            return
        livro_titulo = main_window.tb_acervo_emprestimos.item(selected_row, 1).text()
        livro_renovacao = self.livro_repository.select_livro_by_titulo(livro_titulo)
        emprestimo_renovacao = self.emprestimo_repository.select_one_emprestimo(livro_renovacao)
        dias_atraso = max((datetime.now() - emprestimo_renovacao.data_devolucao).days, 0)

        if dias_atraso > 0:
            QMessageBox.warning(main_window, 'Livro', 'Não é possível renovar livro.\nEmpréstimo em atraso')
        else:
            self.emprestimo_repository.update_emprestimo(emprestimo_renovacao)
            QMessageBox.information(main_window, 'Livro', 'Empréstimo renovado com sucesso!')



    def select_usuario(self, emprestimo_ui):
        if emprestimo_ui.btn_consultar_emprestimo.text() == 'Limpar':
            emprestimo_ui.txt_nome_emprestimo.clear()
            emprestimo_ui.txt_cpf_emprestimo.clear()
            emprestimo_ui.selected_usuario = None
            emprestimo_ui.btn_consultar_emprestimo.setText('Consultar')
        else:
            try:
                usuario_emprestimo = self.usuario_repository.select_usuario_by_cpf(emprestimo_ui.
                                                                                   txt_cpf_emprestimo.
                                                                                   text())
                if emprestimo_ui.txt_cpf_emprestimo.text() != '':
                    emprestimo_ui.txt_nome_emprestimo.setText(usuario_emprestimo.nome)
                    emprestimo_ui.selected_usuario = usuario_emprestimo
                    emprestimo_ui.txt_nome_emprestimo.setReadOnly(True)
                    emprestimo_ui.btn_consultar_emprestimo.setText('Limpar')
                else:
                    QMessageBox.warning(emprestimo_ui, "Atenção", "Digite um CPF para consulta!")
            except Exception as e:
                QMessageBox.warning(emprestimo_ui, "Atenção", "Usuário não encontrado!")
                emprestimo_ui.txt_nome_emprestimo.clear()

