from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.home_and_construction_business import HomeAndConstructionBusiness


class GeneralContractor(HomeAndConstructionBusiness):
    """
A general contractor.
    """
    type_: Literal['https://schema.org/GeneralContractor'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/GeneralContractor'),serialization_alias='class') # type: ignore
