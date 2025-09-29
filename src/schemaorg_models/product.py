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
from .thing import Thing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .country import Country
    from .offer_item_condition import OfferItemCondition
    from .product_group import ProductGroup
    from .adult_oriented_enumeration import AdultOrientedEnumeration
    from .image_object import ImageObject
    from .brand import Brand
    from .energy_consumption_details import EnergyConsumptionDetails
    from .merchant_return_policy import MerchantReturnPolicy
    from .distance import Distance
    from .organization import Organization
    from .property_value import PropertyValue
    from .item_list import ItemList
    from .defined_term import DefinedTerm
    from .demand import Demand
    from .certification import Certification
    from .offer import Offer
    from .review import Review
    from .web_content import WebContent
    from .aggregate_rating import AggregateRating
    from .list_item import ListItem
    from .product_return_policy import ProductReturnPolicy
    from .size_specification import SizeSpecification
    from .audience import Audience
    from .category_code import CategoryCode
    from .grant import Grant
    from .mass import Mass
    from .service import Service
    from .physical_activity_category import PhysicalActivityCategory
    from .product_model import ProductModel
    from .quantitative_value import QuantitativeValue

class Product(Thing):
    '''
    Any offered product or service. For example: a pair of shoes; a concert ticket; the rental of a car; a haircut; or an episode of a TV show streamed online.

    Attributes:
        reviews: Review of the item.
        inProductGroupWithID: Indicates the [[productGroupID]] for a [[ProductGroup]] that this product [[isVariantOf]]. 
        gtin: A Global Trade Item Number ([GTIN](https://www.gs1.org/standards/id-keys/gtin)). GTINs identify trade items, including products and services, using numeric identification codes.

A correct [[gtin]] value should be a valid GTIN, which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a "GS1 Digital Link" URL based on such a string. The numeric component should also have a [valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator) and meet the other rules for valid GTINs. See also [GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) and [Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number) for more details. Left-padding of the gtin values is not required or encouraged. The [[gtin]] property generalizes the earlier [[gtin8]], [[gtin12]], [[gtin13]], and [[gtin14]] properties.

The GS1 [digital link specifications](https://www.gs1.org/standards/Digital-Link/) expresses GTINs as URLs (URIs, IRIs, etc.).
Digital Links should be populated into the [[hasGS1DigitalLink]] attribute.

Note also that this is a definition for how to include GTINs in Schema.org data, and not a definition of GTINs in general - see the GS1 documentation for authoritative details.
        gtin8: The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        isRelatedTo: A pointer to another, somehow related product (or multiple products).
        colorSwatch: A color swatch image, visualizing the color of a [[Product]]. Should match the textual description specified in the [[color]] property. This can be a URL or a fully described ImageObject.
        asin: An Amazon Standard Identification Number (ASIN) is a 10-character alphanumeric unique identifier assigned by Amazon.com and its partners for product identification within the Amazon organization (summary from [Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s article).

Note also that this is a definition for how to include ASINs in Schema.org data, and not a definition of ASINs in general - see documentation from Amazon for authoritative details.
ASINs are most commonly encoded as text strings, but the [asin] property supports URL/URI as potential values too.
        pattern: A pattern that something has, for example 'polka dot', 'striped', 'Canadian flag'. Values are typically expressed as text, although links to controlled value schemes are also supported.
        awards: Awards won by or for this item.
        productionDate: The date of production of the item, e.g. vehicle.
        model: The model of the product. Use with the URL of a ProductModel or a textual representation of the model identifier. The URL of the ProductModel can be from an external source. It is recommended to additionally provide strong product identifiers via the gtin8/gtin13/gtin14 and mpn properties.
        hasCertification: Certification information about a product, organization, service, place, or person.
        isVariantOf: Indicates the kind of product that this is a variant of. In the case of [[ProductModel]], this is a pointer (from a ProductModel) to a base product from which this product is a variant. It is safe to infer that the variant inherits all product features from the base model, unless defined locally. This is not transitive. In the case of a [[ProductGroup]], the group description also serves as a template, representing a set of Products that vary on explicitly defined, specific dimensions only (so it defines both a set of variants, as well as which values distinguish amongst those variants). When used with [[ProductGroup]], this property can apply to any [[Product]] included in the group.
        isFamilyFriendly: Indicates whether this content is family friendly.
        logo: An associated logo.
        aggregateRating: The overall rating, based on a collection of reviews or ratings, of the item.
        sku: The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.
        negativeNotes: Provides negative considerations regarding something, most typically in pro/con lists for reviews (alongside [[positiveNotes]]). For symmetry 

In the case of a [[Review]], the property describes the [[itemReviewed]] from the perspective of the review; in the case of a [[Product]], the product itself is being described. Since product descriptions 
tend to emphasise positive claims, it may be relatively unusual to find [[negativeNotes]] used in this way. Nevertheless for the sake of symmetry, [[negativeNotes]] can be used on [[Product]].

The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most negative is at the beginning of the list).
        width: The width of the item.
        color: The color of the product.
        hasAdultConsideration: Used to tag an item to be intended or suitable for consumption or use by adults only.
        purchaseDate: The date the item, e.g. vehicle, was purchased by the current owner.
        countryOfAssembly: The place where the product was assembled.
        slogan: A slogan or motto associated with the item.
        mobileUrl: The [[mobileUrl]] property is provided for specific situations in which data consumers need to determine whether one of several provided URLs is a dedicated 'mobile site'.

To discourage over-use, and reflecting intial usecases, the property is expected only on [[Product]] and [[Offer]], rather than [[Thing]]. The general trend in web technology is towards [responsive design](https://en.wikipedia.org/wiki/Responsive_web_design) in which content can be flexibly adapted to a wide range of browsing environments. Pages and sites referenced with the long-established [[url]] property should ideally also be usable on a wide variety of devices, including mobile phones. In most cases, it would be pointless and counter productive to attempt to update all [[url]] markup to use [[mobileUrl]] for more mobile-oriented pages. The property is intended for the case when items (primarily [[Product]] and [[Offer]]) have extra URLs hosted on an additional "mobile site" alongside the main one. It should not be taken as an endorsement of this publication style.
    
        keywords: Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.
        hasProductReturnPolicy: Indicates a ProductReturnPolicy that may be applicable.
        award: An award won by or for this item.
        isSimilarTo: A pointer to another, functionally similar product (or multiple products).
        additionalProperty: A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org.\
\
Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.

        productID: The product identifier, such as ISBN. For example: ``` meta itemprop="productID" content="isbn:123-456-789" ```.
        gtin13: The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        offers: An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
      
        audience: An intended audience, i.e. a group for whom something was created.
        hasGS1DigitalLink: The <a href="https://www.gs1.org/standards/gs1-digital-link">GS1 digital link</a> associated with the object. This URL should conform to the particular requirements of digital links. The link should only contain the Application Identifiers (AIs) that are relevant for the entity being annotated, for instance a [[Product]] or an [[Organization]], and for the correct granularity. In particular, for products:<ul><li>A Digital Link that contains a serial number (AI <code>21</code>) should only be present on instances of [[IndividualProduct]]</li><li>A Digital Link that contains a lot number (AI <code>10</code>) should be annotated as [[SomeProduct]] if only products from that lot are sold, or [[IndividualProduct]] if there is only a specific product.</li><li>A Digital Link that contains a global model number (AI <code>8013</code>)  should be attached to a [[Product]] or a [[ProductModel]].</li></ul> Other item types should be adapted similarly.
        isConsumableFor: A pointer to another product (or multiple products) for which this product is a consumable.
        funding: A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        hasMeasurement: A measurement of an item, For example, the inseam of pants, the wheel size of a bicycle, the gauge of a screw, or the carbon footprint measured for certification by an authority. Usually an exact measurement, but can also be a range of measurements for adjustable products, for example belts and ski bindings.
        hasEnergyConsumptionDetails: Defines the energy efficiency Category (also known as "class" or "rating") for a product according to an international energy efficiency standard.
        brand: The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.
        countryOfLastProcessing: The place where the item (typically [[Product]]) was last processed and tested before importation.
        itemCondition: A predefined value from OfferItemCondition specifying the condition of the product or service, or the products or services included in the offer. Also used for product return policies to specify the condition of products accepted for returns.
        material: A material that something is made from, e.g. leather, wool, cotton, paper.
        mpn: The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.
        height: The height of the item.
        releaseDate: The release date of a product or product model. This can be used to distinguish the exact variant of a product.
        size: A standardized size of a product or creative work, specified either through a simple textual string (for example 'XL', '32Wx34L'), a  QuantitativeValue with a unitCode, or a comprehensive and structured [[SizeSpecification]]; in other cases, the [[width]], [[height]], [[depth]] and [[weight]] properties may be more applicable. 
        category: A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.
        weight: The weight of the product or person.
        hasMerchantReturnPolicy: Specifies a MerchantReturnPolicy that may be applicable.
        nsn: Indicates the [NATO stock number](https://en.wikipedia.org/wiki/NATO_Stock_Number) (nsn) of a [[Product]]. 
        gtin14: The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        gtin12: The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        manufacturer: The manufacturer of the product.
        review: A review of the item.
        depth: The depth of the item.
        positiveNotes: Provides positive considerations regarding something, for example product highlights or (alongside [[negativeNotes]]) pro/con lists for reviews.

In the case of a [[Review]], the property describes the [[itemReviewed]] from the perspective of the review; in the case of a [[Product]], the product itself is being described.

The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most positive is at the beginning of the list).
        countryOfOrigin: The country of origin of something, including products as well as creative  works such as movie and TV content.

In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties such as [[contentLocation]] and [[locationCreated]] may be more applicable.

In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.
        isAccessoryOrSparePartFor: A pointer to another product (or multiple products) for which this product is an accessory or spare part.
    '''
    class_: Literal['https://schema.org/Product'] = Field( # type: ignore
        default='https://schema.org/Product',
        alias='@type',
        serialization_alias='@type'
    )
    reviews: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'reviews',
            'https://schema.org/reviews'
        ),
        serialization_alias='https://schema.org/reviews'
    )
    inProductGroupWithID: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'inProductGroupWithID',
            'https://schema.org/inProductGroupWithID'
        ),
        serialization_alias='https://schema.org/inProductGroupWithID'
    )
    gtin: Optional[Union[str, List[str], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gtin',
            'https://schema.org/gtin'
        ),
        serialization_alias='https://schema.org/gtin'
    )
    gtin8: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gtin8',
            'https://schema.org/gtin8'
        ),
        serialization_alias='https://schema.org/gtin8'
    )
    isRelatedTo: Optional[Union['Service', List['Service'], 'Product', List['Product']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isRelatedTo',
            'https://schema.org/isRelatedTo'
        ),
        serialization_alias='https://schema.org/isRelatedTo'
    )
    colorSwatch: Optional[Union['ImageObject', List['ImageObject'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'colorSwatch',
            'https://schema.org/colorSwatch'
        ),
        serialization_alias='https://schema.org/colorSwatch'
    )
    asin: Optional[Union[HttpUrl, List[HttpUrl], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'asin',
            'https://schema.org/asin'
        ),
        serialization_alias='https://schema.org/asin'
    )
    pattern: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'pattern',
            'https://schema.org/pattern'
        ),
        serialization_alias='https://schema.org/pattern'
    )
    awards: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'awards',
            'https://schema.org/awards'
        ),
        serialization_alias='https://schema.org/awards'
    )
    productionDate: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productionDate',
            'https://schema.org/productionDate'
        ),
        serialization_alias='https://schema.org/productionDate'
    )
    model: Optional[Union['ProductModel', List['ProductModel'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'model',
            'https://schema.org/model'
        ),
        serialization_alias='https://schema.org/model'
    )
    hasCertification: Optional[Union['Certification', List['Certification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCertification',
            'https://schema.org/hasCertification'
        ),
        serialization_alias='https://schema.org/hasCertification'
    )
    isVariantOf: Optional[Union['ProductModel', List['ProductModel'], 'ProductGroup', List['ProductGroup']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isVariantOf',
            'https://schema.org/isVariantOf'
        ),
        serialization_alias='https://schema.org/isVariantOf'
    )
    isFamilyFriendly: Optional[Union[bool, List[bool]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isFamilyFriendly',
            'https://schema.org/isFamilyFriendly'
        ),
        serialization_alias='https://schema.org/isFamilyFriendly'
    )
    logo: Optional[Union[HttpUrl, List[HttpUrl], 'ImageObject', List['ImageObject']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'logo',
            'https://schema.org/logo'
        ),
        serialization_alias='https://schema.org/logo'
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
    negativeNotes: Optional[Union['ListItem', List['ListItem'], 'WebContent', List['WebContent'], 'ItemList', List['ItemList'], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'negativeNotes',
            'https://schema.org/negativeNotes'
        ),
        serialization_alias='https://schema.org/negativeNotes'
    )
    width: Optional[Union['QuantitativeValue', List['QuantitativeValue'], 'Distance', List['Distance']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'width',
            'https://schema.org/width'
        ),
        serialization_alias='https://schema.org/width'
    )
    color: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'color',
            'https://schema.org/color'
        ),
        serialization_alias='https://schema.org/color'
    )
    hasAdultConsideration: Optional[Union['AdultOrientedEnumeration', List['AdultOrientedEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasAdultConsideration',
            'https://schema.org/hasAdultConsideration'
        ),
        serialization_alias='https://schema.org/hasAdultConsideration'
    )
    purchaseDate: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'purchaseDate',
            'https://schema.org/purchaseDate'
        ),
        serialization_alias='https://schema.org/purchaseDate'
    )
    countryOfAssembly: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countryOfAssembly',
            'https://schema.org/countryOfAssembly'
        ),
        serialization_alias='https://schema.org/countryOfAssembly'
    )
    slogan: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'slogan',
            'https://schema.org/slogan'
        ),
        serialization_alias='https://schema.org/slogan'
    )
    mobileUrl: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mobileUrl',
            'https://schema.org/mobileUrl'
        ),
        serialization_alias='https://schema.org/mobileUrl'
    )
    keywords: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], 'DefinedTerm', List['DefinedTerm']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'keywords',
            'https://schema.org/keywords'
        ),
        serialization_alias='https://schema.org/keywords'
    )
    hasProductReturnPolicy: Optional[Union['ProductReturnPolicy', List['ProductReturnPolicy']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasProductReturnPolicy',
            'https://schema.org/hasProductReturnPolicy'
        ),
        serialization_alias='https://schema.org/hasProductReturnPolicy'
    )
    award: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'award',
            'https://schema.org/award'
        ),
        serialization_alias='https://schema.org/award'
    )
    isSimilarTo: Optional[Union['Service', List['Service'], 'Product', List['Product']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isSimilarTo',
            'https://schema.org/isSimilarTo'
        ),
        serialization_alias='https://schema.org/isSimilarTo'
    )
    additionalProperty: Optional[Union['PropertyValue', List['PropertyValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'additionalProperty',
            'https://schema.org/additionalProperty'
        ),
        serialization_alias='https://schema.org/additionalProperty'
    )
    productID: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'productID',
            'https://schema.org/productID'
        ),
        serialization_alias='https://schema.org/productID'
    )
    gtin13: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gtin13',
            'https://schema.org/gtin13'
        ),
        serialization_alias='https://schema.org/gtin13'
    )
    offers: Optional[Union['Demand', List['Demand'], 'Offer', List['Offer']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'offers',
            'https://schema.org/offers'
        ),
        serialization_alias='https://schema.org/offers'
    )
    audience: Optional[Union['Audience', List['Audience']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'audience',
            'https://schema.org/audience'
        ),
        serialization_alias='https://schema.org/audience'
    )
    hasGS1DigitalLink: Optional[Union[HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasGS1DigitalLink',
            'https://schema.org/hasGS1DigitalLink'
        ),
        serialization_alias='https://schema.org/hasGS1DigitalLink'
    )
    isConsumableFor: Optional[Union['Product', List['Product']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isConsumableFor',
            'https://schema.org/isConsumableFor'
        ),
        serialization_alias='https://schema.org/isConsumableFor'
    )
    funding: Optional[Union['Grant', List['Grant']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funding',
            'https://schema.org/funding'
        ),
        serialization_alias='https://schema.org/funding'
    )
    hasMeasurement: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMeasurement',
            'https://schema.org/hasMeasurement'
        ),
        serialization_alias='https://schema.org/hasMeasurement'
    )
    hasEnergyConsumptionDetails: Optional[Union['EnergyConsumptionDetails', List['EnergyConsumptionDetails']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasEnergyConsumptionDetails',
            'https://schema.org/hasEnergyConsumptionDetails'
        ),
        serialization_alias='https://schema.org/hasEnergyConsumptionDetails'
    )
    brand: Optional[Union['Organization', List['Organization'], 'Brand', List['Brand']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'brand',
            'https://schema.org/brand'
        ),
        serialization_alias='https://schema.org/brand'
    )
    countryOfLastProcessing: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countryOfLastProcessing',
            'https://schema.org/countryOfLastProcessing'
        ),
        serialization_alias='https://schema.org/countryOfLastProcessing'
    )
    itemCondition: Optional[Union['OfferItemCondition', List['OfferItemCondition']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemCondition',
            'https://schema.org/itemCondition'
        ),
        serialization_alias='https://schema.org/itemCondition'
    )
    material: Optional[Union[str, List[str], 'Product', List['Product'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'material',
            'https://schema.org/material'
        ),
        serialization_alias='https://schema.org/material'
    )
    mpn: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'mpn',
            'https://schema.org/mpn'
        ),
        serialization_alias='https://schema.org/mpn'
    )
    height: Optional[Union['Distance', List['Distance'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'height',
            'https://schema.org/height'
        ),
        serialization_alias='https://schema.org/height'
    )
    releaseDate: Optional[Union[date, List[date]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'releaseDate',
            'https://schema.org/releaseDate'
        ),
        serialization_alias='https://schema.org/releaseDate'
    )
    size: Optional[Union['DefinedTerm', List['DefinedTerm'], str, List[str], 'SizeSpecification', List['SizeSpecification'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'size',
            'https://schema.org/size'
        ),
        serialization_alias='https://schema.org/size'
    )
    category: Optional[Union['PhysicalActivityCategory', List['PhysicalActivityCategory'], 'CategoryCode', List['CategoryCode'], str, List[str], 'Thing', List['Thing'], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'category',
            'https://schema.org/category'
        ),
        serialization_alias='https://schema.org/category'
    )
    weight: Optional[Union['QuantitativeValue', List['QuantitativeValue'], 'Mass', List['Mass']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'weight',
            'https://schema.org/weight'
        ),
        serialization_alias='https://schema.org/weight'
    )
    hasMerchantReturnPolicy: Optional[Union['MerchantReturnPolicy', List['MerchantReturnPolicy']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMerchantReturnPolicy',
            'https://schema.org/hasMerchantReturnPolicy'
        ),
        serialization_alias='https://schema.org/hasMerchantReturnPolicy'
    )
    nsn: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'nsn',
            'https://schema.org/nsn'
        ),
        serialization_alias='https://schema.org/nsn'
    )
    gtin14: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gtin14',
            'https://schema.org/gtin14'
        ),
        serialization_alias='https://schema.org/gtin14'
    )
    gtin12: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'gtin12',
            'https://schema.org/gtin12'
        ),
        serialization_alias='https://schema.org/gtin12'
    )
    manufacturer: Optional[Union['Organization', List['Organization']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'manufacturer',
            'https://schema.org/manufacturer'
        ),
        serialization_alias='https://schema.org/manufacturer'
    )
    review: Optional[Union['Review', List['Review']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'review',
            'https://schema.org/review'
        ),
        serialization_alias='https://schema.org/review'
    )
    depth: Optional[Union['Distance', List['Distance'], 'QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'depth',
            'https://schema.org/depth'
        ),
        serialization_alias='https://schema.org/depth'
    )
    positiveNotes: Optional[Union['WebContent', List['WebContent'], 'ItemList', List['ItemList'], str, List[str], 'ListItem', List['ListItem']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'positiveNotes',
            'https://schema.org/positiveNotes'
        ),
        serialization_alias='https://schema.org/positiveNotes'
    )
    countryOfOrigin: Optional[Union['Country', List['Country']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countryOfOrigin',
            'https://schema.org/countryOfOrigin'
        ),
        serialization_alias='https://schema.org/countryOfOrigin'
    )
    isAccessoryOrSparePartFor: Optional[Union['Product', List['Product']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isAccessoryOrSparePartFor',
            'https://schema.org/isAccessoryOrSparePartFor'
        ),
        serialization_alias='https://schema.org/isAccessoryOrSparePartFor'
    )
