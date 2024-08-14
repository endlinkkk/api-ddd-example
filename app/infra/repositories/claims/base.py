from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Iterable

from domain.entities.claims import Claim
from infra.repositories.filters.claims import GetClaimsFilters


@dataclass
class BaseClaimRepository(ABC):

    @abstractmethod
    def add_claim(self, claim: Claim) -> None: ...

    @abstractmethod
    def get_all_claims(
        self, filters: GetClaimsFilters
    ) -> tuple[Iterable[Claim], int]: ...

    @abstractmethod
    def get_claim_by_claim_oid(self, claim_oid: str) -> Claim: ...

    @abstractmethod
    def delete_claim_by_claim_oid(self, claim_oid) -> None: ...
