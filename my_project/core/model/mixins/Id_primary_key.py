from sqlalchemy.orm import Mapped, mapped_column

class IdPrKey:
    id: Mapped[int] = mapped_column(primary_key=True)