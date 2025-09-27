from typing import List, Literal, Optional, Union
from datetime import date, datetime, time
from pydantic import field_serializer, AliasChoices, Field, HttpUrl
from schemaorg_models.intangible import Intangible

from schemaorg_models.member_program_tier import MemberProgramTier
from schemaorg_models.place import Place
from schemaorg_models.thing import Thing
from schemaorg_models.merchant_return_policy import MerchantReturnPolicy
from schemaorg_models.payment_method import PaymentMethod
from schemaorg_models.organization import Organization
from schemaorg_models.person import Person
from schemaorg_models.event import Event
from schemaorg_models.service import Service
from schemaorg_models.product import Product
from schemaorg_models.menu_item import MenuItem
from schemaorg_models.creative_work import CreativeWork
from schemaorg_models.administrative_area import AdministrativeArea

class Offer(Intangible):
    """
An offer to transfer some rights to an item or to provide a service — for example, an offer to sell tickets to an event, to rent the DVD of a movie, to stream a TV show over the internet, to repair a motorcycle, or to loan a book.\
\
Note: As the [[businessFunction]] property, which identifies the form of offer (e.g. sell, lease, repair, dispose), defaults to http://purl.org/goodrelations/v1#Sell; an Offer without a defined businessFunction value can be assumed to be an offer to sell.\
\
For [GTIN](http://www.gs1.org/barcodes/technical/idkeys/gtin)-related fields, see [Check Digit calculator](http://www.gs1.org/barcodes/support/check_digit_calculator) and [validation guide](http://www.gs1us.org/resources/standards/gtin-validation-guide) from [GS1](http://www.gs1.org/).
    """
    class_: Literal['https://schema.org/Offer'] = Field('class', alias='class', serialization_alias='class') # type: ignore
    asin: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(default=None,validation_alias=AliasChoices('asin', 'https://schema.org/asin'), serialization_alias='https://schema.org/asin')
    @field_serializer('asin')
    def asin2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    hasAdultConsideration: Optional[Union["AdultOrientedEnumeration", List["AdultOrientedEnumeration"]]] = Field(default=None,validation_alias=AliasChoices('hasAdultConsideration', 'https://schema.org/hasAdultConsideration'), serialization_alias='https://schema.org/hasAdultConsideration')
    eligibleTransactionVolume: Optional[Union["PriceSpecification", List["PriceSpecification"]]] = Field(default=None,validation_alias=AliasChoices('eligibleTransactionVolume', 'https://schema.org/eligibleTransactionVolume'), serialization_alias='https://schema.org/eligibleTransactionVolume')
    includesObject: Optional[Union["TypeAndQuantityNode", List["TypeAndQuantityNode"]]] = Field(default=None,validation_alias=AliasChoices('includesObject', 'https://schema.org/includesObject'), serialization_alias='https://schema.org/includesObject')
    eligibleCustomerType: Optional[Union["BusinessEntityType", List["BusinessEntityType"]]] = Field(default=None,validation_alias=AliasChoices('eligibleCustomerType', 'https://schema.org/eligibleCustomerType'), serialization_alias='https://schema.org/eligibleCustomerType')
    shippingDetails: Optional[Union["OfferShippingDetails", List["OfferShippingDetails"]]] = Field(default=None,validation_alias=AliasChoices('shippingDetails', 'https://schema.org/shippingDetails'), serialization_alias='https://schema.org/shippingDetails')
    availabilityEnds: Optional[Union[date, List[date], time, List[time], datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('availabilityEnds', 'https://schema.org/availabilityEnds'), serialization_alias='https://schema.org/availabilityEnds')
    availableDeliveryMethod: Optional[Union["DeliveryMethod", List["DeliveryMethod"]]] = Field(default=None,validation_alias=AliasChoices('availableDeliveryMethod', 'https://schema.org/availableDeliveryMethod'), serialization_alias='https://schema.org/availableDeliveryMethod')
    validFrom: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(default=None,validation_alias=AliasChoices('validFrom', 'https://schema.org/validFrom'), serialization_alias='https://schema.org/validFrom')
    mobileUrl: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('mobileUrl', 'https://schema.org/mobileUrl'), serialization_alias='https://schema.org/mobileUrl')
    validForMemberTier: Optional[Union[MemberProgramTier, List[MemberProgramTier]]] = Field(default=None,validation_alias=AliasChoices('validForMemberTier', 'https://schema.org/validForMemberTier'), serialization_alias='https://schema.org/validForMemberTier')
    deliveryLeadTime: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('deliveryLeadTime', 'https://schema.org/deliveryLeadTime'), serialization_alias='https://schema.org/deliveryLeadTime')
    isFamilyFriendly: Optional[Union[bool, List[bool]]] = Field(default=None,validation_alias=AliasChoices('isFamilyFriendly', 'https://schema.org/isFamilyFriendly'), serialization_alias='https://schema.org/isFamilyFriendly')
    ineligibleRegion: Optional[Union[str, List[str], Place, List[Place], "GeoShape", List["GeoShape"]]] = Field(default=None,validation_alias=AliasChoices('ineligibleRegion', 'https://schema.org/ineligibleRegion'), serialization_alias='https://schema.org/ineligibleRegion')
    gtin13: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('gtin13', 'https://schema.org/gtin13'), serialization_alias='https://schema.org/gtin13')
    hasGS1DigitalLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('hasGS1DigitalLink', 'https://schema.org/hasGS1DigitalLink'), serialization_alias='https://schema.org/hasGS1DigitalLink')
    @field_serializer('hasGS1DigitalLink')
    def hasGS1DigitalLink2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    hasMeasurement: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('hasMeasurement', 'https://schema.org/hasMeasurement'), serialization_alias='https://schema.org/hasMeasurement')
    inventoryLevel: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('inventoryLevel', 'https://schema.org/inventoryLevel'), serialization_alias='https://schema.org/inventoryLevel')
    itemCondition: Optional[Union["OfferItemCondition", List["OfferItemCondition"]]] = Field(default=None,validation_alias=AliasChoices('itemCondition', 'https://schema.org/itemCondition'), serialization_alias='https://schema.org/itemCondition')
    price: Optional[Union[str, List[str], float, List[float]]] = Field(default=None,validation_alias=AliasChoices('price', 'https://schema.org/price'), serialization_alias='https://schema.org/price')
    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = Field(default=None,validation_alias=AliasChoices('additionalProperty', 'https://schema.org/additionalProperty'), serialization_alias='https://schema.org/additionalProperty')
    checkoutPageURLTemplate: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('checkoutPageURLTemplate', 'https://schema.org/checkoutPageURLTemplate'), serialization_alias='https://schema.org/checkoutPageURLTemplate')
    category: Optional[Union["PhysicalActivityCategory", List["PhysicalActivityCategory"], "CategoryCode", List["CategoryCode"], str, List[str], Thing, List[Thing], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('category', 'https://schema.org/category'), serialization_alias='https://schema.org/category')
    @field_serializer('category')
    def category2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    hasMerchantReturnPolicy: Optional[Union[MerchantReturnPolicy, List[MerchantReturnPolicy]]] = Field(default=None,validation_alias=AliasChoices('hasMerchantReturnPolicy', 'https://schema.org/hasMerchantReturnPolicy'), serialization_alias='https://schema.org/hasMerchantReturnPolicy')
    priceCurrency: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('priceCurrency', 'https://schema.org/priceCurrency'), serialization_alias='https://schema.org/priceCurrency')
    availability: Optional[Union["ItemAvailability", List["ItemAvailability"]]] = Field(default=None,validation_alias=AliasChoices('availability', 'https://schema.org/availability'), serialization_alias='https://schema.org/availability')
    gtin14: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('gtin14', 'https://schema.org/gtin14'), serialization_alias='https://schema.org/gtin14')
    priceValidUntil: Optional[Union[date, List[date]]] = Field(default=None,validation_alias=AliasChoices('priceValidUntil', 'https://schema.org/priceValidUntil'), serialization_alias='https://schema.org/priceValidUntil')
    serialNumber: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('serialNumber', 'https://schema.org/serialNumber'), serialization_alias='https://schema.org/serialNumber')
    advanceBookingRequirement: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('advanceBookingRequirement', 'https://schema.org/advanceBookingRequirement'), serialization_alias='https://schema.org/advanceBookingRequirement')
    gtin12: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('gtin12', 'https://schema.org/gtin12'), serialization_alias='https://schema.org/gtin12')
    acceptedPaymentMethod: Optional[Union[str, List[str], PaymentMethod, List[PaymentMethod], "LoanOrCredit", List["LoanOrCredit"]]] = Field(default=None,validation_alias=AliasChoices('acceptedPaymentMethod', 'https://schema.org/acceptedPaymentMethod'), serialization_alias='https://schema.org/acceptedPaymentMethod')
    review: Optional[Union["Review", List["Review"]]] = Field(default=None,validation_alias=AliasChoices('review', 'https://schema.org/review'), serialization_alias='https://schema.org/review')
    availabilityStarts: Optional[Union[datetime, List[datetime], date, List[date], time, List[time]]] = Field(default=None,validation_alias=AliasChoices('availabilityStarts', 'https://schema.org/availabilityStarts'), serialization_alias='https://schema.org/availabilityStarts')
    mpn: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('mpn', 'https://schema.org/mpn'), serialization_alias='https://schema.org/mpn')
    leaseLength: Optional[Union["QuantitativeValue", List["QuantitativeValue"], "Duration", List["Duration"]]] = Field(default=None,validation_alias=AliasChoices('leaseLength', 'https://schema.org/leaseLength'), serialization_alias='https://schema.org/leaseLength')
    priceSpecification: Optional[Union["PriceSpecification", List["PriceSpecification"]]] = Field(default=None,validation_alias=AliasChoices('priceSpecification', 'https://schema.org/priceSpecification'), serialization_alias='https://schema.org/priceSpecification')
    reviews: Optional[Union["Review", List["Review"]]] = Field(default=None,validation_alias=AliasChoices('reviews', 'https://schema.org/reviews'), serialization_alias='https://schema.org/reviews')
    gtin: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(default=None,validation_alias=AliasChoices('gtin', 'https://schema.org/gtin'), serialization_alias='https://schema.org/gtin')
    @field_serializer('gtin')
    def gtin2str(self, val) -> str | List[str]:
        def _to_str(value):
            if isinstance(value, HttpUrl):
                return str(value)
            return value

        if isinstance(val, list):
            return [_to_str(i) for i in val]
        return _to_str(val)

    availableAtOrFrom: Optional[Union[Place, List[Place]]] = Field(default=None,validation_alias=AliasChoices('availableAtOrFrom', 'https://schema.org/availableAtOrFrom'), serialization_alias='https://schema.org/availableAtOrFrom')
    addOn: Optional[Union["Offer", List["Offer"]]] = Field(default=None,validation_alias=AliasChoices('addOn', 'https://schema.org/addOn'), serialization_alias='https://schema.org/addOn')
    businessFunction: Optional[Union["BusinessFunction", List["BusinessFunction"]]] = Field(default=None,validation_alias=AliasChoices('businessFunction', 'https://schema.org/businessFunction'), serialization_alias='https://schema.org/businessFunction')
    gtin8: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('gtin8', 'https://schema.org/gtin8'), serialization_alias='https://schema.org/gtin8')
    seller: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('seller', 'https://schema.org/seller'), serialization_alias='https://schema.org/seller')
    validThrough: Optional[Union[datetime, List[datetime], date, List[date]]] = Field(default=None,validation_alias=AliasChoices('validThrough', 'https://schema.org/validThrough'), serialization_alias='https://schema.org/validThrough')
    eligibleQuantity: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('eligibleQuantity', 'https://schema.org/eligibleQuantity'), serialization_alias='https://schema.org/eligibleQuantity')
    eligibleDuration: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(default=None,validation_alias=AliasChoices('eligibleDuration', 'https://schema.org/eligibleDuration'), serialization_alias='https://schema.org/eligibleDuration')
    itemOffered: Optional[Union[Event, List[Event], Service, List[Service], "AggregateOffer", List["AggregateOffer"], Product, List[Product], MenuItem, List[MenuItem], CreativeWork, List[CreativeWork], "Trip", List["Trip"]]] = Field(default=None,validation_alias=AliasChoices('itemOffered', 'https://schema.org/itemOffered'), serialization_alias='https://schema.org/itemOffered')
    warranty: Optional[Union["WarrantyPromise", List["WarrantyPromise"]]] = Field(default=None,validation_alias=AliasChoices('warranty', 'https://schema.org/warranty'), serialization_alias='https://schema.org/warranty')
    eligibleRegion: Optional[Union["GeoShape", List["GeoShape"], str, List[str], Place, List[Place]]] = Field(default=None,validation_alias=AliasChoices('eligibleRegion', 'https://schema.org/eligibleRegion'), serialization_alias='https://schema.org/eligibleRegion')
    offeredBy: Optional[Union[Organization, List[Organization], Person, List[Person]]] = Field(default=None,validation_alias=AliasChoices('offeredBy', 'https://schema.org/offeredBy'), serialization_alias='https://schema.org/offeredBy')
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = Field(default=None,validation_alias=AliasChoices('aggregateRating', 'https://schema.org/aggregateRating'), serialization_alias='https://schema.org/aggregateRating')
    sku: Optional[Union[str, List[str]]] = Field(default=None,validation_alias=AliasChoices('sku', 'https://schema.org/sku'), serialization_alias='https://schema.org/sku')
    areaServed: Optional[Union["GeoShape", List["GeoShape"], str, List[str], AdministrativeArea, List[AdministrativeArea], Place, List[Place]]] = Field(default=None,validation_alias=AliasChoices('areaServed', 'https://schema.org/areaServed'), serialization_alias='https://schema.org/areaServed')
