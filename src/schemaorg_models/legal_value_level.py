from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class LegalValueLevel(Enumeration):
    """
A list of possible levels for the legal validity of a legislation.
    """
    class_: Literal['https://schema.org/LegalValueLevel'] = Field('class', alias='class', serialization_alias='class') # type: ignore
