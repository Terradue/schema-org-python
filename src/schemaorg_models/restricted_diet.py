from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.enumeration import Enumeration


class RestrictedDiet(Enumeration):
    """
A diet restricted to certain foods or preparations for cultural, religious, health or lifestyle reasons. 
    """
    type_: Literal['https://schema.org/RestrictedDiet'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/RestrictedDiet'),serialization_alias='class') # type: ignore
