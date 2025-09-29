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
from .intangible import Intangible
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .geo_shape import GeoShape
    from .warranty_promise import WarrantyPromise
    from .business_function import BusinessFunction
    from .place import Place
    from .business_entity_type import BusinessEntityType
    from .aggregate_offer import AggregateOffer
    from .delivery_method import DeliveryMethod
    from .item_availability import ItemAvailability
    from .creative_work import CreativeWork
    from .payment_method import PaymentMethod
    from .trip import Trip
    from .price_specification import PriceSpecification
    from .product import Product
    from .organization import Organization
    from .service import Service
    from .offer_item_condition import OfferItemCondition
    from .quantitative_value import QuantitativeValue
    from .administrative_area import AdministrativeArea
    from .event import Event
    from .loan_or_credit import LoanOrCredit
    from .person import Person
    from .type_and_quantity_node import TypeAndQuantityNode
    from .menu_item import MenuItem

class Demand(Intangible):
    '''
    A demand entity represents the public, not necessarily binding, not necessarily exclusive, announcement by an organization or person to seek a certain type of goods or services. For describing demand using this type, the very same properties used for Offer apply.

    Attributes:
        availabilityEnds: The end of the availability of the product or service included in the offer.
        sku: The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.
        eligibleTransactionVolume: The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.
        includesObject: This links to a node or nodes indicating the exact quantity of the products included in  an [[Offer]] or [[ProductCollection]].
        eligibleCustomerType: The type(s) of customers for which the given offer is valid.
        availableDeliveryMethod: The delivery method(s) available for this offer.
        validFrom: The date when the item becomes valid.
        deliveryLeadTime: The typical delay between the receipt of the order and the goods either leaving the warehouse or being prepared for pickup, in case the delivery method is on site pickup.
        ineligibleRegion: The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.\
\
See also [[eligibleRegion]].
      
        gtin13: The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        advanceBookingRequirement: The amount of time that is required between accepting the offer and the actual usage of the resource or service.
        inventoryLevel: The current approximate inventory level for the item or items.
        acceptedPaymentMethod: The payment method(s) that are accepted in general by an organization, or for some specific demand or offer.
        itemCondition: A predefined value from OfferItemCondition specifying the condition of the product or service, or the products or services included in the offer. Also used for product return policies to specify the condition of products accepted for returns.
        availabilityStarts: The beginning of the availability of the product or service included in the offer.
        mpn: The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.
        availability: The availability of this item&#x2014;for example In stock, Out of stock, Pre-order, etc.
        gtin14: The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        serialNumber: The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.
        availableAtOrFrom: The place(s) from which the offer can be obtained (e.g. store locations).
        gtin12: The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        businessFunction: The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.
        gtin8: The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        eligibleQuantity: The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.
        eligibleDuration: The duration for which the given offer is valid.
        itemOffered: An item being offered (or demanded). The transactional nature of the offer or demand is documented using [[businessFunction]], e.g. sell, lease etc. While several common expected types are listed explicitly in this definition, others can be used. Using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
        eligibleRegion: The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.\
\
See also [[ineligibleRegion]].
    
        priceSpecification: One or more detailed price specifications, indicating the unit price and delivery or payment charges.
        gtin: A Global Trade Item Number ([GTIN](https://www.gs1.org/standards/id-keys/gtin)). GTINs identify trade items, including products and services, using numeric identification codes.

A correct [[gtin]] value should be a valid GTIN, which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a "GS1 Digital Link" URL based on such a string. The numeric component should also have a [valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator) and meet the other rules for valid GTINs. See also [GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) and [Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number) for more details. Left-padding of the gtin values is not required or encouraged. The [[gtin]] property generalizes the earlier [[gtin8]], [[gtin12]], [[gtin13]], and [[gtin14]] properties.

The GS1 [digital link specifications](https://www.gs1.org/standards/Digital-Link/) expresses GTINs as URLs (URIs, IRIs, etc.).
Digital Links should be populated into the [[hasGS1DigitalLink]] attribute.

Note also that this is a definition for how to include GTINs in Schema.org data, and not a definition of GTINs in general - see the GS1 documentation for authoritative details.
        areaServed: The geographic area where a service or offered item is provided.
        asin: An Amazon Standard Identification Number (ASIN) is a 10-character alphanumeric unique identifier assigned by Amazon.com and its partners for product identification within the Amazon organization (summary from [Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s article).

Note also that this is a definition for how to include ASINs in Schema.org data, and not a definition of ASINs in general - see documentation from Amazon for authoritative details.
ASINs are most commonly encoded as text strings, but the [asin] property supports URL/URI as potential values too.
        seller: An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.
        validThrough: The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.
        warranty: The warranty promise(s) included in the offer.
    '''
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
    eligibleTransactionVolume: Optional[Union['PriceSpecification', List['PriceSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleTransactionVolume',
            'https://schema.org/eligibleTransactionVolume'
        ),
        serialization_alias='https://schema.org/eligibleTransactionVolume'
    )
    includesObject: Optional[Union['TypeAndQuantityNode', List['TypeAndQuantityNode']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'includesObject',
            'https://schema.org/includesObject'
        ),
        serialization_alias='https://schema.org/includesObject'
    )
    eligibleCustomerType: Optional[Union['BusinessEntityType', List['BusinessEntityType']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleCustomerType',
            'https://schema.org/eligibleCustomerType'
        ),
        serialization_alias='https://schema.org/eligibleCustomerType'
    )
    availableDeliveryMethod: Optional[Union['DeliveryMethod', List['DeliveryMethod']]] = Field(
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
    deliveryLeadTime: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'deliveryLeadTime',
            'https://schema.org/deliveryLeadTime'
        ),
        serialization_alias='https://schema.org/deliveryLeadTime'
    )
    ineligibleRegion: Optional[Union[str, List[str], 'Place', List['Place'], 'GeoShape', List['GeoShape']]] = Field(
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
    advanceBookingRequirement: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'advanceBookingRequirement',
            'https://schema.org/advanceBookingRequirement'
        ),
        serialization_alias='https://schema.org/advanceBookingRequirement'
    )
    inventoryLevel: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inventoryLevel',
            'https://schema.org/inventoryLevel'
        ),
        serialization_alias='https://schema.org/inventoryLevel'
    )
    acceptedPaymentMethod: Optional[Union[str, List[str], 'PaymentMethod', List['PaymentMethod'], 'LoanOrCredit', List['LoanOrCredit']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'acceptedPaymentMethod',
            'https://schema.org/acceptedPaymentMethod'
        ),
        serialization_alias='https://schema.org/acceptedPaymentMethod'
    )
    itemCondition: Optional[Union['OfferItemCondition', List['OfferItemCondition']]] = Field(
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
    availability: Optional[Union['ItemAvailability', List['ItemAvailability']]] = Field(
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
    availableAtOrFrom: Optional[Union['Place', List['Place']]] = Field(
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
    businessFunction: Optional[Union['BusinessFunction', List['BusinessFunction']]] = Field(
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
    eligibleQuantity: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleQuantity',
            'https://schema.org/eligibleQuantity'
        ),
        serialization_alias='https://schema.org/eligibleQuantity'
    )
    eligibleDuration: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleDuration',
            'https://schema.org/eligibleDuration'
        ),
        serialization_alias='https://schema.org/eligibleDuration'
    )
    itemOffered: Optional[Union['Event', List['Event'], 'Service', List['Service'], 'AggregateOffer', List['AggregateOffer'], 'Product', List['Product'], 'MenuItem', List['MenuItem'], 'CreativeWork', List['CreativeWork'], 'Trip', List['Trip']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemOffered',
            'https://schema.org/itemOffered'
        ),
        serialization_alias='https://schema.org/itemOffered'
    )
    eligibleRegion: Optional[Union['GeoShape', List['GeoShape'], str, List[str], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleRegion',
            'https://schema.org/eligibleRegion'
        ),
        serialization_alias='https://schema.org/eligibleRegion'
    )
    priceSpecification: Optional[Union['PriceSpecification', List['PriceSpecification']]] = Field(
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
    areaServed: Optional[Union['GeoShape', List['GeoShape'], str, List[str], 'AdministrativeArea', List['AdministrativeArea'], 'Place', List['Place']]] = Field(
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
    seller: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
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
    warranty: Optional[Union['WarrantyPromise', List['WarrantyPromise']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'warranty',
            'https://schema.org/warranty'
        ),
        serialization_alias='https://schema.org/warranty'
    )
