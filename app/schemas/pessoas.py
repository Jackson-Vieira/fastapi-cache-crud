from database.models import PessoaBase
from uuid import UUID


class PessoaCreate(PessoaBase):
    ...


class PessoaRead(PessoaBase):
    id: UUID


class PessoaPatch(PessoaBase):
    ...
