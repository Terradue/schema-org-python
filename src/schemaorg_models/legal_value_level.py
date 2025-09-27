from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class LegalValueLevel(Enumeration):
    """
A list of possible levels for the legal validity of a legislation.
    """
    type_: Literal['https://schema.org/LegalValueLevel'] = Field(default='https://schema.org/LegalValueLevel', alias='@type', serialization_alias='@type') # type: ignore
