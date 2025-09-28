from __future__ import annotations
from datetime import (
    date,
    datetime,
    time
)
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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .creative_work import CreativeWork
    from .warranty_promise import WarrantyPromise
    from .person import Person
    from .organization import Organization
    from .product import Product
    from .business_entity_type import BusinessEntityType
    from .delivery_method import DeliveryMethod
    from .aggregate_offer import AggregateOffer
    from .payment_method import PaymentMethod
    from .quantitative_value import QuantitativeValue
    from .geo_shape import GeoShape
    from .offer_item_condition import OfferItemCondition
    from .menu_item import MenuItem
    from .type_and_quantity_node import TypeAndQuantityNode
    from .place import Place
    from .event import Event
    from .trip import Trip
    from .price_specification import PriceSpecification
    from .administrative_area import AdministrativeArea
    from .item_availability import ItemAvailability
    from .service import Service
    from .business_function import BusinessFunction
    from .loan_or_credit import LoanOrCredit

class Demand(Intangible):
    """
A demand entity represents the public, not necessarily binding, not necessarily exclusive, announcement by an organization or person to seek a certain type of goods or services. For describing demand using this type, the very same properties used for Offer apply.
    """
    class_: Literal['https://schema.org/Demand'] = Field( # type: ignore
        default='https://schema.org/Demand',
        alias='@type',
        serialization_alias='@type'
    )
    availabilityEnds: Optional[Union[date, List[date], time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availabilityEnds',
            'https://schema.org/availabilityEnds'
        ),
        serialization_alias='https://schema.org/availabilityEnds'
    )
    sku: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sku',
            'https://schema.org/sku'
        ),
        serialization_alias='https://schema.org/sku'
    )
    eligibleTransactionVolume: Optional[Union[PriceSpecification, List[PriceSpecification]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleTransactionVolume',
            'https://schema.org/eligibleTransactionVolume'
        ),
        serialization_alias='https://schema.org/eligibleTransactionVolume'
    )
    includesObject: Optional[Union[TypeAndQuantityNode, List[TypeAndQuantityNode]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includesObject',
            'https://schema.org/includesObject'
        ),
        serialization_alias='https://schema.org/includesObject'
    )
    eligibleCustomerType: Optional[Union[BusinessEntityType, List[BusinessEntityType]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleCustomerType',
            'https://schema.org/eligibleCustomerType'
        ),
        serialization_alias='https://schema.org/eligibleCustomerType'
    )
    availableDeliveryMethod: Optional[Union[DeliveryMethod, List[DeliveryMethod]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableDeliveryMethod',
            'https://schema.org/availableDeliveryMethod'
        ),
        serialization_alias='https://schema.org/availableDeliveryMethod'
    )
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validFrom',
            'https://schema.org/validFrom'
        ),
        serialization_alias='https://schema.org/validFrom'
    )
    deliveryLeadTime: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'deliveryLeadTime',
            'https://schema.org/deliveryLeadTime'
        ),
        serialization_alias='https://schema.org/deliveryLeadTime'
    )
    ineligibleRegion: Optional[Union[str, List[str], Place, List[Place], GeoShape, List[GeoShape]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'ineligibleRegion',
            'https://schema.org/ineligibleRegion'
        ),
        serialization_alias='https://schema.org/ineligibleRegion'
    )
    gtin13: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gtin13',
            'https://schema.org/gtin13'
        ),
        serialization_alias='https://schema.org/gtin13'
    )
    advanceBookingRequirement: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'advanceBookingRequirement',
            'https://schema.org/advanceBookingRequirement'
        ),
        serialization_alias='https://schema.org/advanceBookingRequirement'
    )
    inventoryLevel: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inventoryLevel',
            'https://schema.org/inventoryLevel'
        ),
        serialization_alias='https://schema.org/inventoryLevel'
    )
    acceptedPaymentMethod: Optional[Union[str, List[str], PaymentMethod, List[PaymentMethod], LoanOrCredit, List[LoanOrCredit]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'acceptedPaymentMethod',
            'https://schema.org/acceptedPaymentMethod'
        ),
        serialization_alias='https://schema.org/acceptedPaymentMethod'
    )
    itemCondition: Optional[Union[OfferItemCondition, List[OfferItemCondition]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemCondition',
            'https://schema.org/itemCondition'
        ),
        serialization_alias='https://schema.org/itemCondition'
    )
    availabilityStarts: Optional[Union[datetime, List[datetime], date, List[date], time, List[time]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availabilityStarts',
            'https://schema.org/availabilityStarts'
        ),
        serialization_alias='https://schema.org/availabilityStarts'
    )
    mpn: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mpn',
            'https://schema.org/mpn'
        ),
        serialization_alias='https://schema.org/mpn'
    )
    availability: Optional[Union[ItemAvailability, List[ItemAvailability]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availability',
            'https://schema.org/availability'
        ),
        serialization_alias='https://schema.org/availability'
    )
    gtin14: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gtin14',
            'https://schema.org/gtin14'
        ),
        serialization_alias='https://schema.org/gtin14'
    )
    serialNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serialNumber',
            'https://schema.org/serialNumber'
        ),
        serialization_alias='https://schema.org/serialNumber'
    )
    availableAtOrFrom: Optional[Union[Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableAtOrFrom',
            'https://schema.org/availableAtOrFrom'
        ),
        serialization_alias='https://schema.org/availableAtOrFrom'
    )
    gtin12: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gtin12',
            'https://schema.org/gtin12'
        ),
        serialization_alias='https://schema.org/gtin12'
    )
    businessFunction: Optional[Union[BusinessFunction, List[BusinessFunction]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'businessFunction',
            'https://schema.org/businessFunction'
        ),
        serialization_alias='https://schema.org/businessFunction'
    )
    gtin8: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gtin8',
            'https://schema.org/gtin8'
        ),
        serialization_alias='https://schema.org/gtin8'
    )
    eligibleQuantity: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleQuantity',
            'https://schema.org/eligibleQuantity'
        ),
        serialization_alias='https://schema.org/eligibleQuantity'
    )
    eligibleDuration: Optional[Union[QuantitativeValue, List[QuantitativeValue]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleDuration',
            'https://schema.org/eligibleDuration'
        ),
        serialization_alias='https://schema.org/eligibleDuration'
    )
    itemOffered: Optional[Union[Event, List[Event], Service, List[Service], AggregateOffer, List[AggregateOffer], Product, List[Product], MenuItem, List[MenuItem], CreativeWork, List[CreativeWork], Trip, List[Trip]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemOffered',
            'https://schema.org/itemOffered'
        ),
        serialization_alias='https://schema.org/itemOffered'
    )
    eligibleRegion: Optional[Union[GeoShape, List[GeoShape], str, List[str], Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleRegion',
            'https://schema.org/eligibleRegion'
        ),
        serialization_alias='https://schema.org/eligibleRegion'
    )
    priceSpecification: Optional[Union[PriceSpecification, List[PriceSpecification]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceSpecification',
            'https://schema.org/priceSpecification'
        ),
        serialization_alias='https://schema.org/priceSpecification'
    )
    gtin: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gtin',
            'https://schema.org/gtin'
        ),
        serialization_alias='https://schema.org/gtin'
    )
    areaServed: Optional[Union[GeoShape, List[GeoShape], str, List[str], AdministrativeArea, List[AdministrativeArea], Place, List[Place]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'areaServed',
            'https://schema.org/areaServed'
        ),
        serialization_alias='https://schema.org/areaServed'
    )
    asin: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'asin',
            'https://schema.org/asin'
        ),
        serialization_alias='https://schema.org/asin'
    )
    seller: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'seller',
            'https://schema.org/seller'
        ),
        serialization_alias='https://schema.org/seller'
    )
    validThrough: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validThrough',
            'https://schema.org/validThrough'
        ),
        serialization_alias='https://schema.org/validThrough'
    )
    warranty: Optional[Union[WarrantyPromise, List[WarrantyPromise]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'warranty',
            'https://schema.org/warranty'
        ),
        serialization_alias='https://schema.org/warranty'
    )
