from faker import Faker


import pytest

from domain.entities.claims import Claim
from logic.commands.claims import CreateClaimCommand, DeleteClaimCommand
from logic.mediator.base import Mediator


@pytest.mark.asyncio
async def test_create_claim_command_success(mediator: Mediator):
    fake = Faker()
    fake_title = fake.text(max_nb_chars=15)
    fake_message = fake.text(max_nb_chars=15)
    fake_username = fake.text(max_nb_chars=15)
    fake_email = fake.email(domain="gmail.com")
    fake_status = fake.text(max_nb_chars=15)

    claim: Claim = await mediator.handle_command(
        CreateClaimCommand(
            title=fake_title,
            message=fake_message,
            username=fake_username,
            email=fake_email,
            status=fake_status,
        )
    )
    assert claim
