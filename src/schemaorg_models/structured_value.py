from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.intangible import Intangible

from pydantic import (
    Field
)
from typing import (
    Literal
)

class StructuredValue(Intangible):
    """
Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.
    """
    class_: Literal['https://schema.org/StructuredValue'] = Field( # type: ignore
        default='https://schema.org/StructuredValue',
        alias='@type',
        serialization_alias='@type'
    )
