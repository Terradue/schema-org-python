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
    from .property import Property
    from .enumeration import Enumeration

class _Class(Intangible):
    '''
    A class, also often called a 'Type'; equivalent to rdfs:Class.

    Attributes:
        supersededBy: Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    '''
    class_: Literal['https://schema.org/_Class'] = Field( # type: ignore
        default='https://schema.org/_Class',
        alias='@type',
        serialization_alias='@type'
    )
    supersededBy: Optional[Union['Enumeration', List['Enumeration'], '_Class', List['_Class'], 'Property', List['Property']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'supersededBy',
            'https://schema.org/supersededBy'
        ),
        serialization_alias='https://schema.org/supersededBy'
    )
