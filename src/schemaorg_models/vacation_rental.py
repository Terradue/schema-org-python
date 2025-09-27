from typing import Literal
from pydantic import Field
from schemaorg_models.lodging_business import LodgingBusiness


class VacationRental(LodgingBusiness):
    """
A kind of lodging business that focuses on renting single properties for limited time.
    """
    class_: Literal['https://schema.org/VacationRental'] = Field(default='https://schema.org/VacationRental', alias='@type', serialization_alias='@type') # type: ignore
