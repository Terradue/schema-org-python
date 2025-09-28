from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # put heavy, hint-only imports here
    from schemaorg_models.web_page import WebPage

from datetime import (
    date,
    datetime
)
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
from schemaorg_models.quantitative_value import QuantitativeValue
from schemaorg_models.duration import Duration

class RealEstateListing(WebPage):
    """
A [[RealEstateListing]] is a listing that describes one or more real-estate [[Offer]]s (whose [[businessFunction]] is typically to lease out, or to sell).
  The [[RealEstateListing]] type itself represents the overall listing, as manifested in some [[WebPage]].
  
    """
    class_: Literal['https://schema.org/RealEstateListing'] = Field( # type: ignore
        default='https://schema.org/RealEstateListing',
        alias='@type',
        serialization_alias='@type'
    )
    leaseLength: Optional[Union[QuantitativeValue, List[QuantitativeValue], Duration, List[Duration]]] = Field(
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
