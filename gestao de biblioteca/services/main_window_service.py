import datetime

import pandas as pd

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox

from infra.repository.emprestimo_repository import EmprestimoRepository
from infra.repository.livro_repository import LivroRepository
from infra.repository.usuario_repository import UsuarioRepository


class MainWindowService:
    def __init__(self):

        self.emprestimos_repository = EmprestimoRepository()
        self.livro_repository = LivroRepository()
        self.usuario_repository = UsuarioRepository()

    def populate_tb_acervo(self, main_window):
        emprestimos = self.emprestimos_repository.select_emprestimos_ativos()
        main_window.tb_acervo.setRowCount(len(emprestimos))
        for linha, (emprestimo, usuario, livro) in enumerate(emprestimos):
            main_window.tb_acervo.setItem(linha, 0, QTableWidgetItem(livro.ativo))
            main_window.tb_acervo.setItem(linha, 1, QTableWidgetItem(livro.titulo))
            main_window.tb_acervo.setItem(linha, 2, QTableWidgetItem(livro.autor))
            main_window.tb_acervo.setItem(linha, 3, QTableWidgetItem(emprestimo.data_emprestimo))
            main_window.tb_acervo.setItem(linha, 4, QTableWidgetItem(emprestimo.data_devolucao))
            main_window.tb_acervo.setItem(linha, 5, QTableWidgetItem(usuario.nome))

    def populate_tb_livro(self, main_window):
        main_window.tb_acervo_livros.setRowCount(0)
        lista_livros = self.livro_repository.select_all_livros()
        for livro in lista_livros[:]:
            if not livro.ativo:
                lista_livros.remove(livro)
        main_window.tb_acervo_livros.setRowCount(len(lista_livros))
        for linha, livro in enumerate(lista_livros):
            if livro.ativo is True:
                main_window.tb_acervo_livros.setItem(linha, 0, QTableWidgetItem(livro.titulo))
                main_window.tb_acervo_livros.setItem(linha, 1, QTableWidgetItem(livro.autor))
                main_window.tb_acervo_livros.setItem(linha, 2, QTableWidgetItem(livro.ano))

    def populate_tb_usuarios(self, main_window):
        main_window.tb_usuarios.setRowCount(0)
        lista_usuarios = self.usuario_repository.select_all_usuarios()
        for usuario in lista_usuarios[:]:
            if not usuario.ativo:
                lista_usuarios.remove(usuario)
        main_window.tb_usuarios.setRowCount(len(lista_usuarios))
        for linha, usuario in enumerate(lista_usuarios):
            if usuario.ativo is True:
                main_window.tb_usuarios.setItem(linha, 0, QTableWidgetItem(usuario.nome))

    def populate_relatorio(self, main_window):
        main_window.tb_acervo.setRowCount(0)
        emprestimos = self.emprestimos_repository.select_emprestimos_ativos()
        # TODO Usei a função "select_emprestimos_ativos" aqui, mas talvez sua aplicação não é correta
        main_window.tb_acervo.setRowCount(len(emprestimos))
        for linha, (emprestimo, usuario, livro) in enumerate(emprestimos):
            main_window.tb_acervo.setItem(linha, 0, QTableWidgetItem(livro.ativo))
            main_window.tb_acervo.setItem(linha, 1, QTableWidgetItem(livro.titulo))
            main_window.tb_acervo.setItem(linha, 2, QTableWidgetItem(livro.autor))
            main_window.tb_acervo.setItem(linha, 3, QTableWidgetItem(emprestimo.data_emprestimo))
            main_window.tb_acervo.setItem(linha, 4, QTableWidgetItem(emprestimo.data_devolucao))
            main_window.tb_acervo.setItem(linha, 5, QTableWidgetItem(usuario.nome))

    def export_relatorio(self, main_window):
        if main_window.tb_acervo.rowCount() > 0:
            rows = main_window.tb_acervo.rowCount()
            cols = main_window.tb_acervo.columnCount()
            headers = ['Status', 'Título', 'Autor', 'Data de empréstimo', 'Data de retorno', 'Usuário']
            data = []
            for row in range(rows):
                row_data = []
                for col in range(cols):
                    item = main_window.tb_acervo.item(row, col)
                    if item and item.text():
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                data.append(row_data)
            df = pd.DataFrame(data, columns=headers)

            try:
                df.to_excel(f'relatorio_{datetime.datetime.now()}.xlsx', index=False)
                # TODO Talvez o nome do relatório poderá ser alterado
                QMessageBox.information(main_window, 'Relatório', f'Relatório de empréstimos exportado com sucesso')
            except Exception as e:
                QMessageBox.warning(main_window, 'Atenção:', f'Não foi possível exportar o relatório.\nErro: {e}')
