from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class LegalValueLevel(Enumeration):
    """
A list of possible levels for the legal validity of a legislation.
    """
    class_: Literal['https://schema.org/LegalValueLevel'] = Field(default='https://schema.org/LegalValueLevel', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
