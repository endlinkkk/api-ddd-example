from pydantic_settings import BaseSettings
from pydantic import Field


class Config(BaseSettings):
    mongodb_connection_uri: str = Field(alias="MONGO_DB_CONNECTION_URI")
    mongodb_claim_database: str = Field(default="claim", alias="mongodb_claim_database")
    mongodb_claim_collection: str = Field(
        default="claim", alias="mongodb_claim_collection"
    )
