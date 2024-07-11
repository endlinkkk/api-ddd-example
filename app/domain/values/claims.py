from dataclasses import dataclass, field

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
from domain.values.base import BaseValueObject
from email_validator import validate_email, EmailNotValidError


@dataclass(frozen=True)
class Title(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyTitleException()

        if len(self.value) > 50:
            raise TitleTooLongException(self.value)

    def as_generic_type(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class Text(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyTextException()

    def as_generic_type(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class Status(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyStatusException()

    def as_generic_type(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class Username(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyUsernameException()

        if len(self.value) > 30:
            raise UsernameTooLongException(self.value)

    def as_generic_type(self) -> str:
        return str(self.value)


@dataclass(frozen=True)
class Email(BaseValueObject):
    value: str

    def validate(self):
        if not self.value:
            raise EmptyEmailException()

        try:
            validate_email(self.value)
        except EmailNotValidError:
            raise EmailNotValidException(self.value)

    def as_generic_type(self) -> str:
        return str(self.value)
