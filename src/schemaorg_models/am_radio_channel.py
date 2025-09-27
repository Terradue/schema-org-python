from typing import Literal
from pydantic import Field
from schemaorg_models.radio_channel import RadioChannel


class AMRadioChannel(RadioChannel):
    """
A radio channel that uses AM.
    """
    class_: Literal['https://schema.org/AMRadioChannel'] = Field(default='https://schema.org/AMRadioChannel', alias='@type', serialization_alias='@type') # type: ignore
