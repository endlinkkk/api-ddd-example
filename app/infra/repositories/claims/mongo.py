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
        return claims, count

    async def get_claim_by_claim_oid(self, claim_oid: str) -> Claim:
        find = {"oid": claim_oid}
        claim_document = await self._collection.find_one(find)
        if not claim_document:
            return None

        return convert_claim_document_to_entity(claim_document)

    async def delete_claim_by_claim_oid(self, claim_oid) -> None:
        find = {"oid": claim_oid}
        await self._collection.delete_one(find)
