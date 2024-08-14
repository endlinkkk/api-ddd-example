from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Iterable

from domain.entities.claims import Claim
from infra.repositories.claims.base import BaseClaimRepository
from infra.repositories.filters.claims import GetClaimsFilters


@dataclass
class MemoryClaimRepository(BaseClaimRepository):
    _saved_claims: list[Claim] = field(default_factory=list, kw_only=True)

    async def add_claim(self, claim: Claim) -> None:
        return self._saved_claims.append(claim)

    async def get_all_claims(
        self, filters: GetClaimsFilters
    ) -> tuple[Iterable[Claim], int]:
        claims = self._saved_claims[filters.offset : filters.limit]
        count = len(self._saved_claims)
        if not claims:
            return None
        return claims, count

    async def get_claim_by_claim_oid(self, claim_oid: str) -> Claim:
        for claim in self._saved_claims:
            if claim.oid == claim_oid:
                return claim

    async def delete_claim_by_claim_oid(self, claim_oid) -> None:
        for claim in self._saved_claims:
            if claim.oid == claim_oid:
                self._saved_claims.remove(claim)
                break
