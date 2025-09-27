from typing import Literal
from pydantic import Field
from schemaorg_models.organization import Organization


class NGO(Organization):
    """
Organization: Non-governmental Organization.
    """
    class_: Literal['https://schema.org/NGO'] = Field(default='https://schema.org/NGO', alias='@type', serialization_alias='@type') # type: ignore
