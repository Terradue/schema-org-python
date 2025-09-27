from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class ReturnLabelSourceEnumeration(Enumeration):
    """
Enumerates several types of return labels for product returns.
    """
    type_: Literal['https://schema.org/ReturnLabelSourceEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/ReturnLabelSourceEnumeration'),serialization_alias='class') # type: ignore
