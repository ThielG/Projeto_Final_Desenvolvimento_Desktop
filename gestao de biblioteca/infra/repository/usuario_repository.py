from infra.config.connection import DBConnectionHandler
from infra.entities.usuario import Usuario


class UsuarioRepository:

    @staticmethod
    def select_usuario_by_id(id_usuario):
        with DBConnectionHandler() as db:
            usuario = db.session.query(Usuario).filter(Usuario.id == id_usuario).first()
            return usuario

    @staticmethod
    def select_all_usuarios():
        with DBConnectionHandler() as db:
            usuarios = db.session.query(Usuario).all()
            return usuarios

    @staticmethod
    def select_first_usuario():
        with DBConnectionHandler() as db:
            usuario = db.session.query(Usuario).first()
            return usuario

    @staticmethod
    def insert_one_usuario():
        with DBConnectionHandler() as db:
            db.session.add(Usuario)
            db.session.commit()

    @staticmethod
    def update_usuario(usuario):
        with DBConnectionHandler() as db:
            db.session.query(Usuario).filter(Usuario.id == usuario.id).update({'nome': usuario.nome})
            db.session.commit()

    @staticmethod
    def delete_usuario(usuario):
        with DBConnectionHandler() as db:
            db.session.query(Usuario).filter(Usuario.id == usuario.id).update({'ativo': False})
            db.session.commit()
