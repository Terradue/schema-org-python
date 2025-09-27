from typing import Literal
from pydantic import Field
from schemaorg_models.enumeration import Enumeration


class ReturnFeesEnumeration(Enumeration):
    """
Enumerates several kinds of policies for product return fees.
    """
    class_: Literal['https://schema.org/ReturnFeesEnumeration'] = Field('class', alias='class', serialization_alias='class') # type: ignore
