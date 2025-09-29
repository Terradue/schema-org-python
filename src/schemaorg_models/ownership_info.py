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
from .structured_value import StructuredValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .service import Service
    from .product import Product
    from .organization import Organization
    from .person import Person

class OwnershipInfo(StructuredValue):
    '''
    A structured value providing information about when a certain organization or person owned a certain product.

    Attributes:
        ownedFrom: The date and time of obtaining the product.
        acquiredFrom: The organization or person from which the product was acquired.
        typeOfGood: The product that this structured value is referring to.
        ownedThrough: The date and time of giving up ownership on the product.
    '''
    class_: Literal['https://schema.org/OwnershipInfo'] = Field( # type: ignore
        default='https://schema.org/OwnershipInfo',
        alias='@type',
        serialization_alias='@type'
    )
    ownedFrom: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    acquiredFrom: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    typeOfGood: Optional[Union['Product', List['Product'], 'Service', List['Service']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    ownedThrough: Optional[Union[datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
