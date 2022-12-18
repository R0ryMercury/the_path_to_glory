from project.dao.models.user import User


class UserDao:
    def __init__(self, session) -> None:
        self.session = session

    def create(self, user_d: dict) -> None:
        ent = User(
            username=user_d.get("username"),
            email=user_d.get("email"),
            password=user_d.get("password"),
            first_name=user_d.get("first_name"),
            last_name=user_d.get("last_name"),
        )
        self.session.add(ent)
        self.session.commit()

    def get_user(self, username: str) -> User:
        return self.session.query(User).filter(User.username == username).first()

    def get_all(self) -> list[User]:
        return self.session.query(User).all()

    def delete(self, username: str) -> None:
        self.session.delete(self.get_user(username))
        self.session.commit()

    def update(self, user: User):
        self.session.add(user)
        self.session.commit()
