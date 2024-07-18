from typing import Any, Mapping
from domain.entities.claims import Claim, Message, User
from domain.values.claims import Email, Status, Text, Title, Username


def convert_claim_entity_to_document(claim: Claim) -> dict[str, Any]:
    return {
        "oid": claim.oid,
        "title": claim.title.as_generic_type(),
        "message": claim.message.text.as_generic_type(),
        "status": claim.status.as_generic_type(),
        "created_at": claim.created_at,
        "email": claim.user.email.as_generic_type(),
        "username": claim.user.username.as_generic_type(),
    }


def convert_claim_document_to_entity(claim_document: Mapping[str, Any]) -> Claim:
    return Claim(
        title=Title(value=claim_document["title"]),
        message=Message(text=Text(value=claim_document["message"])),
        status=Status(value=claim_document["status"]),
        created_at=claim_document["created_at"],
        user=User(
            username=Username(value=claim_document["username"]),
            email=Email(value=claim_document["email"]),
        ),
        oid=claim_document["oid"],
    )
