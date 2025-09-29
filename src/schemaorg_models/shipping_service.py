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
    from .service_period import ServicePeriod
    from .fulfillment_type_enumeration import FulfillmentTypeEnumeration
    from .member_program_tier import MemberProgramTier
    from .shipping_conditions import ShippingConditions
    from .quantitative_value import QuantitativeValue

class ShippingService(StructuredValue):
    '''
    ShippingService represents the criteria used to determine if and how an offer could be shipped to a customer.

    Attributes:
        fulfillmentType: Type of fulfillment applicable to the [[ShippingService]].
        shippingConditions: The conditions (constraints, price) applicable to the [[ShippingService]].
        validForMemberTier: The membership program tier an Offer (or a PriceSpecification, OfferShippingDetails, or MerchantReturnPolicy under an Offer) is valid for.
        handlingTime: The typical delay between the receipt of the order and the goods either leaving the warehouse or being prepared for pickup, in case the delivery method is on site pickup.

In the context of [[ShippingDeliveryTime]], Typical properties: minValue, maxValue, unitCode (d for DAY).  This is by common convention assumed to mean business days (if a unitCode is used, coded as "d"), i.e. only counting days when the business normally operates.

In the context of [[ShippingService]], use the [[ServicePeriod]] format, that contains the same information in a structured form, with cut-off time, business days and duration.
    '''
    class_: Literal['https://schema.org/ShippingService'] = Field( # type: ignore
        default='https://schema.org/ShippingService',
        alias='@type',
        serialization_alias='@type'
    )
    fulfillmentType: Optional[Union['FulfillmentTypeEnumeration', List['FulfillmentTypeEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'fulfillmentType',
            'https://schema.org/fulfillmentType'
        ),
        serialization_alias='https://schema.org/fulfillmentType'
    )
    shippingConditions: Optional[Union['ShippingConditions', List['ShippingConditions']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingConditions',
            'https://schema.org/shippingConditions'
        ),
        serialization_alias='https://schema.org/shippingConditions'
    )
    validForMemberTier: Optional[Union['MemberProgramTier', List['MemberProgramTier']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validForMemberTier',
            'https://schema.org/validForMemberTier'
        ),
        serialization_alias='https://schema.org/validForMemberTier'
    )
    handlingTime: Optional[Union['ServicePeriod', List['ServicePeriod'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'handlingTime',
            'https://schema.org/handlingTime'
        ),
        serialization_alias='https://schema.org/handlingTime'
    )
