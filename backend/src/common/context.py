class CurrentUser:
    cuser = None
    role_name = None

    @classmethod
    def set_current_user(cls, user):
        cls.cuser = user
        cls.role_name = cls.cuser.get_role_name()
