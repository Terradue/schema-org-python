from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class ContactPointOption(Enumeration):
    """
Enumerated options related to a ContactPoint.
    """
    class_: Literal['https://schema.org/ContactPointOption'] = Field(default='https://schema.org/ContactPointOption', alias='class', serialization_alias='class') # type: ignore
