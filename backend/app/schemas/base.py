from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, StringConstraints


Identifier = Annotated[str, StringConstraints(min_length=1)]


class SeedModel(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="forbid")


class IdentifiedDocument(SeedModel):
    id: Identifier = Field(alias="_id")
