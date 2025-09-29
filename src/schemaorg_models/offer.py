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
    from .offer_item_condition import OfferItemCondition
    from .offer_shipping_details import OfferShippingDetails
    from .adult_oriented_enumeration import AdultOrientedEnumeration
    from .geo_shape import GeoShape
    from .business_entity_type import BusinessEntityType
    from .merchant_return_policy import MerchantReturnPolicy
    from .organization import Organization
    from .loan_or_credit import LoanOrCredit
    from .property_value import PropertyValue
    from .item_availability import ItemAvailability
    from .payment_method import PaymentMethod
    from .duration import Duration
    from .event import Event
    from .warranty_promise import WarrantyPromise
    from .creative_work import CreativeWork
    from .administrative_area import AdministrativeArea
    from .product import Product
    from .review import Review
    from .price_specification import PriceSpecification
    from .aggregate_rating import AggregateRating
    from .type_and_quantity_node import TypeAndQuantityNode
    from .person import Person
    from .aggregate_offer import AggregateOffer
    from .delivery_method import DeliveryMethod
    from .place import Place
    from .menu_item import MenuItem
    from .category_code import CategoryCode
    from .business_function import BusinessFunction
    from .trip import Trip
    from .thing import Thing
    from .member_program_tier import MemberProgramTier
    from .service import Service
    from .physical_activity_category import PhysicalActivityCategory
    from .quantitative_value import QuantitativeValue

class Offer(Intangible):
    '''
    An offer to transfer some rights to an item or to provide a service — for example, an offer to sell tickets to an event, to rent the DVD of a movie, to stream a TV show over the internet, to repair a motorcycle, or to loan a book.\
\
Note: As the [[businessFunction]] property, which identifies the form of offer (e.g. sell, lease, repair, dispose), defaults to http://purl.org/goodrelations/v1#Sell; an Offer without a defined businessFunction value can be assumed to be an offer to sell.\
\
For [GTIN](http://www.gs1.org/barcodes/technical/idkeys/gtin)-related fields, see [Check Digit calculator](http://www.gs1.org/barcodes/support/check_digit_calculator) and [validation guide](http://www.gs1us.org/resources/standards/gtin-validation-guide) from [GS1](http://www.gs1.org/).

    Attributes:
        asin: An Amazon Standard Identification Number (ASIN) is a 10-character alphanumeric unique identifier assigned by Amazon.com and its partners for product identification within the Amazon organization (summary from [Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s article).

Note also that this is a definition for how to include ASINs in Schema.org data, and not a definition of ASINs in general - see documentation from Amazon for authoritative details.
ASINs are most commonly encoded as text strings, but the [asin] property supports URL/URI as potential values too.
        hasAdultConsideration: Used to tag an item to be intended or suitable for consumption or use by adults only.
        eligibleTransactionVolume: The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.
        includesObject: This links to a node or nodes indicating the exact quantity of the products included in  an [[Offer]] or [[ProductCollection]].
        eligibleCustomerType: The type(s) of customers for which the given offer is valid.
        shippingDetails: Indicates information about the shipping policies and options associated with an [[Offer]].
        availabilityEnds: The end of the availability of the product or service included in the offer.
        availableDeliveryMethod: The delivery method(s) available for this offer.
        validFrom: The date when the item becomes valid.
        mobileUrl: The [[mobileUrl]] property is provided for specific situations in which data consumers need to determine whether one of several provided URLs is a dedicated 'mobile site'.

To discourage over-use, and reflecting intial usecases, the property is expected only on [[Product]] and [[Offer]], rather than [[Thing]]. The general trend in web technology is towards [responsive design](https://en.wikipedia.org/wiki/Responsive_web_design) in which content can be flexibly adapted to a wide range of browsing environments. Pages and sites referenced with the long-established [[url]] property should ideally also be usable on a wide variety of devices, including mobile phones. In most cases, it would be pointless and counter productive to attempt to update all [[url]] markup to use [[mobileUrl]] for more mobile-oriented pages. The property is intended for the case when items (primarily [[Product]] and [[Offer]]) have extra URLs hosted on an additional "mobile site" alongside the main one. It should not be taken as an endorsement of this publication style.
    
        validForMemberTier: The membership program tier an Offer (or a PriceSpecification, OfferShippingDetails, or MerchantReturnPolicy under an Offer) is valid for.
        deliveryLeadTime: The typical delay between the receipt of the order and the goods either leaving the warehouse or being prepared for pickup, in case the delivery method is on site pickup.
        isFamilyFriendly: Indicates whether this content is family friendly.
        ineligibleRegion: The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.\
\
See also [[eligibleRegion]].
      
        gtin13: The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        hasGS1DigitalLink: The <a href="https://www.gs1.org/standards/gs1-digital-link">GS1 digital link</a> associated with the object. This URL should conform to the particular requirements of digital links. The link should only contain the Application Identifiers (AIs) that are relevant for the entity being annotated, for instance a [[Product]] or an [[Organization]], and for the correct granularity. In particular, for products:<ul><li>A Digital Link that contains a serial number (AI <code>21</code>) should only be present on instances of [[IndividualProduct]]</li><li>A Digital Link that contains a lot number (AI <code>10</code>) should be annotated as [[SomeProduct]] if only products from that lot are sold, or [[IndividualProduct]] if there is only a specific product.</li><li>A Digital Link that contains a global model number (AI <code>8013</code>)  should be attached to a [[Product]] or a [[ProductModel]].</li></ul> Other item types should be adapted similarly.
        hasMeasurement: A measurement of an item, For example, the inseam of pants, the wheel size of a bicycle, the gauge of a screw, or the carbon footprint measured for certification by an authority. Usually an exact measurement, but can also be a range of measurements for adjustable products, for example belts and ski bindings.
        inventoryLevel: The current approximate inventory level for the item or items.
        itemCondition: A predefined value from OfferItemCondition specifying the condition of the product or service, or the products or services included in the offer. Also used for product return policies to specify the condition of products accepted for returns.
        price: The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.\
\
Usage guidelines:\
\
* Use the [[priceCurrency]] property (with standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR") instead of including [ambiguous symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign) such as '$' in the value.\
* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.\
* Note that both [RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute) and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values alongside more human-friendly formatting.\
* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
      
        additionalProperty: A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org.\
\
Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

        checkoutPageURLTemplate: A URL template (RFC 6570) for a checkout page for an offer. This approach allows merchants to specify a URL for online checkout of the offered product, by interpolating parameters such as the logged in user ID, product ID, quantity, discount code etc. Parameter naming and standardization are not specified here.
        category: A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.
        hasMerchantReturnPolicy: Specifies a MerchantReturnPolicy that may be applicable.
        priceCurrency: The currency of the price, or a price component when attached to [[PriceSpecification]] and its subtypes.\
\
Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        availability: The availability of this item&#x2014;for example In stock, Out of stock, Pre-order, etc.
        gtin14: The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        priceValidUntil: The date after which the price is no longer available.
        serialNumber: The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.
        advanceBookingRequirement: The amount of time that is required between accepting the offer and the actual usage of the resource or service.
        gtin12: The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        acceptedPaymentMethod: The payment method(s) that are accepted in general by an organization, or for some specific demand or offer.
        review: A review of the item.
        availabilityStarts: The beginning of the availability of the product or service included in the offer.
        mpn: The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.
        leaseLength: Length of the lease for some [[Accommodation]], either particular to some [[Offer]] or in some cases intrinsic to the property.
        priceSpecification: One or more detailed price specifications, indicating the unit price and delivery or payment charges.
        reviews: Review of the item.
        gtin: A Global Trade Item Number ([GTIN](https://www.gs1.org/standards/id-keys/gtin)). GTINs identify trade items, including products and services, using numeric identification codes.

A correct [[gtin]] value should be a valid GTIN, which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a "GS1 Digital Link" URL based on such a string. The numeric component should also have a [valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator) and meet the other rules for valid GTINs. See also [GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) and [Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number) for more details. Left-padding of the gtin values is not required or encouraged. The [[gtin]] property generalizes the earlier [[gtin8]], [[gtin12]], [[gtin13]], and [[gtin14]] properties.

The GS1 [digital link specifications](https://www.gs1.org/standards/Digital-Link/) expresses GTINs as URLs (URIs, IRIs, etc.).
Digital Links should be populated into the [[hasGS1DigitalLink]] attribute.

Note also that this is a definition for how to include GTINs in Schema.org data, and not a definition of GTINs in general - see the GS1 documentation for authoritative details.
        availableAtOrFrom: The place(s) from which the offer can be obtained (e.g. store locations).
        addOn: An additional offer that can only be obtained in combination with the first base offer (e.g. supplements and extensions that are available for a surcharge).
        businessFunction: The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.
        gtin8: The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        seller: An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.
        validThrough: The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.
        eligibleQuantity: The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.
        eligibleDuration: The duration for which the given offer is valid.
        itemOffered: An item being offered (or demanded). The transactional nature of the offer or demand is documented using [[businessFunction]], e.g. sell, lease etc. While several common expected types are listed explicitly in this definition, others can be used. Using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
        warranty: The warranty promise(s) included in the offer.
        eligibleRegion: The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.\
\
See also [[ineligibleRegion]].
    
        offeredBy: A pointer to the organization or person making the offer.
        aggregateRating: The overall rating, based on a collection of reviews or ratings, of the item.
        sku: The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.
        areaServed: The geographic area where a service or offered item is provided.
    '''
    class_: Literal['https://schema.org/Offer'] = Field( # type: ignore
        default='https://schema.org/Offer',
        alias='@type',
        serialization_alias='@type'
    )
    asin: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'asin',
            'https://schema.org/asin'
        ),
        serialization_alias='https://schema.org/asin'
    )
    hasAdultConsideration: Optional[Union['AdultOrientedEnumeration', List['AdultOrientedEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasAdultConsideration',
            'https://schema.org/hasAdultConsideration'
        ),
        serialization_alias='https://schema.org/hasAdultConsideration'
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
    shippingDetails: Optional[Union['OfferShippingDetails', List['OfferShippingDetails']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'shippingDetails',
            'https://schema.org/shippingDetails'
        ),
        serialization_alias='https://schema.org/shippingDetails'
    )
    availabilityEnds: Optional[Union[date, List[date], time, List[time], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availabilityEnds',
            'https://schema.org/availabilityEnds'
        ),
        serialization_alias='https://schema.org/availabilityEnds'
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
    mobileUrl: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mobileUrl',
            'https://schema.org/mobileUrl'
        ),
        serialization_alias='https://schema.org/mobileUrl'
    )
    validForMemberTier: Optional[Union['MemberProgramTier', List['MemberProgramTier']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'validForMemberTier',
            'https://schema.org/validForMemberTier'
        ),
        serialization_alias='https://schema.org/validForMemberTier'
    )
    deliveryLeadTime: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'deliveryLeadTime',
            'https://schema.org/deliveryLeadTime'
        ),
        serialization_alias='https://schema.org/deliveryLeadTime'
    )
    isFamilyFriendly: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isFamilyFriendly',
            'https://schema.org/isFamilyFriendly'
        ),
        serialization_alias='https://schema.org/isFamilyFriendly'
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
    hasGS1DigitalLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasGS1DigitalLink',
            'https://schema.org/hasGS1DigitalLink'
        ),
        serialization_alias='https://schema.org/hasGS1DigitalLink'
    )
    hasMeasurement: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMeasurement',
            'https://schema.org/hasMeasurement'
        ),
        serialization_alias='https://schema.org/hasMeasurement'
    )
    inventoryLevel: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inventoryLevel',
            'https://schema.org/inventoryLevel'
        ),
        serialization_alias='https://schema.org/inventoryLevel'
    )
    itemCondition: Optional[Union['OfferItemCondition', List['OfferItemCondition']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemCondition',
            'https://schema.org/itemCondition'
        ),
        serialization_alias='https://schema.org/itemCondition'
    )
    price: Optional[Union[str, List[str], float, List[float]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'price',
            'https://schema.org/price'
        ),
        serialization_alias='https://schema.org/price'
    )
    additionalProperty: Optional[Union['PropertyValue', List['PropertyValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalProperty',
            'https://schema.org/additionalProperty'
        ),
        serialization_alias='https://schema.org/additionalProperty'
    )
    checkoutPageURLTemplate: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'checkoutPageURLTemplate',
            'https://schema.org/checkoutPageURLTemplate'
        ),
        serialization_alias='https://schema.org/checkoutPageURLTemplate'
    )
    category: Optional[Union['PhysicalActivityCategory', List['PhysicalActivityCategory'], 'CategoryCode', List['CategoryCode'], str, List[str], 'Thing', List['Thing'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'category',
            'https://schema.org/category'
        ),
        serialization_alias='https://schema.org/category'
    )
    hasMerchantReturnPolicy: Optional[Union['MerchantReturnPolicy', List['MerchantReturnPolicy']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMerchantReturnPolicy',
            'https://schema.org/hasMerchantReturnPolicy'
        ),
        serialization_alias='https://schema.org/hasMerchantReturnPolicy'
    )
    priceCurrency: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceCurrency',
            'https://schema.org/priceCurrency'
        ),
        serialization_alias='https://schema.org/priceCurrency'
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
    priceValidUntil: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceValidUntil',
            'https://schema.org/priceValidUntil'
        ),
        serialization_alias='https://schema.org/priceValidUntil'
    )
    serialNumber: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'serialNumber',
            'https://schema.org/serialNumber'
        ),
        serialization_alias='https://schema.org/serialNumber'
    )
    advanceBookingRequirement: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'advanceBookingRequirement',
            'https://schema.org/advanceBookingRequirement'
        ),
        serialization_alias='https://schema.org/advanceBookingRequirement'
    )
    gtin12: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gtin12',
            'https://schema.org/gtin12'
        ),
        serialization_alias='https://schema.org/gtin12'
    )
    acceptedPaymentMethod: Optional[Union[str, List[str], 'PaymentMethod', List['PaymentMethod'], 'LoanOrCredit', List['LoanOrCredit']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'acceptedPaymentMethod',
            'https://schema.org/acceptedPaymentMethod'
        ),
        serialization_alias='https://schema.org/acceptedPaymentMethod'
    )
    review: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'review',
            'https://schema.org/review'
        ),
        serialization_alias='https://schema.org/review'
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
    leaseLength: Optional[Union['QuantitativeValue', List['QuantitativeValue'], 'Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'leaseLength',
            'https://schema.org/leaseLength'
        ),
        serialization_alias='https://schema.org/leaseLength'
    )
    priceSpecification: Optional[Union['PriceSpecification', List['PriceSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceSpecification',
            'https://schema.org/priceSpecification'
        ),
        serialization_alias='https://schema.org/priceSpecification'
    )
    reviews: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviews',
            'https://schema.org/reviews'
        ),
        serialization_alias='https://schema.org/reviews'
    )
    gtin: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gtin',
            'https://schema.org/gtin'
        ),
        serialization_alias='https://schema.org/gtin'
    )
    availableAtOrFrom: Optional[Union['Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'availableAtOrFrom',
            'https://schema.org/availableAtOrFrom'
        ),
        serialization_alias='https://schema.org/availableAtOrFrom'
    )
    addOn: Optional[Union['Offer', List['Offer']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'addOn',
            'https://schema.org/addOn'
        ),
        serialization_alias='https://schema.org/addOn'
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
    warranty: Optional[Union['WarrantyPromise', List['WarrantyPromise']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'warranty',
            'https://schema.org/warranty'
        ),
        serialization_alias='https://schema.org/warranty'
    )
    eligibleRegion: Optional[Union['GeoShape', List['GeoShape'], str, List[str], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'eligibleRegion',
            'https://schema.org/eligibleRegion'
        ),
        serialization_alias='https://schema.org/eligibleRegion'
    )
    offeredBy: Optional[Union['Organization', List['Organization'], 'Person', List['Person']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'offeredBy',
            'https://schema.org/offeredBy'
        ),
        serialization_alias='https://schema.org/offeredBy'
    )
    aggregateRating: Optional[Union['AggregateRating', List['AggregateRating']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'aggregateRating',
            'https://schema.org/aggregateRating'
        ),
        serialization_alias='https://schema.org/aggregateRating'
    )
    sku: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'sku',
            'https://schema.org/sku'
        ),
        serialization_alias='https://schema.org/sku'
    )
    areaServed: Optional[Union['GeoShape', List['GeoShape'], str, List[str], 'AdministrativeArea', List['AdministrativeArea'], 'Place', List['Place']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'areaServed',
            'https://schema.org/areaServed'
        ),
        serialization_alias='https://schema.org/areaServed'
    )
