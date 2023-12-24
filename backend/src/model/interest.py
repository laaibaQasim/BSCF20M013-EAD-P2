from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from helper.utils import create_activity
from common.enums import Activities
from model.base import Base, db


class Interest(Base, db.Model):
    __tablename__ = "interest"
    name = Column(String(100), nullable=False)
    student = relationship(
        "Student", back_populates="interest", cascade="all, delete-orphan"
    )

    @classmethod
    def get_by_name(cls, interest_name):
        interest = db.session.query(cls).filter(cls.name == interest_name).first()
        return interest

    def insert_log(self):
        super().insert_log()
        create_activity(
            Activities.INSERT.name,
            Activities.INSERT.value + self.__tablename__ + " " + self.name,
        )

    def delete_log(self):
        super().delete_log()
        create_activity(
            Activities.DELETE.name,
            Activities.DELETE.value + self.__tablename__ + " " + self.name,
        )

    @classmethod
    def update_log(cls, id):
        super().update_log(id)
        create_activity(
            Activities.UPDATE.name,
            Activities.UPDATE.value + cls.__tablename__ + " " + str(id),
        )

    @classmethod
    def get_log(cls):
        super().get_log()
        create_activity(
            Activities.VIEW.name, Activities.VIEW.value + cls.__tablename__ + "s"
        )

    @classmethod
    def get_by_id_log(cls, id):
        super().get_by_id_log(id)
        create_activity(
            Activities.VIEW.name,
            Activities.VIEW.value + cls.__tablename__ + " with ID: " + str(id),
        )
