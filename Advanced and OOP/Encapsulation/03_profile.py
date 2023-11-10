class Profile:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        else:
            self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_valid_length = len(value) >= 8
        is_upper_case = [char for char in value if char.isupper()]
        is_digit = [char for char in value if char.isdigit()]

        if is_digit and is_valid_length and is_upper_case:
            self.__password = value
        else:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {(len(self.password) * "*")}'

profile_with_invalid_password = Profile('My_username', 'My-password')

