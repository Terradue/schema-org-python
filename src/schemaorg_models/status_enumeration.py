from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class StatusEnumeration(Enumeration):
    """
Lists or enumerations dealing with status types.
    """
    class_: Literal['https://schema.org/StatusEnumeration'] = Field(default='https://schema.org/StatusEnumeration', alias='class', serialization_alias='class') # type: ignore
