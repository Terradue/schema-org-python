from __future__ import annotations
from pydantic import (
    AliasChoices,
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
    """
A structured value indicating the quantity, unit of measurement, and business function of goods included in a bundle offer.
    """
    class_: Literal['https://schema.org/TypeAndQuantityNode'] = Field( # type: ignore
        default='https://schema.org/TypeAndQuantityNode',
        alias='@type',
        serialization_alias='@type'
    )
    amountOfThisGood: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'amountOfThisGood',
            'https://schema.org/amountOfThisGood'
        ),
        serialization_alias='https://schema.org/amountOfThisGood'
    )
    unitText: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'unitText',
            'https://schema.org/unitText'
        ),
        serialization_alias='https://schema.org/unitText'
    )
    businessFunction: Optional[Union["BusinessFunction", List["BusinessFunction"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'businessFunction',
            'https://schema.org/businessFunction'
        ),
        serialization_alias='https://schema.org/businessFunction'
    )
    typeOfGood: Optional[Union["Product", List["Product"], "Service", List["Service"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'typeOfGood',
            'https://schema.org/typeOfGood'
        ),
        serialization_alias='https://schema.org/typeOfGood'
    )
    unitCode: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'unitCode',
            'https://schema.org/unitCode'
        ),
        serialization_alias='https://schema.org/unitCode'
    )
