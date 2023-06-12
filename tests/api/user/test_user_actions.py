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
            "email": test_user.email,
        },
    )
    test_object = Response(response)
    test_object.assert_status_code(200).validate(schemas.UserCreateResponse)


def test_fetch_created_user_data(setup_session):
    test_user = User(setup_session).register().login()
    response = setup_session.get(url="/user", headers={"access-token": test_user.access_token})
    test_object = Response(response)
    test_object.assert_status_code(200).validate(schemas.UserDataResponse)


def test_succesfull_login(setup_session):
    test_user = User(setup_session).register()
    response = setup_session.post(
        url="/user/login",
        data={"username": test_user.username, "password": test_user.password},
    )
    test_object = Response(response)
    test_object.assert_status_code(200).validate(schemas.LoginResponse)


def test_unsuccessful_login(setup_session):
    test_user = User(setup_session).register()
    response = setup_session.post(
        url="/user/login",
        data={"username": test_user.password, "password": test_user.username},
    )
    test_object = Response(response)
    test_object.assert_status_code(400)


def test_change_user_only_password(setup_session):
    test_user = User(setup_session).register().login()
    password = test_user.password
    test_user.set_password('changedpassword')
    response = setup_session.put(
        url="/user/edit",
        headers={
            "access-token": test_user.access_token,
            "password": password
        },
        json={
            "password": test_user.password
        }
    )
    test_object = Response(response)
    test_object.assert_status_code(200).validate(schemas.UserUpdateResponse).validate_user(test_user)


def test_change_user_only_name(setup_session):
    test_user = User(setup_session).register().login().set_username()
    response = setup_session.put(
        url="/user/edit",
        headers={
            "access-token": test_user.access_token,
            "password": test_user.password
        },
        json={
            "username": test_user.username
        }
    )
    test_user.login()
    test_object = Response(response)
    test_object.assert_status_code(200).validate(schemas.UserUpdateResponse).validate_user(test_user)


def test_change_user_only_email(setup_session):
    test_user = User(setup_session).register().login().set_email()
    response = setup_session.put(
        url="/user/edit",
        headers={
            "access-token": test_user.access_token,
            "password": test_user.password
        },
        json={
            "email": test_user.email
        }
    )
    test_object = Response(response)
    test_object.assert_status_code(200).validate(schemas.UserUpdateResponse).validate_user(test_user)


#   Methods using orm to check directly with database. Theese cases are in need of a properly integrated and encapsulated, but the time is short 
#   and these should be good enough for an example
def test_create_user_and_check_with_db(setup_session):
    test_user = User(setup_session).register()
    assert test_user.validate_user_with_db()


def test_last_login_date_is_null_after_register(setup_session):
    test_user = User(setup_session).register()
    assert test_user.last_login_equals(None)


def test_last_login_date_is_not_null_after_register(setup_session):
    test_user = User(setup_session).register().login()
    assert test_user.last_login_doesnt_equal(None)