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
    from .business_function import BusinessFunction
    from .product import Product
    from .service import Service

class TypeAndQuantityNode(StructuredValue):
    '''
    A structured value indicating the quantity, unit of measurement, and business function of goods included in a bundle offer.

    Attributes:
        amountOfThisGood: The quantity of the goods included in the offer.
        unitText: A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for
<a href='unitCode'>unitCode</a>.
        businessFunction: The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.
        typeOfGood: The product that this structured value is referring to.
        unitCode: The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.
    '''
    class_: Literal['https://schema.org/TypeAndQuantityNode'] = Field( # type: ignore
        default='https://schema.org/TypeAndQuantityNode',
        alias='@type',
        serialization_alias='@type'
    )
    amountOfThisGood: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    unitText: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    businessFunction: Optional[Union['BusinessFunction', List['BusinessFunction']]] = Field(
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
    unitCode: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
