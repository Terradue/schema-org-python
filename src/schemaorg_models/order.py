from typing import List, Literal, Optional, Union
from datetime import date, datetime
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible

from schemaorg_models.parcel_delivery import ParcelDelivery
from schemaorg_models.person import Person
from schemaorg_models.organization import Organization
from schemaorg_models.payment_method import PaymentMethod
from schemaorg_models.invoice import Invoice
from schemaorg_models.order_item import OrderItem
from schemaorg_models.service import Service
from schemaorg_models.product import Product

class Order(Intangible):
    """
An order is a confirmation of a transaction (a receipt), which can contain multiple line items, each represented by an Offer that has been accepted by the customer.
    """
    class_: Literal['https://schema.org/Order'] = Field(default='https://schema.org/Order', alias='@type', serialization_alias='@type') # type: ignore
    orderDelivery: Optional[Union[ParcelDelivery, List[ParcelDelivery]]] = Field(default=None, validation_alias=AliasChoices('orderDelivery', 'https://schema.org/orderDelivery'), serialization_alias='https://schema.org/orderDelivery')
    broker: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('broker', 'https://schema.org/broker'), serialization_alias='https://schema.org/broker')
    isGift: Optional[Union[bool, List[bool]]] = Field(default=None, validation_alias=AliasChoices('isGift', 'https://schema.org/isGift'), serialization_alias='https://schema.org/isGift')
    customer: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('customer', 'https://schema.org/customer'), serialization_alias='https://schema.org/customer')
    paymentMethod: Optional[Union[str, List[str], PaymentMethod, List[PaymentMethod]]] = Field(default=None, validation_alias=AliasChoices('paymentMethod', 'https://schema.org/paymentMethod'), serialization_alias='https://schema.org/paymentMethod')
    merchant: Optional[Union[Person, List[Person], Organization, List[Organization]]] = Field(default=None, validation_alias=AliasChoices('merchant', 'https://schema.org/merchant'), serialization_alias='https://schema.org/merchant')
    discountCurrency: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('discountCurrency', 'https://schema.org/discountCurrency'), serialization_alias='https://schema.org/discountCurrency')
    confirmationNumber: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('confirmationNumber', 'https://schema.org/confirmationNumber'), serialization_alias='https://schema.org/confirmationNumber')
    orderStatus: Optional[Union["OrderStatus", List["OrderStatus"]]] = Field(default=None, validation_alias=AliasChoices('orderStatus', 'https://schema.org/orderStatus'), serialization_alias='https://schema.org/orderStatus')
    partOfInvoice: Optional[Union[Invoice, List[Invoice]]] = Field(default=None, validation_alias=AliasChoices('partOfInvoice', 'https://schema.org/partOfInvoice'), serialization_alias='https://schema.org/partOfInvoice')
    orderNumber: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('orderNumber', 'https://schema.org/orderNumber'), serialization_alias='https://schema.org/orderNumber')
    acceptedOffer: Optional[Union["Offer", List["Offer"]]] = Field(default=None, validation_alias=AliasChoices('acceptedOffer', 'https://schema.org/acceptedOffer'), serialization_alias='https://schema.org/acceptedOffer')
    seller: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(default=None, validation_alias=AliasChoices('seller', 'https://schema.org/seller'), serialization_alias='https://schema.org/seller')
    paymentDueDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('paymentDueDate', 'https://schema.org/paymentDueDate'), serialization_alias='https://schema.org/paymentDueDate')
    billingAddress: Optional[Union["PostalAddress", List["PostalAddress"]]] = Field(default=None, validation_alias=AliasChoices('billingAddress', 'https://schema.org/billingAddress'), serialization_alias='https://schema.org/billingAddress')
    orderedItem: Optional[Union[OrderItem, List[OrderItem], Service, List[Service], Product, List[Product]]] = Field(default=None, validation_alias=AliasChoices('orderedItem', 'https://schema.org/orderedItem'), serialization_alias='https://schema.org/orderedItem')
    orderDate: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('orderDate', 'https://schema.org/orderDate'), serialization_alias='https://schema.org/orderDate')
    paymentDue: Optional[Union[datetime, List[datetime]]] = Field(default=None, validation_alias=AliasChoices('paymentDue', 'https://schema.org/paymentDue'), serialization_alias='https://schema.org/paymentDue')
    paymentUrl: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None, validation_alias=AliasChoices('paymentUrl', 'https://schema.org/paymentUrl'), serialization_alias='https://schema.org/paymentUrl')
    @field_serializer('paymentUrl')
    def paymentUrl2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    discountCode: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('discountCode', 'https://schema.org/discountCode'), serialization_alias='https://schema.org/discountCode')
    paymentMethodId: Optional[Union[str, List[str]]] = Field(default=None, validation_alias=AliasChoices('paymentMethodId', 'https://schema.org/paymentMethodId'), serialization_alias='https://schema.org/paymentMethodId')
    discount: Optional[Union[str, List[str], float, List[float]]] = Field(default=None, validation_alias=AliasChoices('discount', 'https://schema.org/discount'), serialization_alias='https://schema.org/discount')
