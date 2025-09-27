from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class ContactPointOption(Enumeration):
    """
Enumerated options related to a ContactPoint.
    """
    class_: Literal['https://schema.org/ContactPointOption'] = Field(default='https://schema.org/ContactPointOption', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
