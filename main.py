class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, "admin")
        self.__user = []

    def add_user(self, user):
        self.__user.append(user)
        if user not in self.__user:
            self.__users.append(user)

    def remove_user(self, user):
        if user in self.__users:
            self.__users.remove(user)





