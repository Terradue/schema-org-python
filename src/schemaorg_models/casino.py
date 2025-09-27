from typing import Literal
from pydantic import Field
from schemaorg_models.entertainment_business import EntertainmentBusiness


class Casino(EntertainmentBusiness):
    """
A casino.
    """
    class_: Literal['https://schema.org/Casino'] = Field('class', alias='class', serialization_alias='class') # type: ignore
