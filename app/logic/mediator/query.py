from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from logic.queries.base import QR, QT, BaseQuery, BaseQueryHandler


@dataclass(eq=False)
class QueryMediator(ABC):

    queries_map: dict[QT, BaseQueryHandler] = field(
        default_factory=lambda: dict(), kw_only=True
    )

    @abstractmethod
    def register_query(self, query: QT, query_handler: BaseQueryHandler[QT, QR]): ...

    @abstractmethod
    async def handle_query(self, query: BaseQuery) -> QR: ...
