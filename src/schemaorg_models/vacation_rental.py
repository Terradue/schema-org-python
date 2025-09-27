from typing import Literal
from pydantic import Field
from schemaorg_models.lodging_business import LodgingBusiness


class VacationRental(LodgingBusiness):
    """
A kind of lodging business that focuses on renting single properties for limited time.
    """
    type_: Literal['https://schema.org/VacationRental'] = Field(default='https://schema.org/VacationRental', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
