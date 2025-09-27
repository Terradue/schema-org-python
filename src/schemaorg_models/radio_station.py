from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.local_business import LocalBusiness


class RadioStation(LocalBusiness):
    """
A radio station.
    """
    type_: Literal['https://schema.org/RadioStation'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/RadioStation'),serialization_alias='class') # type: ignore
