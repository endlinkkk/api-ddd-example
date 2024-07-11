from pydantic import BaseModel

from domain.entities.claims import Claim

class CreateClaimResponseSchema(BaseModel):
    oid: str
    title: str

    @classmethod
    def from_entity(cls, claim: Claim) -> "CreateClaimResponseSchema":
        return cls(oid=claim.oid, title=claim.title.as_generic_type())


class CreateClaimRequestSchema(BaseModel):
    title: str
    message: str
    username: str
    email: str
    status: str





