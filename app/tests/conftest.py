from pytest import fixture
from punq import Container
from infra.repositories.claims.base import BaseClaimRepository
from logic.mediator import Mediator
from tests.fixtures import init_dummy_container


@fixture(scope="function")
def container() -> Container:
    return init_dummy_container()


@fixture(scope="function")
def mediator(container: Container) -> Mediator:
    return container.resolve(Mediator)


@fixture(scope="function")
def claim_repository(container: Container) -> BaseClaimRepository:
    return container.resolve(BaseClaimRepository)
