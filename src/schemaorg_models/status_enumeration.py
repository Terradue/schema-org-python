from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class StatusEnumeration(Enumeration):
    """
Lists or enumerations dealing with status types.
    """
    type_: Literal['https://schema.org/StatusEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/StatusEnumeration'),serialization_alias='class') # type: ignore
