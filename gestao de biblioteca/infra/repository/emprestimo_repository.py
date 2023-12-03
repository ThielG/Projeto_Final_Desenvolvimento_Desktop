from datetime import datetime
from sqlalchemy.orm import joinedload

from infra.config.connection import DBConnectionHandler
from infra.entities.usuario import Usuario
from infra.entities.livro import Livro
from infra.entities.emprestimo import Emprestimo


class EmprestimoRepository:

    @staticmethod
    def insert_emprestimo(usuario, livro):
        with DBConnectionHandler() as db:
            emp = Emprestimo()
            emp.livro_id = livro.id
            emp.usuario_id = usuario.id
            today = datetime.now()
            emp.data_emprestimo = today
            try:
                db.session.add(emp)
                db.session.commit()
            except Exception as e:
                print(f'Erro: {e}')

    @staticmethod
    def finalize_emprestimo(usuario, livro):
        with DBConnectionHandler() as db:
            today = datetime.now()
            try:
                db.session.query(Emprestimo).filter(Emprestimo.livro_id == livro.id,
                                                    Emprestimo.usuario_id == usuario.id,
                                                    ).update({'data_devolucao': today})
                db.session.commit()
            except Exception as e:
                print(f'Erro: {e}')

    @staticmethod
    def select_all_emprestimos():
        with DBConnectionHandler() as db:
            emprestimos = db.session.query(Emprestimo).options(joinedload(Emprestimo.usuarios),
                                                               joinedload(Emprestimo.livros)).all()
            return emprestimos

    @staticmethod
    # TODO Talvez a função "select_emprestimos_ativos" não faça sentido na lógica que estamos aplicando
    def select_emprestimos_ativos():
        with DBConnectionHandler as db:
            emprestimos = (db.session.query(Emprestimo, Usuario, Livro).join(Usuario, Usuario.id == Emprestimo.usuario_id)
                           .join(Livro, Livro.id == Emprestimo.livro_id).filter(Emprestimo.data_devolucao.is_(None)).all())
            return emprestimos

    @staticmethod
    def delete_emprestimo(data):
        with DBConnectionHandler() as db:
            db.session.delete(data)
            db.session.commit()
