from functools import lru_cache
from infra.repositories.claims.base import BaseClaimRepository
from infra.repositories.claims.mongo import MongoDBClaimRepository
from logic.commands.claims import CreateClaimCommand, CreateClaimCommandHandler
from logic.mediator import Mediator
from punq import Container, Scope
from motor.motor_asyncio import AsyncIOMotorClient
from logic.queries.claims import GetClaimsQuery, GetClaimsQueryHandler
from settings.config import Config


@lru_cache(1)
def init_container():
    return _init_container()


def _init_container() -> Container:
    container = Container()

    container.register(CreateClaimCommandHandler)
    container.register(Config, instance=Config(), scope=Scope.singleton)

    def init_mediator() -> Mediator:
        mediator = Mediator()

        mediator.register_command(
            CreateClaimCommand,
            [
                container.resolve(CreateClaimCommandHandler),
            ],
        )
        mediator.register_query(
            GetClaimsQuery,
            container.resolve(GetClaimsQueryHandler),
        )
        return mediator

    def init_claim_mongodb_repository() -> MongoDBClaimRepository:
        config: Config = container.resolve(Config)
        client = AsyncIOMotorClient(
            config.mongodb_connection_uri, serverSelectionTimeoutMS=3000
        )
        return MongoDBClaimRepository(
            mongo_db_client=client,
            mongo_db_db_name=config.mongodb_claim_database,
            mongo_db_collection_name=config.mongodb_claim_collection,
        )

    container.register(
        BaseClaimRepository,
        factory=init_claim_mongodb_repository,
        scope=Scope.singleton,
    )
    container.register(GetClaimsQueryHandler)
    container.register(Mediator, factory=init_mediator)

    return container
