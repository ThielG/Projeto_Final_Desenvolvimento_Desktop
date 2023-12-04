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
    data_fim_reserva:  Mapped[datetime] = mapped_column(nullable=True)
    ativo: Mapped[bool] = mapped_column(nullable=False, default=False)
    usuarios = relationship("Usuario", back_populates="emprestimos")
    livros = relationship("Livro", back_populates="emprestimos")

    @property
    def status_livro(self):
        return self.livro.status if self.livro else None