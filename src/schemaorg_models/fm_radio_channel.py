from typing import Literal
from pydantic import Field
from schemaorg_models.radio_channel import RadioChannel


class FMRadioChannel(RadioChannel):
    """
A radio channel that uses FM.
    """
    type_: Literal['https://schema.org/FMRadioChannel'] = Field(default='https://schema.org/FMRadioChannel', alias='@type', serialization_alias='@type') # type: ignore
