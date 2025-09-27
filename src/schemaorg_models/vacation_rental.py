from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.lodging_business import LodgingBusiness


class VacationRental(LodgingBusiness):
    """
A kind of lodging business that focuses on renting single properties for limited time.
    """
    type_: Literal['https://schema.org/VacationRental'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/VacationRental'),serialization_alias='class') # type: ignore
