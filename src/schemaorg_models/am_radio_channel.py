from typing import Literal
from pydantic import Field
from schemaorg_models.radio_channel import RadioChannel


class AMRadioChannel(RadioChannel):
    """
A radio channel that uses AM.
    """
    class_: Literal['https://schema.org/AMRadioChannel'] = Field('class', alias='class', serialization_alias='class') # type: ignore
