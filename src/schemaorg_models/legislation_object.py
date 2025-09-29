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
from .legislation import Legislation
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .legal_value_level import LegalValueLevel

class LegislationObject(Legislation):
    '''
    A specific object or file containing a Legislation. Note that the same Legislation can be published in multiple files. For example, a digitally signed PDF, a plain PDF and an HTML version.

    Attributes:
        legislationLegalValue: The legal value of this legislation file. The same legislation can be written in multiple files with different legal values. Typically a digitally signed PDF have a "stronger" legal value than the HTML file of the same act.
    '''
    class_: Literal['https://schema.org/LegislationObject'] = Field( # type: ignore
        default='https://schema.org/LegislationObject',
        alias='@type',
        serialization_alias='@type'
    )
    legislationLegalValue: Optional[Union['LegalValueLevel', List['LegalValueLevel']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
