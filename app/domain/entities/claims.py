from dataclasses import dataclass, field
from datetime import datetime

from domain.entities.base import BaseEntity
from domain.events.claims import NewClaimCreatedEvevnt
from domain.values.claims import Email, Status, Text, Title, Username


@dataclass(eq=False)
class User(BaseEntity):
    username: Username
    email: Email

    @classmethod
    def create_user(cls, username: Username, email: Email) -> "User":
        user = cls(username=username, email=email)
        return user


@dataclass(eq=False)
class Message(BaseEntity):
    text: Text

    @classmethod
    def create_message(cls, text: Text) -> "Message":
        message = cls(text=text)
        return message


@dataclass(eq=False)
class Claim(BaseEntity):
    title: Title
    message: Message
    created_at: datetime = field(default_factory=datetime.now, kw_only=True)
    status: Status
    user: User

    @classmethod
    def create_claim(
        cls, title: Title, message: Message, status: Status, user: User
    ) -> "Claim":
        claim = cls(title=title, message=message, status=status, user=user)
        claim.register_event(
            NewClaimCreatedEvevnt(
                claim_id=claim.oid,
                claim_title=claim.title,
                clain_status=claim.status
            )
        )
        return claim
