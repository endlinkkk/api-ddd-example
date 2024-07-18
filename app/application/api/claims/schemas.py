from datetime import datetime
from pydantic import BaseModel

from application.api.schemas import BaseQueryResponseSchema
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


class ClaimDetailSchema(BaseModel):
    oid: str
    created_at: datetime
    title: str
    message: str
    status: str
    username: str
    email: str

    @classmethod
    def from_entity(cls, claim: Claim) -> "ClaimDetailSchema":
        return ClaimDetailSchema(
            oid=claim.oid,
            created_at=claim.created_at,
            title=claim.title.as_generic_type(),
            message=claim.message.text.as_generic_type(),
            status=claim.status.as_generic_type(),
            username=claim.user.username.as_generic_type(),
            email=claim.user.email.as_generic_type(),
        )


class GetClaimsResponseSchema(BaseQueryResponseSchema):
    items: list[ClaimDetailSchema]
