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
from .lodging_business import LodgingBusiness

class BedAndBreakfast(LodgingBusiness):
    '''
    Bed and breakfast.
<br /><br />
See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    '''
    class_: Literal['https://schema.org/BedAndBreakfast'] = Field( # type: ignore
        default='https://schema.org/BedAndBreakfast',
        alias='@type',
        serialization_alias='@type'
    )
