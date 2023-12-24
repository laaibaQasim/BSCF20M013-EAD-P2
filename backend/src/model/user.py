from common.enums import Activities
from helper.utils import create_activity
from model.base import Base, db
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User(Base, db.Model):
    __tablename__ = "user"
    __table_args__ = {"extend_existing": True}

    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(126), default="pucit")
    role_id = Column(Integer, ForeignKey("role.id"))

    # One-to-one relationship with Student
    student = relationship("Student", uselist=False, back_populates="user")
    role = relationship("Role", back_populates="user")
    activities = relationship(
        "UserActivity", back_populates="user", cascade="all, delete-orphan"
    )

    def get_role_name(self):
        if self.role:
            return self.role.name
        return None

    @classmethod
    def get_by_email(cls, email):
        create_activity(
            Activities.VIEW.name,
            Activities.VIEW.value + cls.__tablename__ + " with email: " + str(email),
        )
        return db.session.query(cls).filter(cls.email == email).first()

    def insert_log(self):
        super().insert_log()
        create_activity(
            Activities.INSERT.name,
            Activities.INSERT.value + self.__tablename__ + " " + str(self.name),
        )

    def delete_log(self):
        super().delete_log()
        create_activity(
            Activities.DELETE.name,
            Activities.DELETE.value + self.__tablename__ + " " + str(self.name),
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
