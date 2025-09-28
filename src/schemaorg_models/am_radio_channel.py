from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.radio_channel import RadioChannel

from pydantic import (
    Field
)
from typing import (
    Literal
)

class AMRadioChannel(RadioChannel):
    """
A radio channel that uses AM.
    """
    class_: Literal['https://schema.org/AMRadioChannel'] = Field( # type: ignore
        default='https://schema.org/AMRadioChannel',
        alias='@type',
        serialization_alias='@type'
    )
