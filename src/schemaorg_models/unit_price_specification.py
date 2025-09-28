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
from .price_specification import PriceSpecification
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .quantitative_value import QuantitativeValue
    from .price_component_type_enumeration import PriceComponentTypeEnumeration
    from .price_type_enumeration import PriceTypeEnumeration
    from .duration import Duration

class UnitPriceSpecification(PriceSpecification):
    """
The price asked for a given offer by the respective organization or person.
    """
    class_: Literal['https://schema.org/UnitPriceSpecification'] = Field( # type: ignore
        default='https://schema.org/UnitPriceSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    unitText: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'unitText',
            'https://schema.org/unitText'
        ),
        serialization_alias='https://schema.org/unitText'
    )
    billingDuration: Optional[Union["Duration", List["Duration"], float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'billingDuration',
            'https://schema.org/billingDuration'
        ),
        serialization_alias='https://schema.org/billingDuration'
    )
    unitCode: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'unitCode',
            'https://schema.org/unitCode'
        ),
        serialization_alias='https://schema.org/unitCode'
    )
    referenceQuantity: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'referenceQuantity',
            'https://schema.org/referenceQuantity'
        ),
        serialization_alias='https://schema.org/referenceQuantity'
    )
    priceComponentType: Optional[Union["PriceComponentTypeEnumeration", List["PriceComponentTypeEnumeration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceComponentType',
            'https://schema.org/priceComponentType'
        ),
        serialization_alias='https://schema.org/priceComponentType'
    )
    billingIncrement: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'billingIncrement',
            'https://schema.org/billingIncrement'
        ),
        serialization_alias='https://schema.org/billingIncrement'
    )
    priceType: Optional[Union[str, List[str], "PriceTypeEnumeration", List["PriceTypeEnumeration"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceType',
            'https://schema.org/priceType'
        ),
        serialization_alias='https://schema.org/priceType'
    )
    billingStart: Optional[Union[float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'billingStart',
            'https://schema.org/billingStart'
        ),
        serialization_alias='https://schema.org/billingStart'
    )
