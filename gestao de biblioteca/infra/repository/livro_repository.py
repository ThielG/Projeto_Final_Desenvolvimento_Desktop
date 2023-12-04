from infra.config.connection import DBConnectionHandler
from infra.entities.livro import Livro


class LivroRepository:

    @staticmethod
    def select_livro_by_id(id_livro):
        with DBConnectionHandler() as db:
            livro = db.session.query(Livro).filter(Livro.id == id_livro).first()
            return livro

    @staticmethod
    def select_livro_by_titulo(titulo_livro):
        with DBConnectionHandler() as db:
            livro = db.session.query(Livro).filter(Livro.titulo == titulo_livro).first()
            return livro

    @staticmethod
    def select_livro_by_autor(autor_livro):
        with DBConnectionHandler() as db:
            livro = db.session.query(Livro).filter(Livro.autor == autor_livro).first()
            return livro

    @staticmethod
    def select_livro_by_ano(ano_livro):
        with DBConnectionHandler() as db:
            livro = db.session.query(Livro).filter(Livro.ano == ano_livro).first()
            return livro

    @staticmethod
    def select_all_livros():
        with DBConnectionHandler() as db:
            livro = db.session.query(Livro).all()
            return livro

    @staticmethod
    def select_first_livro():
        with DBConnectionHandler() as db:
            livro = db.session.query(Livro).first()
            return livro

    @staticmethod
    def insert_one_livro(livro):
        with DBConnectionHandler() as db:
            db.session.add(livro)
            db.session.commit()

    @staticmethod
    def update_livro(livro):
        with DBConnectionHandler() as db:
            db.session.query(Livro).filter(Livro.id == livro.id).update({'titulo': livro.titulo, 'autor': livro.autor, 'ano': livro.ano})
            db.session.commit()

    @staticmethod
    def delete_livro(livro):
        with DBConnectionHandler() as db:
            db.session.query(Livro).filter(Livro.id == livro.id).update({'ativo': False})
            db.session.commit()
