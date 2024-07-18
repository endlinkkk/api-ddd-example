from dataclasses import dataclass
from typing import Iterable
from motor.core import AgnosticClient
from domain.entities.claims import Claim
from infra.repositories.claims.base import BaseClaimRepository
from infra.repositories.claims.converters import (
    convert_claim_document_to_entity,
    convert_claim_entity_to_document,
)
from infra.repositories.filters.claims import GetClaimsFilters


@dataclass
class MongoDBClaimRepository(BaseClaimRepository):
    mongo_db_client: AgnosticClient
    mongo_db_db_name: str
    mongo_db_collection_name: str

    @property
    def _collection(self):
        return self.mongo_db_client[self.mongo_db_db_name][
            self.mongo_db_collection_name
        ]

    async def add_claim(self, claim: Claim) -> None:

        await self._collection.insert_one(
            convert_claim_entity_to_document(claim),
        )

    async def get_all_claims(
        self, filters: GetClaimsFilters
    ) -> tuple[Iterable[Claim], int]:
        cursor = self._collection.find({})
        claims = [
            convert_claim_document_to_entity(claim_document)
            async for claim_document in cursor.skip(filters.offset).limit(filters.limit)
        ]
        count = await self._collection.count_documents(filter={})
        if not claims:
            return None
        return claims, count
