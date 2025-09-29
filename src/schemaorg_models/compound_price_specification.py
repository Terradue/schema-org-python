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
from .price_specification import PriceSpecification
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .unit_price_specification import UnitPriceSpecification
    from .price_type_enumeration import PriceTypeEnumeration

class CompoundPriceSpecification(PriceSpecification):
    '''
    A compound price specification is one that bundles multiple prices that all apply in combination for different dimensions of consumption. Use the name property of the attached unit price specification for indicating the dimension of a price component (e.g. "electricity" or "final cleaning").

    Attributes:
        priceType: Defines the type of a price specified for an offered product, for example a list price, a (temporary) sale price or a manufacturer suggested retail price. If multiple prices are specified for an offer the [[priceType]] property can be used to identify the type of each such specified price. The value of priceType can be specified as a value from enumeration PriceTypeEnumeration or as a free form text string for price types that are not already predefined in PriceTypeEnumeration.
        priceComponent: This property links to all [[UnitPriceSpecification]] nodes that apply in parallel for the [[CompoundPriceSpecification]] node.
    '''
    class_: Literal['https://schema.org/CompoundPriceSpecification'] = Field( # type: ignore
        default='https://schema.org/CompoundPriceSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    priceType: Optional[Union[str, List[str], 'PriceTypeEnumeration', List['PriceTypeEnumeration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceType',
            'https://schema.org/priceType'
        ),
        serialization_alias='https://schema.org/priceType'
    )
    priceComponent: Optional[Union['UnitPriceSpecification', List['UnitPriceSpecification']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceComponent',
            'https://schema.org/priceComponent'
        ),
        serialization_alias='https://schema.org/priceComponent'
    )
