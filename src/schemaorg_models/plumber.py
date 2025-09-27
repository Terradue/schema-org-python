from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class Plumber(HomeAndConstructionBusiness):
    """
A plumbing service.
    """
    type_: Literal['https://schema.org/Plumber'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Plumber'),serialization_alias='class') # type: ignore
