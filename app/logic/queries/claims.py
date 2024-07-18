from dataclasses import dataclass
from typing import Generic, Iterable

from domain.entities.claims import Claim
from infra.repositories.claims.base import BaseClaimRepository
from infra.repositories.filters.claims import GetClaimsFilters
from logic.exceptions.claims import ClaimNotFoundException, ClaimsNotFoundException
from logic.queries.base import QR, QT, BaseQuery, BaseQueryHandler


@dataclass(frozen=True)
class GetClaimsQuery(BaseQuery):
    filters: GetClaimsFilters


@dataclass(frozen=True)
class GetClaimQuery(BaseQuery):
    claim_oid: str


@dataclass(frozen=True)
class GetClaimsQueryHandler(BaseQueryHandler, Generic[QR, QT]):
    claims_repository: BaseClaimRepository

    async def handle(self, query: GetClaimsQuery) -> tuple[Iterable[Claim], int]:
        claims, count = await self.claims_repository.get_all_claims(
            filters=query.filters
        )

        if not claims:
            raise ClaimsNotFoundException()

        return claims, count


@dataclass(frozen=True)
class GetClaimQueryHandler(BaseQueryHandler, Generic[QR, QT]):
    claims_repository: BaseClaimRepository

    async def handle(self, query: GetClaimQuery) -> Claim:
        claim = await self.claims_repository.get_claim_by_claim_oid(
            claim_oid=query.claim_oid
        )

        if not claim:
            raise ClaimNotFoundException(query.claim_oid)

        return claim
