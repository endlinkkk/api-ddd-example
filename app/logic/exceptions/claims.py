from dataclasses import dataclass

from logic.exceptions.base import LogicException


@dataclass(eq=False)
class ClaimsNotFoundException(LogicException):

    @property
    def message(self):
        return "Claims not found"
