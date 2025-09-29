from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
from pydantic import (
    field_serializer,
    field_validator,
    AliasChoices,
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl
)
from typing import (
    List,
    Literal,
    Optional,
    Union
)
from .intangible import Intangible

class StructuredValue(Intangible):
    '''
    Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.
    '''
    class_: Literal['https://schema.org/StructuredValue'] = Field( # type: ignore
        default='https://schema.org/StructuredValue',
        alias='@type',
        serialization_alias='@type'
    )
