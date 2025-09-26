from typing import Union, List, Optional
from pydantic import AliasChoices, Field
from schemaorg_models.intangible import Intangible

from schemaorg_models.parcel_delivery import ParcelDelivery
from schemaorg_models.service import Service
from schemaorg_models.product import Product

class OrderItem(Intangible):
    """
An order item is a line of an order. It includes the quantity and shipping details of a bought offer.
    """
    orderQuantity: Optional[Union[float, List[float], "QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('orderQuantity', 'https://schema.org/orderQuantity'),serialization_alias='https://schema.org/orderQuantity')
    orderItemStatus: Optional[Union["OrderStatus", List["OrderStatus"]]] = Field(default=None,validation_alias=AliasChoices('orderItemStatus', 'https://schema.org/orderItemStatus'),serialization_alias='https://schema.org/orderItemStatus')
    orderItemNumber: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('orderItemNumber', 'https://schema.org/orderItemNumber'),serialization_alias='https://schema.org/orderItemNumber')
    orderDelivery: Optional[Union[ParcelDelivery, List[ParcelDelivery]]] = Field(default=None,validation_alias=AliasChoices('orderDelivery', 'https://schema.org/orderDelivery'),serialization_alias='https://schema.org/orderDelivery')
    orderedItem: Optional[Union["OrderItem", List["OrderItem"], Service, List[Service], Product, List[Product]]] = Field(default=None,validation_alias=AliasChoices('orderedItem', 'https://schema.org/orderedItem'),serialization_alias='https://schema.org/orderedItem')
