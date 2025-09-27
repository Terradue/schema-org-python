from typing import List, Literal, Optional, Union
from pydantic import AliasChoices, Field
from schemaorg_models.structured_value import StructuredValue

from schemaorg_models.fulfillment_type_enumeration import FulfillmentTypeEnumeration
from schemaorg_models.member_program_tier import MemberProgramTier

class ShippingService(StructuredValue):
    """
ShippingService represents the criteria used to determine if and how an offer could be shipped to a customer.
    """
    class_: Literal['https://schema.org/ShippingService'] = Field(default='https://schema.org/ShippingService', alias='http://www.w3.org/2000/01/rdf-schema#Class', serialization_alias='http://www.w3.org/2000/01/rdf-schema#Class') # type: ignore
    fulfillmentType: Optional[Union[FulfillmentTypeEnumeration, List[FulfillmentTypeEnumeration]]] = Field(default=None, validation_alias=AliasChoices('fulfillmentType', 'https://schema.org/fulfillmentType'), serialization_alias='https://schema.org/fulfillmentType')
    shippingConditions: Optional[Union["ShippingConditions", List["ShippingConditions"]]] = Field(default=None, validation_alias=AliasChoices('shippingConditions', 'https://schema.org/shippingConditions'), serialization_alias='https://schema.org/shippingConditions')
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = Field(default=None, validation_alias=AliasChoices('validForMemberTier', 'https://schema.org/validForMemberTier'), serialization_alias='https://schema.org/validForMemberTier')
    handlingTime: Optional[Union["ServicePeriod", List["ServicePeriod"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None, validation_alias=AliasChoices('handlingTime', 'https://schema.org/handlingTime'), serialization_alias='https://schema.org/handlingTime')
