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
from .structured_value import StructuredValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .warranty_scope import WarrantyScope
    from .quantitative_value import QuantitativeValue

class WarrantyPromise(StructuredValue):
    '''
    A structured value representing the duration and scope of services that will be provided to a customer free of charge in case of a defect or malfunction of a product.

    Attributes:
        warrantyScope: The scope of the warranty promise.
        durationOfWarranty: The duration of the warranty promise. Common unitCode values are ANN for year, MON for months, or DAY for days.
    '''
    class_: Literal['https://schema.org/WarrantyPromise'] = Field( # type: ignore
        default='https://schema.org/WarrantyPromise',
        alias='@type',
        serialization_alias='@type'
    )
    warrantyScope: Optional[Union['WarrantyScope', List['WarrantyScope']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    durationOfWarranty: Optional[Union['QuantitativeValue', List['QuantitativeValue']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
