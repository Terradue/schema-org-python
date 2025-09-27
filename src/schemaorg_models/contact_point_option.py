from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class ContactPointOption(Enumeration):
    """
Enumerated options related to a ContactPoint.
    """
    type_: Literal['https://schema.org/ContactPointOption'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ContactPointOption'),serialization_alias='class') # type: ignore
