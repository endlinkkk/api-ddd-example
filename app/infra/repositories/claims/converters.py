from domain.entities.claims import Claim


def convert_claim_entity_to_document(claim: Claim):
    return {
        "oid": claim.oid,
        "title": claim.title.as_generic_type(),
        "message": claim.message.text.as_generic_type(),
        "status": claim.status.as_generic_type(),
        "created_at": claim.created_at,
    }
