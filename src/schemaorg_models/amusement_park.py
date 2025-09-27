from typing import Literal
from pydantic import Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class AmusementPark(EntertainmentBusiness):
    """
An amusement park.
    """
    class_: Literal['https://schema.org/AmusementPark'] = Field('class', alias='class', serialization_alias='class') # type: ignore
