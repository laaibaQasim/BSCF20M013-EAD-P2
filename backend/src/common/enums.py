from enum import Enum as PyEnum


class Enum(str, PyEnum):
    @classmethod
    def exists(cls, item):
        return item in [x.value for x in cls]

    @classmethod
    def list(cls):
        return [x.value for x in cls]

    @classmethod
    def select(cls, key):
        for member in cls:
            if member.name == key:
                return member.value


class Degree(Enum):
    BS = "Bachelors"
    MS = "Masters"
    PHD = "Doctorate"


class Roles(Enum):
    ADMIN = "admin"
    STUDENT = "student"


class Departments(Enum):
    CS = "Computer Science"
    IT = "Information Technology"
    ME = "Mechanical Engineering"
    SE = "Software Engineering"
    ARTS = "Arts"


class Activities(Enum):
    LOGIN = "Logging in the system "
    LOGOUT = "Logging out the system "
    CPS = "Changing Page Size "
    BACK = "Clicking Back on the page navigation "
    NEXT = "Clicking Next on the page navigation "
    INSERT = "Entering "
    UPDATE = "Updating "
    DELETE = "Deleting "
    VIEW = "Viewing "
