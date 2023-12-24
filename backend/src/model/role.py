from common.enums import Activities
from helper.utils import create_activity
from model.base import Base, db
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Role(Base, db.Model):
    __tablename__ = "role"
    __table_args__ = {"extend_existing": True}

    name = Column(String(10), nullable=False)

    # One-to-one relationship with User
    user = relationship("User", back_populates="role", cascade="all, delete-orphan")

    @classmethod
    def get_role_by_name(cls, role_name):
        return db.session.query(Role).filter_by(name=role_name).first()

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
            Activities.DELETE.value + self.__tablename__ + " " + str(self.id),
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
