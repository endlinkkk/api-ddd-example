from dataclasses import dataclass

from domain.exceptions.base import ApplicationException


@dataclass()
class EmptyTitleException(ApplicationException):
    @property
    def message(self):
        return f"Title cannot be empty"


@dataclass()
class TitleTooLongException(ApplicationException):
    text: str

    @property
    def message(self):
        return f"Title is too long"


@dataclass()
class EmptyTextException(ApplicationException):
    @property
    def message(self):
        return f"Text cannot be empty"


@dataclass()
class EmptyStatusException(ApplicationException):
    @property
    def message(self):
        return f"Status cannot be empty"


@dataclass()
class EmptyUsernameException(ApplicationException):
    @property
    def message(self):
        return f"Username cannot be empty"


@dataclass()
class UsernameTooLongException(ApplicationException):
    text: str

    @property
    def message(self):
        return f"Username is too long"


@dataclass()
class EmptyEmailException(ApplicationException):
    @property
    def message(self):
        return f"Email cannot be empty"


@dataclass()
class EmailNotValidException(ApplicationException):
    text: str

    @property
    def message(self):
        return f"Incorrect email.\nYour email: {self.text}.\nExamples of correct emails: [example@example.com, john.doe@domain.org, info+newsletter@company.net]"
