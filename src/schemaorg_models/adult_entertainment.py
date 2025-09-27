from typing import Literal
from pydantic import Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class AdultEntertainment(EntertainmentBusiness):
    """
An adult entertainment establishment.
    """
    class_: Literal['https://schema.org/AdultEntertainment'] = Field('class', alias='class', serialization_alias='class') # type: ignore
