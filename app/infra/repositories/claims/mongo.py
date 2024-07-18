from dataclasses import dataclass
from typing import Iterable
from motor.core import AgnosticClient
from domain.entities.claims import Claim
from infra.repositories.claims.base import BaseClaimRepository
from infra.repositories.claims.converters import (
    convert_claim_document_to_entity,
    convert_claim_entity_to_document,
)


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

    async def get_all_claims(self, limit: int) -> Iterable[Claim]:
        claims_document = await self._collection.find({}).to_list(length=limit)
        if not claims_document:
            return None
        return [
            convert_claim_document_to_entity(claim_document)
            for claim_document in claims_document
        ]
