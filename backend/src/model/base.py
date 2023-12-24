from __future__ import annotations

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr

db = SQLAlchemy(session_options={"autoflush": False})


@as_declarative()
class Base(object):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=True)
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=True,
    )

    @declared_attr
    def __tablename__(cls) -> str:
        """
        Generate __tablename__ automatically

        Returns:
            Table name
        """
        return cls.__name__.lower()

    def insert(self) -> Base:
        """
        Insert

        :return: Base
        """
        self.insert_log()
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self) -> Base:
        """
        Delete

        :return: Base
        """
        self.delete_log()
        db.session.delete(self)
        db.session.commit()
        return self

    @classmethod
    def update(cls, id: int, to_update: dict) -> None:
        """
        Update row by id

        :param id:
        :param to_update:
        :return:
        """
        # insert_Activity(Activities.UPDATE.name, (Activities.UPDATE.value + cls.__tablename__))
        cls.update_log(id)
        db.session.query(cls).filter(cls.id == id).update(to_update)
        db.session.commit()

    @classmethod
    def get_by_id(cls, id: int):
        """
        Get object by id

        :param id:
        :return:
        """
        # insert_Activity(Activities.VIEW.name, (Activities.VIEW.value + cls.__tablename__))
        cls.get_by_id_log(id)
        row = db.session.query(cls).filter_by(id=id).first()
        return row

    @classmethod
    def get(cls):
        """

        :return:
        """
        # insert_Activity(Activities.VIEW.name, (Activities.VIEW.value + cls.__tablename__))
        cls.get_log()
        rows = db.session.query(cls).all()
        return rows

    def insert_log(self):
        pass

    def delete_log(self):
        pass

    @classmethod
    def update_log(cls, id):
        pass

    @classmethod
    def get_log(cls):
        pass

    @classmethod
    def get_by_id_log(cls, id):
        pass
