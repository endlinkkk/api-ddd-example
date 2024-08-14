from dataclasses import dataclass, field
from typing import ClassVar
from domain.events.base import BaseEvent


@dataclass
class NewClaimReceivedEvent(BaseEvent):
    message_text: str
    message_oid: str
    claim_oid: str


@dataclass
class NewClaimCreatedEvent(BaseEvent):
    claim_id: str
    claim_title: str
    clain_status: str


@dataclass
class ClaimDeletedEvent(BaseEvent):
    claim_id: str
    claim_title: ClassVar[str] = "Claim Has Been Deleted"
