from functools import lru_cache
from infra.repositories.claims import BaseClaimRepository, MemoryClaimRepository
from logic.commands.claims import CreateClaimCommand, CreateClaimCommandHandler
from logic.mediator import Mediator
from punq import Container, Scope



def init_mediator(
    mediator: Mediator,
    container: Container
):
    mediator.register_command(
        CreateClaimCommand,
        [
            container.resolve(CreateClaimCommandHandler),
        ],
    )


@lru_cache(1)
def init_container():
    return _init_container()


def _init_container() -> Container:
    container = Container()
    container.register(BaseClaimRepository, MemoryClaimRepository, scope=Scope.singleton)
    container.register(CreateClaimCommandHandler)

    def init_mediator() -> Mediator:
        mediator = Mediator()

        mediator.register_command(
            CreateClaimCommand,
            [
                container.resolve(CreateClaimCommandHandler),
            ],
        )
        return mediator
    container.register(Mediator, factory=init_mediator)

    return container
