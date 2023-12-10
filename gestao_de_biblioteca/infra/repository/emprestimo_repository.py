from datetime import datetime, timedelta
from sqlalchemy.orm import joinedload

from infra.config.connection import DBConnectionHandler
from infra.entities.usuario import Usuario
from infra.entities.livro import Livro
from infra.entities.emprestimo import Emprestimo
from infra.repository.livro_repository import LivroRepository


class EmprestimoRepository:

    @staticmethod
    def insert_emprestimo(usuario, livro):
        with DBConnectionHandler() as db:
            emp = Emprestimo()
            emp.livro_id = livro.id
            emp.usuario_id = usuario.id
            today = datetime.now()
            emp.data_emprestimo = today
            emp.data_devolucao = today + timedelta(days=7)
            emp.ativo = True
            livro.status_disponivel = False
            try:
                db.session.add(emp)
                db.session.commit()
            except Exception as e:
                print(f'Erro: {e}')

    @staticmethod
    def finalize_emprestimo(emprestimo):
        livro = emprestimo.livro
        usuario = emprestimo.usuario
        with DBConnectionHandler() as db:
            today = datetime.now()
            try:
                db.session.query(Emprestimo).filter(Emprestimo.livro_id == livro.id,
                                                    Emprestimo.usuario_id == usuario.id,
                                                    ).update({'data_devolucao': today,
                                                              'ativo': False})
                db.session.query(Livro).filter(Livro.id == livro.id).update({'status_disponivel': True})
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
    def select_emprestimos_in_period(begin_date, end_date):
        try:
            begin_date = datetime.strptime(begin_date, '%d/%m/Y')
            end_date = datetime.strptime(end_date, '%d/%m/%Y')
            end_date = end_date.replace(hour=23, minute=59, second=59)
            with DBConnectionHandler() as db:
                emprestimos = (
                    db.session.query(Emprestimo, Usuario, Livro)
                    .join(Usuario, Usuario.id == Emprestimo.usuario_id)
                    .join(Livro, Livro.id == Emprestimo.livro_id)
                    .filter(
                        Emprestimo.data_emprestimo.between(begin_date, end_date)
                    ).options(
                        joinedload(Emprestimo.usuario),
                        joinedload(Emprestimo.livro)
                    )
                    .all()
                )
                return emprestimos
        except Exception as e:
            print(e)
    @staticmethod
    def select_emprestimo_by_livro(livro):
        with DBConnectionHandler() as db:
            emprestimo = db.session.query(Emprestimo).filter(Emprestimo.livro_id == livro.id).first()
            return emprestimo


    @staticmethod
    def select_emprestimos_ativos():
        with DBConnectionHandler as db:
            emprestimos = (
                db.session.query(Emprestimo, Usuario, Livro).join(Usuario, Usuario.id == Emprestimo.usuario_id)
                .join(Livro, Livro.id == Emprestimo.livro_id).filter(Emprestimo.ativo._is(True)).all())
            return emprestimos


    @staticmethod
    def delete_emprestimo(data):
        with DBConnectionHandler() as db:
            db.session.delete(data)
            db.session.commit()
