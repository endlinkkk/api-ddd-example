from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Iterable

from domain.entities.claims import Claim


@dataclass
class BaseClaimRepository(ABC):
    @abstractmethod
    def add_claim(self, claim: Claim) -> None: ...

    @abstractmethod
    def get_all_claims(self, limit: int) -> Iterable[Claim]: ...
