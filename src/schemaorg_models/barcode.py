from typing import Literal
from pydantic import Field
from schemaorg_models.image_object import ImageObject


class Barcode(ImageObject):
    """
An image of a visual machine-readable code such as a barcode or QR code.
    """
    class_: Literal['https://schema.org/Barcode'] = Field('class', alias='class', serialization_alias='class') # type: ignore
