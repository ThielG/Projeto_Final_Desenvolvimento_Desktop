from PySide6.QtWidgets import QMessageBox

from infra.entities.usuario import Usuario
from infra.repository.emprestimo_repository import EmprestimoRepository
from infra.repository.usuario_repository import UsuarioRepository
from infra.repository.livro_repository import LivroRepository
from services.main_window_service import MainWindowService


class UsuarioService:
    def __init__(self):
        self.service_main_window = MainWindowService()
        self.emprestimo_repository = EmprestimoRepository()
        self.livro_repository = LivroRepository()
        self.usuario_repository = UsuarioRepository()
        self.main_window_service = MainWindowService()

    def insert_usuario(self, main_window):
        usuario = Usuario()
        usuario.nome = main_window.txt_nome_usuario.text()
        usuario.cpf = main_window.txt_cpf_usuario.text()
        usuario.ativo = True
        if main_window.txt_nome_usuario.text() == '':
            QMessageBox.warning(main_window, "Atenção", "Nome inválido.")
        elif main_window.txt_cpf_usuario.text() == '':
            QMessageBox.warning(main_window, "Atenção", "CPF inválido.")
        elif len(main_window.txt_cpf_usuario.text()) != 11:

            QMessageBox.warning(main_window, "Atenção", "CPF incompleto.")

        else:
            try:
                self.usuario_repository.insert_one_usuario(usuario)
                main_window.txt_nome_usuario.setText('')
                main_window.txt_cpf_usuario.setText('')
                main_window.repopulate_all_tables()

                QMessageBox.information(main_window, "Cadastro de usuário", "Usuário cadastrado com sucesso!")
            except Exception as e:
                QMessageBox.warning(main_window, "Atenção", f"Problema ao cadastrar usuário.\n {e}")

    def update_usuario(self, main_window):
        if main_window.btn_editar_usuario.text() == 'Editar':
            selected_rows = main_window.tb_usuario.selectionModel().selectedRows()
            if not selected_rows:
                return
            selected_row = selected_rows[0].row()
            main_window.txt_cpf_usuario.setText(main_window.tb_usuario.item(selected_row, 0).text())
            main_window.txt_nome_usuario.setText(main_window.tb_usuario.item(selected_row, 1).text())
            main_window.txt_cpf_usuario.setReadOnly(True)
            main_window.btn_editar_usuario.setText('Atualizar')
        else:
            cpf_usuario = main_window.txt_cpf_usuario.text()
            usuario_updated = self.usuario_repository.select_usuario_by_cpf(cpf_usuario)
            usuario_updated.nome = main_window.txt_nome_usuario.text()
            if main_window.txt_nome_usuario.text() == '':
                QMessageBox.warning(main_window, "Atenção", "Nome inválido.")
            else:
                try:
                    self.usuario_repository.update_usuario(usuario_updated)
                    QMessageBox.information(main_window, "Cadastro de usuário", "Usuário atualizado com sucesso")
                    main_window.btn_editar_usuario.setText('Editar')
                    main_window.txt_nome_usuario.clear()
                    main_window.txt_cpf_usuario.clear()
                    main_window.repopulate_all_tables()

                except Exception as e:
                    QMessageBox.warning(main_window, "Atenção", f"Problema ao atualizar funcionário.\n{e}")

    def delete_usuario(self, main_window):
        selected_rows = main_window.tb_usuario.selectionModel().selectedRows()
        if not selected_rows:
            return
        selected_row = selected_rows[0].row()
        usuario_delete = self.usuario_repository.select_usuario_by_cpf(main_window.tb_usuario.item(
                                                                        selected_row, 0).text())
        msg_box = QMessageBox(main_window)
        msg_box.setWindowTitle('Remover usuário')
        msg_box.setText(f'Tem certeza de que deseja remover o usuário {usuario_delete.nome}?')
        msg_box.setIcon(QMessageBox.Question)
        yes_button = msg_box.addButton("Sim", QMessageBox.YesRole)
        no_button = msg_box.addButton("No", QMessageBox.NoRole)
        msg_box.exec()
        if msg_box.clickedButton() == yes_button:
            try:
                self.usuario_repository.delete_usuario(usuario_delete)
                main_window.repopulate_all_tables()
            except Exception as e:
                QMessageBox.warning(main_window, "Atenção", "Problema ao remover usuário.\n"f"{e}")

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
                QMessageBox.warning(emprestimo_ui, "Atenção", f"Usuário não encontrado!\n{e}")
                emprestimo_ui.txt_nome_emprestimo.clear()


