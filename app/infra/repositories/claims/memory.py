from dataclasses import dataclass, field
from abc import ABC, abstractmethod

from domain.entities.claims import Claim
from infra.repositories.claims.base import BaseClaimRepository


@dataclass
class MemoryClaimRepository(BaseClaimRepository):
    _saved_claims: list[Claim] = field(default_factory=list, kw_only=True)

    async def add_claim(self, claim: Claim) -> None:
        return self._saved_claims.append(claim)
