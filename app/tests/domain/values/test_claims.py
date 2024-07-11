from datetime import datetime
from faker import Faker
import pytest

from domain.entities.claims import Claim, Message, User
from domain.exceptions.claims import (
    EmailNotValidException,
    EmptyEmailException,
    EmptyStatusException,
    EmptyTextException,
    EmptyTitleException,
    EmptyUsernameException,
    TitleTooLongException,
    UsernameTooLongException,
)
from domain.values.claims import Email, Status, Text, Title, Username


def test_create_message_success():
    text = Text(Faker().text(max_nb_chars=254))
    message = Message(text=text)

    assert message.text == text


def test_create_user_success():
    username = Username(Faker().text(max_nb_chars=10))
    email = Email(Faker().email(domain="gmail.com"))
    user = User(username=username, email=email)

    assert user.username == username
    assert user.email == email


def test_create_claim_success():
    text = Text(Faker().text(max_nb_chars=254))
    title = Title(Faker().text(max_nb_chars=10))
    message = Message(text=text)
    status = Status(Faker().text(max_nb_chars=10))
    username = Username(Faker().text(max_nb_chars=10))
    email = Email(Faker().email(domain="gmail.com"))
    user = User(username=username, email=email)

    claim = Claim(title=title, message=message, status=status, user=user)

    assert claim.created_at.date() == datetime.today().date()
    assert claim.message == message
    assert claim.status == status
    assert claim.title == title
    assert claim.user == user


def test_create_title_is_empty():
    with pytest.raises(EmptyTitleException):
        title = Title("")


def test_create_title_too_long():
    with pytest.raises(TitleTooLongException):
        title = Title("hello" * 256)


def test_create_text_is_empty():
    with pytest.raises(EmptyTextException):
        text = Text("")


def test_create_status_is_empty():
    with pytest.raises(EmptyStatusException):
        status = Status("")


def test_create_username_is_empty():
    with pytest.raises(EmptyUsernameException):
        username = Username("")


def test_create_username_too_long():
    with pytest.raises(UsernameTooLongException):
        username = Username("username" * 256)


def test_create_email_is_empty():
    with pytest.raises(EmptyEmailException):
        email = Email("")


def test_create_email_is_not_valid():
    with pytest.raises(EmailNotValidException):
        email = Email(Faker().text(max_nb_chars=10))
