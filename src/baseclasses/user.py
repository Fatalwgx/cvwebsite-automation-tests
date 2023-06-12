from faker import Faker
from src.baseclasses.reponse import Response
import requests


class User:
    def __init__(self, session) -> None:
        self.username = ...
        self.password = ...
        self.email = ...
        self.session = session
        self.set_fake_data()

    def set_password(self, password):
        self.password = password

    def set_username(self, username):
        self.username = username

    def set_email(self, email):
        self.email = email

    def set_fake_data(self):
        fake = Faker()
        self.set_username(fake.unique.first_name())
        self.set_password(fake.password())
        self.set_email(fake.email())

    def register_user(self):
        if self.username is None and self.password is None and self.email is None:
            self.set_fake_data()
        r = self.session.post(
            url='/user/register',
            json={
                "username": self.username,
                "password": self.password,
                "email": self.email
            }
        )
