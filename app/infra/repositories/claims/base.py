from dataclasses import dataclass, field
from abc import ABC, abstractmethod

from domain.entities.claims import Claim


@dataclass
class BaseClaimRepository(ABC):
    @abstractmethod
    def add_claim(self, claim: Claim) -> None: ...
