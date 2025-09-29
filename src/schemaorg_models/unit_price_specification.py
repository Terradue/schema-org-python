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
from .price_specification import PriceSpecification
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .duration import Duration
    from .price_component_type_enumeration import PriceComponentTypeEnumeration
    from .quantitative_value import QuantitativeValue
    from .price_type_enumeration import PriceTypeEnumeration

class UnitPriceSpecification(PriceSpecification):
    '''
    The price asked for a given offer by the respective organization or person.

    Attributes:
        unitText: A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for
<a href='unitCode'>unitCode</a>.
        billingDuration: Specifies for how long this price (or price component) will be billed. Can be used, for example, to model the contractual duration of a subscription or payment plan. Type can be either a Duration or a Number (in which case the unit of measurement, for example month, is specified by the unitCode property).
        unitCode: The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.
        referenceQuantity: The reference quantity for which a certain price applies, e.g. 1 EUR per 4 kWh of electricity. This property is a replacement for unitOfMeasurement for the advanced cases where the price does not relate to a standard unit.
        priceComponentType: Identifies a price component (for example, a line item on an invoice), part of the total price for an offer.
        billingIncrement: This property specifies the minimal quantity and rounding increment that will be the basis for the billing. The unit of measurement is specified by the unitCode property.
        priceType: Defines the type of a price specified for an offered product, for example a list price, a (temporary) sale price or a manufacturer suggested retail price. If multiple prices are specified for an offer the [[priceType]] property can be used to identify the type of each such specified price. The value of priceType can be specified as a value from enumeration PriceTypeEnumeration or as a free form text string for price types that are not already predefined in PriceTypeEnumeration.
        billingStart: Specifies after how much time this price (or price component) becomes valid and billing starts. Can be used, for example, to model a price increase after the first year of a subscription. The unit of measurement is specified by the unitCode property.
    '''
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
    billingDuration: Optional[Union['Duration', List['Duration'], float, List[float], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
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
    referenceQuantity: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'referenceQuantity',
            'https://schema.org/referenceQuantity'
        ),
        serialization_alias='https://schema.org/referenceQuantity'
    )
    priceComponentType: Optional[Union['PriceComponentTypeEnumeration', List['PriceComponentTypeEnumeration']]] = Field(
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
    priceType: Optional[Union[str, List[str], 'PriceTypeEnumeration', List['PriceTypeEnumeration']]] = Field(
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
