from __future__ import annotations

from sqlalchemy.orm import relationship, Mapped, mapped_column

from infra.config.base import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    ativo: Mapped[bool] = mapped_column(default=True, nullable=False)
    emprestimos = relationship("Emprestimo", back_populates="usuarios", cascade="save-update")

    def __repr__(self):
        return f'Usuario [nome = {self.nome}]'
