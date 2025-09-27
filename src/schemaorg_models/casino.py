from typing import Literal
from pydantic import Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class Casino(EntertainmentBusiness):
    """
A casino.
    """
    class_: Literal['https://schema.org/Casino'] = Field(default='https://schema.org/Casino', alias='@type', serialization_alias='@type') # type: ignore
