from dataclasses import dataclass
from motor.core import AgnosticClient
from domain.entities.claims import Claim
from infra.repositories.claims.base import BaseClaimRepository
from infra.repositories.claims.converters import convert_claim_entity_to_document


@dataclass
class MongoDBClaimRepository(BaseClaimRepository):
    mongo_db_client: AgnosticClient
    mongo_db_db_name: str
    mongo_db_collection_name: str

    def _get_claim_collection(self):
        return self.mongo_db_client[self.mongo_db_db_name][
            self.mongo_db_collection_name
        ]

    async def add_claim(self, claim: Claim) -> None:
        collection = self._get_claim_collection()

        await collection.insert_one(
            convert_claim_entity_to_document(claim),
        )
