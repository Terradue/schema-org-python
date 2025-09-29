from __future__ import annotations
from datetime import (
    date
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
from .thing import Thing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .brand import Brand
    from .quantitative_value import QuantitativeValue
    from .web_content import WebContent
    from .review import Review
    from .list_item import ListItem
    from .audience import Audience
    from .demand import Demand
    from .merchant_return_policy import MerchantReturnPolicy
    from .service import Service
    from .aggregate_rating import AggregateRating
    from .product_return_policy import ProductReturnPolicy
    from .grant import Grant
    from .physical_activity_category import PhysicalActivityCategory
    from .product_group import ProductGroup
    from .energy_consumption_details import EnergyConsumptionDetails
    from .mass import Mass
    from .country import Country
    from .property_value import PropertyValue
    from .distance import Distance
    from .certification import Certification
    from .adult_oriented_enumeration import AdultOrientedEnumeration
    from .offer import Offer
    from .image_object import ImageObject
    from .offer_item_condition import OfferItemCondition
    from .size_specification import SizeSpecification
    from .category_code import CategoryCode
    from .organization import Organization
    from .item_list import ItemList
    from .defined_term import DefinedTerm
    from .product_model import ProductModel

class Product(Thing):
    """
Any offered product or service. For example: a pair of shoes; a concert ticket; the rental of a car; a haircut; or an episode of a TV show streamed online.
    """
    class_: Literal['https://schema.org/Product'] = Field( # type: ignore
        default='https://schema.org/Product',
        alias='@type',
        serialization_alias='@type'
    )
    reviews: Optional[Union["Review", List["Review"]]] = Field(
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
    isRelatedTo: Optional[Union["Service", List["Service"], "Product", List["Product"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isRelatedTo',
            'https://schema.org/isRelatedTo'
        ),
        serialization_alias='https://schema.org/isRelatedTo'
    )
    colorSwatch: Optional[Union["ImageObject", List["ImageObject"], HttpUrl, List[HttpUrl]]] = Field(
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
    pattern: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str]]] = Field(
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
    model: Optional[Union["ProductModel", List["ProductModel"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'model',
            'https://schema.org/model'
        ),
        serialization_alias='https://schema.org/model'
    )
    hasCertification: Optional[Union["Certification", List["Certification"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasCertification',
            'https://schema.org/hasCertification'
        ),
        serialization_alias='https://schema.org/hasCertification'
    )
    isVariantOf: Optional[Union["ProductModel", List["ProductModel"], "ProductGroup", List["ProductGroup"]]] = Field(
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
    logo: Optional[Union[HttpUrl, List[HttpUrl], "ImageObject", List["ImageObject"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'logo',
            'https://schema.org/logo'
        ),
        serialization_alias='https://schema.org/logo'
    )
    aggregateRating: Optional[Union["AggregateRating", List["AggregateRating"]]] = Field(
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
    negativeNotes: Optional[Union["ListItem", List["ListItem"], "WebContent", List["WebContent"], "ItemList", List["ItemList"], str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'negativeNotes',
            'https://schema.org/negativeNotes'
        ),
        serialization_alias='https://schema.org/negativeNotes'
    )
    width: Optional[Union["QuantitativeValue", List["QuantitativeValue"], "Distance", List["Distance"]]] = Field(
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
    hasAdultConsideration: Optional[Union["AdultOrientedEnumeration", List["AdultOrientedEnumeration"]]] = Field(
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
    keywords: Optional[Union[str, List[str], HttpUrl, List[HttpUrl], "DefinedTerm", List["DefinedTerm"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'keywords',
            'https://schema.org/keywords'
        ),
        serialization_alias='https://schema.org/keywords'
    )
    hasProductReturnPolicy: Optional[Union["ProductReturnPolicy", List["ProductReturnPolicy"]]] = Field(
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
    isSimilarTo: Optional[Union["Service", List["Service"], "Product", List["Product"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isSimilarTo',
            'https://schema.org/isSimilarTo'
        ),
        serialization_alias='https://schema.org/isSimilarTo'
    )
    additionalProperty: Optional[Union["PropertyValue", List["PropertyValue"]]] = Field(
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
    offers: Optional[Union["Demand", List["Demand"], "Offer", List["Offer"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'offers',
            'https://schema.org/offers'
        ),
        serialization_alias='https://schema.org/offers'
    )
    audience: Optional[Union["Audience", List["Audience"]]] = Field(
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
    isConsumableFor: Optional[Union["Product", List["Product"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isConsumableFor',
            'https://schema.org/isConsumableFor'
        ),
        serialization_alias='https://schema.org/isConsumableFor'
    )
    funding: Optional[Union["Grant", List["Grant"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'funding',
            'https://schema.org/funding'
        ),
        serialization_alias='https://schema.org/funding'
    )
    hasMeasurement: Optional[Union["QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasMeasurement',
            'https://schema.org/hasMeasurement'
        ),
        serialization_alias='https://schema.org/hasMeasurement'
    )
    hasEnergyConsumptionDetails: Optional[Union["EnergyConsumptionDetails", List["EnergyConsumptionDetails"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'hasEnergyConsumptionDetails',
            'https://schema.org/hasEnergyConsumptionDetails'
        ),
        serialization_alias='https://schema.org/hasEnergyConsumptionDetails'
    )
    brand: Optional[Union["Organization", List["Organization"], "Brand", List["Brand"]]] = Field(
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
    itemCondition: Optional[Union["OfferItemCondition", List["OfferItemCondition"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'itemCondition',
            'https://schema.org/itemCondition'
        ),
        serialization_alias='https://schema.org/itemCondition'
    )
    material: Optional[Union[str, List[str], "Product", List["Product"], HttpUrl, List[HttpUrl]]] = Field(
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
    height: Optional[Union["Distance", List["Distance"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
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
    size: Optional[Union["DefinedTerm", List["DefinedTerm"], str, List[str], "SizeSpecification", List["SizeSpecification"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'size',
            'https://schema.org/size'
        ),
        serialization_alias='https://schema.org/size'
    )
    category: Optional[Union["PhysicalActivityCategory", List["PhysicalActivityCategory"], "CategoryCode", List["CategoryCode"], str, List[str], "Thing", List["Thing"], HttpUrl, List[HttpUrl]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'category',
            'https://schema.org/category'
        ),
        serialization_alias='https://schema.org/category'
    )
    weight: Optional[Union["QuantitativeValue", List["QuantitativeValue"], "Mass", List["Mass"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'weight',
            'https://schema.org/weight'
        ),
        serialization_alias='https://schema.org/weight'
    )
    hasMerchantReturnPolicy: Optional[Union["MerchantReturnPolicy", List["MerchantReturnPolicy"]]] = Field(
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
    manufacturer: Optional[Union["Organization", List["Organization"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'manufacturer',
            'https://schema.org/manufacturer'
        ),
        serialization_alias='https://schema.org/manufacturer'
    )
    review: Optional[Union["Review", List["Review"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'review',
            'https://schema.org/review'
        ),
        serialization_alias='https://schema.org/review'
    )
    depth: Optional[Union["Distance", List["Distance"], "QuantitativeValue", List["QuantitativeValue"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'depth',
            'https://schema.org/depth'
        ),
        serialization_alias='https://schema.org/depth'
    )
    positiveNotes: Optional[Union["WebContent", List["WebContent"], "ItemList", List["ItemList"], str, List[str], "ListItem", List["ListItem"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'positiveNotes',
            'https://schema.org/positiveNotes'
        ),
        serialization_alias='https://schema.org/positiveNotes'
    )
    countryOfOrigin: Optional[Union["Country", List["Country"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'countryOfOrigin',
            'https://schema.org/countryOfOrigin'
        ),
        serialization_alias='https://schema.org/countryOfOrigin'
    )
    isAccessoryOrSparePartFor: Optional[Union["Product", List["Product"]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'isAccessoryOrSparePartFor',
            'https://schema.org/isAccessoryOrSparePartFor'
        ),
        serialization_alias='https://schema.org/isAccessoryOrSparePartFor'
    )
