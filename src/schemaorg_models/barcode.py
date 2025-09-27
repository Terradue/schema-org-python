from typing import Literal
from pydantic import AliasChoices, Field
from schemaorg_models.image_object import ImageObject


class Barcode(ImageObject):
    """
An image of a visual machine-readable code such as a barcode or QR code.
    """
    type_: Literal['https://schema.org/Barcode'] = Field('class', alias=AliasChoices('@type', 'https://schema.org/Barcode'),serialization_alias='class') # type: ignore
