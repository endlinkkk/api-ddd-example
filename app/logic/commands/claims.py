from dataclasses import dataclass

from domain.entities.claims import Claim, Message, User
from domain.values.claims import Email, Status, Text, Title, Username
from infra.repositories.claims.base import BaseClaimRepository
from logic.commands.base import BaseCommand, BaseCommandHandler


@dataclass(frozen=True)
class CreateClaimCommand(BaseCommand):
    title: str
    message: str
    username: str
    email: str
    status: str


@dataclass(frozen=True)
class DeleteClaimCommand(BaseCommand):
    claim_oid: str


@dataclass(frozen=True)
class CreateClaimCommandHandler(BaseCommandHandler[CreateClaimCommand, Claim]):
    claim_repository: BaseClaimRepository

    async def handle(self, command: CreateClaimCommand) -> Claim:
        title = Title(value=command.title)
        text = Text(value=command.message)
        email = Email(value=command.email)
        username = Username(value=command.username)
        status = Status(value=command.status)

        message = Message.create_message(text=text)
        user = User.create_user(username=username, email=email)

        claim = Claim.create_claim(
            title=title, message=message, status=status, user=user
        )
        await self.claim_repository.add_claim(claim)

        return claim


@dataclass(frozen=True)
class DeleteClaimCommandHandler(BaseCommandHandler[DeleteClaimCommand, None]):
    claim_repository: BaseClaimRepository

    async def handle(self, command: DeleteClaimCommand) -> None:
        await self.claim_repository.delete_claim_by_claim_oid(command.claim_oid)
