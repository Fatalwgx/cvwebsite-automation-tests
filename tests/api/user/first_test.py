import requests
import os

from src.schemas import schemas
from src.baseclasses.reponse import Response
from src.baseclasses.user import User


def test_create_user(setup_session):
    test_user = User(setup_session)
    response = setup_session.post(
        url="/user/register",
        json={
            "username": test_user.username,
            "password": test_user.password,
            "email": test_user.email
        }
    )
    test_object = Response(response)
    test_object \
        .assert_status_code(200) \
        .validate(schemas.UserCreateResponse)


def test_fetch_created_user_data(setup_session):
    response = setup_session.post(
        url="/user",
        header={}
    )
    test_object = Response(response)
    test_object \
        .assert_status_code(200) \
        .validate(schemas.UserCreateResponse)
    