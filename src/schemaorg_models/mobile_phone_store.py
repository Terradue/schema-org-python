from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .store import Store

class MobilePhoneStore(Store):
    """
A store that sells mobile phones and related accessories.
    """
    class_: Literal['https://schema.org/MobilePhoneStore'] = Field( # type: ignore
        default='https://schema.org/MobilePhoneStore',
        alias='@type',
        serialization_alias='@type'
    )
