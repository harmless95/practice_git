from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy import MetaData

from utils.conv_file import camel_case_to_snake_case
from core.config import setting


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention=setting.db.naming_convention)

    @declared_attr.directive
    def __tablename__(cls):
        return f"{camel_case_to_snake_case(cls.__name__)}s"
