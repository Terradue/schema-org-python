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
from .product import Product

class IndividualProduct(Product):
    '''
    A single, identifiable product instance (e.g. a laptop with a particular serial number).

    Attributes:
        serialNumber: The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.
    '''
    class_: Literal['https://schema.org/IndividualProduct'] = Field( # type: ignore
        default='https://schema.org/IndividualProduct',
        alias='@type',
        serialization_alias='@type'
    )
    serialNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serialNumber',
            'https://schema.org/serialNumber'
        ),
        serialization_alias='https://schema.org/serialNumber'
    )
