from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .radio_channel import RadioChannel

class FMRadioChannel(RadioChannel):
    """
A radio channel that uses FM.
    """
    class_: Literal['https://schema.org/FMRadioChannel'] = Field( # type: ignore
        default='https://schema.org/FMRadioChannel',
        alias='@type',
        serialization_alias='@type'
    )
