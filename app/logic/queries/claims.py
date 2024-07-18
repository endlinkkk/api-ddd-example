from dataclasses import dataclass
from typing import Generic, Iterable

from domain.entities.claims import Claim
from infra.repositories.claims.base import BaseClaimRepository
from logic.exceptions.claims import ClaimsNotFoundException
from logic.queries.base import QR, QT, BaseQuery, BaseQueryHandler


@dataclass(frozen=True)
class GetClaimsQuery(BaseQuery):
    limit: int


@dataclass(frozen=True)
class GetClaimsQueryHandler(BaseQueryHandler, Generic[QR, QT]):
    claims_repository: BaseClaimRepository

    async def handle(self, query: GetClaimsQuery) -> Iterable[Claim]:
        claims = await self.claims_repository.get_all_claims(limit=query.limit)

        if not claims:
            raise ClaimsNotFoundException()

        return claims
