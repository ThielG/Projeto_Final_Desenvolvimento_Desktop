from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column, relationship
from infra.config.base import Base


class Livro(Base):
    __tablename__ = "livros"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    autor: Mapped[str] = mapped_column(nullable=False)
    ano: Mapped[int] = mapped_column(nullable=False)
    ativo: Mapped[bool] = mapped_column(default=True, nullable=False)
    status_disponivel: Mapped[bool] = mapped_column(default=True, nullable=False)
    emprestimos = relationship("Emprestimo", back_populates="livro", cascade="save-update")


    def __repr__(self):
        return f'Livro [titulo = {self.titulo}, autor = {self.autor}, ano = {self.ano}]'
        # TODO talvez a função de puxar o resumo do livro deverá ser adicionada nessa parte do código ^
