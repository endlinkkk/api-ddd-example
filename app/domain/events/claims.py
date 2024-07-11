from dataclasses import dataclass, field

from domain.events.base import BaseEvent


@dataclass
class NewClaimReceivedEvent(BaseEvent):
    message_text: str
    message_oid: str
    claim_oid: str


@dataclass
class NewClaimCreatedEvevnt(BaseEvent):
    claim_id: str
    claim_title: str
    clain_status: str
