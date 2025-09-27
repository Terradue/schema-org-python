from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class Electrician(HomeAndConstructionBusiness):
    """
An electrician.
    """
    type_: Literal['https://schema.org/Electrician'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Electrician'),serialization_alias='class') # type: ignore
