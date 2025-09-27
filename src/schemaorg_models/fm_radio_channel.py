from typing import Literal
from pydantic import Field
from schemaorg_models.radio_channel import RadioChannel


class FMRadioChannel(RadioChannel):
    """
A radio channel that uses FM.
    """
    class_: Literal['https://schema.org/FMRadioChannel'] = Field(default='https://schema.org/FMRadioChannel', alias='class', serialization_alias='class') # type: ignore
