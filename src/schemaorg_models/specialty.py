from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class Specialty(Enumeration):
    """
One of the domain specialities to which this web page's content applies.
    """
    type_: Literal['https://schema.org/Specialty'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Specialty'),serialization_alias='class') # type: ignore
