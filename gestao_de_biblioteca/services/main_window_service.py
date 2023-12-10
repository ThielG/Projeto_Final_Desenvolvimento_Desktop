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



    def populate_tb_acervo(self, main_window, lista_livros):
        for livro in lista_livros[:]:
            if not livro.ativo:
                lista_livros.remove(livro)

        main_window.tb_acervo_livro.setRowCount(len(lista_livros))
        for linha, livro in enumerate(lista_livros):
            if livro.ativo is True:
                main_window.tb_acervo_emprestimos.setItem(linha, 0, QTableWidgetItem(
                    "Dispovível" if livro.status_disponivel is True else "Emprestado"))
                main_window.tb_acervo_emprestimos.setItem(linha, 1, QTableWidgetItem(livro.titulo))
                main_window.tb_acervo_emprestimos.setItem(linha, 2, QTableWidgetItem(livro.autor))
                main_window.tb_acervo_emprestimos.setItem(linha, 2, QTableWidgetItem(livro.ano))

    def pesquisar_livro(self, main_window):
        tipo_pesquisa = main_window.cb_tipo_pesquisa.currentText()
        if main_window.txt_pesquisa_inicio.text() != "":
            if tipo_pesquisa == "Título":
                lista_livros = self.livro_repository.select_livro_by_titulo(main_window.txt_pesquisa_inicio.text())
            elif tipo_pesquisa == "Ano":
                lista_livros = self.livro_repository.select_livro_by_ano(main_window.txt_pesquisa_inicio.text())
            elif tipo_pesquisa == "Autor":
                lista_livros = self.livro_repository.select_livro_by_autor(main_window.txt_pesquisa_inicio.text())
            else:
                QMessageBox.warning(main_window, 'Pesquisa', 'Tipo de pesquisa inválido.')
                return
        else:
            QMessageBox.warning(main_window, 'Pesquisa', 'Informe um texto de pesquisa e selecione o tipo.')
            return

        self.populate_tb_acervo(main_window, lista_livros)


    def pesquisar_livro_by_titulo(self, main_window):
        if main_window.txt_pesquisa_inicio.text() != "" and main_window.cb_tipo_pesquisa.currentText() == "Título":
            livros = self.livro_repository.select_livro_by_titulo(main_window.txt_pesquisa_inicio.text())

            for livro in livros[:]:
                if not livro.ativo:
                    livros.remove(livro)

            self.populate_tb_acervo(main_window, livros)

    def pesquisar_livro_by_autor(self, main_window):
        if main_window.txt_pesquisa_inicio.text() != "" and main_window.cb_tipo_pesquisa.currentText() == "Autor":
            livros = self.livro_repository.select_livro_by_autor(main_window.txt_pesquisa_inicio.text())

            for livro in livros[:]:
                if not livro.ativo:
                    livros.remove(livro)

            self.populate_tb_acervo(main_window, livros)

    def pesquisar_livro_by_ano(self, main_window):
        if main_window.txt_pesquisa_inicio.text() != "" and main_window.cb_tipo_pesquisa.currentText() == "Ano":
            livros = self.livro_repository.select_livro_by_ano(main_window.txt_pesquisa_inicio.text())

            for livro in livros[:]:
                if not livro.ativo:
                    livros.remove(livro)

            self.populate_tb_acervo(main_window, livros)

    def populate_tb_livro(self, main_window):
        main_window.tb_acervo_livro.setRowCount(0)
        lista_livros = self.livro_repository.select_all_livros()
        for livro in lista_livros[:]:
            if not livro.ativo:
                lista_livros.remove(livro)
        main_window.tb_acervo_livro.setRowCount(len(lista_livros))
        for linha, livro in enumerate(lista_livros):
            if livro.ativo is True:
                main_window.tb_acervo_livro.setItem(linha, 0, QTableWidgetItem(livro.titulo))
                main_window.tb_acervo_livro.setItem(linha, 1, QTableWidgetItem(livro.autor))
                main_window.tb_acervo_livro.setItem(linha, 2, QTableWidgetItem(str(livro.ano)))
                main_window.tb_acervo_livro.setItem(linha, 3, QTableWidgetItem(""))

    def populate_tb_usuarios(self, main_window):
        main_window.tb_usuario.setRowCount(0)
        lista_usuarios = self.usuario_repository.select_all_usuarios()
        for usuario in lista_usuarios[:]:
            if not usuario.ativo:
                lista_usuarios.remove(usuario)
        main_window.tb_usuario.setRowCount(len(lista_usuarios))
        for linha, usuario in enumerate(lista_usuarios):
            if usuario.ativo is True:
                main_window.tb_usuario.setItem(linha, 0, QTableWidgetItem(usuario.cpf))
                main_window.tb_usuario.setItem(linha, 1, QTableWidgetItem(usuario.nome))

    # def populate_relatorio(self, main_window):
    #     main_window.tb_emprestimos.setRowCount(0)
    #     emprestimos = self.emprestimos_repository.select_emprestimos_in_period()
    #     main_window.tb_emprestimos.setRowCount(len(emprestimos))
    #     for linha, (emprestimo, usuario, livro) in enumerate(emprestimos):
    #         main_window.tb_emprestimos.setItem(linha, 0, QTableWidgetItem(livro.titulo))
    #         main_window.tb_emprestimos.setItem(linha, 1, QTableWidgetItem(emprestimo.data_emprestimo))
    #         main_window.tb_emprestimos.setItem(linha, 2, QTableWidgetItem(emprestimo.data_devolucao))
    #         main_window.tb_emprestimos.setItem(linha, 3, QTableWidgetItem(usuario.nome))
    #         main_window.tb_emprestimos.setItem(linha, 4, QTableWidgetItem(livro.autor))


    # def export_relatorio(self, main_window):
    #     #TODO para relatórios será necessário colocar o botão novamente, e validar se a tabela atual da página
    #     # é a tabela de emprestimos ou a de livros(pesquisa)
    #     if main_window.tb_emprestimos.rowCount() > 0:
    #         rows = main_window.tb_emprestimos.rowCount()
    #         cols = main_window.tb_emprestimos.columnCount()
    #         headers = ['Status', 'Título', 'Autor', 'Data de empréstimo', 'Data de retorno', 'Usuário']
    #         data = []
    #         for row in range(rows):
    #             row_data = []
    #             for col in range(cols):
    #                 item = main_window.tb_emprestimos.item(row, col)
    #                 if item and item.text():
    #                     row_data.append(item.text())
    #                 else:
    #                     row_data.append('')
    #             data.append(row_data)
    #         df = pd.DataFrame(data, columns=headers)
    #
    #         try:
    #             df.to_excel(f'relatorio_{datetime.datetime.now()}.xlsx', index=False)
    #             # TODO Talvez o nome do relatório poderá ser alterado
    #             QMessageBox.information(main_window, 'Relatório', f'Relatório de empréstimos exportado com sucesso')
    #         except Exception as e:
    #             QMessageBox.warning(main_window, 'Atenção:', f'Não foi possível exportar o relatório.\nErro: {e}')
