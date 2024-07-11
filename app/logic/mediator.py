from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterable

from domain.events.base import BaseEvent
from logic.commands.base import CR, CT, BaseCommand, BaseCommandHandler
from logic.events.base import ER, ET, BaseEventHandler
from logic.exceptions.mediator import (
    CommandHandlersNotRegisteredException,
    EventHandlersNotRegisteredException,
)


@dataclass(eq=False)
class Mediator:
    events_map: dict[ET, BaseEventHandler] = field(
        default_factory=lambda: defaultdict(list), kw_only=True
    )
    commands_map: dict[CT, BaseCommandHandler] = field(
        default_factory=lambda: defaultdict(list), kw_only=True
    )

    def register_event(
        self, event: ET, event_handlers: Iterable[BaseEventHandler[ET, ER]]
    ):
        self.events_map[event].extend(event_handlers)

    def register_command(
        self, command: CT, command_handlers: Iterable[BaseCommandHandler[CT, CR]]
    ):
        self.commands_map[command].extend(command_handlers)

    async def handle_event(self, event: BaseEvent) -> Iterable[ER]:
        event_type = event.__class__
        handlers = self.events_map[event_type]
        if not handlers:
            raise EventHandlersNotRegisteredException(event_type)

        return [await handler.handle(event) for handler in handlers]

    async def handle_command(self, command: BaseCommand) -> Iterable[CR]:
        command_type = command.__class__
        handlers = self.commands_map[command_type]
        if not handlers:
            raise CommandHandlersNotRegisteredException(command_type)

        return [await handler.handle(command) for handler in handlers]
