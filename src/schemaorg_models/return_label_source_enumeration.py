from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class ReturnLabelSourceEnumeration(Enumeration):
    """
Enumerates several types of return labels for product returns.
    """
    class_: Literal['https://schema.org/ReturnLabelSourceEnumeration'] = Field(default='https://schema.org/ReturnLabelSourceEnumeration', alias='class', serialization_alias='class') # type: ignore
