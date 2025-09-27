from typing import Literal
from pydantic import Field
from schemaorg_models.local_business import LocalBusiness


class RadioStation(LocalBusiness):
    """
A radio station.
    """
    class_: Literal['https://schema.org/RadioStation'] = Field('class', alias='class', serialization_alias='class') # type: ignore
