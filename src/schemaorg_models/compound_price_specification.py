from __future__ import annotations
from pydantic import (
    AliasChoices,
    Field
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
    """
A compound price specification is one that bundles multiple prices that all apply in combination for different dimensions of consumption. Use the name property of the attached unit price specification for indicating the dimension of a price component (e.g. "electricity" or "final cleaning").
    """
    class_: Literal['https://schema.org/CompoundPriceSpecification'] = Field( # type: ignore
        default='https://schema.org/CompoundPriceSpecification',
        alias='@type',
        serialization_alias='@type'
    )
    priceType: Optional[Union[str, List[str], PriceTypeEnumeration, List[PriceTypeEnumeration]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceType',
            'https://schema.org/priceType'
        ),
        serialization_alias='https://schema.org/priceType'
    )
    priceComponent: Optional[Union[UnitPriceSpecification, List[UnitPriceSpecification]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'priceComponent',
            'https://schema.org/priceComponent'
        ),
        serialization_alias='https://schema.org/priceComponent'
    )
