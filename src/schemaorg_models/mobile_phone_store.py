from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.store import Store

from pydantic import (
    Field
)
from typing import (
    Literal
)

class MobilePhoneStore(Store):
    """
A store that sells mobile phones and related accessories.
    """
    class_: Literal['https://schema.org/MobilePhoneStore'] = Field( # type: ignore
        default='https://schema.org/MobilePhoneStore',
        alias='@type',
        serialization_alias='@type'
    )
