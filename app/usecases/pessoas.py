from sqlmodel.ext.asyncio.session import AsyncSession


class PessoaUseCases:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
