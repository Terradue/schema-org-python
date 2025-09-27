from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class AdultOrientedEnumeration(Enumeration):
    """
Enumeration of considerations that make a product relevant or potentially restricted for adults only.
    """
    type_: Literal['https://schema.org/AdultOrientedEnumeration'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/AdultOrientedEnumeration'),serialization_alias='class') # type: ignore
