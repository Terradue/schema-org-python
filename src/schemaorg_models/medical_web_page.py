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
    from .medical_audience_type import MedicalAudienceType
    from .medical_audience import MedicalAudience

class MedicalWebPage(WebPage):
    '''
    A web page that provides medical information.

    Attributes:
        medicalAudience: Medical audience for page.
        aspect: An aspect of medical practice that is considered on the page, such as 'diagnosis', 'treatment', 'causes', 'prognosis', 'etiology', 'epidemiology', etc.
    '''
    class_: Literal['https://schema.org/MedicalWebPage'] = Field( # type: ignore
        default='https://schema.org/MedicalWebPage',
        alias='@type',
        serialization_alias='@type'
    )
    medicalAudience: Optional[Union['MedicalAudience', List['MedicalAudience'], 'MedicalAudienceType', List['MedicalAudienceType']]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
    aspect: Optional[Union[str, List[str]]] = Field(
        default=None,
        validation_alias=AliasChoices(
            'genre',
            'https://schema.org/genre'
        ),
        serialization_alias='https://schema.org/genre'
    )
