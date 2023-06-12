from faker import Faker
from src.baseclasses.reponse import Response
import requests


class User:
    def __init__(self, session) -> None:
        self.username = ...
        self.password = ...
        self.email = ...
        self.session = session
        self.access_token = ...
        self.set_fake_data()

    def set_password(self, password):
        self.password = password
        return self

    def set_username(self, username):
        self.username = username
        return self

    def set_email(self, email):
        self.email = email
        return self
    
    def set_access_token(self, access_token):
        self.access_token = access_token

    def set_fake_data(self):
        fake = Faker()
        self.set_username(fake.unique.first_name())
        self.set_password(fake.password())
        self.set_email(fake.email())
        return self

    def register(self):
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
        return self

    def login(self):
        r = self.session.post(
            url="/user/login",
            data={
                "username": self.username,
                "password": self.password
            }
        )
        self.set_access_token(r.json().get('access_token'))
        return self
