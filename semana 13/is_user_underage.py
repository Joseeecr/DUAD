from datetime import date

class User:
    date_of_birth : date

    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year

        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return age


def is_user_underage(func):
    def wrapper(user):
        if user.age < 18:
            raise ValueError("You are underage!")
        return func(user)

    return wrapper

@is_user_underage
def create_user(user):
    print(f"User with date of birth {user.date_of_birth} can be created")

user1 = User(date(1990, 10, 10))
user2 = User(date(2000, 10, 10))
user3 = User(date(2009, 1, 1))

create_user(user1)
create_user(user2)
create_user(user3)