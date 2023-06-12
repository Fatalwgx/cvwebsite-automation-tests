import random
from faker import Faker
from sqlalchemy.orm import Session


from cvwebsite_tests.model.db.postgres import get_db
from cvwebsite_tests.model.db import models


fake = Faker()


class User:
    def __init__(self, session) -> None:
        self.username = ...
        self.password = ...
        self.email = ...
        self.session = session
        self.access_token = ...
        self.id = ...
        self.db: Session = ...
        self.set_fake_data()

    def init_db(self):
        self.db: Session = next(get_db())

    def set_password(self, password: str = None):
        if password is None:
            self.password = fake.password()
        else: self.password = password
        return self

    def set_username(self, username: str = None):
        if username is None:
            self.username = fake.first_name() + str(random.randint(0, 9999))
        else: self.username = username
        return self

    def set_email(self, email: str = None):
        if email is None:
            self.email = fake.email()
        else: self.email = email
        return self
    
    def set_access_token(self, access_token):
        self.access_token = access_token

    def set_id(self, id):
        self.id = id
        return self

    def set_fake_data(self):
        self.set_username()
        self.set_password()
        self.set_email()
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
        self.set_id(r.json().get('id'))
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
    
    def validate_user_with_db(self):
        self.init_db()
        db_user = self.db.query(models.Accounts).filter(models.Accounts.id == self.id).first()
        if db_user.id == self.id and db_user.username == self.username and db_user.email == self.email:
            return True
        else:
            return False

    def last_login_equals(self, last_login):
        self.init_db()
        db_user = self.db.query(models.Accounts).filter(models.Accounts.id == self.id).first()
        if db_user.last_login == last_login:
            return True
        else:
            return False
        
    def last_login_doesnt_equal(self, last_login):
        self.init_db()
        db_user = self.db.query(models.Accounts).filter(models.Accounts.id == self.id).first()
        if db_user.last_login != last_login:
            return True
        else:
            return False
