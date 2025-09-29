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
from .image_object import ImageObject

class Barcode(ImageObject):
    '''
    An image of a visual machine-readable code such as a barcode or QR code.
    '''
    class_: Literal['https://schema.org/Barcode'] = Field( # type: ignore
        default='https://schema.org/Barcode',
        alias='@type',
        serialization_alias='@type'
    )
