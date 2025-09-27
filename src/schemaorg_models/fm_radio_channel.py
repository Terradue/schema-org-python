from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.radio_channel import RadioChannel


class FMRadioChannel(RadioChannel):
    """
A radio channel that uses FM.
    """
    type_: Literal['https://schema.org/FMRadioChannel'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/FMRadioChannel'),serialization_alias='class') # type: ignore
