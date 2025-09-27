from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class Locksmith(HomeAndConstructionBusiness):
    """
A locksmith.
    """
    type_: Literal['https://schema.org/Locksmith'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Locksmith'),serialization_alias='class') # type: ignore
