from dataclasses import dataclass


@dataclass
class GetClaimsFilters:
    limit: int = 10
    offset: int = 0
