from __future__ import annotations
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from infra.config.base import Base


class Emprestimo(Base):
    __tablename__ = 'emprestimos'

    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"), primary_key=True)
    livro_id: Mapped[int] = mapped_column(ForeignKey("livros.id"), primary_key=True)
    data_emprestimo: Mapped[datetime] = mapped_column(nullable=True)
    data_devolucao: Mapped[datetime] = mapped_column(nullable=True)
    usuarios = relationship("Usuario", back_populates="emprestimos")
    livros = relationship("livro", back_populates="emprestimos")
