from pydantic import BaseModel

from infra.repositories.filters.claims import GetClaimsFilters as GetClaimsInfraFilters


class GetClaimsFilters(BaseModel):
    limit: int = 10
    offset: int = 0

    def to_infra(self):
        return GetClaimsInfraFilters(limit=self.limit, offset=self.offset)
