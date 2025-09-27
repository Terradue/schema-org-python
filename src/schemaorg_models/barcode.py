from typing import Literal
from pydantic import Field
from schemaorg_models.image_object import ImageObject


class Barcode(ImageObject):
    """
An image of a visual machine-readable code such as a barcode or QR code.
    """
    type_: Literal['https://schema.org/Barcode'] = Field(default='https://schema.org/Barcode', alias='@type', serialization_alias='http://www.w3.org/2000/01/rdf-schema#/Class') # type: ignore
