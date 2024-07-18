from dataclasses import dataclass

from logic.exceptions.base import LogicException


@dataclass(eq=False)
class ClaimsNotFoundException(LogicException):

    @property
    def message(self):
        return "Claims not found"


@dataclass(eq=False)
class ClaimNotFoundException(LogicException):
    claim_oid: str

    @property
    def message(self):
        return f"Claim with this ID was not found: {self.claim_oid}"
