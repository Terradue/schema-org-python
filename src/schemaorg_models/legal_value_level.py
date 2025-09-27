from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class LegalValueLevel(Enumeration):
    """
A list of possible levels for the legal validity of a legislation.
    """
    type_: Literal['https://schema.org/LegalValueLevel'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/LegalValueLevel'),serialization_alias='class') # type: ignore
