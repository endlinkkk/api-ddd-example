from punq import Container, Scope

from infra.repositories.claims.base import BaseClaimRepository

from infra.repositories.claims.memory import MemoryClaimRepository
from logic.init import _init_container


def init_dummy_container() -> Container:
    container = _init_container()

    container.register(
        BaseClaimRepository, MemoryClaimRepository, scope=Scope.singleton
    )
    return container
