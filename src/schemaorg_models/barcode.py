from __future__ import annotations
from pydantic import (
    Field
)
from typing import (
    Literal
)
from .image_object import ImageObject

class Barcode(ImageObject):
    """
An image of a visual machine-readable code such as a barcode or QR code.
    """
    class_: Literal['https://schema.org/Barcode'] = Field( # type: ignore
        default='https://schema.org/Barcode',
        alias='@type',
        serialization_alias='@type'
    )
