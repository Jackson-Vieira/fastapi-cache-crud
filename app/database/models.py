from uuid import uuid4, UUID
from sqlmodel import Field, SQLModel
from typing import List


class PessoaBase(SQLModel):
    apelido: str = Field(max_length=32, unique=True)
    nome: str = Field(max_length=100)
    nascimento: str = Field(max_length=10)
    stack: List[str] = Field(default=None)


class Pessoa(PessoaBase, table=True):
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )

    __tablename__ = "pessoas"
