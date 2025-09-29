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
from .web_page import WebPage
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .duration import Duration
    from .quantitative_value import QuantitativeValue

class RealEstateListing(WebPage):
    '''
    A [[RealEstateListing]] is a listing that describes one or more real-estate [[Offer]]s (whose [[businessFunction]] is typically to lease out, or to sell).
  The [[RealEstateListing]] type itself represents the overall listing, as manifested in some [[WebPage]].
  

    Attributes:
        leaseLength: Length of the lease for some [[Accommodation]], either particular to some [[Offer]] or in some cases intrinsic to the property.
        datePosted: Publication date of an online listing.
    '''
    class_: Literal['https://schema.org/RealEstateListing'] = Field( # type: ignore
        default='https://schema.org/RealEstateListing',
        alias='@type',
        serialization_alias='@type'
    )
    leaseLength: Optional[Union['QuantitativeValue', List['QuantitativeValue'], 'Duration', List['Duration']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'leaseLength',
            'https://schema.org/leaseLength'
        ),
        serialization_alias='https://schema.org/leaseLength'
    )
    datePosted: Optional[Union[date, List[date], datetime, List[datetime]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'datePosted',
            'https://schema.org/datePosted'
        ),
        serialization_alias='https://schema.org/datePosted'
    )
